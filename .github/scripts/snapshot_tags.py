#!/usr/bin/env python3
"""Rebuild tags.json from the open issues that carry a ```room-tag``` block, and keep each
tag issue's status label in sync. Runs in GitHub Actions on every issue change.

tags.json is the map's fallback when the GitHub API is rate-limited for a viewer's network."""
import json, os, re, subprocess, sys, datetime

REPO = os.environ["REPO"]
TAG_RE = re.compile(r"```room-tag\s*\n(.*?)\n```", re.S)
LABELS = {"moving_out": "status: moving out", "not_needed": "status: no longer needed", "long_storage": "status: long-term storage"}

def gh(*args, input=None):
    return subprocess.run(["gh", *args], check=True, capture_output=True, text=True, input=input).stdout

issues = json.loads(gh("api", "--paginate", "--slurp", f"repos/{REPO}/issues?state=open&per_page=100"))
issues = [i for page in issues for i in page if "pull_request" not in i]
keep = []
for i in issues:
    m = TAG_RE.search(i.get("body") or "")
    if not m:
        continue
    try:
        tag = json.loads(m.group(1))
    except ValueError:
        print(f"#{i['number']}: room-tag block is not valid JSON, skipped", file=sys.stderr)
        continue
    keep.append({"number": i["number"], "html_url": i["html_url"], "user": {"login": i["user"]["login"]},
                 "created_at": i["created_at"], "updated_at": i["updated_at"], "body": i["body"]})
    want = LABELS.get(tag.get("status"))
    have = {l["name"] for l in i.get("labels", [])}
    if want and want not in have:
        args = ["issue", "edit", str(i["number"]), "-R", REPO, "--add-label", want]
        for other in set(LABELS.values()) & have - {want}:
            args += ["--remove-label", other]
        gh(*args)

snap = {"updated": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"), "issues": keep}
old = None
if os.path.exists("tags.json"):
    try:
        old = json.load(open("tags.json")).get("issues")
    except ValueError:
        pass
if old != keep:
    json.dump(snap, open("tags.json", "w"), indent=1)
    print(f"tags.json updated: {len(keep)} tags")
else:
    print(f"tags.json unchanged: {len(keep)} tags")
