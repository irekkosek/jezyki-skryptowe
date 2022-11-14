#!/bin/bash

#count down number of words in each text file
find *.txt | xargs -I _ wc -w _ > dane_wyjsciowe.txt