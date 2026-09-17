# HaLow (802.11ah)

!!! warning "Experimental — actively under test"
    PugetMesh is **beginning HaLow testing at Haystack**. Treat everything here as evolving: AREDN's HaLow support is still maturing, and our local band plan and hardware picks will firm up as testing progresses. Coordinate on [Discord](https://discord.gg/ANvUg3AyZt) before putting a HaLow node on the air.

## What HaLow is

**HaLow (IEEE 802.11ah)** is a WiFi standard that operates in sub-GHz spectrum—including the 902–928 MHz ISM band, and amateur allocations near 900 MHz where permitted. Compared to 2.4/5 GHz microwave it trades raw speed for **much longer range and far better penetration through foliage and terrain**.

- **Throughput:** roughly hundreds of kbps up to a few Mbps, depending on conditions
- **Channel width:** 1, 2, 4, or 8 MHz—narrower channels mean a smaller spectral footprint and longer range
- **IP-native:** it's standard WiFi/IP, so it drops directly into an AREDN mesh

That combination makes HaLow attractive for **obstructed paths**—forested valleys, terrain shadows, and sites where a clean 2.4/5 GHz line of sight simply isn't available.

## Status in AREDN

HaLow support landed in AREDN's **version 4 (Babel-only) production line** for *some* 900 MHz radios. It is real, but still rough around the edges:

- Support is limited to specific radios—**verify your exact model** against the [Supported Devices list](https://www.arednmesh.org/content/supported-devices-0) before buying.
- Driver support in current Linux kernels is immature; expect **occasional device restarts** and some troubleshooting, and note that HaLow nodes may need a power cycle after a firmware upgrade.
- Because it's v4, HaLow nodes are **Babel-only** and won't talk to legacy OLSR-only nodes.

Known-working hardware to date includes the **Morse Micro MM-HL1-EX** and **Heltec HT-HD01 / HT-HD01 V2**. More radios are being added over time—check the release notes and supported-devices list.

## 900 MHz coexistence

HaLow at ~900 MHz shares spectrum with our [MeshCore](/meshcore/) and [Meshtastic](/meshtastic/) LoRa networks, which also live in the 900 MHz band. Before deploying HaLow:

- **Plan your frequency/channel** to avoid stepping on the LoRa mesh (and vice-versa).
- Keep channels **as narrow as the link allows**—a 1 MHz HaLow channel is far easier to fit around the LoRa mesh than an 8 MHz one.
- **Coordinate on [Discord](https://discord.gg/ANvUg3AyZt)** so we keep the band usable for everyone.

## Local testing at Haystack

We're in the early stages of evaluating HaLow for PugetMesh at **Haystack**. Questions we're working through:

- Which supported radios perform best on our regional paths
- Realistic throughput and range on obstructed links
- A band/channel plan that coexists cleanly with MeshCore/Meshtastic
- How HaLow links best tie into the existing 2.4 GHz AREDN backbone

*(Hardware under test, band plan, and results to be documented here as the Haystack testing develops.)*

If you're testing HaLow, share your results on [Discord](https://discord.gg/ANvUg3AyZt)—real-world regional data is exactly what we need right now.
