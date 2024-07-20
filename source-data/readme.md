# CSV Generator Script

This script generates the CSV files from different sources. The sources are retrieved from the following URLs:

* DelphiDoom: https://raw.githubusercontent.com/jval1972/DelphiDoom/master/udmf_delphidoom.txt
* DSDA-Doom: https://raw.githubusercontent.com/kraflab/dsda-doom/master/docs/udmf.md
* EDGE-Classic: https://raw.githubusercontent.com/edge-classic/EDGE-classic/master/docs/specifications/UDMF%20EDGE-Classic%20Extensions.txt
* Eternity Engine: https://eternity.youfailit.net/rest.php/v1/page/UDMF
* GZDoom: https://raw.githubusercontent.com/kraflab/dsda-doom/master/docs/udmf.md

They are stored locally and only retrieved when the local copies are more than 24 hours old.

The resulting CSV files are directly written to `../csv/`.