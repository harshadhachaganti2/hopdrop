# HopDrop — Prototype (Streamlit + GitHub)

This repo contains the HopDrop interactive HTML/JS prototype, embedded inside a
tiny Streamlit app so it can be deployed for free via **Streamlit Community Cloud**.

## Files

- `app.py` — Streamlit entry point. Loads `hopdrop.html` and renders it full-page.
- `hopdrop.html` — The actual prototype (all UI, styles, and JS in one file).
- `requirements.txt` — Python dependencies.

## 1. Push to GitHub

```bash
git init
git add .
git commit -m "HopDrop prototype"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```

## 2. Deploy on Streamlit Community Cloud

1. Go to https://share.streamlit.io and sign in with GitHub.
2. Click **"New app"**.
3. Pick your repo, branch (`main`), and set **Main file path** to `app.py`.
4. Click **Deploy**.

That's it — Streamlit will install `requirements.txt` and run `app.py`,
which loads and displays `hopdrop.html` as a full interactive prototype
(role switcher, all screens, route/savings/ops dashboards, etc.).

## Notes

- All interactivity (tab switching, booking flow, toasts) is plain JS inside
  `hopdrop.html`, running inside an iframe via `streamlit.components.v1.html`.
  No Python logic is needed for the app to work.
- If you edit `hopdrop.html`, just commit + push — Streamlit Cloud auto-redeploys.
- To increase/decrease the embedded viewport height, change the `height=900`
  value in `app.py`.
