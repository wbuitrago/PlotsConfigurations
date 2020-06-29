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
# groupPlot['Other Bgr']  = {
#     'nameHR'   : "Other Bgr",
#     'isSignal' : 0,
#     'color'    : ROOT.kGreen,
#     'samples'  : ['ZZ','VVV','TTV','DPS']
# }

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
# # }
# groupPlot['WZ_QCD']  = {
#     'nameHR' : "WZ QCD",
#     'isSignal' : 0,
#     'color'    : ROOT.kRed, # kViolet+10
#     'samples'  : ['WZ_QCD']
# }
# groupPlot['WLLJJ_EWK']  = {
#     'nameHR' : "WZ EWK",
#     'isSignal' : 0,
#     'color'    : ROOT.kMagenta, # kViolet+10
#     'samples'  : ['WLLJJ_EWK']
# }
# groupPlot['Vg']  = {
#                   'nameHR' : "V#gamma",
#                   'isSignal' : 0,
#                   'color'    : ROOT.kOrange,   # kOrange + 10
#                   'samples'  : ['Vg','VgS_L','VgS_H']
#               }
# groupPlot['WW_QCD']  = {
#                   'nameHR' : "W^{#pm}W^{#pm} QCD",
#                   'isSignal' : 0,
#                   'color'    : ROOT.kViolet, # kViolet
#                   'samples'  : ['WW_QCD']
#               }
# groupPlot['non-prompt']  = {
#                   'nameHR' : 'non-Prompt',
#                   'isSignal' : 0,
#                   'color': ROOT.kYellow,    # kYellow
#                   'samples'  : ['Fake_lep']
#               }
groupPlot['DY']  = {
                  'nameHR' : 'DY',
                  'isSignal' : 0,
                  'color': Grey,    # kYellow
                  'samples'  : ['DY']
              } 
              
groupPlot['DY_ss']  = {
                  'nameHR' : 'DY_ss',
                  'isSignal' : 2,
                  'color': Green,    # kYellow
                  'samples'  : ['DY_ss']
              }            

groupPlot['DY_cf']  = {
                  'nameHR' : 'DY_cf',
                  'isSignal' : 2,
                  'color': Azure,    # kYellow
                  'samples'  : ['DY_cf']
              }      
                                        
groupPlot['top']  = {
                  'nameHR' : 'top',
                  'isSignal' : 0,
                  'color': Red,    # kYellow
                  'samples'  : ['top']
              }  

groupPlot['top_cf']  = {
                  'nameHR' : 'top_cf',
                  'isSignal' : 2,
                  'color': Orange,    # kYellow
                  'samples'  : ['top_cf']
              }  
        
groupPlot['top_ss']  = {
                  'nameHR' : 'top_ss',
                  'isSignal' : 2,
                  'color': Yellow,    # kYellow
                  'samples'  : ['top_ss']
              }  

# SM official samples
# groupPlot['WW_EWK']  = {
#                   'nameHR' : "W^{#pm}W^{#pm} EWK",
#                   'isSignal' : 1,
#                   'color'    : ROOT.kBlue-7, # kAzure+4
#                   'samples'  : ['WpWp_EWK']
#               }


#####################################
# EFT samples (internal latinos)
# groupPlot['WW_EWK_sm']  = {
#                   'nameHR'   : "W^{#pm}W^{#pm} EWK SM + EFT (k={})".format(str(eft_scale_param)),
#                   'isSignal' : 0,
#                   'color'    : ROOT.kBlue, 
#                   'samples'  : ['sm','linear','quadratic']
#               }

# groupPlot['WW_EWK_sm']  = {
#                   'nameHR'   : "W^{#pm}W^{#pm} EWK sm",
#                   'isSignal' : 0,
#                   'color'    : ROOT.kBlue, 
#                   'samples'  : ['sm']
#               }              

