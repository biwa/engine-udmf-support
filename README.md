# UDMF support in engines

This page contains tables of which UDMF fields for each map element are supported by which engines. Since some engine's documentation about supported UDMF fields is not complete and/or correct these tables do not claim to be complete or correct, either. **Pull requsts to improve the data are welcome.**

General information about UDMF:
- DoomWiki: https://doomwiki.org/wiki/UDMF

Base UDMF specifications (v1.1):
- https://github.com/ZDoom/gzdoom/blob/master/specs/udmf.txt
- https://www.doomworld.com/eternity/engine/stuff/udmf11.txt

Engine specific information:
- DSDA-Doom: https://github.com/kraflab/dsda-doom/blob/master/docs/udmf.md
- Eternity Engine: https://eternity.youfailit.net/wiki/UDMF
- GZDoom: https://github.com/ZDoom/gzdoom/blob/master/specs/udmf_zdoom.txt
## Linedef
|      Field       | Type |Base|DSDA-Doom|Eternity|GZDoom|
|------------------|------|:--:|:-------:|:------:|:----:|
|alpha             |float | -  |   ✔️    |   ✔️   |  ✔️  |
|anycross          |bool  | -  |   ✔️    |   -    |  ✔️  |
|arg0              |int   | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|arg0str           |string| -  |    -    |   -    |  ✔️  |
|arg1              |int   | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|arg1str           |string| -  |    -    |   -    |  ✔️  |
|arg2              |int   | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|arg3              |int   | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|arg4              |int   | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|automapstyle      |int   | -  |   ✔️    |   -    |  ✔️  |
|blockeverything   |bool  | -  |   ✔️    |   ✔️   |  ✔️  |
|blockfloaters     |bool  | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|blockhitscan      |bool  | -  |   ✔️    |   -    |  ✔️  |
|blocking          |bool  | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|blocklandmonsters |bool  | -  |    -    |   ✔️   |  -   |
|blockmonsters     |bool  | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|blockplayers      |bool  | -  |   ✔️    |   ✔️   |  ✔️  |
|blockprojectiles  |bool  | -  |   ✔️    |   -    |  ✔️  |
|blocksight        |bool  | -  |   ✔️    |   -    |  ✔️  |
|blocksound        |bool  | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|blockuse          |bool  | -  |   ✔️    |   -    |  ✔️  |
|checkswitchrange  |bool  | -  |   ✔️    |   -    |  ✔️  |
|clipmidtex        |bool  | -  |   ✔️    |   ✔️   |  ✔️  |
|comment           |string| ✔️ |   ✔️    |   ✔️   |  ✔️  |
|damagespecial     |bool  | -  |   ✔️    |   -    |  ✔️  |
|deathspecial      |bool  | -  |   ✔️    |   -    |  ✔️  |
|dontdraw          |bool  | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|dontpegbottom     |bool  | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|dontpegtop        |bool  | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|drawfullheight    |bool  | -  |    -    |   -    |  ✔️  |
|firstsideonly     |bool  | -  |   ✔️    |   ✔️   |  ✔️  |
|health            |int   | -  |   ✔️    |   -    |  ✔️  |
|healthgroup       |int   | -  |   ✔️    |   -    |  ✔️  |
|id                |int   | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|impact            |bool  | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|jumpover          |bool  | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|lm_sampledist_bot |int   | -  |    -    |   -    |  ✔️  |
|lm_sampledist_line|int   | -  |    -    |   -    |  ✔️  |
|lm_sampledist_mid |int   | -  |    -    |   -    |  ✔️  |
|lm_sampledist_top |int   | -  |    -    |   -    |  ✔️  |
|locknumber        |int   | -  |   ✔️    |   -    |  ✔️  |
|lowerportal       |bool  | -  |    -    |   ✔️   |  -   |
|mapped            |bool  | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|midtex3d          |bool  | -  |   ✔️    |   ✔️   |  ✔️  |
|midtex3dimpassible|bool  | -  |   ✔️    |   ✔️   |  ✔️  |
|missilecross      |bool  | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|monsteractivate   |bool  | -  |   ✔️    |   -    |  ✔️  |
|monstercross      |bool  | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|monsterpush       |bool  | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|monstershoot      |bool  | -  |    -    |   ✔️   |  -   |
|monsteruse        |bool  | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|moreids           |string| -  |   ✔️    |   -    |  ✔️  |
|noskywalls        |bool  | -  |    -    |   -    |  ✔️  |
|passuse           |bool  | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|playercross       |bool  | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|playerpush        |bool  | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|playeruse         |bool  | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|playeruseback     |bool  | -  |   ✔️    |   -    |  ✔️  |
|polycross         |bool  | -  |    -    |   ✔️   |  -   |
|portal            |int   | -  |    -    |   ✔️   |  -   |
|renderstyle       |string| -  |    -    |   ✔️   |  ✔️  |
|repeatspecial     |bool  | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|revealed          |bool  | -  |   ✔️    |   -    |  ✔️  |
|secret            |bool  | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|sideback          |int   | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|sidefront         |int   | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|special           |int   | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|tranmap           |string| -  |    -    |   ✔️   |  -   |
|translucent       |bool  | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|transparent       |bool  | -  |   ✔️    |   -    |  ✔️  |
|twosided          |bool  | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|upperportal       |bool  | -  |    -    |   ✔️   |  -   |
|v1                |int   | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|v2                |int   | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|wrapmidtex        |bool  | -  |   ✔️    |   -    |  ✔️  |
|zoneboundary      |bool  | -  |    -    |   ✔️   |  ✔️  |

