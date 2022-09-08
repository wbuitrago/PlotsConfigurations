
cd /afs/cern.ch/user/a/abulla/CMSSW_10_6_4/src/LatinoAnalysis/ShapeAnalysis/test/draw
python DrawNuisancesAll.py \
    --inputFile /afs/cern.ch/user/a/abulla/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/VBF_W/2018/sys/datacards/mu_SR/mjj/shapes/histos_mu_SR.root  \
    --outputDirPlots /afs/cern.ch/user/a/abulla/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/VBF_W/2018/sys/plots \
    --nuisancesFile /afs/cern.ch/user/a/abulla/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/VBF_W/2018/sys/nuisances.py  \
    --samplesFile   /afs/cern.ch/user/a/abulla/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/VBF_W/2018/sys/samples.py \
    --cutName mu_SR