# gtfo-apparel-icons

> Generate SVG's for the apparel colour schemes.

## Setup

Unfortunately, the prefab names and in-game labels do not match, so multiple steps are required to extract the necessary files and match with their in-game label.

This process will have to be run whenever GTFO's palettes are updated. The path provided may also change between versions of GTFO and the tooling below.

**To export the color data:**

1. Install [AssetRipper](https://github.com/AssetRipper/AssetRipper/releases)
2. Open _AssetRipper_
3. Check "_Skip StreamingAssets folder_"
3. Press _File_ → _Open File_ and select:  
```C:\Program Files (x86)\Steam\steamapps\common\GTFO\GTFO_Data\sharedassets3.assets```
3. Press _File_ → _Open Folder_
4. Select the installation location of GTFO:  
```C:\Program Files (x86)\Steam\steamapps\common\GTFO```
5. Once loaded, expand `sharedassets3.assets`, expand  `GameObjects` and select `Palette002Hackett`
6. Press _Export_ → "_Export all Files of Selected Type_"
7. Select this project's directory
8. Once complete, a new folder will be created, titled `GTFO`.

<small>For some reason, extracting the files directly from `sharedassets3.assets` will not export the necessary color definitions.</small>

**To export the palette name data:**

- Install [r2modman](https://thunderstore.io/package/ebkr/r2modman/)
- Within _r2modman_
	- Install the [BepInExPack GTFO](https://gtfo.thunderstore.io/package/BepInEx/BepInExPack_GTFO/) package.
	- Install the [MTFO](https://gtfo.thunderstore.io/package/dakkhuza/MTFO/) package.
	- Press "_Start modded_" to create the necessary config files. Once launched, quit the game.
- Browse to:  ```%USERPROFILE%\AppData\Roaming\r2modmanPlus-local\GTFO\profiles\Default\BepInEx\config```
	- Edit `MTFO.ini` and set `Dump GameData` to `true`
- Within _r2modman_, re-launch the game with by pressing "_Start modded_". Once launched, quit the game.
- Browse to:  
```%USERPROFILE%\AppData\Roaming\r2modmanPlus-local\GTFO\profiles\Default\BepInEx\GameData-Dump\```
	- Locate and copy the file `GameData_VanityItemsTemplateDataBlock_bin.json` into this project's directory.

## Generate

**Extract the palette as a JSON:**

```sh
python extract_palette.py
```

**Generate the SVG icons:**

```sh
python generate_icons.py
```
