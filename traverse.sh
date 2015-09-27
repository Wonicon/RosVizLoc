#!/usr/bin/env bash

label=1
CMD=`pwd`/gen_svm_train.py
SUBDIR=$(find -mindepth 1 -maxdepth 1 -type d)

echo $SUBDIR
for DIR in $SUBDIR
do
    echo $DIR
    JPGS=$(find $DIR -name "*.jp[e]g")
    echo $JPGS
    echo $label
    $CMD $label $JPGS
    label=`expr $label + 1`
done
