#!/bin/bash

for mcut in 100 200 300 400 500
do  
    for detajjcut in 10 15 20 25
    do
        for var in 0 1 2 3
        do
            root -l -e ".x plot.cxx(${var},${mcut},${detajjcut})" -q
        done
    done
done

mkdir plot_mjj
mv *mjj*.png plot_mjj

mkdir plot_detajj
mv *detajj*.png plot_detajj

mkdir plot_mll
mv *mll*.png plot_mll

mkdir plot_jetpt2
mv *jetpt2*.png plot_jetpt2
