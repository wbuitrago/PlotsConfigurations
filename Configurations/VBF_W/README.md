To install
====

    cmsrel CMSSW_10_6_4
    cd CMSSW_10_6_4/src/
    cmsenv

    git clone --branch 13TeV git@github.com:latinos/setup.git LatinosSetup

    source LatinosSetup/SetupShapeOnly.sh

    scramv1 b -j 20

    git clone -b VBF_W  git@github.com:UniMiBAnalyses/PlotsConfigurations.git

    scramv1 b -j 20

    
Customization:

    cd LatinoAnalysis/Tools/python
    cp userConfig_TEMPLATE.py userConfig.py
    # edit the userConfig.py so the paths correspond to a directory where you have write access (this will be used to write log files)
    cd -
    scramv1 b -j 20
    
    
   
