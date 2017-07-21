#!/usr/bin/python2
import argparse
import os
import urllib
import subprocess
from datetime import date, datetime, timedelta

# Pillow
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

URL_FORMAT = 'http://go-dl.eve-files.com/media/corp/verite/{0}'
FONT = ImageFont.truetype("FreeSans.ttf", 96)

def download(label, dl_dest):
    pic = label + '.png'
    file_dest = os.path.join(dl_dest, pic)
    if os.path.isfile(file_dest):
        print 'Skipping ' + label
        return file_dest
    target = URL_FORMAT.format(pic)
    print 'Downloading ' + label + '...'
    try:
        urllib.urlretrieve(target, file_dest)
    except Exception:
        print 'Could not download ' + label
        pass
    return file_dest

def edit_image(label, fpath, save_dest, retries_left=3):
    if retries_left < 0:
        print "Couldn't process " + label
        return False
    try:
       img = Image.open(fpath)
       draw = ImageDraw.Draw(img)
       draw.text((650, 1024), label, fill=0xFFFFFF, font=FONT)
       img.save(save_dest)
    except Exception:
        return edit_image(label, fpath, save_dest, retries_left=retries_left-1)
    return True

def mkdirs(dirs):
    for dest in dirs:
        if not os.path.exists(dest):
            os.makedirs(dest)

def main(index, end, dl_dest, save_dest, output_path):
    image_number = 0
    while index <= end:
        label = index.strftime(date_fmt) 
        dl_path = download(label, dl_dest)
        edit_image(label, dl_path, os.path.join(save_dest, 'img{0:04}.png'.format(image_number)))
        index += timedelta(days=1)
        image_number += 1
    # Now extend the last frame a little bit
    for suffix in range(0, 70):
        edit_image(label, dl_path, os.path.join(save_dest, 'img{0:04}.png'.format(image_number + suffix)))
    if os.path.exists(output_path):
        os.unlink(output_path)
    ffmpeg_cmd = 'ffmpeg -f image2 -i {0} {1}'.format(os.path.join(save_dest, 'img%04d.png'), output_path)
    result = subprocess.call(ffmpeg_cmd.split(' '))
    if result == 0:
        print '\n'
        print 'Done!\n'
    else:
        print 'Could not convert image to video'

if __name__ == '__main__':
    date_fmt = '%Y%m%d'
    today = date.today().strftime(date_fmt)
    parser = argparse.ArgumentParser(description='Create a timelapse of Verite\'s classic EVE Influence maps')
    parser.add_argument('start', metavar='START_DATE', help='A date in the format Ymd (20070809)')
    parser.add_argument('end', metavar='END_DATE', nargs='?', default=today, help='A date in the format Ymd (20170809);\ndefaults to the current date')
    parser.add_argument('--originals-dir', metavar='PATH', default='originals', help='Where to save downloaded images')
    parser.add_argument('--modified-dir', metavar='PATH', default='images', help='Where to save edited images')
    parser.add_argument('--output_path', metavar='FILENAME', default='video.avi', help='The filename of the final video (and by extension the file format chosen for ffmpeg)')
    args = parser.parse_args()
    start = datetime.strptime(args.start, date_fmt)
    end = datetime.strptime(args.end, date_fmt)
    dl_dest = args.originals_dir
    save_dest = args.modified_dir
    mkdirs([dl_dest, save_dest])
    main(start, end, dl_dest, save_dest, args.output_path)
