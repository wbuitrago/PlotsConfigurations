# example of configuration file


tag = '2017_sr_v6'
outputDir = 'rootFile'
treeName = 'Events'

# luminosity to normalize to
lumi = 41.53

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
# structure file for datacard
structureFile = 'structure.py'
# nuisances file for mkDatacards and for mkShape
nuisancesFile = 'nuisances.py'
# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
outputDirPlots = '/eos/user/f/fcetorel/www/VBS_OS/test/2017/signal_region_v6'
# used by mkDatacards to define output directory for datacards
outputDirDatacard = '/afs/cern.ch/work/f/fcetorel/private/work2/VBS_OS/CMSSW_10_2_15_patch2/src/PlotsConfigurations/Configurations/VBSOS/SignalRegions/2017/'


