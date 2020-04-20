#!/bin/bash

# variables
variables=(
    pt1
    mll
    met
    mjj
    pt1VSmjj
    mllVSmjj
)

binning=(
    # 3bin
    4bin
    # 5bin
)

rm confidence_intervals.csv 
echo "variable,1 sigma l, 1 sigma r,1 sigma width, 2 sigma l, 2 sigma r,2 sigma withd" > confidence_intervals.csv 
for bin in "${binning[@]}"
    do
    echo "binning ${bin}"
    cd ${bin}
    for var in "${variables[@]}"
        do 
        echo "variable ${var}"
        cd ${var}           
        root -b higgsCombineTest.MultiDimFit.mH125.root higgsCombineTest.MultiDimFit.mH125.root -e ".x ../../draw_db_def.cxx(\"${bin}_${var}\")" -q
        cd ..
    done
    cd ..
done

