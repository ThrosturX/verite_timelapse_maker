# Verite Timelapse Maker

Requirements:

* Python2
* Pillow (PIL) for Python2
* `ffmpeg`

## Note

Please consider supporting http://eve-files.com/ -- especially if you plan on using this yourself, as each downloaded year of images constitutes about 250 MB of data.

## Usage

```
usage: influence_stitcher.py [-h] [--originals-dir DIR] [--modified-dir DIR]
                             DATE [DATE]

Create a timelapse of Verite's classic EVE Influence maps

positional arguments:
  DATE                 A date in the format Ymd (20070809)
  DATE                 A date in the format Ymd (20170809)

optional arguments:
  -h, --help           show this help message and exit
  --originals-dir DIR  Where to save downloaded images
  --modified-dir DIR   Where to save edited images
```
