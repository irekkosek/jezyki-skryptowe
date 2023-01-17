#!/bin/bash
#change permissions in folder
dir=$1
echo "change read(1) or write(2) permissions:"
read choice

if [ $choice -eq 1 ]; then
    chmod -v -R +r $dir >> info.txt
elif [ $choice -eq 2 ]; then
    chmod -v -R +w $dir >> info.txt
fi