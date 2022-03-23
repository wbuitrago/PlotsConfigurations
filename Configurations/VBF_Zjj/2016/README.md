Signal region
=====================

How to run the analysis.
    
# Produce the shapes:

    mkShapesMulti.py --pycfg=configuration.py --doBatch=1 --batchSplit=Samples,Files --batchQueue=workday

# Hadd the root files:

    mkShapesMulti.py --pycfg=configuration.py --doHadd=1 --batchSplit=Samples,Files --doNotCleanup --nThreads=10

or

    hadd rootFile/plots_vbf_zjj_2016.root rootFile/plots_vbf_zjj_2016_ALL_*.root

    
# Resubmit:

    ls -alrth /afs/cern.ch/user/a/amassiro/jobs/jobs/mkShapes__vbf_zjj_2016__ALL/*/mkShapes__*.jid | awk '{print "  sed -i @s/workday/tomorrow/g@      " $9}'  | tr "@" "'" |  sed 's/jid/jds/'    

    ls -alrth /afs/cern.ch/user/a/amassiro/jobs/jobs/mkShapes__vbf_zjj_2016__ALL/*/mkShapes__*.jid | awk '{print "condor_submit " $9}'  | sed 's/jid/jds/'    

        
        
# Make plots:

    mkPlot.py --pycfg=configuration.py --inputFile rootFile/plots_vbf_zjj_2016.root --onlyPlot=cratio --linearOnly --showIntegralLegend=1
    mkPlot.py --pycfg=configuration.py --inputFile rootFile/plots_vbf_zjj_2016.root --showIntegralLegend=1
    mkPlot.py --pycfg=configuration.py --inputFile rootFile/plots_vbf_zjj_2016.root --showIntegralLegend=1  --plotNormalizedDistributionsTHstack
    mkPlot.py --pycfg=configuration.py --inputFile rootFile/plots_vbf_zjj_2016.root --showIntegralLegend=1  --plotNormalizedDistributions

    
    
    
Special usecase:

    easyDescription.py --inputFileSamples samples.py --outputFileSamples extended_samples.py

    

# Make datacards

    mkDatacards.py --pycfg configuration.py --inputFile rootFile/plots_vbf_zjj_2016.root

    
# combine datacards 

    cd /afs/cern.ch/user/a/amassiro/Framework/Combine/CMSSW_10_2_13/src/
    cmsenv
    cd -
    

    combineCards.py ewkz_topcr=datacards/Top_13TeV_2j_eemm/events/datacard.txt \
                    ewkz_wwcr=datacards/WW_13TeV_2j_eemm/events/datacard.txt \
                    ewkz_zjjhigh=datacards/Zjj_13TeV_2j_eemm-high/detajjmjj/datacard.txt \
                    ewkz_zjjlow=datacards/Zjj_13TeV_2j_eemm-low/detajjmjj/datacard.txt \
                    > combined.txt
                    
                    
    text2workspace.py     combined.txt    -o combined.root

    
# fit 


    combine -M FitDiagnostics   -t -1 --expectSignal=1 combined.root   &> logFit.txt
    combine -M AsymptoticLimits -t -1 --expectSignal=0 combined.root   &> logLimit.txt
    combine -M Significance     -t -1 --expectSignal=1 combined.root   &> logSignificance.txt
