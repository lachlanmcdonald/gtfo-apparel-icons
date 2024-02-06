# gtfo-apparel-icons

> Generate SVG's for the apparel colour schemes in GTFO.

## Setup

Unfortunately, the prefab names and in-game labels do not match, so multiple steps are required to extract the necessary files and match with their in-game label.

This process will have to be run whenever GTFO's palettes are updated. The path provided may also change between versions of GTFO and the tooling below. These files have not been included within this repository as they are copyrighted.

**To export the color data:**

1. Install and launch [AssetRipper](https://github.com/AssetRipper/AssetRipper/releases)
3. Check "_Skip StreamingAssets folder_"
3. Press _File_ → _Open Folder_
4. Select the installation location of GTFO:  
```C:\Program Files (x86)\Steam\steamapps\common\GTFO```
5. Once loaded, select `sharedassets3.assets` → `GameObjects` → `Palette002Hackett`
7. Press _Export_ → _Export all Files of Selected Type_
8. Extract to this project's directory
9. Once complete, a new folder will be created titled `GTFO`.

<small>For some reason, extracting the files directly from `sharedassets3.assets` will not export the necessary color definitions.</small>

**To export the palette name data:**

1. Install and launch [r2modman](https://thunderstore.io/package/ebkr/r2modman/)
2. Within _r2modman_
	1. Install the [BepInExPack GTFO](https://gtfo.thunderstore.io/package/BepInEx/BepInExPack_GTFO/) and [MTFO](https://gtfo.thunderstore.io/package/dakkhuza/MTFO/) packages
	3. Press _Start modded_ to create the necessary config files.
	4. Once GTFO has launched successfully, quit the game
3. Browse to:  ```%USERPROFILE%\AppData\Roaming\r2modmanPlus-local\GTFO\profiles\Default\BepInEx\config```
	- Edit `MTFO.ini` and set `Dump GameData` to `true`
4. Within _r2modman_:
	1. Re-launch the game by pressing _Start modded_
	2. Once GTFO has launched successfully, quit the game
6. Browse to:  
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

## Clean-up

After export, unnecessary files can be deleted with:

```sh
git clean -f -X .\GTFO\
```
