# Emily's Wardrobe as an app on the Kindle

`android/` builds a small Android app (APK) for the Fire 7 (5th gen, SV98LN).
It is the same Kindle build as `kindle/index.html`, bundled inside the app, so
it opens from the home screen, runs full screen, and works offline (weather
needs Wi-Fi). **Installing it does not need root.**

## Get the APK

Every push that touches `android/`, `kindle/` or `wardrobe-data.js` builds the
app on GitHub Actions ("Kindle app" workflow).

- **From main:** the newest build is always at
  `https://github.com/ActualityMedia/emily-wardrobe/releases/download/kindle-app/emily-wardrobe.apk`
- **From a branch:** open the workflow run on GitHub and download the
  `emily-wardrobe-apk` artifact (it's a zip with the APK inside).

## Install it on the Kindle

1. On the Kindle, open **Settings > Security** and turn on
   **Apps from Unknown Sources**.
2. Open Silk and go to the download link above. When it finishes, tap the
   download and choose **Install**.
   (Or copy `emily-wardrobe.apk` to the tablet over USB and tap it in the
   **Docs** app.)
3. Open **Emily's Wardrobe** from the home screen.
4. Optional: turn **Apps from Unknown Sources** back off.

The app turns to landscape or portrait as you rotate the tablet, even when
the Fire's rotation lock is on.

## Updating

Install the new APK the same way. It's signed with the same key every time
(`android/app/emily-wardrobe.keystore`), so it installs over the old one and
**saved outfits and trips are kept**. Uninstalling the app erases them.

Outfits saved in Silk (the web version) don't carry over into the app; they're
stored separately.

## Building it yourself

Needs JDK 17 and the Android SDK (platform 34):

```
cd android
./gradlew assembleRelease
# -> android/app/build/outputs/apk/release/app-release.apk
```