## Sidedef
|        Field        | Type  |  Base  |DSDA-Doom| Eternity | GZDoom |
|---------------------|-------|:------:|:-------:|:--------:|:------:|
|clampgradient_bottom |bool   |   -    |    -    |    -     |   ✔️   |
|clampgradient_mid    |bool   |   -    |    -    |    -     |   ✔️   |
|clampgradient_top    |bool   |   -    |    -    |    -     |   ✔️   |
|clipmidtex           |bool   |   -    |   ✔️    |    -     |   ✔️   |
|coloradd_bottom      |int    |   -    |    -    |    -     |   ✔️   |
|coloradd_mid         |int    |   -    |    -    |    -     |   ✔️   |
|coloradd_top         |int    |   -    |    -    |    -     |   ✔️   |
|colorization_bottom  |int    |   -    |    -    |    -     |   ✔️   |
|colorization_mid     |int    |   -    |    -    |    -     |   ✔️   |
|colorization_top     |int    |   -    |    -    |    -     |   ✔️   |
|comment              |string |   ✔️   |   ✔️    |    ✔️    |   ✔️   |
|flipgradient_bottom  |bool   |   -    |    -    |    -     |   ✔️   |
|flipgradient_mid     |bool   |   -    |    -    |    -     |   ✔️   |
|flipgradient_top     |bool   |   -    |    -    |    -     |   ✔️   |
|light                |int    |   -    |   ✔️    |    ✔️    |   ✔️   |
|light_bottom         |int    |   -    |   ✔️    |    ✔️    |   ✔️   |
|light_mid            |int    |   -    |   ✔️    |    ✔️    |   ✔️   |
|light_top            |int    |   -    |   ✔️    |    ✔️    |   ✔️   |
|lightabsolute        |bool   |   -    |   ✔️    |    ✔️    |   ✔️   |
|lightabsolute_bottom |bool   |   -    |   ✔️    |    ✔️    |   ✔️   |
|lightabsolute_mid    |bool   |   -    |   ✔️    |    ✔️    |   ✔️   |
|lightabsolute_top    |bool   |   -    |   ✔️    |    ✔️    |   ✔️   |
|lightfog             |bool   |   -    |   ✔️    |    -     |   ✔️   |
|lm_sampledist_bot    |int    |   -    |    -    |    -     |   ✔️   |
|lm_sampledist_line   |int    |   -    |    -    |    -     |   ✔️   |
|lm_sampledist_mid    |int    |   -    |    -    |    -     |   ✔️   |
|lm_sampledist_top    |int    |   -    |    -    |    -     |   ✔️   |
|lowercolor_bottom    |int    |   -    |    -    |    -     |   ✔️   |
|lowercolor_mid       |int    |   -    |    -    |    -     |   ✔️   |
|lowercolor_top       |int    |   -    |    -    |    -     |   ✔️   |
|nodecals             |bool   |   -    |    -    |    -     |   ✔️   |
|nofakecontrast       |bool   |   -    |   ✔️    |    -     |   ✔️   |
|nogradient_bottom    |bool   |   -    |    -    |    -     |   ✔️   |
|nogradient_mid       |bool   |   -    |    -    |    -     |   ✔️   |
|nogradient_top       |bool   |   -    |    -    |    -     |   ✔️   |
|offsetx              |*mixed*|✔️ (int)|✔️ (int) |✔️ (float)|✔️ (int)|
|offsetx_bottom       |float  |   -    |   ✔️    |    ✔️    |   ✔️   |
|offsetx_mid          |float  |   -    |   ✔️    |    ✔️    |   ✔️   |
|offsetx_top          |float  |   -    |   ✔️    |    ✔️    |   ✔️   |
|offsety              |*mixed*|✔️ (int)|✔️ (int) |✔️ (float)|✔️ (int)|
|offsety_bottom       |float  |   -    |   ✔️    |    ✔️    |   ✔️   |
|offsety_mid          |float  |   -    |   ✔️    |    ✔️    |   ✔️   |
|offsety_top          |float  |   -    |   ✔️    |    ✔️    |   ✔️   |
|scalex_bottom        |float  |   -    |   ✔️    |    -     |   ✔️   |
|scalex_mid           |float  |   -    |   ✔️    |    -     |   ✔️   |
|scalex_top           |float  |   -    |   ✔️    |    -     |   ✔️   |
|scaley_bottom        |float  |   -    |   ✔️    |    -     |   ✔️   |
|scaley_mid           |float  |   -    |   ✔️    |    -     |   ✔️   |
|scaley_top           |float  |   -    |   ✔️    |    -     |   ✔️   |
|sector               |int    |   ✔️   |   ✔️    |    ✔️    |   ✔️   |
|skew_bottom_type     |string |   -    |    -    |    ✔️    |   -    |
|skew_middle_type     |string |   -    |    -    |    ✔️    |   -    |
|skew_top_type        |string |   -    |    -    |    ✔️    |   -    |
|smoothlighting       |bool   |   -    |   ✔️    |    -     |   ✔️   |
|texturebottom        |string |   ✔️   |   ✔️    |    ✔️    |   ✔️   |
|texturemiddle        |string |   ✔️   |   ✔️    |    ✔️    |   ✔️   |
|texturetop           |string |   ✔️   |   ✔️    |    ✔️    |   ✔️   |
|uppercolor_bottom    |int    |   -    |    -    |    -     |   ✔️   |
|uppercolor_mid       |int    |   -    |    -    |    -     |   ✔️   |
|uppercolor_top       |int    |   -    |    -    |    -     |   ✔️   |
|useowncoloradd_bottom|bool   |   -    |    -    |    -     |   ✔️   |
|useowncoloradd_mid   |bool   |   -    |    -    |    -     |   ✔️   |
|useowncoloradd_top   |bool   |   -    |    -    |    -     |   ✔️   |
|useowncolors_bottom  |bool   |   -    |    -    |    -     |   ✔️   |
|useowncolors_mid     |bool   |   -    |    -    |    -     |   ✔️   |
|useowncolors_top     |bool   |   -    |    -    |    -     |   ✔️   |
|wrapmidtex           |bool   |   -    |   ✔️    |    -     |   ✔️   |

