# Puget Mesh Meshcore Repeater Setup

These are guidelines to help you setup a new Meshcore repeater which will work well within Puget Mesh. Repeaters in Meshcore are encouraged, each enhances the coverage of the mesh.

## Locating your Repeater

A repeater with an omnidirectional antenna (which is most of them) needs to have good line of site to other repeaters. This means getting it up high. On your roof or on a mast that is above the roof or in the yard free in a clear space. For directional antennas you need good line of site to the other repeater you aim to mesh with.

## Encryption Keys

Before you get started, it is good to understand every Meshcore device has a set of private and public keys for encrypting traffic.  The public key is used within the Mesh as the unique ID of your node. You can even search by public key in the [MeshExplorer Search Tool https://map.w0z.is/search](https://map.w0z.is/search).

Meshcore uses the first two characters of your public key on the mesh as the abbreviated id of your repeater when viewing the paths messages have traveled. It is not a _strict_ requirement, but unique prefixes are helpful in the larger Puget Mesh system.

Meshcore's firmware can not know what prefixes are already in use, and it will generate perfectly good random public and private keys with a public key prefix that is already in use by another repeater.

In the Repeater Setup steps you will check if your auto-generated public key has a unique prefix and it not, you will follow the steps to create new keys using the [Meshcore Custom Key Generator site https://gessaman.com/mc-keygen/](https://gessaman.com/mc-keygen/).

>NOTE: If you have security concerns about this approach, go to the [meshcore-web-keygen GitHub repo](https://github.com/agessaman/meshcore-web-keygen), download and run it locally.

## Repeater Setup

Once you have [flashed your repeater](https://flasher.meshcore.co.uk/) with the web flasher (chromium browser required). The Meshcore documentation explains how to [configure your repeater](https://github.com/meshcore-dev/MeshCore/blob/main/docs/faq.md#31-q-how-do-you-configure-a-repeater-or-a-room-server) over USB.  The web based config app is at [https://config.meshcore.dev/](https://config.meshcore.dev/)

Key items for you to get right:

- **Public Key**: Check if your auto-generated Public Key prefix (the first two characters) are unique.

  1. Go to the [MeshExplore Stats https://map.w0z.is/stats](https://map.w0z.is/stats#used-prefixes)
  2. Is there already a repeater using your prefix? If no, you're good to go.
  3. Is your prefix in use? Scroll down to the [MeshExplore Unused Repeater Prefixes](https://map.w0z.is/stats#unused-prefixes).
  4. Select one you would like to use and the Meshcore Custom Key Generator site will open. You will see the prefix you selected. Click Generate Key.
  5. Copy the public and private keys and save them. We'll finishing setting up the repeater and change them at the end using the web console.

- **Name**: It is helpful if your repeater gives a hint about the location, such as a landmark, neighborhood or cross streets.
- **Location**: Set the Latitude and Longitude in decimal format (47.xxxx, -122.xxxx)
- **Guest and Admin Password**: Use a strong password. Repeaters can be administered over the mesh from the Meshcore app.
- **Radio Settings**: Repeaters and clients use the “USA/Canada (Recommended)” preset.

    Frequency | 910.525 MHz
    -- | --
    Bandwidth | 62.5 kHz
    Spreading Factor | 7
    Coding Rate | 5

## Setting Private and Public Keys

If your auto-generated key did not have a unique prefix, you should have generated a new private and public key and saved them. Go back to the [Web Flasher https://flasher.meshcore.co.uk/](https://flasher.meshcore.co.uk/) and above the list of all the devices, on the right side, click on the Console button and connect to your device. Once you are connected you will see a command prompt:

  1. At the prompt, type in `set prv.key` and paste in your Private Key.
  2. Type in `reboot`.
  3. After your device reboots, verify that the private key is correct by running `get prv.key`.

## Remote Management

Before you put your repeater up on a pole where you can't easily reach it, practice remotely managing it with a Meshcore companion device. With your Meshcore companion app open:

1. Go to Contact
2. In the menu, select Add Contact and fill in the form:  
    **Contact Type**: Repeater  
    **Name**: Your Repeater Name  
    **Public Key**: The public key you generated earlier  
3. Save the contact (check mark)  
4. Open the contact in the list
5. Select Remote Management (and wait the seconds..)
6. Put in your admin password and Login

You should now be logged in and able to Get Stats from the menu, or issue console commands. For all the commands see the [Repeater & Room Server CLI Reference](https://github.com/meshcore-dev/MeshCore/wiki/Repeater-&-Room-Server-CLI-Reference).

## Repeater Testing

You can search for your repeater by name or public key using [MeshExplorer https://map.w0z.is/search](https://map.w0z.is/search)

Using the Config app or managing remotely from a companion deviceissue the advert command on your repeater. If your location is good, your antenna is good and you have other repeaters in range you will see your repeater show up in MeshExplorer and on the Map (assuming you set the location).

Once you see your repeater in MeshExplorer, expand a Recent Advert and look at the Paths and Graph views to see who is receiving your adverts directly and which are also receiving it via the mesh.
