# Build and install Version 5.0
Upload to your GitHub repository (replace what is there): `www`, `android-overrides` (changed: voice), `android-res`, `signing` (unchanged), `package.json`, `capacitor.config.json`, `patch_manifest.py`, `BUILD-WORKFLOW.yml`, and replace `.github/workflows/build-apk.yml` with the text of the new BUILD-WORKFLOW.yml. Do NOT change `signing/debug.keystore`.
Download artifact Claude_V5.0-APK and install app-debug.apk over 4.2.1: data stays (same app ID, same key, versionCode 8).
After install: More > Voice > Test voice (raise the media volume).
If a build step for the icon or black launch screen fails, delete that step.
