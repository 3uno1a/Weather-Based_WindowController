from subprocess import call
import os

def convert(src, dst):
    command = f'MP4Box -add {src} {dst}'
    call([command], shell = True)
    os.remove(src)


def convert_cv(src, dst):
    command = f'ffmpeg -i {src} -vcodec libx264 -f mp4 {dst}'
    call([command], shell = True)
    os.remove(src)