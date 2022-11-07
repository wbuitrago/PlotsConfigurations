# plot configuration

from ROOT import TColor
from itertools import product

# groupPlot = {}
# 
# Groups of samples to improve the plots.
# If not defined, normal plots is used

colors = {
    # https://root.cern.ch/doc/master/classTColor.html#C02
    'kWhite'   : 0,
    'kBlack'   : 1,
    'kGray'    : 920,
    'kRed'     : 632,
    'kGreen'   : 416,
    'kBlue'    : 600,
    'kYellow'  : 400,
    'kMagenta' : 616,
    'kCyan'    : 432,
    'kOrange'  : 800,
    'kSpring'  : 820,
    'kTeal'    : 840,
    'kAzure'   : 860,
    'kViolet'  : 880,
    'kPink'    : 900, 
}

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

'''
    "Wjets_deta5": (247, 155, 7),#f79b07
    "Wjets_deta4": (247, 175, 7), #f7af07
    "Wjets_deta3": (247, 195, 7), #f7c307
    "Wjets_deta2": (247, 215, 7), #f7d707
    "Wjets_deta1": (247, 235, 7), #f7eb07
'''

jetbin_detabins = [3,3,2]
#wjets_palette = ['#FFF59D', '#FFEE58', '#FFD54F', '#FFB300', '#FF8F00', '#F57C00', '#E65100','#BF360C']
wjets_palette = ['#DF7000', '#FF8A00','#FFA133','#F7C307','#FFE200','#FFEC57']



wjets_bins = ["Wjets_res_"+str(ir) for ir in range(1,22)] + ["Wjets_boost_"+str(ir) for ir in range(1,8)]

groupPlot['VV+VVV']  = {  
                  'nameHR' : 'VV+VVV',
                  'isSignal' : 0,
                  'color': palette["Pink"], #palette["Peach3"],  
                  'samples'  : ['VVV', 'VV','ggWW'],
                  'fill': 1001
              }

groupPlot['DY']  = {  
                  'nameHR' : "DY",
                  'isSignal' : 0,
                  'color'    : palette["GreenDarker"],
                  'samples'  : ['DY'],
                  'fill': 1001
              }

groupPlot['Others']  = {  
                'nameHR' : "VBF-V + V#gamma",
                'isSignal' : 0,
                'color':palette["GreenLighter"],# palette["Green5"],    #Green2
                'samples'  : ['VBF-V_dipole', 'Vg','VgS' ],
                'fill': 1001
            }


groupPlot['Fake']  = {  
                'nameHR' : "Non-prompt",
                'isSignal' : 0,
                'color': palette["LightBlue"],   
                'samples'  : ['Fake'],
                'fill': 1001
            }


groupPlot['top']  = {  
                 'nameHR' : 'top',
                 'isSignal' : 0,
                 'color':  palette["MediumBlue"], #palette["MediumBlue2"],  
                 'samples'  : ['top'],
                 'fill': 1001
             }



groupPlot["Wjets"]  = {  
                        'nameHR' : 'W+Jets',
                        'isSignal' : 0,
                        'color':   palette["Yellow"],
                        'samples'  : wjets_bins,
                        'fill': 1001
                }


# groupPlot['VBS']  = {  
#                  'nameHR' : 'VBS',
#                  'isSignal' : 1,
#                  'color': colors["kRed"]+1,   
#                  'samples'  : ['ewk_WpWp', 'ewk_WmWm', 'ewk_WpZ', 'ewk_WmZ', 'ewk_WpWm', 'ewk_ZZ'],
#                  'fill': 1001
#               }

groupPlot['ewk_WpWp']  = {  
                 'nameHR' : 'ewk_WpWp',
                 'isSignal' : 1,
                 'color': colors["kBlue"], #palette["Peach3"],   
                 'samples'  : ['ewk_WpWp'],
                 'fill': 1001
              }

groupPlot['ewk_WpWm']  = {  
                 'nameHR' : 'ewk_WpWm',
                 'isSignal' : 1,
                 'color': palette["Orange2"],   
                 'samples'  : ['ewk_WpWm'],
                 'fill': 1001
              }

