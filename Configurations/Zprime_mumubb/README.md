To install
====

    cmsrel CMSSW_10_6_4
    cd CMSSW_10_6_4/src/
    cmsenv

    git clone --branch 13TeV git@github.com:latinos/setup.git LatinosSetup

    source LatinosSetup/SetupShapeOnly.sh

    scramv1 b -j 20

    git clone -b VBF_Zjj  git@github.com:UniMiBAnalyses/PlotsConfigurations.git

    scramv1 b -j 20

    
Customization:

    cd LatinoAnalysis/Tools/python
    cp userConfig_TEMPLATE.py userConfig.py
    # edit the userConfig.py so the paths correspond to a directory where you have write access (this will be used to write log files)
    cd -
    scramv1 b -j 20
    
    
    
# Super combination

    cd /afs/cern.ch/user/a/amassiro/Framework/Combine/CMSSW_10_2_13/src/
    cmsenv
    cd -
    


    combineCards.py ewkz_2018_topcr=2018/datacards/Top_13TeV_2j_eemm/events/datacard.txt \
                    ewkz_2018_wwcr=2018/datacards/WW_13TeV_2j_eemm/events/datacard.txt \
                    ewkz_2018_zjjhigh=2018/datacards/Zjj_13TeV_2j_eemm-high/detajjmjj/datacard.txt \
                    ewkz_2018_zjjlow=2018/datacards/Zjj_13TeV_2j_eemm-low/detajjmjj/datacard.txt \
                    ewkz_2017_topcr=2017/datacards/Top_13TeV_2j_eemm/events/datacard.txt \
                    ewkz_2017_wwcr=2017/datacards/WW_13TeV_2j_eemm/events/datacard.txt \
                    ewkz_2017_zjjhigh=2017/datacards/Zjj_13TeV_2j_eemm-high/detajjmjj/datacard.txt \
                    ewkz_2017_zjjlow=2017/datacards/Zjj_13TeV_2j_eemm-low/detajjmjj/datacard.txt \
                    ewkz_2016_topcr=2016/datacards/Top_13TeV_2j_eemm/events/datacard.txt \
                    ewkz_2016_wwcr=2016/datacards/WW_13TeV_2j_eemm/events/datacard.txt \
                    ewkz_2016_zjjhigh=2016/datacards/Zjj_13TeV_2j_eemm-high/detajjmjj/datacard.txt \
                    ewkz_2016_zjjlow=2016/datacards/Zjj_13TeV_2j_eemm-low/detajjmjj/datacard.txt \
                    > combined.txt
                    
                    
    text2workspace.py     combined.txt    -o combined.root
    
    
    
    combine -M FitDiagnostics   -t -1 --expectSignal=1 combined.root   &> logFit.txt
    combine -M AsymptoticLimits -t -1 --expectSignal=0 combined.root   &> logLimit.txt
    combine -M Significance     -t -1 --expectSignal=1 combined.root   &> logSignificance.txt

    
    combine -M MultiDimFit -d combined.root  --algo=grid --points 100 --setParameterRanges r=0.7,1.3   -n "likelihoodScan_ewkz_runII" -m 125 -t -1  --setParameters r=1  >> likelihoodScan.txt
    combine -M MultiDimFit -d combined.root  --algo=grid --points 100 --setParameterRanges r=0.7,1.3   -n "likelihoodScan_ewkz_runII_Observed" -m 125         >> likelihoodScanObserved.txt
    
    combineTool.py -d combined.root -M MultiDimFit    \
                    --algo=grid  --setParameterRanges  r=0.7,1.3    -n "likelihoodScan_ewkz_runII"   \
                    --points 100    --job-mode lxbatch --task-name lxbatch-likelihoodScan_ewkz_runII  --split-points 1  \
                    -t -1  \
                    --job-mode=condor --sub-opt '+JobFlavour = "espresso"' 
                    
                    
    hadd likelihoodScan_ewkz_runII.root    higgsCombinelikelihoodScan_ewkz_runII.POINTS.*.MultiDimFit.mH120.root

    r99t likelihoodScan_ewkz_runII.root   drawNLL.C
    r99t likelihoodScan_ewkz_runII_Observed.root   drawNLL.C
    
    r99t higgsCombinelikelihoodScan_ewkz_runII.MultiDimFit.mH125.root   drawNLL.C

    
    
    
    
    