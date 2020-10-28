# example of configuration file

tag = 'vbs_2016'
outputDir = 'rootFile'
treeName = 'Events'
date='181020'
# luminosity to normalize to
lumi = 35.9

# file with TTree aliases
aliasesFile = 'aliases.py'

# file with list of variables
variablesFile = 'variables.py' 

# file with list of cuts
cutsFile = 'cuts.py' 

# file with list of samples
samplesFile = 'samples.py' 

# file with list of plot
plotFile = 'plot.py'

# nuisances file for mkDatacards and for mkShape
nuisancesFile = 'nuisances.py'
# structure file for datacard
structureFile = 'structure.py'

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
outputDirPlots = '/eos/user/f/fcetorel/www/VBS_OS/test/2016/ControlRegions_v6_'+date

