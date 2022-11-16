#!/bin/bash
n=$1
rev=$(echo $n | rev)
if [[ $n == $rev ]]; then
   echo "tekst to palindrom"
else
   echo "tekst to nie palindrom"
fi