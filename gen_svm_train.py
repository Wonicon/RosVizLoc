#!/usr/bin/env python

import os
import sys
import cv2


def vector(fp,filename):
    arr = cv2.imread(filename).flatten()
    i = 1 # Index required for libsvm
    rgb = 0 # Indicate a full rgb data
    value = 0 # The rgb value
    for data in arr:
        value = value * 255 + data
        rgb = rgb + 1
        if rgb == 3:
            fp.write("%d:%d " % (i, value))
            i = i + 1
            value = 0
            rgb = 0

if len(sys.argv) < 3:
    print "Too few arguments"
    exit()

fp = open("train", "a")
fp.write(sys.argv[1] + " ")

for arg in sys.argv[2:]:
    print os.path.abspath(arg)
    vector(fp, arg)
fp.close
