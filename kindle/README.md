# Emily's Wardrobe on the Kindle Fire (SV98LN)

`kindle/index.html` is a lightweight build of the app for the original 2011
Kindle Fire (model SV98LN). It does everything the desktop page does (closet,
filters, outfit builder, saved outfits, trips and packing lists, weather) but is
written for that tablet's limits. **No rooting or jailbreak is needed.**

## The hardware, and what changed for it

| Kindle Fire SV98LN | What the Kindle build does about it |
| --- | --- |
| 512 MB RAM, 1 GHz dual-core TI OMAP4 | Uses 256 px palette images (0.5 MB total instead of 9.9 MB); no animated rain/snow/leaves/blobs, no drop-shadow filters |
| Fire OS 6.3 (Android 2.3) with the old Silk browser | Plain ES5 JavaScript; no flexbox, grid, CSS variables or `calc`; weather icons are PNG, not SVG |
| Silk can't negotiate modern HTTPS (TLS 1.2), so the GitHub Pages site won't load | Runs from files copied onto the tablet; weather is fetched over plain HTTP |
| Touchscreen, no mouse | Tap to add/remove pieces instead of drag-and-drop; labels always visible; bigger tap targets; instant taps (no 300 ms delay) |
| 7" 1024 x 600 screen | Landscape keeps the outfit figure pinned on the left while you pick; portrait stacks it on top. Every screen is a normal page, so the Kindle's Back button works |
| Wi-Fi only, no GPS | Weather uses Wi-Fi location if allowed, then the last known spot, then northern Ohio |

## Put it on the Kindle

1. Plug the Kindle into a computer with a micro-USB cable. It shows up as a
   drive called **KINDLE**.
2. Make a folder on that drive called `emily-wardrobe`, and copy into it:
   - the `kindle` folder
   - `wardrobe-data.js`

   (The full-size `wardrobe` image folder isn't needed on the tablet.)
3. Tap **Disconnect** on the Kindle, then unplug it.
4. Open **Web** (Silk) and go to:

   `file:///mnt/sdcard/emily-wardrobe/kindle/index.html`

5. Bookmark it so Emily can open it from the bookmarks list.

If Silk refuses to open the `file://` address, the fallback is a tiny
sideloaded app that wraps the same page. That still doesn't need root, only
**Settings > Device > Allow Installation of Applications from unknown sources**.

## Good to know

- Outfits and trips are saved in the Kindle's browser storage, so they live on
  that tablet only. Clearing Silk's data erases them.
- After adding new clothes to `wardrobe-data.js`, rebuild the small images and
  copy the `kindle` folder over again:

  ```
  python3 kindle/build_assets.py
  ```

- The desktop `index.html` is unchanged.
