
# nuisances

#nuisances = {}

# name of samples here must match keys in samples.py

################################ EXPERIMENTAL UNCERTAINTIES  #################################

#### Luminosity
# luminosity uncertainty is 2.3%

nuisances['lumi']  = {
    'name'  : 'lumi_13TeV_2018',
    'samples'  : {
        'sm'                : '1.023',
        'sm_lin_quad_cqq1'  : '1.023',
        'quad_cqq1'         : '1.023',
        'sm_lin_quad_cqq11' : '1.023',
        'quad_cqq11'        : '1.023',
        'sm_lin_quad_cqq3'  : '1.023',
        'quad_cqq3'         : '1.023',
        'sm_lin_quad_cqq31' : '1.023',
        'quad_cqq31'        : '1.023',
        'sm_lin_quad_cW'    : '1.023',
        'quad_cW'           : '1.023',
        'sm_lin_quad_cHl3'  : '1.023',
        'quad_cHl3'         : '1.023',
        'sm_lin_quad_cHq3'  : '1.023',
        'quad_cHq3'         : '1.023',
        'sm_lin_quad_cll1'  : '1.023',
        'quad_cll1'         : '1.023',
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
