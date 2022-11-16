#!/bin/bash
read file_types
read dir

files=($dir/*.$type)
echo $files | wc -l
cat $files 
