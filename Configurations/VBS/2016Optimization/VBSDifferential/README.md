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

    mkShapes.py --pycfg=configuration.py \
                --batchSplit=AsMuchAsPossible \
                --doBatch=True

The jobs can take a while, thus it is natural to check their status.

    mkBatch.py --status
To see all the jobs running on the batch system:

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

    mkShapes.py --pycfg=configuration.py \
                --batchSplit=AsMuchAsPossible \
                --doHadd=True
*NB*: If the --batchSplit=AsMuchAsPossible option is used, do not _hadd_ the outputs by hand but use the command above instead. Otherwise the MC statistical uncertainties are not treated in the correct way.


# 4. Read histograms

At this stage one can either produce plots or datacards.

### Produce plots

Now we are ready to make data/MC comparison plots.

	mkPlot.py --inputFile=rootFile_test/plots_VBS_SS_test.root \ 
		  --scaleToPlot=1.9 \
  		  --showIntegralLegend=1


### Produce datacards

    mkDatacards.py --pycfg=configuration.py \
                   --inputFile=rootFile_test/plots_VBS_SS_test.root
### Combine

First create the workspace for MultiParamateres Fit:

	text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --PO verbose \
--PO 'map=.*/Signal_bin0:r1[1,0.8,1.2]' \
--PO 'map=.*/Signal_bin1:r2[1,0.8,1.2]' \
--PO 'map=.*/Signal_bin2:r3[1,0.8,1.2]' \
pt1.combined.txt -o workspace.pt1.combined.txt.root


	combine -M MultiDimFit -t -1 --setParameters r1=1,r2=1,r3=1 --algo=grid --points=1000 workspace.pt1.root > result.MultiDimFit.workspace.pt1.root.grid.txt

