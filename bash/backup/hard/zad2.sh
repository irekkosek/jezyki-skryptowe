#!/bin/bash
files=(*txt)
file=${files[0]}
echo "$file"

for i in *.txt; do
    if [ "$i" == "$file" ]; then
        continue
    fi
    if [ -z "$(diff $i $file)" ]; then
        echo "$i" >> takie_same.txt
    else
        echo "$i" >> rozne.txt
    fi
done

sort -o takie_same.txt takie_same.txt
sort -o rozne.txt rozne.txt
