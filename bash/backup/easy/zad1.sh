#!/bin/bash

#Convert base 10 to base 16
(echo "obase=16"; cat dane_wejsciowe.txt) | bc > dane_wyjsciowe.txt