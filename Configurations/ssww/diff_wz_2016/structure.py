# structure configuration for datacard

#structure = {}

# keys here must match keys in samples.py
#

## Reducible Bkg

structure['Vg']  = {
    'isSignal' : 0,
    'isData'   : 0
}

#structure['ChMisId']  = {
#    'isSignal' : 0,
#    'isData'   : 0
#}

#structure['ttbar'] = {
#    'isSignal' : 0,
#    'isData'   : 0
#}

structure['ZZ']  = {
    'isSignal' : 0,
    'isData'   : 0
}

structure['WZ_QCD']  = {
    'isSignal' : 0,
    'isData'   : 0
}

structure['WZ_EWK']  = {
    'isSignal' : 0,
    'isData'   : 0
}
structure['WZTo2L2Q']  = {
    'isSignal' : 0,
    'isData'   : 0
}
structure['VgS2']  = {
    'isSignal' : 0,
    'isData'   : 0
}
structure['DPS']  = {
    'isSignal' : 0,
    'isData'   : 0
}

structure['VVV']  = {
    'isSignal' : 0,
    'isData'   : 0,
}
structure['TTV']  = {
    'isSignal' : 0,
    'isData'   : 0,
}
##Irreducible Bkg

structure['WpWp_QCD']  = {
    'isSignal' : 0,
    'isData'   : 0
}

##Signal
structure['WpWp_EWK']  = {
    'isSignal' : 1,
    'isData'   : 0
}
#Fake
structure['Fake_lep']  = {
    'isSignal' : 0,
    'isData'   : 0,
}

# data


structure['DATA']  = {
    'isSignal' : 0,
    'isData'   : 1
}