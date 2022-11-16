#!/bin/bash
#check if palindrome
n=$1
rev=$(echo $n | rev)
if [ $n -eq $rev ]; then
   echo "tekst to palindrom"
else
   echo "tekst to nie palindrom"
fi