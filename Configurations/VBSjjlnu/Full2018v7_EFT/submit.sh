# mkShapesMulti.py --pycfg=configuration_fit_Combination_2018.py --doBatch=1 --batchSplit=Samples,Files --batchQueue=longlunch
# mkShapesMulti.py --pycfg=configuration_fit_Combination_2018.py --doHadd=1 --batchSplit=Samples,Files --batchQueue=longlunch --doNotCleanup --nThreads=10 
mkPlot.py --pycfg=configuration_fit_EFT_2018.py  --inputFile=plots_fit_2018_split_Combined_total_EFT.root --showIntegralLegend=1 --plotNormalizedIncludeData=1 --plotNormalizedDistributions --onlyPlot=cratio --minLogC=50 --maxLogC=1e7 --minLogCratio=50 --maxLogCratio=1e7 --scaleToPlot=1

# mkPlot.py --pycfg=configuration_fit_EFT_2018.py  --inputFile=rootFile_fit_2018_split_Giacomo/plots_fit_2018_split_Giacomo.root --showIntegralLegend=1 --plotNormalizedIncludeData=1 --plotNormalizedDistributions --onlyPlot=cratio --minLogC=10 --minLogCratio 50 --maxLogCratio 1e7 --scaleToPlot=1
