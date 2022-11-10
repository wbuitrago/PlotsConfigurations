# Configuration file to produce initial root files 

treeName = 'Events'
import os
import copy
import inspect

folderpath = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
folderpath = os.path.dirname(folderpath)

with open(folderpath + "/config.py") as file:
    exec(file.read())

if extract:
    tag = 'extract_new_18'
    outputDir = 'extract/samples/' # create the directory first!
else:
    tag = 'vbf_zjj_2018'
    outputDir = 'rootFile'

# file with TTree aliases
aliasesFile = 'aliases.py'

# file with list of variables
variablesFile = 'variables.py'

# file with list of cuts
cutsFile = 'cuts.py' 

# file with list of samples
samplesFile = 'samples.py' 

# file with list of samples
plotFile = 'plot.py' 

# luminosity to normalize to (in 1/fb)
lumi = 59.74

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
#outputDirPlots = 'plots'
outputDirPlots = 'plots'


# used by mkDatacards to define output directory for datacards
outputDirDatacard = 'datacards'

# structure file for datacard
structureFile = 'structure.py'

# nuisances file for mkDatacards and for mkShape
nuisancesFile = 'nuisances.py'
