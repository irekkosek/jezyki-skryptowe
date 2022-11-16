#!/bin/bash

#!/bin/bash
read input

files=($input)
#delete white characters in file word
for file in "${files[@]}"; do
    sed "s/ //g" $file > "${file}_dane_wyjsciowe.txt"
done