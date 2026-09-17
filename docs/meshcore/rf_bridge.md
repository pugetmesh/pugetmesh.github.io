# RF Bridge & Backhaul

*More bandwidth, fewer retransmissions, faster propagation.*

A busy local mesh and a long-distance backhaul link want opposite radio settings. Locally you want a fast, short-range preset so neighborhood traffic moves quickly; between hilltops you want something slower and more robust—or wider and higher-power—to make the long hop reliable. Once you split those settings, something has to carry traffic across the seam. That something is an **RF bridge**: one logical node with a foot in both networks, passing packets between them so the rest of the mesh never sees the boundary.

This page collects our backhaul work: the 500 kHz preset we're testing, how to bridge it to the local mesh, and the FCC rules that make 500 kHz the compliant path to real power.

## 500 kHz backhaul testing

Our local mesh runs the standard **62.5 kHz** preset (see [Overview](index.md)). That preset is efficient and works well for neighborhood coverage, but under FCC Part 15 it operates as a narrowband emission at low power (see [FCC 900 MHz Regulations](#fcc-900-mhz-regulations) below).

**500 kHz is different.** At a 6 dB bandwidth of 500 kHz, a LoRa signal clears the FCC's digital-modulation floor in 902–928 MHz and becomes eligible for the higher power limit—up to 1 W conducted—which is exactly what a long backhaul hop needs. That makes 500 kHz an attractive candidate for a dedicated backhaul band that is both **higher-power and FCC-compliant**, sitting above the local mesh rather than competing with it.

The payoff we're after is the tagline above: a wider channel carries **more bandwidth** (a higher data rate), which shortens each packet's time on air and—together with the higher legal power—means **fewer retransmissions** and, in turn, **faster propagation** of traffic across the mesh. Test1 and Test2 exist to confirm that payoff on real regional paths.

!!! note "Test1 — Sept 11–15, 2026"
    We ran **Test1** from Friday, September 11 through Tuesday, September 15, 2026 to evaluate a 500 kHz preset for backhaul and FCC compliance, using the [LoRa bridging guide](https://meshcore.nexus/guides/lora-bridging) we created, embedded below. *Hardware, band plan, and results will be documented here as the analysis wraps up.*

Trade-offs to keep in mind: a wider channel has a larger spectral footprint (plan it to coexist with the 62.5 kHz mesh), and higher power brings the [antenna-gain derate](#fcc-900-mhz-regulations) into play. Coordinate on [Discord](https://discord.gg/ANvUg3AyZt) before putting a high-power backhaul node on the air.

## RF Bridge

To join a 500 kHz backhaul to the 62.5 kHz local mesh, you need a bridge that lives on both. Two methods work today with off-the-shelf software:

- **OpenHop Repeater RF Fabric** — two LoRa radios on one Linux host, joined in software; one node, one identity, one config file.
- **MeshCore ESP-NOW bridge** — two ESP32 repeaters, each on its own frequency, linked over 2.4 GHz; a compile-time firmware option (the `*_repeater_bridge_espnow` builds).

Both preserve MeshCore's encryption, paths, and routing—the packet goes through the real mesh pipeline rather than being replayed as raw radio bytes—so a crossing looks like one ordinary hop.

!!! info "Full guide"
    The complete guide is embedded below. If it doesn't load, open it directly: **[Bridging Two LoRa Frequencies](https://meshcore.nexus/guides/lora-bridging)** (meshcore.nexus, by Adam Gessaman / PugetMesh).

<iframe src="https://meshcore.nexus/guides/lora-bridging" title="Bridging Two LoRa Frequencies — meshcore.nexus" width="100%" height="700" frameborder="0" style="border:0;" loading="lazy"></iframe>

## FCC 900 MHz Regulations

Why 500 kHz? It comes straight from the rules for the 902–928 MHz ISM band. The FCC governs the band through two coexisting Part 15 sections:

- **§15.247** — the digital / spread-spectrum path. It requires a **6 dB bandwidth of at least 500 kHz** and, in return, allows up to **1 W** conducted output.
- **§15.249** — a narrowband path with **no** bandwidth minimum, but a far lower limit (~0.75 mW EIRP).

A 62.5 kHz (or 125 kHz) LoRa channel sits **below** the 500 kHz floor, so it isn't eligible for §15.247's power—it's lawful only under §15.249's much lower limit (LoRa isn't a frequency-hopping system, so that alternate path doesn't apply either). Cross 500 kHz and the high-power digital path opens up. One more catch for backhaul: in the 900 MHz band there's **no antenna-gain allowance**—directional gain above 6 dBi means reducing conducted power 1:1.

That's the whole reason 500 kHz is our backhaul candidate: it's the narrowest preset that can legally carry real power.

!!! info "Full reference"
    Summary above; the full, eCFR-cited reference is embedded below. If it doesn't load, open it directly: **[FCC Rules for 902–928 MHz & LoRa](https://stuff.cisien.com/fcc-900mhz-regulations.html)** (stuff.cisien.com, by Chris Curwick, CC BY-SA 4.0). This is reference material, not regulatory advice—verify against the current eCFR before relying on it.

<iframe src="https://stuff.cisien.com/fcc-900mhz-regulations.html" title="FCC Rules for 902–928 MHz & LoRa — stuff.cisien.com" width="100%" height="700" frameborder="0" style="border:0;" loading="lazy"></iframe>
