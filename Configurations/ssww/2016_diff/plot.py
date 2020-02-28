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
groupPlot['Vg']  = {
    'nameHR' : "V#gamma",
    'isSignal' : 0,
    'color'    : ROOT.kCyan-7,   # kOrange + 10
    'samples'  : ['Vg','VgS']
}
groupPlot['ZZ']  = {
    'nameHR' : "ZZ",
    'isSignal' : 0,
    'color'    : ROOT.kMagenta, # kViolet+10
    'samples'  : ['ZZ']
}
groupPlot['WZ_QCD']  = {
    'nameHR' : "WZ_QCD",
    'isSignal' : 0,
    'color'    : ROOT.kRed, # kViolet+10
    'samples'  : ['WZ_QCD']
}
groupPlot['WZ_EWK']  = {
    'nameHR' : "WZ_EWK",
    'isSignal' : 0,
    'color'    : ROOT.kMagenta-10, # kViolet+10
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
groupPlot['WpWp_QCD']  = {
    'nameHR' : "W^{\pm}W^{\pm} QCD",
    'isSignal' : 0,
    'color'    : ROOT.kViolet-4, # kViolet
    'samples'  : ['WpWp_QCD']
}



groupPlot['non-prompt']  = {
    'nameHR' : 'non-Prompt',
    'isSignal' : 0,
    'color': ROOT.kYellow-4,    # kYellow
    'samples'  : ['Fake_lep']
}
'''
groupPlot['WpWp_EWK_fid']  = {
                  'nameHR' : "WpWpEWK_fid",
                  'isSignal' : 0,
                  'color'    : ROOT.kBlue-7, # kAzure+4
                  'samples'  : ['WpWp_EWK_fid']
              }
'''
groupPlot['WpWp_EWK_out']  = {
                  'nameHR' : "WpWpEWK_out",
                  'isSignal' : 0,
                  'color'    : ROOT.kBlue, # kAzure+4
                  'samples'  : ['WpWp_EWK_out']
              }
plot['WpWp_EWK_out']  = {
    'color': Yellow,    # kYellow
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}
'''
# lep1 pt
groupPlot['WpWp_EWK_lep1pt_bin0']  = {
                  'nameHR' : "WpWp EWK bin0",
                  'isSignal' : 0,
                  'color'    : ROOT.kBlue-7, # kAzure+4
                  'samples'  : ['WpWp_EWK_lep1pt_bin0']
              }
plot['WpWp_EWK_lep1pt_bin0']  = {
    'color': Yellow,    # kYellow
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}
groupPlot['WpWp_EWK_lep1pt_bin1']  = {
                  'nameHR' : "WpWp EWK bin1",
                  'isSignal' : 0,
                  'color'    : ROOT.kBlue-3, # kAzure+4
                  'samples'  : ['WpWp_EWK_lep1pt_bin1']
              }
plot['WpWp_EWK_lep1pt_bin1']  = {
    'color': Yellow,    # kYellow
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}
groupPlot['WpWp_EWK_lep1pt_bin2']  = {
                  'nameHR' : "WpWp EWK bin2",
                  'isSignal' : 0,
                  'color'    : ROOT.kBlue, # kAzure+4
                  'samples'  : ['WpWp_EWK_lep1pt_bin2']
              }
plot['WpWp_EWK_lep1pt_bin2']  = {
    'color': Yellow,    # kYellow
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}
# lep2 pt
groupPlot['WpWp_EWK_lep2pt_bin0']  = {
                  'nameHR' : "WpWp EWK bin0",
                  'isSignal' : 0,
                  'color'    : ROOT.kBlue-7, # kAzure+4
                  'samples'  : ['WpWp_EWK_lep2pt_bin0']
              }
plot['WpWp_EWK_lep2pt_bin0']  = {
    'color': Yellow,    # kYellow
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}
groupPlot['WpWp_EWK_lep2pt_bin1']  = {
                  'nameHR' : "WpWp EWK bin1",
                  'isSignal' : 0,
                  'color'    : ROOT.kBlue-3, # kAzure+4
                  'samples'  : ['WpWp_EWK_lep2pt_bin1']
              }
plot['WpWp_EWK_lep2pt_bin1']  = {
    'color': Yellow,    # kYellow
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}
groupPlot['WpWp_EWK_lep2pt_bin2']  = {
                  'nameHR' : "WpWp EWK bin2",
                  'isSignal' : 0,
                  'color'    : ROOT.kBlue, # kAzure+4
                  'samples'  : ['WpWp_EWK_lep2pt_bin2']
              }
plot['WpWp_EWK_lep2pt_bin2']  = {
    'color': Yellow,    # kYellow
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}
# jet1 pt
groupPlot['WpWp_EWK_jet1pt_bin0']  = {
                  'nameHR' : "WpWp EWK bin0",
                  'isSignal' : 0,
                  'color'    : ROOT.kBlue-7, # kAzure+4
                  'samples'  : ['WpWp_EWK_jet1pt_bin0']
              }
plot['WpWp_EWK_jet1pt_bin0']  = {
    'color': Yellow,    # kYellow
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}
groupPlot['WpWp_EWK_jet1pt_bin1']  = {
                  'nameHR' : "WpWp EWK bin1",
                  'isSignal' : 0,
                  'color'    : ROOT.kBlue-3, # kAzure+4
                  'samples'  : ['WpWp_EWK_jet1pt_bin1']
              }
plot['WpWp_EWK_jet1pt_bin1']  = {
    'color': Yellow,    # kYellow
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}
groupPlot['WpWp_EWK_jet1pt_bin2']  = {
                  'nameHR' : "WpWp EWK bin2",
                  'isSignal' : 0,
                  'color'    : ROOT.kBlue, # kAzure+4
                  'samples'  : ['WpWp_EWK_jet1pt_bin2']
              }
plot['WpWp_EWK_jet1pt_bin2']  = {
    'color': Yellow,    # kYellow
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}
# jet2pt
groupPlot['WpWp_EWK_jet2pt_bin0']  = {
                  'nameHR' : "WpWp EWK bin0",
                  'isSignal' : 0,
                  'color'    : ROOT.kBlue-7, # kAzure+4
                  'samples'  : ['WpWp_EWK_jet2pt_bin0']
              }
plot['WpWp_EWK_jet2pt_bin0']  = {
    'color': Yellow,    # kYellow
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}
groupPlot['WpWp_EWK_jet2pt_bin1']  = {
                  'nameHR' : "WpWp EWK bin1",
                  'isSignal' : 0,
                  'color'    : ROOT.kBlue-3, # kAzure+4
                  'samples'  : ['WpWp_EWK_jet2pt_bin1']
              }
plot['WpWp_EWK_jet2pt_bin1']  = {
    'color': Yellow,    # kYellow
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}
groupPlot['WpWp_EWK_jet2pt_bin2']  = {
                  'nameHR' : "WpWp EWK bin2",
                  'isSignal' : 0,
                  'color'    : ROOT.kBlue, # kAzure+4
                  'samples'  : ['WpWp_EWK_jet2pt_bin2']
              }
plot['WpWp_EWK_jet2pt_bin2']  = {
    'color': Yellow,    # kYellow
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}
# mll
groupPlot['WpWp_EWK_mll_bin0']  = {
                  'nameHR' : "WpWp EWK bin0",
                  'isSignal' : 0,
                  'color'    : ROOT.kBlue-7, # kAzure+4
                  'samples'  : ['WpWp_EWK_mll_bin0']
              }
plot['WpWp_EWK_mll_bin0']  = {
    'color': Yellow,    # kYellow
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}
groupPlot['WpWp_EWK_mll_bin1']  = {
                  'nameHR' : "WpWp EWK bin1",
                  'isSignal' : 0,
                  'color'    : ROOT.kBlue-3, # kAzure+4
                  'samples'  : ['WpWp_EWK_mll_bin1']
              }
plot['WpWp_EWK_mll_bin1']  = {
    'color': Yellow,    # kYellow
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}
groupPlot['WpWp_EWK_mll_bin2']  = {
                  'nameHR' : "WpWp EWK bin2",
                  'isSignal' : 0,
                  'color'    : ROOT.kBlue, # kAzure+4
                  'samples'  : ['WpWp_EWK_mll_bin2']
              }
plot['WpWp_EWK_mll_bin2']  = {
    'color': Yellow,    # kYellow
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}
'''
# mjj
groupPlot['WpWp_EWK_mjj_bin0']  = {
    'nameHR' : "WpWp EWK bin0",
    'isSignal' : 0,
    'color'    : ROOT.kBlue-7, # kAzure+4
    'samples'  : ['WpWp_EWK_mjj_bin0']
}
plot['WpWp_EWK_mjj_bin0']  = {
    'color': Yellow,    # kYellow
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}
groupPlot['WpWp_EWK_mjj_bin1']  = {
    'nameHR' : "WpWp EWK bin1",
    'isSignal' : 0,
    'color'    : ROOT.kBlue-3, # kAzure+4
    'samples'  : ['WpWp_EWK_mjj_bin1']
}
plot['WpWp_EWK_mjj_bin1']  = {
    'color': Yellow,    # kYellow
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}
groupPlot['WpWp_EWK_mjj_bin2']  = {
    'nameHR' : "WpWp EWK bin2",
    'isSignal' : 0,
    'color'    : ROOT.kBlue, # kAzure+4
    'samples'  : ['WpWp_EWK_mjj_bin2']
}
plot['WpWp_EWK_mjj_bin2']  = {
    'color': Yellow,    # kYellow
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
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

plot['WpWp_QCD']  = {
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
plot['WZ_QCD']  = {
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
    'isBlind'  : 1 ,
    'scale'    : 1.0
}

# additional options
legend['lumi'] = 'L = 35.92/fb'

legend['sqrt'] = '#sqrt{s} = 13 TeV'