# Welcome

[![Puget Mesh Logo](/static/PugetMeshLogo_200.png){ align=left }](/static/PugetMeshLogo.svg)
## Connecting the Puget Sound, Regardless of the Grid.

**Puget Mesh** is a volunteer-led community building off-grid, community-owned communication networks across the Puget Sound region. Our primary focus is **[MeshCore](/meshcore/)**—a resilient, low-power LoRa texting network—alongside **[AREDN](/aredn/)** high-speed data for emergency communications and our legacy **[Meshtastic](/meshtastic/)** network. Together these provide resilient digital infrastructure for disaster preparedness, emergency response, and everyday experimentation.

**New to mesh networking?** You’ve come to the right place. Beyond the technology, we are a community of builders. Whether you’re looking to troubleshoot a node or brainstorm your next project, our Discord server is the hub for our off-mesh collaboration. Use it to ask for help and also to meet others in your area in one of the regional location channels.
</br>
</br>

**Get Involved:** Join our [Discord](https://discord.gg/ANvUg3AyZt). We use it for nearly all of our communication outside the mesh.

**Follow Us:** We occasionally post user projects and events on both [Bluesky](https://bsky.app/profile/pugetmesh.org) and [Instagram](https://www.instagram.com/pugetmesh)

**Contact Us:** For official inquiries, please email [inquiries@pugetmesh.org](mailto:inquiries@pugetmesh.org).

---
## Which network is right for me?

!!! tip "Start here — MeshCore"
    For most people, **MeshCore** is the best way to get on the mesh today. It runs on inexpensive, low-power LoRa hardware, works off-grid, and is the most active and effective network in our region. → **[Get on MeshCore](/meshcore/)**

!!! note "AREDN — high-speed EmComm data"
    **AREDN** turns commercial WiFi hardware into a high-speed IP mesh for amateur radio operators, carrying IP phones, Winlink, file transfer, and video. It requires a ham license at the frequencies and power levels we use in this region. → **[Explore AREDN](/aredn/)**

!!! note "Meshtastic — legacy / interop"
    We still operate **Meshtastic** infrastructure, but most new deployments should choose MeshCore. → **[Meshtastic](/meshtastic/)**

---
## Current Events:

### Test2 — 500 kHz MeshCore Spectrum Test (Sept 19–20, 2026)
**More bandwidth, fewer retransmissions, faster propagation** — that's the goal of our 500 kHz backhaul, and Test2 goes looking for the frequency to deliver it. On Friday, September 19 and Saturday, September 20, 2026 we'll run a spectrum study to find the optimal frequency for our [500 kHz backhaul](/meshcore/rf_bridge/), which means taking the **[Cougar Mountain repeater](/meshcore/equipment/#cougar-mountain)** offline a few times to sweep and analyze the RF spectrum. Expect intermittent Cougar outages across those two days. Questions or coordination in the [backhaul-testing Discord channel](https://discord.com/channels/1291139029814739084/1549925039388885033).

### Test3 — Modified frequency, SF, and CR (Sep 21 - 22, 48 hours)

*Mon Sep 21, 5:00 PM → Wed Sep 23, 5:00 PM Pacific (48 hours)*

**Next step towards more bandwidth, fewer retransmissions, faster propagation.** Building on Test1 and Test2, Test3 changes **frequency, spreading factor, and coding rate** together to see how they trade off in the field. The current proposed settings are **911.340 MHz, 500 kHz BW, SF8, CR7** — provisional, to be updated after Test2 completes. The exact start/stop schedule, radio settings, and step commands are encoded in the scheduler link and shown in the embedded schedule below.

We'll step these settings in a **coordinated fashion**, running bridges to keep the mesh usable throughout, and we'll attempt to **limit impact to the mesh** as we go. The aim is to optimize penetration and error handling while balancing our speed and bandwidth goals and the supporting calculations. We've already been doing limited testing between non-critical repeaters; now we need to observe the real-world impact on our own unique mesh. Coordination happens in the [backhaul-testing Discord channel](https://discord.com/channels/1291139029814739084/1549925039388885033).

!!! info "Test schedule"
    The live preset-test schedule is embedded below. If it doesn't load, open it directly: **[Test3 preset schedule](https://mikecarper.github.io/MeshCore/preset_test/?start=2026-09-22T00:00:00.000Z&end=2026-09-24T00:00:00.000Z&tz=America/Los_Angeles&freq=911.34&bw=500&sf=8&cr=7&tx=22)** (mikecarper.github.io).

<iframe src="https://mikecarper.github.io/MeshCore/preset_test/?start=2026-09-22T00:00:00.000Z&end=2026-09-24T00:00:00.000Z&tz=America/Los_Angeles&freq=911.34&bw=500&sf=8&cr=7&tx=22" title="Test3 preset schedule — mikecarper.github.io/MeshCore" width="100%" height="700" frameborder="0" style="border:0;" loading="lazy"></iframe>

---

## Past Events:
### Test1 — 500 kHz MeshCore backhaul trial (Sept 11–15, 2026)
From Friday, September 11 through Tuesday, September 15, 2026 we ran **Test1**, evaluating a **500 kHz** LoRa preset for backhaul links and FCC compliance. 500 kHz is the minimum 6 dB bandwidth the FCC requires for the higher-power digital path in the 902–928 MHz band, making it a candidate for longer, higher-power backhaul hops than our 62.5 kHz local preset. See **[RF Bridge &amp; Backhaul](/meshcore/rf_bridge/)** for background, the [LoRa bridging guide](https://meshcore.nexus/guides/lora-bridging) we created, and the [FCC 900 MHz rules](https://stuff.cisien.com/fcc-900mhz-regulations.html).

### May 2025 Meshtastic ShortFast Experiment!
For the Month of May we are trialing SHORT_FAST/ShortFast. We encourage all users to move their nodes over for the whole month of May. [More information can be found on the event page here.](/meshtastic/may2025)
[![May 2025 Meshtastic ShortFast Experiment](/media/meshtastic/May2025-SF-Announcement.jpg)](/meshtastic/may2025)

### April 12th, 2025:
In-Person Meetup hosted by the [Radio Club of Tacoma, W7DK](https://www.w7dk.org/).
![Meshtastic Meetup, April 2025](/media/12April2025_Meshtastic_Meetup.jpg)

### November 23rd, 2024:
In-Person Meetup at the [Shoreline Library](https://maps.app.goo.gl/B4RmdBR16wtdEE3Q7).
![Meshtastic Meetup, Nov. 2024](/media/23Nov2024_Meshtastic_Meetup.png)


### October 12th, 2024:
AREDN Flashing Party at the Seattle Public Library, Broadview Branch.
![AREDN Flashing Party, Oct. 2024](/media/AREDN%20Flashing%20Party-12Oct2024.jpg)
