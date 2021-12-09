#!/usr/bin/env python

import sys

arguments = sys.argv
if (len(arguments) > 1):
    pass
else:
    sys.exit()


file_out = open(arguments[1][:arguments[1].rfind(".")] + ".lst", "wb")
# start bytes
file_out.write(b"\xFF\xFE\xFF\x1A\x65\x00\x43\x00\x61\x00\x72\x00\x20\x00\x50\x00\x6C\x00\x61\x00\x79\x00\x20\x00\x4C\x00\x69\x00\x73\x00\x74\x00\x20\x00\x56\x00\x65\x00\x72\x00\x73\x00\x69\x00\x6F\x00\x6E\x00\x20\x00\x31\x00\x2E\x00\x33\x00")

file_in = open(arguments[1], "r")

while True:
    line = file_in.readline()
    if not line:
        break

    if (not line.startswith('File')):
        continue

    song = line[line.find("=") + 1:-1]
    song = song.replace("E:\\", "\\USB Disk\\")

    file_out.write(b"\xFF\xFE\xFF")
    file_out.write(len(song).to_bytes(1, 'little'))
    file_out.write(bytes(song, 'UTF-16LE'))

file_in.close()

# end bytes
file_out.write(b"\xFF\xFE\xFF\x11\x5F\x00\x65\x00\x6E\x00\x64\x00\x5F\x00\x6F\x00\x66\x00\x5F\x00\x70\x00\x6C\x00\x61\x00\x79\x00\x6C\x00\x69\x00\x73\x00\x74\x00\x5F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")

file_out.close()
