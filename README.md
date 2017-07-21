# Verite Timelapse Maker

Requirements:

* Python2
* Pillow (PIL) for Python2
* `ffmpeg`

## Note

Please consider supporting http://eve-files.com/ -- especially if you plan on using this yourself, as each downloaded year of images constitutes about 250 MB of data.

## Usage

```
usage: influence_stitcher.py [-h] [--originals-dir PATH] [--modified-dir PATH]
                             [--output_path FILENAME]
                             START_DATE [END_DATE]

Create a timelapse of Verite's classic EVE Influence maps

positional arguments:
  START_DATE            A date in the format Ymd (20070809)
  END_DATE              A date in the format Ymd (20170809)
                        defaults to the current date

optional arguments:
  -h, --help            show this help message and exit
  --originals-dir PATH  Where to save downloaded images
  --modified-dir PATH   Where to save edited images
  --output_path FILENAME
                        The filename of the final video (and by extension the
                        file format chosen for ffmpeg)
```