## Sector
|          Field          | Type |Base|DSDA-Doom|Eternity|GZDoom|
|-------------------------|------|:--:|:-------:|:------:|:----:|
|alphaceiling             |float | -  |    -    |   ✔️   |  ✔️  |
|alphafloor               |float | -  |    -    |   ✔️   |  ✔️  |
|attachceiling            |int   | -  |    -    |   ✔️   |  -   |
|attachfloor              |int   | -  |    -    |   ✔️   |  -   |
|ceiling_reflect          |float | -  |    -    |   -    |  ✔️  |
|ceilingglowcolor         |int   | -  |    -    |   -    |  ✔️  |
|ceilingglowheight        |float | -  |    -    |   -    |  ✔️  |
|ceilingid                |int   | -  |    -    |   ✔️   |  -   |
|ceilingplane_a           |float | -  |    -    |   -    |  ✔️  |
|ceilingplane_b           |float | -  |    -    |   -    |  ✔️  |
|ceilingplane_c           |float | -  |    -    |   -    |  ✔️  |
|ceilingplane_d           |float | -  |    -    |   -    |  ✔️  |
|ceilingterrain           |string| -  |    -    |   ✔️   |  ✔️  |
|color_ceiling            |int   | -  |    -    |   -    |  ✔️  |
|color_floor              |int   | -  |    -    |   -    |  ✔️  |
|color_sprites            |int   | -  |    -    |   -    |  ✔️  |
|color_wallbottom         |int   | -  |    -    |   -    |  ✔️  |
|color_walltop            |int   | -  |    -    |   -    |  ✔️  |
|coloradd_ceiling         |int   | -  |    -    |   -    |  ✔️  |
|coloradd_floor           |int   | -  |    -    |   -    |  ✔️  |
|coloradd_sprites         |int   | -  |    -    |   -    |  ✔️  |
|coloradd_walls           |int   | -  |    -    |   -    |  ✔️  |
|colorization_ceiling     |int   | -  |    -    |   -    |  ✔️  |
|colorization_floor       |int   | -  |    -    |   -    |  ✔️  |
|colormapbottom           |string| -  |    -    |   ✔️   |  -   |
|colormapmid              |string| -  |    -    |   ✔️   |  -   |
|colormaptop              |string| -  |    -    |   ✔️   |  -   |
|comment                  |string| ✔️ |   ✔️    |   ✔️   |  ✔️  |
|damage_endgodmode        |bool  | -  |    -    |   ✔️   |  -   |
|damage_exitlevel         |bool  | -  |    -    |   ✔️   |  -   |
|damageamount             |int   | -  |   ✔️    |   ✔️   |  ✔️  |
|damagehazard             |bool  | -  |   ✔️    |   -    |  ✔️  |
|damageinterval           |int   | -  |   ✔️    |   ✔️   |  ✔️  |
|damageterraineffect      |bool  | -  |    -    |   ✔️   |  ✔️  |
|damagetype               |string| -  |    -    |   ✔️   |  ✔️  |
|desaturation             |float | -  |    -    |   -    |  ✔️  |
|dropactors               |bool  | -  |    -    |   -    |  ✔️  |
|fadecolor                |int   | -  |    -    |   -    |  ✔️  |
|floor_reflect            |float | -  |    -    |   -    |  ✔️  |
|floorglowcolor           |int   | -  |    -    |   -    |  ✔️  |
|floorglowheight          |float | -  |    -    |   -    |  ✔️  |
|floorid                  |int   | -  |    -    |   ✔️   |  -   |
|floorplane_a             |float | -  |    -    |   -    |  ✔️  |
|floorplane_b             |float | -  |    -    |   -    |  ✔️  |
|floorplane_c             |float | -  |    -    |   -    |  ✔️  |
|floorplane_d             |float | -  |    -    |   -    |  ✔️  |
|floorterrain             |string| -  |    -    |   ✔️   |  ✔️  |
|fogdensity               |int   | -  |    -    |   -    |  ✔️  |
|friction                 |int   | -  |    -    |   ✔️   |  -   |
|gravity                  |float | -  |   ✔️    |   -    |  ✔️  |
|health3d                 |int   | -  |    -    |   -    |  ✔️  |
|health3dgroup            |int   | -  |    -    |   -    |  ✔️  |
|healthceiling            |int   | -  |    -    |   -    |  ✔️  |
|healthceilinggroup       |int   | -  |    -    |   -    |  ✔️  |
|healthfloor              |int   | -  |    -    |   -    |  ✔️  |
|healthfloorgroup         |int   | -  |    -    |   -    |  ✔️  |
|heightceiling            |int   | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|heightfloor              |int   | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|hidden                   |bool  | -  |   ✔️    |   -    |  ✔️  |
|id                       |int   | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|leakiness                |int   | -  |   ✔️    |   ✔️   |  ✔️  |
|lightceiling             |int   | -  |   ✔️    |   ✔️   |  ✔️  |
|lightceilingabsolute     |bool  | -  |   ✔️    |   ✔️   |  ✔️  |
|lightcolor               |int   | -  |    -    |   -    |  ✔️  |
|lightfloor               |int   | -  |   ✔️    |   ✔️   |  ✔️  |
|lightfloorabsolute       |bool  | -  |   ✔️    |   ✔️   |  ✔️  |
|lightlevel               |int   | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|lightseqalt              |bool  | -  |    -    |   ✔️   |  -   |
|lightsequence            |bool  | -  |    -    |   ✔️   |  -   |
|lm_sampledist_ceiling    |int   | -  |    -    |   -    |  ✔️  |
|lm_sampledist_floor      |int   | -  |    -    |   -    |  ✔️  |
|moreids                  |string| -  |   ✔️    |   -    |  ✔️  |
|noattack                 |bool  | -  |   ✔️    |   -    |  ✔️  |
|nofallingdamage          |bool  | -  |    -    |   -    |  ✔️  |
|norespawn                |bool  | -  |    -    |   -    |  ✔️  |
|noskywalls               |bool  | -  |    -    |   -    |  ✔️  |
|phasedlight              |bool  | -  |    -    |   ✔️   |  -   |
|portal_ceil_attached     |bool  | -  |    -    |   ✔️   |  -   |
|portal_ceil_blocksound   |bool  | -  |    -    |   ✔️   |  ✔️  |
|portal_ceil_disabled     |bool  | -  |    -    |   ✔️   |  ✔️  |
|portal_ceil_nopass       |bool  | -  |    -    |   ✔️   |  ✔️  |
|portal_ceil_norender     |bool  | -  |    -    |   ✔️   |  ✔️  |
|portal_ceil_overlaytype  |string| -  |    -    |   ✔️   |  ✔️  |
|portal_ceil_useglobaltex |bool  | -  |    -    |   ✔️   |  -   |
|portal_floor_attached    |bool  | -  |    -    |   ✔️   |  -   |
|portal_floor_blocksound  |bool  | -  |    -    |   ✔️   |  ✔️  |
|portal_floor_disabled    |bool  | -  |    -    |   ✔️   |  ✔️  |
|portal_floor_nopass      |bool  | -  |    -    |   ✔️   |  ✔️  |
|portal_floor_norender    |bool  | -  |    -    |   ✔️   |  ✔️  |
|portal_floor_overlaytype |string| -  |    -    |   ✔️   |  ✔️  |
|portal_floor_useglobaltex|bool  | -  |    -    |   ✔️   |  -   |
|portalceiling            |int   | -  |    -    |   ✔️   |  -   |
|portalfloor              |int   | -  |    -    |   ✔️   |  -   |
|renderstyleceiling       |string| -  |    -    |   -    |  ✔️  |
|renderstylefloor         |string| -  |    -    |   -    |  ✔️  |
|rotationceiling          |float | -  |   ✔️    |   ✔️   |  ✔️  |
|rotationfloor            |float | -  |   ✔️    |   ✔️   |  ✔️  |
|scroll_ceil_type         |string| -  |    -    |   ✔️   |  ✔️  |
|scroll_ceil_x            |float | -  |    -    |   ✔️   |  ✔️  |
|scroll_ceil_y            |float | -  |    -    |   ✔️   |  ✔️  |
|scroll_floor_type        |string| -  |    -    |   ✔️   |  ✔️  |
|scroll_floor_x           |float | -  |    -    |   ✔️   |  ✔️  |
|scroll_floor_y           |float | -  |    -    |   ✔️   |  ✔️  |
|secret                   |bool  | -  |    -    |   ✔️   |  -   |
|silent                   |bool  | -  |   ✔️    |   -    |  ✔️  |
|soundsequence            |string| -  |    -    |   ✔️   |  ✔️  |
|special                  |int   | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|textureceiling           |string| ✔️ |   ✔️    |   ✔️   |  ✔️  |
|texturefloor             |string| ✔️ |   ✔️    |   ✔️   |  ✔️  |
|waterzone                |bool  | -  |    -    |   -    |  ✔️  |
|xpanningceiling          |float | -  |   ✔️    |   ✔️   |  ✔️  |
|xpanningfloor            |float | -  |   ✔️    |   ✔️   |  ✔️  |
|xscaleceiling            |float | -  |   ✔️    |   ✔️   |  ✔️  |
|xscalefloor              |float | -  |   ✔️    |   ✔️   |  ✔️  |
|ypanningceiling          |float | -  |   ✔️    |   ✔️   |  ✔️  |
|ypanningfloor            |float | -  |   ✔️    |   ✔️   |  ✔️  |
|yscaleceiling            |float | -  |   ✔️    |   ✔️   |  ✔️  |
|yscalefloor              |float | -  |   ✔️    |   ✔️   |  ✔️  |

