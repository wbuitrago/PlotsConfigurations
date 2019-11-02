# plot configuration

# groupPlot = {}
#
# Groups of samples to improve the plots.
# If not defined, normal plots is used
#

import copy

origcuts=copy.deepcopy(cuts)

print origcuts
cuts = []


for cut in origcuts:
    print cut
    for cat in origcuts[cut]['categories']:
        cuts.append(cut+"_"+cat)

print cuts

# groupPlot = {}
#
# Groups of samples to improve the plots (merge different sample during plot).
# If not defined, normal plots is used
#
Red=632; Violet=880; Green=416; Orange=800; Yellow=400; Azure=860; signal=0
groupPlot['VV']  = {
                  'nameHR' : "VV",
                  'isSignal' : 0,
                  'color'    : ROOT.kMagenta-10, # kViolet+10
                  'samples'  : ['WZ','ZZ','WZ_EWK']
              }
groupPlot['VVV']  = {
    'nameHR' : 'VVV',
    'isSignal' : 0,
    'color': ROOT.kSpring-9, # kGreen
    'samples'  : ['VVV']
}
groupPlot['TTV']  = {
    'nameHR' : 'TTV',
    'isSignal' : 0,
    'color': ROOT.kGray, # kGreen
    'samples'  : ['TTV']
}
groupPlot['DPS']  = {
    'nameHR' : 'DPS',
    'isSignal' : 0,
    'color': ROOT.kGray+5, # kGreen
    'samples'  : ['DPS']
}
groupPlot['Vg']  = {
                  'nameHR' : "V#gamma",
                  'isSignal' : 0,
                  'color'    : ROOT.kCyan-7,   # kOrange + 10
                  'samples'  : ['Vg']
              }

groupPlot['WW_strong']  = {
                  'nameHR' : "WW QCD",
                  'isSignal' : 0,
                  'color'    : ROOT.kViolet-4, # kViolet
                  'samples'  : ['WW_strong']
              }



groupPlot['non-prompt']  = {
                  'nameHR' : 'non-Prompt',
                  'isSignal' : 0,
                  'color': ROOT.kYellow-4,    # kYellow
                  'samples'  : ['Fake_lep']
              }
'''
groupPlot['TL_TT']  = {
                  'nameHR' : "SSWW TTTL",
                  'isSignal' : 0,
                  'color'    : Azure+8, # kAzure+4
                  'samples'  : ['TL_TT']
              }
groupPlot['LL']  = {
                  'nameHR' : "SSWW LL",
                  'isSignal' : 0,
                  'color'    : Azure+4, # kAzure+4
                  'samples'  : ['LL']
              }
'''
'''
groupPlot['WpWp_EWK']  = {
                  'nameHR' : "WW EWK",
                  'isSignal' : 0,
                  'color'    : ROOT.kBlue-7, # kAzure+4
                  'samples'  : ['WW_EWK']
              }
'''
groupPlot['WW_EWK_bin0']  = {'nameHR' : "Signal bin 0",
                             'isSignal' : signal,
                             'color'    : ROOT.kAzure-9, # kAzure+4
                             'samples'  : ['Signal_bin0']
                             }
plot['Signal_bin0']  = {
    'color': ROOT.kAzure-9,
    'isSignal': 0,
    'isData': 0,
    'scale': 1.
    }
groupPlot['WW_EWK_bin1']  = {'nameHR' : "Signal bin 1",
                             'isSignal' : signal,
                             'color'    : ROOT.kAzure-4, # kAzure+4
                             'samples'  : ['Signal_bin1']
                             }
plot['Signal_bin1']  = {
    'color': ROOT.kAzure-4,
    'isSignal': 0,
    'isData': 0,
    'scale': 1.
    }
groupPlot['WW_EWK_bin2']  = {'nameHR' : "Signal bin 2",
                             'isSignal' : signal,
                             'color'    : ROOT.kAzure, # kAzure+4
                             'samples'  : ['Signal_bin2']
                             }
plot['Signal_bin2']  = {
    'color': ROOT.kAzure-2,
    'isSignal': 0,
    'isData': 0,
    'scale': 1.
    }
groupPlot['WW_EWK_bin3']  = {'nameHR' : "Signal bin 3",
                             'isSignal' : signal,
                             'color'    : ROOT.kAzure+4, # kAzure+4
                             'samples'  : ['Signal_bin3']
                             }
plot['Signal_bin3']  = {
    'color': ROOT.kAzure+4,
    'isSignal': 0,
    'isData': 0,
    'scale': 1.
    }
groupPlot['WW_EWK_bin4']  = {'nameHR' : "Signal bin 4",
                             'isSignal' : signal,
                             'color'    : ROOT.kAzure+8, # kAzure+4
                             'samples'  : ['Signal_bin4']
                             }
plot['Signal_bin4']  = {
    'color': ROOT.kAzure+8,
    'isSignal': 0,
    'isData': 0,
    'scale': 1.
    }
#plot = {}

# keys here must match keys in samples.py
#
##Fake and prompt substraction
plot['Fake_lep']  = {
    'color': Yellow,    # kYellow
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}

##Signal
'''
plot['WW_EWK']  = {
    'color': Azure+4, # kAzure+4
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}
plot['LL']  = {
    'color': Azure+4, # kAzure+4
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}
plot['TL_TT']  = {
    'color': Azure+8, # kAzure+4
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}
'''
plot['WW_strong']  = {
    'color': Violet, # kViolet
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}

plot['Vg']  = {
    'color': Orange+10, # kOrange+10
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}
##Reducible Background
##VV plot
plot['ZZ']  = {
    'color': Violet+10, # kViolet+10
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}
plot['WZ']  = {
    'color': Violet+10, # kViolet+10
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}
plot['DPS']  = {
    'color': Violet+10, # kViolet+10
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}
##VVV
plot['VVV']  = {
    'color': Green, # kGreen
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}
plot['TTV']  = {
    'color': Green+10, # kGreen
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}
##Data
plot['DATA']  = {
    'nameHR' : 'Data',
    'color': 1 ,
    'isSignal' : 0,
    'isData'   : 1 ,
    'isBlind'  : 1 ,
    'scale'    : 1.0
}

# additional options
legend['lumi'] = 'L = 35.867/fb'

legend['sqrt'] = '#sqrt{s} = 13 TeV'