# groupPlot['WW_EWK_int']  = {
#                   'nameHR'   : "W^{#pm}W^{#pm} EWK int",
#                   'isSignal' : 0,
#                   'color'    : ROOT.kViolet, 
#                   'samples'  : ['linear']
#               }
# groupPlot['WW_EWK_bsm']  = {
#                   'nameHR'   : "W^{#pm}W^{#pm} EWK bsm ",
#                   'isSignal' : 0,
#                   'color'    : ROOT.kCyan+2, 
#                   'samples'  : ['quadratic']
#               }
#####################################


#plot = {}

# keys here must match keys in samples.py
#

# ##Fake and prompt substraction
# plot['Fake_lep']  = {
#     'color': Yellow,    # kYellow
#     'isSignal' : 0,
#     'isData'   : 0,
#     'scale'    : 1.0
# }

# plot['WZ_QCD']  = {
#     'color': Violet+10, # kViolet+10
#     'isSignal' : 0,
#     'isData'   : 0,
#     'scale'    : 1.0
# }

# plot['WLLJJ_EWK']  = {
#     'color': Violet+10, # kViolet+10
#     'isSignal' : 0,
#     'isData'   : 0,
#     'scale'    : 1.0
# }

# plot['WW_QCD']  = {
#     'color': Violet, # kViolet
#     'isSignal' : 0,
#     'isData'   : 0,
#     'scale'    : 1.0
# }

# plot['Vg']  = {
#     'color': Orange+10, # kOrange+10
#     'isSignal' : 0,
#     'isData'   : 0,
#     'scale'    : 1.0
# }
# plot['VgS_L']  = {
#     'color': Orange+10, # kOrange+10
#     'isSignal' : 0,
#     'isData'   : 0,
#     'scale'    : 1.0
# }
# plot['VgS_H']  = {
#     'color': Orange+10, # kOrange+10
#     'isSignal' : 0,
#     'isData'   : 0,
#     'scale'    : 1.0
# }
# ##Reducible Background
# ##VV plot
# plot['ZZ']  = {
#     'color': Violet+10, # kViolet+10
#     'isSignal' : 0,
#     'isData'   : 0,
#     'scale'    : 1.0
# }
# plot['DPS']  = {
#     'color': Violet+10, # kViolet+10
#     'isSignal' : 0,
#     'isData'   : 0,
#     'scale'    : 1.0
# }
# ##VVV
# plot['VVV']  = {
#     'color': Green, # kGreen
#     'isSignal' : 0,
#     'isData'   : 0,
#     'scale'    : 1.0
# }
# plot['TTV']  = {
#     'color': Green+10, # kGreen
#     'isSignal' : 0,
#     'isData'   : 0,
#     'scale'    : 1.0
# }
plot['DY']  = {
    'color': Grey, # kGreen
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}

plot['DY_ss']  = {
    'color': Grey, # kGreen
    'isSignal' : 1,
    'isData'   : 0,
    'scale'    : 1.0
}

plot['DY_cf']  = {
    'color': Grey, # kGreen
    'isSignal' : 1,
    'isData'   : 0,
    'scale'    : 1.0
}

# plot['DY_ss']  = {
#     'color': Green, # kGreen
#     'isSignal' : 0,
#     'isData'   : 0,
#     'scale'    : 1.0
# }


plot['top']  = {
    'color': Yellow, # kGreen
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}

plot['top_cf']  = {
    'color': Yellow, # kGreen
    'isSignal' : 1,
    'isData'   : 0,
    'scale'    : 1.0
}

plot['top_ss']  = {
    'color': Yellow, # kGreen
    'isSignal' : 1,
    'isData'   : 0,
    'scale'    : 1.0
}



# ##Signal
# plot['WpWp_EWK']  = {
#     'color': Azure+4, # kAzure+4
#     'isSignal' : 1,
#     'isData'   : 0,
#     'scale'    : 1.0
# }

#####################################
# EFT samples (internal latinos)
## Standard Model
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

# ##Data
# plot['DATA']  = {
#     'nameHR' : 'Data',
#     'color': 1 ,
#     'isSignal' : 0,
#     'isData'   : 1 ,
#     'isBlind'  : 1 ,
#     'scale'    : 1.0
# }


# additional options
legend['lumi'] = 'L = 59.74/fb'

legend['sqrt'] = '#sqrt{s} = 13 TeV'
