2016 configuration and optimization towards differential measurement
====


By following these instructions one should be able to read latino trees, produce histograms, make plots and datacards, combine the datacards, and extract the analysis significance.


# 0. Everything starts here

```
export CMSSW_DIRECTORY=~/CMSSW_8_0_26_patch1/src
export CONFIGURATION_DIRECTORY=$CMSSW_DIRECTORY/PlotsConfigurations/Configuration/YourConfigPath

```
Modify *$CMSSW_DIRECTORY/LatinoAnalysis/Tools/python/userConfig.py* (rename *userConfig_TEMPLATE.py* as *userConfig.py*)
```
#!/usr/bin/env python
baseDir  = '/gwpool/users/afendillo/'
jobDir   = baseDir+'jobs/'
workDir  = baseDir+'workspace/'
```
Change the baseDir location.
# 1. Produce histograms

This step reads the post-processed latino trees and produces histograms for several variables and phase spaces.

    cd $CONFIGURATION_DIRECTORY

    mkShapes.py --pycfg=configuration.py --batchSplit=AsMuchAsPossible --doBatch=True

The jobs can take a while, thus it is natural to check their status.

    mkBatch.py --status
To see all the jobs running on the batch system (hercules):

    qstat  

After all your jobs are finished, and before going to the next step, check the .jid files in the following output directory (the name of directory is specified in configuration.py):

    ls -l $CMSSW_DIRECTORY/jobs/mkShapes__VBS_SS_test/*.jid
    
If you find .jid files it means that the corresponding jobs failed, check the .err and .out files to understand the reason of the failure.

If several jobs failed and you want to resubmit them all at once you can do:
	
	for i in *jid; do qsub ${i/jid/sh}; done
To resubmit one job use

	qsub jobs/mkShapes__VBS_SS_test/*.sh
# 3. Put all your apples in one basket

Once the previous jobs have finished we _hadd_ the outputs.

    mkShapes.py --pycfg=configuration.py --batchSplit=AsMuchAsPossible -doHadd=True

*NB*: If the --batchSplit=AsMuchAsPossible option is used, do not _hadd_ the outputs by hand but use the command above instead. Otherwise the MC statistical uncertainties are not treated in the correct way.


# 4. Read histograms

At this stage one can either produce plots or datacards.

### Produce plots

Now we are ready to make data/MC comparison plots.

	mkPlot.py --inputFile=rootFile_test/plots_VBS_SS_test.root --scaleToPlot=1.9 --showIntegralLegend=1


### Produce datacards

    mkDatacards.py --pycfg=configuration.py --inputFile=rootFile_test/plots_VBS_SS_test.root

# 5. Combine Tools
Tool used to perform statistical analysis. The methods used for the inclusive measurement are:

Fit to extract the expected parameter

    combine -d path_to_datacard.txt -M FitDiagnostics -t -1 -m 125 -n VBS 

Expected significance

    combine -d path_to_datacard.txt -M Significance -t -1 -m 125 -n VBS 

All the measurements are performed using the blind option (-t -1)
# WZ

This is the configuration with the WZ EWK considered as signal as well. It can be used to define the WZ region and perform measurements about WZ scattering.


# Differential Configuration

They are the configurations used to perform the differential measurements.

Definition used:
* Gen-Parameters: the number of gen bins and the relative width defined to perform the study;
* Reco-Parameters: the bins and range used to define the fitted distribution

The procedure used to obtain the configurations can be summarized in three phases:

* Look for the variable that has the smaller variation between Gen and Reco-level distribution. This is done using both the response matrix and GenVsReco plots;
* The best variables (the leptonic ones) are compared using different configuration (changing both Gen and Reco level parameters) to find the most precise one;
* Further tests are performed on the best variable chosen looking for the best set of Gen-Bins and Reco-Parameters to use;

## Combine 
In this part of the analysis a multidimensional fit is employed:

Create the workspace: 

    text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel -m 125 --PO verbose --PO 'map=.*/Signal_bin0:r1[1,0,2]' --PO 'map=.*/Signal_bin1:r2[1,0,2]' --PO 'map=.*/Signal_bin2:r3[1,0,2]' path_to_datacard.txt -o workspace_name.root

Perform the multidimensional fit:

    combine -M MultiDimFit -m 125 --setParameters r1=1,r2=1,r3=1 --algo=singles -t -1 -S 1 --cl=0.68 workspace_name.root -n VBS_Diff_singles 

The blind option is used one again (-t -1)
