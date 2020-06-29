# plot configuration

# groupPlot = {}
#
# Groups of samples to improve the plots.
# If not defined, normal plots is used
#

# groupPlot = {}
#
# Groups of samples to improve the plots (merge different sample during plot).
# If not defined, normal plots is used
#

# TEMPLATE for groupPlot[] dictionary entry
# groupPlot['GROUPNAME']  = {  
#                   'nameHR' : "NAME THAT GOES IN THE LEGEND",
#                   'isSignal' : 0, #overrides entries in plot
#                   'color'    : 617,   #overrides entries in plot
#                   'samples'  : [] #List of sampels to group under the same name in the legend
# }

# TEMPLATE for plot[] dictionary entry
# plot['NAME']  = { #same name as in samples.py  
#     'color': 418,    # kGreen+2
#     'isSignal' : VALUE, # 0 -> background: all samples with this flag set to 0 are plotted stacked. 
#                                 # 1 -> is signal: this gets plotted both stacked and superimposed
#                                 # 2 -> is signal: this gets plotted only superimposed, not stacked. 
#     'isData'   : 0, #0/1 with obvious meaning. It is not a duplicate of structure.py. This is used to handle blinding. See below.
#     'isBlind' : 0 # if set to 1, all samples with isData = 1 are not shown.
#     'scale'    : 1.0, # OPTIONAL whether to scale the sample by a fixed amount
#     'cuts'  : {       #OPTIONAL: whether to plot this sample only for specified cuts and applying the specified scale factor.
#                        'cut name'      : scale value ,
#      },
# }


Red=632; Violet=880; Green=416; Orange=800; Yellow=400; Azure=860
# other bgr


# group plots for signal region
# other_bgr contains all the minor backgrounds

# WW QCD
groupPlot['WW_strong']  = {
                  'nameHR' : "W^{#pm}W^{#pm} QCD",
                  'isSignal' : 0,
                  'color'    : ROOT.kRed, # kViolet
                  'samples'  : ['WW_strong']
              }

# WZ EWK
groupPlot['WLLJJ_EWK']  = {
    'nameHR' : "WZ EWK",
    'isSignal' : 0,
    'color'    : ROOT.kCyan, # kViolet+10
    'samples'  : ['WLLJJ_EWK']
}

# Other Bgr
groupPlot['Other Bgr']  = {
    'nameHR' : "Other Bgr",
    'isSignal' : 0,
    'color'    : ROOT.kGreen, # kViolet+10
    'samples'  : ['ZZ','VVV','TTV','DPS','Vg','VgS']
}

# WZ QCD
groupPlot['WLLJJ_QCD']  = {
    'nameHR' : "WZ QCD",
    'isSignal' : 0,
    'color'    : ROOT.kOrange, # kViolet+10
    'samples'  : ['WLLJJ_QCD','WZTo2L2Q']
}

# non-prompt
groupPlot['non-prompt']  = {
                  'nameHR' : 'non-Prompt',
                  'isSignal' : 0,
                  'color': ROOT.kYellow,    # kYellow
                  'samples'  : ['Fake_lep']
              }
# signal
groupPlot['WW_EWK']  = {
                  'nameHR' : "W^{#pm}W^{#pm} EWK",
                  'isSignal' : 1,
                  'color'    : ROOT.kBlue, # kAzure+4
                  'samples'  : ['WpWp_EWK']
              }

# plot = {}

# keys here must match keys in samples.py

plot['WLLJJ_QCD']  = {
    'color': Violet+10, # kViolet+10
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}
plot['WZTo2L2Q']  = {
    'color': Violet+10, # kViolet+10
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}
plot['WLLJJ_EWK']  = {
    'color': Violet+10, # kViolet+10
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}
##Fake and prompt substraction
plot['Fake_lep']  = {
    'color': Yellow,    # kYellow
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}
##Signal
plot['WpWp_EWK']  = {
    'color': Azure+4, # kAzure+4
    'isSignal' : 1,
    'isData'   : 0,
    'scale'    : 1.0
}
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
legend['lumi'] = 'L = 41.53/fb'

legend['sqrt'] = '#sqrt{s} = 13 TeV'
