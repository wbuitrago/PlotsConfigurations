Signal region
=====================

How to run the analysis.
    
# Produce the shapes:

    mkShapesMulti.py --pycfg=configuration.py --doBatch=1 --batchSplit=Samples,Files --batchQueue=workday

# Hadd the root files:

    mkShapesMulti.py --pycfg=configuration.py --doHadd=1 --batchSplit=Samples,Files --doNotCleanup --nThreads=10

or

    hadd rootFile/plots_vbf_zjj_2017.root rootFile/plots_vbf_zjj_2017_ALL_*.root
    

# Make plots:

    mkPlot.py --pycfg=configuration.py --inputFile rootFile/plots_vbf_zjj_2017.root --onlyPlot=cratio --linearOnly --showIntegralLegend=1
    mkPlot.py --pycfg=configuration.py --inputFile rootFile/plots_vbf_zjj_2017.root --showIntegralLegend=1

    
    
Special usecase:

    easyDescription.py --inputFileSamples samples.py --outputFileSamples extended_samples.py

    
