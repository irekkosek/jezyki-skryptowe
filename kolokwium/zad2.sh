#!/bin/bash
type=$1
dir=$2

files=($dir/*.$type)
ls "${files[@]}" | wc -l > info.txt
cat "${files[@]}"
