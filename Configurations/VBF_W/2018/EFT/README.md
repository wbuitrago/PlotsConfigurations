Signal region
=====================

How to run the analysis.
    
# Produce the shapes:

    mkShapesMulti.py --pycfg=configuration.py --doBatch=1 --batchSplit=Samples,Files --batchQueue=workday

# Hadd the root files:

    mkShapesMulti.py --pycfg=configuration.py --doHadd=1 --batchSplit=Samples,Files --doNotCleanup --nThreads=10

or

    hadd rootFile/plots_vbf_w_EFT_2018.root rootFile/plots_vbf_w_EFT_2018_ALL_*.root
    hadd rootFile/plots_vbf_w_EFT_2018.root rootFile/plots_vbf_w_EFT_2018_do.root rootFile/prov/plots_vbf_w_EFT_2018.root 


# Make plots:

    mkPlot.py --pycfg=configuration.py --inputFile rootFile/plots_vbf_w_EFT_2018.root --onlyPlot=cratio --linearOnly --showIntegralLegend=1 --plotNormalizedDistributions


    mkPlot.py --pycfg=configuration.py --inputFile rootFile/plots_vbf_w_EFT_2018.root --showIntegralLegend=1
    mkPlot.py --pycfg=configuration.py --inputFile rootFile/plots_vbf_w_EFT_2018.root --showIntegralLegend=1  --plotNormalizedDistributionsTHstack
    mkPlot.py --pycfg=configuration.py --inputFile rootFile/plots_vbf_w_EFT_2018.root --showIntegralLegend=1  --plotNormalizedDistributions

# Make DataCards
    mkDatacards.py --pycfg=configuration.py --inputFile rootFile/plots_vbf_w_EFT_2018.root


# Make nuis plot
    python DrawNuisancesAll.py \
     --inputFile ../../../../PlotsConfigurations/Configurations/VBF_W/2018/sys/datacards/topcr/eta1/shapes/histos_topcr.root  \
     --outputDirPlots ../../../../PlotsConfigurations/Configurations/VBF_W/2018/sys/topcr_nuisance  \
     --nuisancesFile ../../../../PlotsConfigurations/Configurations/VBF_W/2018/sys/nuisances.py  \
     --samplesFile   ../../../../PlotsConfigurations/Configurations/VBF_W/2018/sys/samples.py \
     --cutName topcr