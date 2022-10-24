

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
Red=632; Violet=880; Green=416; Orange=800; Yellow=400; Azure=860

palette = {
    "Orange": (242, 108, 13), #f26c0d  
    "Yellow": (247, 195, 7), #f7c307
    "LightBlue": (153, 204, 255), #99ccff
    "MediumBlue": (72, 145, 234),  #4891ea
    "MediumBlue2": (56, 145, 224),    #3891e0
    "DarkBlue": (8, 103, 136), #086788
    "Green": (47, 181, 85), #2fb555
    "Green2": (55, 183, 76),  #37b74c
    "Green3": (16,235,52),#10eb34
    "Green4": (68, 175, 105), #44af69
    "Green5": (29,194,106),#1DC26A
    "Green6" : (27,177,97), #1BB161
    "Green7": (108, 198, 140), # 6CC68C
    "GreenLighter": (93, 192, 128),  #5DC080
    "GreenDarker": (14, 150, 78), # 14, 150, 78
    "LightGreen" : (82, 221, 135), #52dd87
    "Violet": (242, 67, 114), #f24372  
    "Pink": (247, 191, 223), #F7BFDF,
    "Peach": (255, 143, 133), #F7C59F
    "Peach2": (255, 146, 51), #FF9233
    "Peach3": (255, 157, 71), #
    "Pink2" : (253, 161, 155), #FD9BA1
    "Orange": (255,156, 51),
    "Orange2": (255,135, 31)
}

palette2 = {
    "Yellow": (234,180,100), #SSWW
    "Violet": (121,16,255), # tVx
    "DeadViolet": (95,94,149), # Nonprompt
    "Red": (198,60,85), # WZ QCD
    "GreenPure": (0,108,0), # Vg
    "Swamp": (53,91,56), # EWK WZ
    "LightGreen": (122,142,70), # Other bkg
    "lightAzure": (153, 204, 255), # ZZ
    "fullAzure": (49,195,255), # Wrong sign
}

groupPlot['ZZ']  = {
    'nameHR':"ZZ", 
    'isSignal':0, 
    #'color': palette["Green2"], 
    'color': palette2["lightAzure"], 
    'samples':['ZZ'],
    'fill': 1001
}

groupPlot['WZ_QCD']  = {
    'nameHR':"WZ QCD", 
    'isSignal':0, 
    #'color':palette["Pink2"], 
    'color': palette2["Red"],
    'samples':['WZ_QCD'],
    'fill': 1001
}

groupPlot['WZ_EWK']  = {
    'nameHR':"WZ EWK", 
    'isSignal':0, 
    #'color':palette["Peach"], 
    'color': palette2["Swamp"],
    'samples':['WZ_EWK'],
    'fill': 1001
}
groupPlot['VVV']  = {
    'nameHR':'VVV', 
    'isSignal':0, 
    #'color':palette["Green3"], 
    'color': palette2["LightGreen"],
    'samples':['VVV'],
    'fill': 1001
}

groupPlot['tVx']  = {
    'nameHR':'tVx', 
    'isSignal':0, 
    #'color':palette["Yellow"], 
    'color': palette2["Violet"],
    'samples':['TTV','tZq'],
    'fill': 1001
}

groupPlot['DPS']  = {
    'nameHR':'DPS', 
    'isSignal':0, 
    #'color':palette["MediumBlue"], 
    'color': palette2["LightGreen"],
    'samples':['DPS'],
    'fill': 1001
}

#groupPlot['Vg']  = dict(nameHR="V#gamma", isSignal=0, color=ROOT.kCyan - 7, samples=['Vg', 'VgS1_H','VgS1_L'])
groupPlot['WpWp_QCD']  = {
    'nameHR':"W^{#pm}W^{#pm} QCD", 
    'isSignal':0, 
    #'color':palette["Violet"], 
    'color': palette2["LightGreen"],
    'samples':['WpWp_QCD'],
    'fill': 1001
}

