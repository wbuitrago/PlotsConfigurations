#!/bin/bash
## FIXME this is where the Combine framework is installed
cd /afs/cern.ch/work/f/fcetorel/private/work2/combine/CMSSW_10_2_13
eval `scramv1 runtime -sh`
cd -

## work directory
date=140820
var=mjj
flav=all #could be ee, mm, df, all
workDir=/afs/cern.ch/work/f/fcetorel/private/work2/VBS_OS/CMSSW_10_2_15_patch2/src/PlotsConfigurations/Configurations/VBS_OS/Full2017_v6/FitDir/
workspaceDir=workspace

cd $workDir
output=${flav}_${var}


combineTool.py -M Impacts -d ${workspaceDir}/${output}.root -m 125 -t -1 --setParameters r_vbs=1 --redefineSignalPOIs=r_vbs --X-rtd MINIMIZER_analytic --allPars --doInitialFit
#combineTool.py -M Impacts --job-mode condor -d ${workspaceDir}/${output}.root -m 125 -t -1 --setParameters r_vbs=1 --redefineSignalPOIs=r_vbs --X-rtd MINIMIZER_analytic -allPars  --doFits
#combineTool.py -M Impacts -d ${workspaceDir}/${output}.root -m 125 -t -1 --setParameters r_vbs=1 --redefineSignalPOIs=r_vbs --X-rtd MINIMIZER_analytic -o ${workspaceDir}/impacts_2017_${output}.json 


#DO impacts without correlation
combineTool.py -M Impacts --job-mode condor -d ${workspaceDir}/${output}.root -m 125 -t -1 --setParameters r_vbs=1 --redefineSignalPOIs=r_vbs --X-rtd MINIMIZER_analytic --doImpactNoCorr --allPars --doFits
#combineTool.py -M Impacts -d ${workspaceDir}/${output}.root -m 125 -t -1 --setParameters r_vbs=1 --redefineSignalPOIs=r_vbs --X-rtd MINIMIZER_analytic --doImpactNoCorr --allPars  -o ${workspaceDir}/impacts_2017_${output}_noCorr.json 

#plotImpacts.py -i ${workspaceDir}/impacts_2017_${output}_noCorr.json -o ${workspaceDir}/impacts_2017_${output}_noCorr 
cd $workDir
