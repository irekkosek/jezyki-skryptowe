#!/bin/bash

folders=("$@")
for folder in "${folders[@]}"; do
    files=($(find $folder -type f -mtime -1))
    for file in "${files[@]}"; do
        echo "$file" >> "zmodyfikowane.txt"
    done
done