#!/usr/bin/env bash

python DrawBar.py\
 --data 712.6650 220.5163 232.7826 524.5636 \
 --legend_list "p=0.99,l=1,g=1" "p=0.9,l=1,g=1" "p=0.99,l=5,g=1" "p=0.99,l=1,g=5" \
 --y_label "Average system utility" \
 --picture_name figure1.pdf \
 --legend_position 9 \
 --legend_column 1
