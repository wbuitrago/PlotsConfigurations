# plot configuration



# groupPlot = {}
# 
# Groups of samples to improve the plots.
# If not defined, normal plots is used
#
'''
groupPlot['Higgs']  = {  
                  'nameHR' : 'Higgs',
                  'isSignal' : 0,
                  'color': 632, # kRed 
		  'samples'  : ['H_htt', 'H_hww', 'ZH_hww', 'ggZH_hww', 'WH_hww', 'qqH_hww', 'ggH_hww','bbH_hww','ttH_hww','ZH_htt', 'ggZH_htt', 'WH_htt', 'qqH_htt', 'ggH_htt','bbH_htt','ttH_htt' ]
		  #'samples'  : ['H_htt', 'H_hww', 'ZH_hww', 'ggZH_hww', 'WH_hww', 'qqH_hww', 'ggH_hww','bbH_hww','ttH_hww', 'qqH_htt', 'ggH_htt' ]
              }
'''

groupPlot['Fake']  = {
                  'nameHR' : 'nonprompt',
                  'isSignal' : 0,
                  'color': 921,    # kGray + 1
                  'samples'  : ['Fake_m', 'Fake_e']
}

groupPlot['Multiboson']  = {  
                  'nameHR' : 'Multiboson',
                  'isSignal' : 0,
                  'color': 617, # kViolet + 1  
                  'samples'  : ['VVV', 'VZ', 'WZ', 'ZZ', 'Vg', 'Wg', 'VgS_H', 'VgS_L']
              }

groupPlot['WW']  = {  
                  'nameHR' : 'WW',
                  'isSignal' : 0,
                  'color': 851, # kAzure -9 
                  'samples'  : ['WW', 'ggWW']
              }

groupPlot['DY_hardJets']  = {  
                  'nameHR' : "DY no PU jets",
                  'isSignal' : 0,
                  'color': 418,    # kGreen+2
                  'samples'  : ['DY_hardJets']
              }

groupPlot['DY_PUJets']  = {  
                  'nameHR' : "DY 1 PU jet",
                  'isSignal' : 0,
                  'color': 416,    # kGreen
                  'samples'  : ['DY_PUJets']
              }

groupPlot['top']  = {  
                  'nameHR' : 'tW and t#bar{t}',
                  'isSignal' : 0,
                  'color': 400,   # kYellow
                  'samples'  : ['top']
              }

groupPlot['VBS']  = {
                  'nameHR' : 'VBS',
                  'isSignal' : 0,
                  'color': 888, #666,
                  'samples'  : ['WWewk']
              }


groupPlot['Zjj']  = {  
                  'nameHR': 'Zjj',
                  'isSignal' : 1,
                  'color': 600,    # kBlue
                  'samples'    : ['Zjj']
              }


#plot = {}

# keys here must match keys in samples.py    
#             
plot['DY_hardJets']  = {  
                  'color': 418,    # kGreen+2
                  'isSignal' : 0,
                  'isData'   : 0, 
                  'scale'    : 1.0,
              }

plot['DY_PUJets']  = {  
                  'color': 416,    # kGreen
                  'isSignal' : 0,
                  'isData'   : 0, 
                  'scale'    : 1.0,
              }

plot['Zjj']  = {  
                  'color': 600,    # kBlue
                  'isSignal' : 1,
                  'isData'   : 0,
                  'scale'    : 1.0                  
              }

plot['WWewk']  = {
                  'color': 851, # kAzure -9 
                  'isSignal' : 0,
                  'isData'   : 0,
                  #'scale'    : 1.0   # ele/mu trigger efficiency   datadriven
                  }

plot['Fake_m']  = {  
                  'color': 921,    # kGray + 1
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0                  
              }


plot['Fake_e']  = {  
                  'color': 921,    # kGray + 1
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0                  
              }

              
plot['top'] = {   
                  'nameHR' : 'tW and t#bar{t}',
                  'color': 400,   # kYellow
                  'isSignal' : 0,
                  'isData'   : 0, 
                  #'scale'    : 1.0,
                  #'cuts'  : {
                       #'hww2l2v_13TeV_of0j'      : 0.94 ,
                       #'hww2l2v_13TeV_top_of0j'  : 0.94 , 
                       #'hww2l2v_13TeV_dytt_of0j' : 0.94 ,
                       #'hww2l2v_13TeV_em_0j'     : 0.94 , 
                       #'hww2l2v_13TeV_me_0j'     : 0.94 , 
                       ##
                       #'hww2l2v_13TeV_of1j'      : 0.86 ,
                       #'hww2l2v_13TeV_top_of1j'  : 0.86 , 
                       #'hww2l2v_13TeV_dytt_of1j' : 0.86 ,
                       #'hww2l2v_13TeV_em_1j'     : 0.86 , 
                       #'hww2l2v_13TeV_me_1j'     : 0.86 , 
                        #},
                  }


plot['WW']  = {
                  'color': 851, # kAzure -9 
                  'isSignal' : 0,
                  'isData'   : 0,    
                  'scale'    : 1.0   # ele/mu trigger efficiency   datadriven
                  }

plot['ggWW']  = {
                  'color': 850, # kAzure -10
                  'isSignal' : 0,
                  'isData'   : 0,    
                  'scale'    : 1.0
                  }

plot['Vg']  = { 
                  'color': 859, # kAzure -1  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }

plot['VgS_H'] = { 
                  'color'    : 617,   # kViolet + 1  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }

plot['VgS_L'] = {
                  'color'    : 617,   # kViolet + 1  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }


plot['VZ']  = { 
                  'color': 858, # kAzure -2  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }

plot['VVV']  = { 
                  'color': 857, # kAzure -3  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }


# data

plot['DATA']  = { 
                  'nameHR' : 'Data',
                  'color': 1 ,  
                  'isSignal' : 0,
                  'isData'   : 1 ,
                  'isBlind'  : 0
              }




# additional options

legend['lumi'] = 'L = 41.5 fb^-1'

legend['sqrt'] = '#sqrt{s} = 13 TeV'




