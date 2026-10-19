# Robotics Room Move-Out

A walkable 3D scan (Gaussian splat) of the robotics room. Teams use it to tag what happens to their things before the move.

**Site:** https://artash-flyx.github.io/workshop-splat/ · **Model comparison:** [compare.html](https://artash-flyx.github.io/workshop-splat/compare.html)

## For teams
- **Move:** click the orange arrows on the floor, or press the arrow keys, to hop between 9 spots. Click a dot on the map to jump. Drag to look around; WASD walks freely.
- **Tag:** press **Tag an area** and drag a box around the thing. In the small popup, pick a team (**Skyrunners, RoboSub, Escape Room, General, Previous teams**) and a status: *moving out by a date*, *no longer needed* (unused or a previous team's), or *long-term storage*. The area stays outlined in 3D for everyone.
- **Save:** you're sent to GitHub with a pre-filled issue; press **Submit new issue**. This needs a free GitHub account. To change or remove a tag, open its pin → **Edit on GitHub**.

## For organizers
- Every tag is an open issue here, labelled by status (the labels are applied automatically). Filter by label or search by team.
- **Remove a tag:** close its issue. **Fix a tag:** edit the JSON in its `room-tag` block. The map reads that block, not the text above it.
- **Spreadsheet:** the tag list's **CSV** link downloads every tag.
- The map reads tags live from the GitHub API. When a network hits GitHub's limit of 60 requests an hour, it falls back to `tags.json`, which the *Snapshot room tags* Action rebuilds on every issue change.

## Models
| Version | What it is |
|---|---|
| Original | 3.0M Gaussians, 30k steps, first camera solve (557 views) |
| High quality | 6.0M Gaussians, 60k steps, same camera solve |
| Final | 6.0M Gaussians, 75k steps, new camera solve (909 views, recovers the corners the first solve lost) |
| Lite | Final, decimated to 1.5M for phones and weak laptop GPUs |

The map uses Final (or Lite on phones). Every version sits in one shared coordinate frame, so tags line up on all of them.
The site is static files. To run it locally: `python3 -m http.server 8000`, then open <http://localhost:8000/>.
Built with COLMAP 4.2.1, gsplat 1.6.0 (MCMC), PlayCanvas splat-transform (SOG), three.js r180 and Spark 2.3.1 (MIT, see `vendor/LICENSES.txt`).
