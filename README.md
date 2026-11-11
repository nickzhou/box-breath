# Box Breath

**Summary.** Box Breath is a one-button box breathing guide. The web app lives in `site/` and is the product on every platform. Capacitor wraps the same folder for the App Store and Google Play.

## Folders

| Folder | Contents |
|---|---|
| `site/` | Website (`index.html`), app (`app/index.html`), privacy policy, offline worker, icons. Deploy this folder as-is. |
| `store-assets/` | Store screenshots for iPhone 6.9-inch, iPad 13-inch, Android phone, and the Google Play feature graphic. |
| `Drafts/` | Platform decision, store listings, marketing plan. |
| `tools/` | Python scripts: local server, icon generator, screenshot capture. |

## Preview locally

Run `python3 tools/serve.py 8765`, then open http://localhost:8765. If macOS blocks Python from reading Google Drive, copy the project to a local folder first.

## Publish the website

Upload the `site/` folder to any static host (GitHub Pages, Cloudflare Pages, Netlify). There is no build step. HTTPS is required for offline support and home-screen install.

## Build the iOS and Android apps

Do this from a local (non-Drive) copy of the project. Requires Node.js, full Xcode for iOS, and Android Studio for Android.

1. Set `appId` in `capacitor.config.json` to your reverse-domain ID, for example `com.yourname.boxbreath`.
2. `npm install`
3. `npx cap add ios` and `npx cap add android`
4. `npx cap sync`
5. `npx cap open ios`, set your signing team in Xcode, then Product > Archive to upload.
6. `npx cap open android`, then Build > Generate Signed App Bundle.

Use `site/icons/icon-1024.png` as the app icon source.

## Before submitting

- Test voice and sound on a real iPhone. Confirm speech works inside the wrapped app.
- Add the contact email to `site/privacy.html`.
- Regenerate screenshots after any design change: copy `tools/shots.html` and `tools/feature.html` next to the served site, then run `python3 tools/make_screenshots.py http://localhost:8765 store-assets`.
