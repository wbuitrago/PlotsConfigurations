#!/bin/bash


# datacards folders for sssr config and wzcr config

srDatacardsFolder="/afs/cern.ch/user/d/dbrambil/CMSSW_10_2_18/src/PlotsConfigurations/Configurations/VBS/EFT/Full2018/datacards_VBS_SS_2018_test_fullconfig_apr19"
# CHANGE THIS FOLDER NAME
crDatacardsFolder="/afs/cern.ch/user/d/dbrambil/CMSSW_10_2_18/src/PlotsConfigurations/Configurations/VBS/EFT/Full2018_cr_WZ/datacards_VBS_SS_2018_cr_WZ_full_nuis_mar03"

# cuts
SignalRegion="SS_sr_emu"
ControlRegion="wz_vbs_total"

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

for bin in "${binning[@]}"
    do
    echo "binning ${bin}"
    mkdir ${bin}
    cd ${bin}
    for var in "${variables[@]}"
        do 
        echo "variable ${var}"
        mkdir ${var} 
        cd ${var}     
        combineCards.py ${crDatacardsFolder}/${ControlRegion}/events/datacard.txt \
            ${srDatacardsFolder}/${SignalRegion}/${var}_${bin}/datacard.txt \
            > combined__${ControlRegion}__${SignalRegion}__${var}_${bin}.txt   

        text2workspace.py combined__${ControlRegion}__${SignalRegion}__${var}_${bin}.txt \
            -P HiggsAnalysis.AnalyticAnomalousCoupling.AnomalousCouplingOneOp:analiticAnomalousCouplingOneOp --PO=k_my,r \
            -o combined__${ControlRegion}__${SignalRegion}__${var}_${bin}_model_test.root             

        combine -M MultiDimFit combined__${ControlRegion}__${SignalRegion}__${var}_${bin}_model_test.root \
            --algo=grid --points 120  -m 125 -t -1 --expectSignal=1 --redefineSignalPOIs k_my \
            --freezeParameters r --setParameters r=1,k_my=0 --setParameterRanges k_my=-2.0,2.0     

        cd ..
    done
    cd ..
done

