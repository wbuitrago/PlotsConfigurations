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


Red=632; Violet=880; Green=416; Orange=800; Yellow=400; Azure=860; Grey=920

eft_scale = 1.0

# to use this just comment out groupplots for all the samples included
# Other Bgr
groupPlot['Other Bgr']  = {
    'nameHR'   : "Other Bgr",
    'isSignal' : 0,
    'color'    : ROOT.kGreen,
    'samples'  : ['ZZ','VVV','TTV','DPS']
}
# groupPlot['ZZ']  = {
#     'nameHR' : "ZZ",
#     'isSignal' : 0,
#     'color'    : ROOT.kMagenta-10, # kViolet+10
#     'samples'  : ['ZZ']
# }
# groupPlot['VVV']  = {
#     'nameHR' : 'VVV',
#     'isSignal' : 0,
#     'color': ROOT.kSpring-9, # kGreen
#     'samples'  : ['VVV']
# }
# groupPlot['TTV']  = {
#     'nameHR' : 'TTV',
#     'isSignal' : 0,
#     'color': ROOT.kGray, # kGreen
#     'samples'  : ['TTV']
# }
# groupPlot['DPS']  = {
#     'nameHR' : 'DPS',
#     'isSignal' : 0,
#     'color': ROOT.kGray, # kGreen
#     'samples'  : ['DPS']
# }
groupPlot['WZ_QCD']  = {
    'nameHR' : "WZ QCD",
    'isSignal' : 0,
    'color'    : ROOT.kRed, # kViolet+10
    'samples'  : ['WZ_QCD']
}
groupPlot['WLLJJ_EWK']  = {
    'nameHR' : "WZ EWK",
    'isSignal' : 0,
    'color'    : ROOT.kMagenta, # kViolet+10
    'samples'  : ['WLLJJ_EWK']
}
groupPlot['Vg']  = {
                  'nameHR' : "V#gamma",
                  'isSignal' : 0,
                  'color'    : ROOT.kOrange,   # kOrange + 10
                  'samples'  : ['Vg','VgS_L','VgS_H']
              }
groupPlot['WW_QCD']  = {
                  'nameHR' : "W^{#pm}W^{#pm} QCD",
                  'isSignal' : 0,
                  'color'    : ROOT.kViolet, # kViolet
                  'samples'  : ['WW_QCD']
              }
groupPlot['non-prompt']  = {
                  'nameHR' : 'non-Prompt',
                  'isSignal' : 0,
                  'color': ROOT.kYellow,    
                  'samples'  : ['Fake_lep']
              }

groupPlot['mischarge']  = {
                  'nameHR'   : "MisCharge",
                  'isSignal' : 0,
                  'color'    : ROOT.kGreen + 2, 
                  'samples'  : ['DY','top','WW','WWewk','ggWW']
              }

# SM official samples
groupPlot['WW_EWK']  = {
                  'nameHR' : "W^{#pm}W^{#pm} EWK",
                  'isSignal' : 1,
                  'color'    : ROOT.kBlue-7, # kAzure+4
                  'samples'  : ['WpWp_EWK']
              }


# #####################################
# # EFT samples (internal latinos)

# groupPlot['WW_EWK_sm']  = {
#                   'nameHR'   : "W^{#pm}W^{#pm} EWK sm",
#                   'isSignal' : 3,
#                   'color'    : ROOT.kBlue, 
#                   'samples'  : ['sm']
#               }              

# groupPlot['WW_EWK_int']  = {
#                   'nameHR'   : "EFT C_{W} int",
#                   'isSignal' : 3,
#                   'color'    : ROOT.kViolet, 
#                   'samples'  : ['linear']
#               }
# groupPlot['WW_EWK_bsm']  = {
#                   'nameHR'   : "EFT C_{W} bsm",
#                   'isSignal' : 3,
#                   'color'    : ROOT.kCyan, 
#                   'samples'  : ['quadratic']
#               }
# #####################################


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

plot['WZ_QCD']  = {
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

plot['WW_QCD']  = {
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
plot['VgS_L']  = {
    'color': Orange+10, # kOrange+10
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}
plot['VgS_H']  = {
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

# mischarge samples
#---------------------------------
# mischarge_SF = 1.7
mischarge_SF = 1.0
plot['DY']  = {
    'color': Grey, # kGreen
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : mischarge_SF
}
plot['top']  = {
    'color': Grey, # kGreen
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : mischarge_SF
}
plot['WW']  = {
    'color': Grey, # kGreen
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : mischarge_SF
}
plot['WWewk']  = {
    'color': Grey, # kGreen
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : mischarge_SF
}
plot['ggWW']  = {
    'color': Grey, # kGreen
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : mischarge_SF
}
#---------------------------------


##Signal
plot['WpWp_EWK']  = {
    'color': Azure+4, # kAzure+4
    'isSignal' : 1,
    'isData'   : 0,
    'scale'    : 1.0
}

#####################################

# # EFT samples (private prod.)
# ## Standard Model
# eft_scale = 1.0
# plot['sm']  = {
#     'color': Azure+4, # kAzure+4
#     'isSignal' : 1,
#     'isData'   : 0,
#     'scale'    : 1.0
# }

# ## Linear Interference Term
# plot['linear']  = {
#     'color': Red+4, # kAzure+4
#     'isSignal' : 1,
#     'isData'   : 0,
#     'scale'    : eft_scale
# }

# ## Quadratic BSM Term
# plot['quadratic']  = {
#     'color': Azure+4, # kAzure+4
#     'isSignal' : 1,
#     'isData'   : 0,
#     'scale'    : eft_scale
# }            

#####################################

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
legend['lumi'] = 'L = 59.74/fb'

legend['sqrt'] = '#sqrt{s} = 13 TeV'