## Vertex
| Field  |Type |Base|DSDA-Doom|Eternity|GZDoom|
|--------|-----|:--:|:-------:|:------:|:----:|
|x       |float| ✔️ |   ✔️    |   ✔️   |  ✔️  |
|y       |float| ✔️ |   ✔️    |   ✔️   |  ✔️  |
|zceiling|float| -  |    -    |   -    |  ✔️  |
|zfloor  |float| -  |    -    |   -    |  ✔️  |

## Thing
|      Field      | Type |Base|DSDA-Doom|Eternity|GZDoom|
|-----------------|------|:--:|:-------:|:------:|:----:|
|alpha            |float | -  |   ✔️    |   -    |  ✔️  |
|ambush           |bool  | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|angle            |int   | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|arg0             |int   | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|arg0str          |string| -  |    -    |   -    |  ✔️  |
|arg1             |int   | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|arg1str          |string| -  |    -    |   -    |  ✔️  |
|arg2             |int   | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|arg3             |int   | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|arg4             |int   | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|class1           |bool  | ✔️ |    -    |   ✔️   |  ✔️  |
|class10          |bool  | -  |    -    |   -    |  ✔️  |
|class11          |bool  | -  |    -    |   -    |  ✔️  |
|class12          |bool  | -  |    -    |   -    |  ✔️  |
|class13          |bool  | -  |    -    |   -    |  ✔️  |
|class14          |bool  | -  |    -    |   -    |  ✔️  |
|class15          |bool  | -  |    -    |   -    |  ✔️  |
|class16          |bool  | -  |    -    |   -    |  ✔️  |
|class2           |bool  | ✔️ |    -    |   ✔️   |  ✔️  |
|class3           |bool  | ✔️ |    -    |   ✔️   |  ✔️  |
|class4           |bool  | -  |    -    |   -    |  ✔️  |
|class5           |bool  | -  |    -    |   -    |  ✔️  |
|class6           |bool  | -  |    -    |   -    |  ✔️  |
|class7           |bool  | -  |    -    |   -    |  ✔️  |
|class8           |bool  | -  |    -    |   -    |  ✔️  |
|class9           |bool  | -  |    -    |   -    |  ✔️  |
|comment          |string| ✔️ |   ✔️    |   ✔️   |  ✔️  |
|conversation     |int   | -  |    -    |   -    |  ✔️  |
|coop             |bool  | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|countsecret      |bool  | -  |   ✔️    |   -    |  ✔️  |
|dm               |bool  | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|dormant          |bool  | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|fillcolor        |int   | -  |    -    |   -    |  ✔️  |
|floatbobphase    |int   | -  |    -    |   -    |  ✔️  |
|friend           |bool  | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|friendlyseeblocks|int   | -  |    -    |   -    |  ✔️  |
|gravity          |float | -  |   ✔️    |   -    |  ✔️  |
|health           |float | -  |   ✔️    |   ✔️   |  ✔️  |
|height           |float | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|id               |int   | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|invisible        |bool  | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|lm_sampledistance|int   | -  |    -    |   -    |  ✔️  |
|lm_suncolor      |string| -  |    -    |   -    |  ✔️  |
|nocount          |bool  | -  |    -    |   -    |  ✔️  |
|pitch            |int   | -  |    -    |   -    |  ✔️  |
|renderstyle      |string| -  |   ✔️    |   -    |  ✔️  |
|roll             |int   | -  |    -    |   -    |  ✔️  |
|scale            |float | -  |    -    |   -    |  ✔️  |
|scalex           |float | -  |   ✔️    |   -    |  ✔️  |
|scaley           |float | -  |   ✔️    |   -    |  ✔️  |
|score            |int   | -  |    -    |   -    |  ✔️  |
|single           |bool  | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|skill1           |bool  | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|skill10          |bool  | -  |    -    |   -    |  ✔️  |
|skill11          |bool  | -  |    -    |   -    |  ✔️  |
|skill12          |bool  | -  |    -    |   -    |  ✔️  |
|skill13          |bool  | -  |    -    |   -    |  ✔️  |
|skill14          |bool  | -  |    -    |   -    |  ✔️  |
|skill15          |bool  | -  |    -    |   -    |  ✔️  |
|skill16          |bool  | -  |    -    |   -    |  ✔️  |
|skill2           |bool  | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|skill3           |bool  | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|skill4           |bool  | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|skill5           |bool  | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|skill6           |bool  | -  |    -    |   -    |  ✔️  |
|skill7           |bool  | -  |    -    |   -    |  ✔️  |
|skill8           |bool  | -  |    -    |   -    |  ✔️  |
|skill9           |bool  | -  |    -    |   -    |  ✔️  |
|special          |int   | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|standing         |bool  | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|strifeally       |bool  | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|translucent      |bool  | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|type             |int   | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|x                |float | ✔️ |   ✔️    |   ✔️   |  ✔️  |
|y                |float | ✔️ |   ✔️    |   ✔️   |  ✔️  |

