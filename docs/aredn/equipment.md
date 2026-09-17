# AREDN Equipment

AREDN runs on specific commercial WiFi radios. Always confirm a device is on the official [Supported Devices list](https://www.arednmesh.org/content/supported-devices-0) before buying—support changes with each release, and outwardly identical models sometimes differ inside.

## Common device families

Most local nodes fall into a few categories:

- **2.4 GHz sector / omni nodes** — good for filling in a neighborhood or acting as a local hub. We standardize on 2.4 GHz, Channel -2 (see [Getting Started](getting_started.md)).
- **Directional dishes / basestations** — for long point-to-point backbone links between sites with clear line of sight.
- **PC / virtual nodes** — AREDN can also run on x86 hardware or a VM to host services (Winlink, phones, file shares) behind a radio node.

!!! tip
    Pair every radio with its matching PoE injector, and a weatherproof mount if it's going outdoors. Confirm the exact hardware revision against the supported-devices list before you order.

## HaLow (802.11ah) — 900 MHz

AREDN now supports some 900 MHz HaLow radios, which trade microwave speed for much better range and terrain/foliage penetration. It's an emerging option we're actively testing—see the dedicated **[HaLow (802.11ah)](halow.md)** page.
