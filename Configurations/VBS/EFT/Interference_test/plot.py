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

# to use this just comment out groupplots for all the samples included
# Other Bgr


groupPlot['WW_QCD']  = {
                  'nameHR' : "W^{#pm}W^{#pm} QCD",
                  'isSignal' : 0,
                  'color'    : Green,
                  'samples'  : ['WW_QCD']
              }

# groupPlot['WW_EWK']  = {
#                   'nameHR' : "W^{#pm}W^{#pm} EWK",
#                   'isSignal' : 0,
#                   'color'    : Orange,
#                   'samples'  : ['WpWp_EWK']
#               }

groupPlot['WW_EWK_mg']  = {
                  'nameHR' : "W^{#pm}W^{#pm} EWK mg",
                  'isSignal' : 0,
                  'color'    : Azure,
                  'samples'  : ['WpWp_EWK_mg']
              }              
              

groupPlot['WW_EWK_QCD']  = {
                  'nameHR' : "W^{#pm}W^{#pm} EWK QCD",
                  'isSignal' : 2,
                  'color'    : Red,
                  'samples'  : ['WW_EWK_QCD']
              }

plot['WW_QCD']  = {
    'color': Green,
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}
##Signal
# plot['WpWp_EWK']  = {
#     'color': Azure,
#     'isSignal' : 0,
#     'isData'   : 0,
#     'scale'    : 1.0
# }

plot['WpWp_EWK_mg']  = {
    'color': Azure,
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}


##Signal
plot['WW_EWK_QCD']  = {
    'color': Red, 
    'isSignal' : 1,
    'isData'   : 0,
    'scale'    : 1.0
}


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
