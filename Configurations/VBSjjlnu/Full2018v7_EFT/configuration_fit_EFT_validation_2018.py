# example of configuration file
treeName= 'Events'


tag = 'fit_2018_split_EFT_validation'
direc = "conf_fit_EFT_validation"

# used by mkShape to define output directory for root files
outputDir = 'rootFile_'+tag 

# file with TTree aliases
aliasesFile = direc+'/aliases.py'

# file with list of variables
variablesFile = direc+'/variables_EFT.py'

# file with list of cuts
cutsFile = direc +'/cuts.py' 

# file with list of samples
samplesFile = direc+'/samples_split.py' 
# samplesFile = direc+'/samples.py'

#t file with list of samples
plotFile = direc+'/plot_EFT.py' 

# luminosity to normalize to (in 1/fb)
lumi = 59.74

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
#outputDirPlots = 'plot_'+tag +"_rescaled/detajpt_ext"
outputDirPlots = 'plot_'+tag  

# used by mkDatacards to define output directory for datacards
outputDirDatacard = 'datacards_'+tag 
# outputDirDatacard = 'datacards_'+tag +"_Dipole_split_v4"

# structure file for datacard
structureFile = direc+'/structure_split.py'


# nuisances file for mkDatacards and for mkShape
# nuisancesFile = direc+'/nuisances.py'
# nuisancesFile = direc + '/nuisances_datacard_split.py'
# nuisancesFile = direc + '/nuisances_datacard_split_2pois.py'
nuisancesFile = direc + '/nuisances_EFT.py'


customizeScript = direc + '/customize.py'
