#!/bin/bash
files=($1/*.txt)

sed -i -r 's/"(.+)"/\1/g' "${files[@]}"
