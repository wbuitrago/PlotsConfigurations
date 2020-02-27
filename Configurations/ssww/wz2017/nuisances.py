
# nuisances
from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight

def nanoGetSampleFiles(inputDir, Sample):
    return getSampleFiles(inputDir, Sample, False, 'nanoLatino_')

try:
    mc = [skey for skey in samples if skey != 'DATA' and not skey.startswith('Fake')]
except NameError:
    mc = []
    cuts = {}
    nuisances = {}
    def makeMCDirectory(x=''):
        return ''

nuisances['lumi']  = {
    'name'  : 'lumi_13TeV_2017',
    'samples'  : {
        'Vg'       : '1.023',
        'VgS'      : '1.023',
        'ZZ'   : '1.023',
        'WZ_QCD'       : '1.023',
        'WZ_EWK'       : '1.023',
        'VVV'      : '1.023',
        'DPS'  : '1.023',
        'WpWp_QCD'  : '1.023',
        'WpWp_EWK'   : '1.023',
    },
    'type'  : 'lnN',
}
# statistical fluctuation
# on MC/data
# "stat" is a special word to identify this nuisance
# Use the following if you want to apply the automatic combine MC stat nuisances->Faster than bin-by-bin
nuisances['stat']  = {
    'type'  : 'auto',
    'maxPoiss'  : '10',
    'includeSignal'  : '1',
    'samples' : {}
}


# Differnt type of uncentainties: type->ln N: (modify only event yeld) use a lognorm distributions with sigma = uncertainty. For normalization rateParam
# can be used--> use a uniform distribution;
# Shape: modify not only the events yelds but the event selection too (the shape) will run the varied shapes
# according to the following two possible kinds
# kind-> weight: Use the specified weight to reweight events;
# tree: uses the provided alternative trees;
# The MC statistics is a particular uncertainty: is caused by our finite statistics used to elaborate the template fits. Two approach: unfied and bin-by-bin (bbb)
