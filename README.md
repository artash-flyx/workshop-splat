# Workshop Walkthrough

A walkable 3D Gaussian splat of a workshop, rebuilt from a 65-second phone video, with a viewer for comparing model versions at the same viewpoint.

Open the GitHub Pages site for this repo. Switch models with the buttons or keys **1–4**; **B** flips back.
Walk with **WASD**, **Q/E** for down/up, drag to look, and **Space** to play the filmed path.

| Version | What it is |
|---|---|
| Original | 3.0M Gaussians, 30k steps, first camera solve (557 views) |
| High quality | 6.0M Gaussians, 60k steps, same camera solve |
| Final | 6.0M Gaussians, 75k steps, new camera solve (909 views; recovers the corners the first solve lost) |
| Lite | Final, decimated to 1.5M for phones and weak laptop GPUs |

The whole site is static files. To run it locally: `python3 -m http.server 8000`, then open <http://localhost:8000/>.
Built with COLMAP 4.2.1, gsplat 1.6.0 (MCMC), PlayCanvas splat-transform (SOG), three.js r180 and Spark 2.3.1 (MIT, see `vendor/LICENSES.txt`).
