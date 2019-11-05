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
Red=632; Violet=880; Green=416; Orange=800; Yellow=400; Azure=860
groupPlot['ZZ']  = {
    'nameHR' : "ZZ",
    'isSignal' : 0,
    'color'    : ROOT.kMagenta-10, # kViolet+10
    'samples'  : ['ZZ']
}
groupPlot['WZ_QCD']  = {
    'nameHR' : "WLLJJ_QCD",
    'isSignal' : 0,
    'color'    : ROOT.kRed, # kViolet+10
    'samples'  : ['WZ']
}
groupPlot['WZ_EWK']  = {
    'nameHR' : "WLLJJ_EWK",
    'isSignal' : 0,
    'color'    : ROOT.kMagenta, # kViolet+10
    'samples'  : ['WZ_EWK']
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
    'samples'  : ['Vg','VgS']
}

groupPlot['WW_strong']  = {
    'nameHR' : "W^{#pm}W^{#pm} QCD",
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
groupPlot['WpWp_EWK']  = {
    'nameHR' : "W^{#pm}W^{#pm} EWK",
    'isSignal' : 0,
    'color'    : ROOT.kBlue-7, # kAzure+4
    'samples'  : ['WW_EWK']
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
plot['WW_EWK']  = {
    'color': Azure+4, # kAzure+4
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}
'''
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
plot['VgS']  = {
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
plot['WZ_EWK']  = {
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
    'isBlind'  : 0 ,
    'scale'    : 1.0
}

# additional options
legend['lumi'] = 'L = 35.92/fb'

legend['sqrt'] = '#sqrt{s} = 13 TeV'
