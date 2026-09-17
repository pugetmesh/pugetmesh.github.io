# Getting Started with AREDN

Getting on AREDN takes three steps: get supported hardware, flash it with AREDN firmware, and set it to the band and channel the local mesh uses.

## 1. Check your hardware

AREDN runs on specific commercial WiFi radios (and some PC/virtual targets). You may already own a supported device—check the official [Supported Devices list](https://www.arednmesh.org/content/supported-devices-0) before buying anything. See our [Equipment](equipment.md) page for what works well in our region.

!!! note "AREDN is now Babel-only (version 4+)"
    As of the 4.x production releases, AREDN has dropped the legacy OLSR routing protocol in favor of Babel. If you have older nodes, get them onto a recent 3.25.x (or newer) release so they speak Babel before joining. See the [AREDN release notes](https://github.com/aredn/aredn/blob/main/RELEASE_NOTES.md) for details.

## 2. Flash AREDN firmware

Follow the official AREDN [documentation](https://docs.arednmesh.org/en/latest/) — the *Getting Started → Installing AREDN Firmware* section — for your specific device. The first-time flash procedure varies by manufacturer, and the official docs are excellent and kept current, so we won't duplicate them here.

We periodically host **flashing parties** where experienced members help you get a node loaded and configured. Watch [Discord](https://discord.gg/ANvUg3AyZt) and the [events on our home page](/#current-events) for the next one.

## 3. Use our local band and channel

In the Puget Sound region we primarily use **2.4 GHz, Channel -2 (2397 MHz)** with **10 MHz** bandwidth.

Setting | Value
---: | :---
Band | 2.4 GHz
Channel | -2 (2397 MHz)
Bandwidth | 10 MHz

[HamWAN](https://hamwan.org/) has asked that we avoid the 5 GHz space where possible, since that is what they primarily occupy. If you need a link that 2.4 GHz can't make, coordinate on Discord first.

## Next steps

- Set your node's **name/callsign** and **location** so it appears correctly to the rest of the mesh.
- Publish your position to the [map](map.md) so we know where to grow.
- Join the AREDN discussion on our [Discord](https://discord.gg/ANvUg3AyZt).
