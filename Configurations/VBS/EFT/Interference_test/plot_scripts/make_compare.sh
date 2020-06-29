#!/bin/bash

for mcut in 100 200 300 400 500
do  
    for detajjcut in 10 15 20 25
    do
        for var in 0 1
        do
            root -l -e ".x compare.cxx(${var},${mcut},${detajjcut})" -q
        done
    done
done

mkdir compare_mjj
mv *mjj*.png compare_mjj

mkdir compare_detajj
mv *detajj*.png compare_detajj