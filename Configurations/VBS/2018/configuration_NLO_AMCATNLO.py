# example of configuration file
treeName= 'Events'

date='ZZSelection_New_NLOAMCAT6tagnotflv'

tag = 'VBS_ZZSelection_New_NLOAMCAT6tagnotflv'+date


# used by mkShape to define output directory for root files
outputDir = 'rootFile'+date

# file with TTree aliases
aliasesFile = 'aliases.py'

# file with list of variables
variablesFile = 'variables.py'

# file with list of cuts
cutsFile = 'cuts_1.py'
#cutsFile = 'cuts_forPlots.py'

# file with list of samples
samplesFile = 'samples_NLOAMC.py'

# file with list of samples
plotFile = 'plot_NLOAMC.py'

# luminosity to normalize to (in 1/fb)
lumi = 59.74

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
outputDirPlots = 'plotVBS'+date


# used by mkDatacards to define output directory for datacards
outputDirDatacard = 'datacards'+date


# structure file for datacard
structureFile = 'structure.py'


# nuisances file for mkDatacards and for mkShape
nuisancesFile = 'nuisances.py'