groupPlot['non-prompt']  = {
    'nameHR':'non-Prompt', 
    'isSignal':0, 
    #'color': palette["LightBlue"], 
    'color': palette2["DeadViolet"],
    'samples':['Fake_lep'],
    'fill': 1001
}

groupPlot['Wrong-sign']  = {
    'nameHR':"Wrong-sign", 
    'isSignal':0, 
    #'color':palette["Orange"], 
    'color': palette2["fullAzure"],
    'samples':['WW','Top','DY','Higgs'],
    'fill': 1001
}

groupPlot['SSWW']  = {
    'nameHR':"W^{#pm}W^{#pm} EWK", 
    'isSignal':0, 
    #'color':palette["DarkBlue"], 
    'color': palette2["Yellow"],
    'samples':['SSWW'],
    'fill': 1001
}
#groupPlot['Wrong-sign']  = dict(nameHR="mischarge", isSignal=0, color=ROOT.kOrange, samples=['WW','Top','DY','Higgs'])
#plot = {}

# keys here must match keys in samples.py
##Fake and prompt substraction
plot['Fake_lep']  = {
    'color':Yellow, 
    'isSignal':0, 
    'isData':0, 
    'scale':1.0
}
##Signal
plot['SSWW']  = {
    'color':Azure + 4, 
    'isSignal':0, 
    'isData':0, 
    'scale':1.0
 } 
plot['WpWp_QCD']  = {
    'color':Violet, 
    'isSignal':0, 
    'isData':0, 
    'scale':1.0
}
plot['Vg']  = dict(color=1, isSignal=0, isData=0, scale=1.0)
plot['VgS1_H']  = dict(color=1, isSignal=0, isData=0, scale=1.0) # VgS VgS1 VgS2
plot['VgS1_L']  = dict(color=1, isSignal=0, isData=0, scale=1.0) # VgS VgS1 VgS2
##Reducible Background
##VV plot


plot['ZZ']  = {
    'color':Violet + 10, 
    'isSignal':0, 
    'isData':0, 
    'scale':1.0
}

# plot['ggZZ']  = {
#     'color':Violet + 10, 
#     'isSignal':0, 
#     'isData':0, 
#     'scale':1.0
# }

plot['WZ_QCD']  = {
    'color':Violet + 10, 
    'isSignal':0, 
    'isData':0, 
    'scale':1.0
} # WZ_QCD WZ_QCD_powheg WZ_QCD_AMCNLO

plot['WZ_EWK']  = {
    'color':Violet + 10, 
    'isSignal':0, 
    'isData':0, 
    'scale':1.0
}

plot['DPS']  = {
    'color':Violet + 10, 
    'isSignal':0, 
    'isData':0, 
    'scale':1.0
}
##VVV

plot['VVV']  = {
    'color':Green, 
    'isSignal':0, 
    'isData':0, 
    'scale':1.0
}

plot['TTV']  = {
    'color':Green + 10, 
    'isSignal':0, 
    'isData':0, 
    'scale':1.0
}

plot['tZq']  = {
    'color':Green + 10, 
    'isSignal':0, 
    'isData':0, 
    'scale':1.0
}

plot['WW']  = {
    'color':Green + 10, 
    'isSignal':0, 
    'isData':0, 
    'scale':1.0
}

plot['Top']  = {
    'color':Green + 10, 
    'isSignal':0, 
    'isData':0, 
    'scale':1.0
}

plot['DY']  = {
    'color':Green + 10, 
    'isSignal':0, 
    'isData':0, 
    'scale':1.0
}

plot['Higgs']  = {
    'color':Green + 10, 
    'isSignal':0, 
    'isData':0, 
    'scale':1.0
}
##Data

plot['DATA']  = {
    'nameHR':'Data', 
    'color':1, 
    'isSignal':0, 
    'isData':1, 
    'isBlind':0, 
    'scale':1.0
}

# additional options
legend['lumi'] = 'L = 59.74/fb'
#legend['lumi'] = 'L = 137.19/fb'

legend['sqrt'] = '#sqrt{s} = 13 TeV'
