#!/bin/bash
read -p "Enter the name of the file: " file

if [ -f "$file" ]; then
    echo "File exists"
else
    echo "File does not exist"
    return 1
fi

sed 's/ //g' "$file" > "${file}_nospace.txt"