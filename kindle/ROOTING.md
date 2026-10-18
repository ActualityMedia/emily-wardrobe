# Rooting the Fire 7 (5th gen, SV98LN)

**You don't need root for Emily's Wardrobe.** The app installs with
"Apps from Unknown Sources" (see [APP.md](APP.md)). Root is only worth it if
you want to go further: remove Amazon's lock-screen ads and apps, block
Fire OS updates for good, make the tablet boot straight into the wardrobe app,
or replace Fire OS with a custom ROM.

> **Risk:** rooting can leave the tablet permanently unusable ("bricked").
> The method below changes the bootloader, and on most firmware it means
> opening the case and shorting a contact on the circuit board. A slip with
> the tweezers, a wrong file, or a power loss mid-flash can kill it. It wipes
> nothing by itself, but plan as if everything on the tablet will be lost.
> These steps come from the XDA community, not Amazon. Read the XDA thread
> linked below in full before starting; if it disagrees with this page,
> follow the thread.

## 1. Check the firmware version (on the tablet)

**Settings > Device Options > System Updates.** It shows
"Your tablet is running Fire OS 5.x.x.x". Write it down. It decides which path
you take in step 4.

While you're there, keep the tablet **off Wi-Fi** until you're done, so Amazon
can't push an update halfway through.

## 2. What you need

- A computer running **Linux**. An installed Ubuntu or Linux Mint works, and
  so does an Ubuntu live USB stick. The scripts don't work on Windows or macOS.
- A good micro-USB **data** cable.
- For firmware 5.3.3 and newer: plastic pry tools and fine tweezers or a bent
  paperclip.
- The tablet charged above 50%.
- The **amonet** unlock package for "ford" (the Fire 7 5th gen), from the XDA
  thread: *[UNLOCK][ROOT][TWRP][UNBRICK][DOWNGRADE] Fire 7 (ford and austin)*
  — https://xdaforums.com/t/unlock-root-twrp-unbrick-downgrade-fire-7-ford-and-austin.3899860/
- **Magisk** (the root manager) as a flashable zip, linked from the same
  thread.

## 3. Set up the Linux computer

These commands are for Ubuntu and Linux Mint (Mint is built on Ubuntu, so
nothing else changes):

```
sudo apt update
sudo apt install python3 python3-serial adb fastboot
sudo systemctl stop ModemManager
sudo systemctl disable ModemManager
sudo adduser $USER dialout     # then log out and back in
```

Stopping ModemManager matters: it grabs new USB serial devices to check
whether they're modems, which interrupts the bootrom step. Re-enable it
afterwards with `sudo systemctl enable --now ModemManager` if you use a
mobile-broadband modem. On an Ubuntu live USB, run
`sudo add-apt-repository universe` before installing.

Unzip the amonet package and `cd` into its folder.

## 4. Get the tablet into bootrom mode

**Firmware 5.3.2 or older:** you don't need to open it. Power the tablet off,
then hold the volume button the XDA thread names while you plug in the USB
cable. Go to step 5.

**Firmware 5.3.3 or newer:** you have to open the case.

1. Power the tablet off completely.
2. Starting next to the microSD slot, work a plastic pry tool around the edge
   and lift off the back.
3. Lift off the metal shield over the chips, slowly. Don't pry against
   components.
4. Find the test point the XDA thread shows in its photos. **Use those photos;
   don't guess.** The metal frame is ground.
5. Hold the tweezers so they touch the test point and the frame, plug the USB
   cable into the computer, hold for a few seconds, then let go.

## 5. Unlock the bootloader and install TWRP

With the tablet in bootrom mode and connected:

```
sudo ./bootrom-step.sh
```

Follow its prompts. When it says to, the tablet reboots and the script
continues with:

```
sudo ./fastboot-step.sh
```

The tablet should reboot into **TWRP** (the custom recovery). Swipe to allow
modifications.

If the computer doesn't see the tablet: try another USB port, check `dmesg`,
and make sure ModemManager is stopped.

## 6. Back up, then root

In TWRP:

1. **Backup**: back up Boot, System and Data to a microSD card. Keep this
   backup; it's your way back.
2. **Install**: copy the Magisk zip to the microSD card, select it, swipe to
   flash.
3. **Reboot > System.** The first boot can take several minutes.

Open the Magisk app to confirm root.

## 7. After rooting (optional)

- Install Emily's Wardrobe from [APP.md](APP.md) as usual.
- To have the tablet open straight into the wardrobe app, install a kiosk or
  single-app launcher and set it as the default home screen.
- Re-assemble the case only once you've confirmed it boots.

## If it goes wrong

- Stuck on the logo or boot-looping: hold power to switch off, then hold
  **power + volume** as the XDA thread describes to get into TWRP, and restore
  your backup.
- Can't reach TWRP at all: the same amonet package includes an unbrick path
  through bootrom mode (step 4). Ask in the XDA thread with your firmware
  version.
