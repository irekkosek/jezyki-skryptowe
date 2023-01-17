#!/bin/bash
# List files by their types and put in txt
file_types=("$@")
for type in "${file_types[@]}"; do
    files=(*.$type)
    for file in "${files[@]}"; do
        echo "$file" >> "lista_plikow_rozszerzenie_${type}.txt"
    done
    sort -o "lista_plikow_rozszerzenie_${type}.txt" "lista_plikow_rozszerzenie_${type}.txt"
done