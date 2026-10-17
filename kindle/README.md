# Emily's Wardrobe on the Kindle Fire (SV98LN)

`kindle/index.html` is a lightweight build of the app for the Amazon Fire 7
5th generation (2015, model SV98LN, Amazon device code KFFOWI). It does
everything the desktop page does (closet, filters, outfit builder, saved
outfits, trips and packing lists, weather) but is written for that tablet's
limits. **No rooting or jailbreak is needed.**

## The hardware, and what changed for it

| Fire 7 (5th gen) | What the Kindle build does about it |
| --- | --- |
| 1 GB RAM, 1.3 GHz quad-core Cortex-A7, Mali-450 GPU | Uses 256 px palette images (0.5 MB total instead of 9.9 MB); no animated rain/snow/leaves/blobs, no drop-shadow filters |
| Fire OS 5 (Android 5.1), Silk browser | Plain, conservative JavaScript and CSS so it also works if Silk hasn't been updated in years; weather icons are PNG |
| Touchscreen, no mouse | Tap to add/remove pieces instead of drag-and-drop; labels always visible; bigger tap targets; instant taps |
| 7" 1024 x 600 screen | Landscape keeps the outfit figure pinned on the left while you pick; portrait stacks it on top. Every screen is a normal page, so the Back button works |
| Wi-Fi only, no GPS | Weather uses Wi-Fi location if allowed, then the last known spot, then northern Ohio |

## Put it on the Kindle

**Easiest, once this is merged:** open Silk and go to
`https://actualitymedia.github.io/emily-wardrobe/kindle/`, then bookmark it
(or use Silk's menu to add it to the home screen).

**If that page won't load**, copy it onto the tablet instead:

1. Plug the Kindle into a computer with a USB cable. On a Mac you'll need
   Android File Transfer; on Windows it shows up as **Fire** under This PC.
2. In the tablet's **Internal storage**, make a folder called
   `emily-wardrobe` and copy into it the `kindle` folder and
   `wardrobe-data.js`. (The full-size `wardrobe` folder isn't needed.)
3. Unplug, open Silk, and go to
   `file:///sdcard/emily-wardrobe/kindle/index.html`, then bookmark it.

## Good to know

- Outfits and trips are saved in the tablet's browser storage, so they live on
  that tablet only (and separately for the hosted page and the copied file).
  Clearing Silk's data erases them.
- After adding new clothes to `wardrobe-data.js`, rebuild the small images:

  ```
  python3 kindle/build_assets.py
  ```

- The desktop `index.html` is unchanged.