groupPlot['ewk_WmWm']  = {  
                 'nameHR' : 'ewk_WmWm',
                 'isSignal' : 1,
                 'color': palette["Pink2"],   
                 'samples'  : ['ewk_WmWm'],
                 'fill': 1001
              }

groupPlot['ewk_WmZ']  = {  
                 'nameHR' : 'ewk_WmZ',
                 'isSignal' : 1,
                 'color': colors["kMagenta"],   
                 'samples'  : ['ewk_WmZ'],
                 'fill': 1001
              }

groupPlot['ewk_WpZ']  = {  
                 'nameHR' : 'ewk_WpZ',
                 'isSignal' : 1,
                 'color': colors["kRed"],   
                 'samples'  : ['ewk_WpZ'],
                 'fill': 1001
              }

groupPlot['ewk_ZZ']  = {  
                 'nameHR' : 'ewk_ZZ',
                 'isSignal' : 1,
                 'color': colors["kGray"],   
                 'samples'  : ['ewk_ZZ'],
                 'fill': 1001
              }

#plot = {}

# keys here must match keys in samples.py    
# 

plot['ewk_WpWp']  = { 
                  'color': wjets_palette[0],    
                  'isSignal' : 1,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }


plot['ewk_WmWm']  = {
                  'color': wjets_palette[1],  
                  'isSignal' : 1,
                  'isData'   : 0,
                  'scale'    : 1.   ,
              }   
         


plot['ewk_WpWm']  = {  
                'color': wjets_palette[2],
                'isSignal' : 1,
                'isData'   : 0, 
                'scale'    : 1.0,
            }

plot['ewk_WpZ']  = {
                  'color': wjets_palette[3],  
                  'isSignal' : 1,
                  'isData'   : 0,
                  'scale'    : 1.   ,
              }

plot['ewk_WmZ']  = {
                  'color': wjets_palette[4],  
                  'isSignal' : 1,
                  'isData'   : 0,
                  'scale'    : 1.   ,
              }   
         


plot['ewk_ZZ']  = {  
                'color': wjets_palette[5],
                'isSignal' : 1,
                'isData'   : 0, 
                'scale'    : 1.0,
            }


#################

plot['VVV']  = { 
                  'color': colors["kAzure"] -3,    
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }


plot['VV']  = {
                  'color': colors['kGreen']+3,  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.   ,
              }   
         


plot['DY']  = {  
                'color': colors['kMagenta']+1,
                'isSignal' : 0,
                'isData'   : 0, 
                'scale'    : 1.0,
            }

plot['VBF-V_dipole']  = {
                  'color': colors['kYellow']+3,  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.   ,
              }

plot['Vg']  = {
                  'color': colors['kGreen']+3,  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.   ,
              }   
         


plot['VgS']  = {  
                'color': colors['kMagenta']+1,
                'isSignal' : 0,
                'isData'   : 0, 
                'scale'    : 1.0,
            }

plot['ggWW']  = {  
                'color': colors['kMagenta']+1,
                'isSignal' : 0,
                'isData'   : 0, 
                'scale'    : 1.0,
            }

plot['Fake']  = {  
                'color': colors['kTeal'],
                'isSignal' : 0,
                'isData'   : 0, 
                'scale'    : 1.0,
            }


plot['top'] = {   
                 'color': colors['kAzure']-1,
                 'isSignal' : 0,
                 'isData'   : 0, 
                 'scale'    : 1.0 
                 }


for wjetbin in wjets_bins:
    plot[wjetbin] = {   
                    'color': colors['kAzure']-1,
                    'isSignal' : 0,
                    'isData'   : 0, 
                    'scale'    : 1.0 
                    }

# # data

plot['DATA']  = { 
                 'nameHR' : 'Data',
                 'color': 1 ,  
                 'isSignal' : 0,
                 'isData'   : 1 ,
                 'isBlind'  : 0
             }

# additional options

legend['lumi'] = 'L = 59.74/fb'

legend['sqrt'] = '#sqrt{s} = 13 TeV'