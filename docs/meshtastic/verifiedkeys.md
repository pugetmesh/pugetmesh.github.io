# Encryption Keys
Meshtastic uses a [Public Key Infrastructure (PKI)](https://en.wikipedia.org/wiki/Public_key_infrastructure). In an attempt to provide some level of authenticity, we will use this page to capture the public key for verified users and one of their nodes.

Be sure to backup your public/private keys! In the app you can do this exporting the configuration and saving it elsewhere, or manually copy the keys from the security section. Be sure to never share your Private Keys! If you lose your keys, all other nodes on the network will need to remove your node from their list, in the mean time your node will show up with a red lock symbol indicating that your key has changed. 

## How to Become Verified
You will need to contact me to arrange a method of verification. This can best be done via the [Puget Mesh Discord](https://discord.gg/ANvUg3AyZt) server. 

## How to Verify Others
[![Puget Mesh Logo](/media/NodeInfo_Android.png){ width="250", align=left }](/media/NodeInfo_Android.png)
Ue the table below to verify users on the mesh. You can get the node information via the mobile apps. In Android it is (currently) accessible by selecting "More details" once you click the node short name from the node list tab. 

**Note:** As of November 2024, you can only access public keys for other nodes via the [Meshtastic Command Line Interface](https://meshtastic.org/docs/software/python/cli/). 

</br>
</br>

## Verfied Meshtastic PubKeys
[Link to verified public key csv File](https://github.com/pugetmesh/pugetmesh.github.io/blob/main/docs/meshtastic/verified_pubkeys.csv)

{{ read_csv('meshtastic/verified_pubkeys.csv') }}
