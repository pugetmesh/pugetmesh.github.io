# FAQ

## New User Expectations
It is important to know that Meshtastic is under rapid development, and is not yet a *polished* product. There are bugs and quirks but that is part of the fun. If you have just turned on your Meshtastic device for the first time, get it in a good location (being next to a window can help) and let it run overnight. It takes time to see other nodes, and for other nodes to see you. Some users choose to share their position (GPS or fixed coordinates) which will appear on the maps. There are a few public maps available showing nodes (that choose to share their position) but we use [https://meshtastic.davekeogh.com/](https://meshtastic.davekeogh.com/).


## FAQ's

* **What firmware version should I flash my device with?**
    1. It is best to ask our Discord since this answer constantly changes, and not always forward/newer.
    1. There have been many times that the online firmware documentation does not include known issues.
* **What is LongFast and how is it different from LONG_FAST?**
    1. LongFast is the name of the default channel when using the LONG_FAST modem preset.
    1. LONG_FAST is a modem preset, along with MEDIUM_FAST, SHORT_FAST, and others. These are a collection of settings that tell the LoRa radio how to send and receive data over RF.
* **How do I know if I am connected to the mesh?**
    1. Seeing other nodes appear in your node list is a good indicator.
    1. Allow your node to run overnight and search for it (long name, short name, or either ID string) on the [webmap](https://meshtastic.davekeogh.com/).
    1. See if your LongFast messages are appearing on the "#LongFast" thread of the "mqtt-messages" channel on our Discord server. 
* **Why am I not getting any responses to my messages sent in LongFast or Direct Messages?**
    1. The mesh is (currently) a fairly quiet place. We do have a [weekly net](/meshtastic/#weekly-net). This doesn't mean that you are not connected.
    1. Check out our discord as received messages are automatically published there. Specifically Meshtastic > mqtt-messages > LongFast.
    1. Many nodes are unmonitored and just serve to connect the mesh. We encourage use of "📵" in the long name to indicate that your node will not respond to direct messages. 
* **I have manually added a channel but do not see any messages, and no one is hearing me.**
    1. Make sure the channel PSK and Name are correct. 
    1. Both need to be 100% correct for messages to exchange. This includes extra spaces at the end of either field.     
* **I am not seeing any other nodes on my list, even after running overnight.**
    1. Make sure your node is somewhere it can signal, near a window can be a good place.
    1. Ensure your region is set (Choose "US") on the settings tab of the app.
    1. Our primary mesh uses the default settings of LONG_FAST and slot 20, not in ham mode. 
    1. Check the steps listed under "How do I know if I am connected to the mesh?" above.
* **My node keeps rebooting, or having other apparent issues.**
    1. Try reflashing your node again, and then try older firmware versions. This may take several attempts.
* **I have everything configured correctly for <FEATURE> to work, but it does not. Why?**
    1. Meshtastic has a lot of hard-coded special cases that may prevent you from using it in the way you desire. These are difficult to capture any one place, so please engage with us on discord, or another help forum to learn more.
* **Where can I go to learn even more?**
    1. The Puget Sound Repeater Group holds [Educational Presentations](https://web.psrg.org/educational-presentations/), covering many topics including a [video recording of Adam's Meshtastic presentation](https://www.youtube.com/watch?v=QyhIoz4HR4s).
    1. In November 2024, [Ham Radio 2.0 (YouTube)](https://www.youtube.com/watch?v=YywOlirsOMA) interviewed Meshtastic Developers, and they shared some _Meshtastic_ insights.

## Join the Discord
We love chatting on and off of the mesh. The [Discord](https://discord.gg/ANvUg3AyZt) is also a great place to get help, share pictures, and get ideas for projects.
<iframe src="https://e.widgetbot.io/channels/1291139029814739084/1294852768019910777" allow="clipboard-write; fullscreen" height="750" width="100%"></iframe>
