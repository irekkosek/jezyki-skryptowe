#!/bin/bash

#remove word in files
for file in $1/*; do
sed "s/$2//g" "$file" > tmpfile && mv tmpfile "$file"
done