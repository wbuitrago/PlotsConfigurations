# plot configuration



# groupPlot = {}
# 
# Groups of samples to improve the plots.
# If not defined, normal plots is used
#

groupPlot['top']  = {  
                  'nameHR' : 'tW and t#bar{t}',
                  'isSignal' : 0,
                  'color': 400,   # kYellow
                  'samples'  : ['top']
              }
groupPlot['WWqcd']  = {  
                  'nameHR' : 'WpWm_QCD_noTop',
                  'isSignal' : 0,
                  'color': 851, # kAzure -9 
                  'samples'  : ['WWqcd']
              }

groupPlot['DY']  = {  
                  'nameHR' : "DY",
                  'isSignal' : 0,
                  'color': 418,    # kGreen+2
                  'samples'  : ['DY']
              }
groupPlot['others'] = {  
                  'nameHR' : 'others',
                  'isSignal' : 0,
                  'color': 857, # kAzure -3  
                  'samples'  : ['VVV','VZ','Vg', 'VgS_H', 'VgS_L','qqH_hww', 'ggH_hww']
                  }
'''
groupPlot['VVV']  = {  
                  'nameHR' : 'VVV',
                  'isSignal' : 0,
                  'color': 857, # kAzure -3  
                  'samples'  : ['VVV']
              }
groupPlot['VZ']  = {  
                  'nameHR' : "VZ",
                  'isSignal' : 0,
                  'color'    : 617,   # kViolet + 1  
                  'samples'  : ['VZ']
              }
groupPlot['Vg']  = {  
                  'nameHR' : "V#gamma(*)",
                  'isSignal' : 0,
                  'color'    : 631, # kRed -1
                  'samples'  : ['Vg', 'VgS_H', 'VgS_L']
              }
'''
groupPlot['Fake']  = {  
                  'nameHR' : 'Non-prompt',
                  'isSignal' : 0,
                  'color': 921,    # kGray + 1
                  'samples'  : ['Fake_em', 'Fake_me', 'Fake_ee', 'Fake_mm']
              }
'''
groupPlot['Higgs']  = {  
                  'nameHR' : 'Higgs',
                  'isSignal' : 0,
                  'color': 632, 
		  'samples'  : [ 'qqH_hww', 'ggH_hww']
  

            }

groupPlot['all_bkg']  = {
                  'nameHR' : 'all_bkg',
                  'isSignal' : 0,
                  'color': 921,
		  'samples'  : ['qqH_hww', 'ggH_hww','Fake_em','Fake_me','Fake_mm','Fake_ee', 'Vg', 'VgS_H', 'VgS_L','VZ', 'VVV','WWqcd', 'DY','top' ]       
}
'''
groupPlot['WWewk']  = {
                  'nameHR' : 'WpWmJJ_EWK_noTop',
                  'isSignal' : 1,
                  'color': 2,
		  'samples'  : [ 'WWewk']                                                                             
              }

#plot = {}

# keys here must match keys in samples.py    
#   
plot['DY']  = { 
                  'nameHR' : 'DY',
                  'color': 1 ,  
                  'isSignal' : 0,
                  'isData'   : 0 

              }
plot['top']  = { 
                  'nameHR' : 'top',
                  'color': 2 ,  
                  'isSignal' : 0,
                  'isData'   : 0 

              }
plot['VVV']  = { 
                  'nameHR' : 'VVV',
                  'color': 3 ,  
                  'isSignal' : 0,
                  'isData'   : 0 

              }
plot['VZ']  = { 
                  'nameHR' : 'VZ',
                  'color': 4 ,  
                  'isSignal' : 0,
                  'isData'   : 0 

              }

plot['Vg']  = {  
                  'nameHR' : "V#gamma",
                  'isSignal' : 0,
                  'color'    : 6,   
                  'isData'   : 0 
              }

plot['VgS_H']  = {  
                  'nameHR' : "V#gamma*",
                  'isSignal' : 0,
                  'color'    : 9,   
                  'isData'   : 0 
              }
plot['VgS_L']  = {  
                  'nameHR' : "V#gamma*",
                  'isSignal' : 0,
                  'color'    : 9,   
                  'isData'   : 0 
              }

plot['WW']  = {
                  'nameHR' : 'WW',
                  'isSignal' : 0,
                  'isData'   : 0 ,
                  'color': 7 #                                                                           
              }
plot['WWqcd']  = {
                  'nameHR' : 'WpWmJJ_QCD_noTop',
                  'isSignal' : 0,
                  'isData'   : 0 ,
                  'color': 7 #                                                                           
              }
plot['ggWW']  = {
                  'nameHR' : 'ggWW',
                  'isSignal' : 0,
                  'isData'   : 0 ,
                  'color': 9 #                                                                           
              }
plot['Fake_em']  = { 
                 'nameHR' : 'Fake',
                 'color': 921 ,  
                 'isSignal' : 0,
                 'isData'   : 0 
             }
plot['Fake_me']  = { 
                 'nameHR' : 'Fake',
                 'color': 921 ,  
                 'isSignal' : 0,
                 'isData'   : 0 
             }
plot['Fake_ee']  = { 
                 'nameHR' : 'Fake',
                 'color': 921 ,  
                 'isSignal' : 0,
                 'isData'   : 0 
             }
plot['Fake_mm']  = { 
                 'nameHR' : 'Fake',
                 'color': 921 ,  
                 'isSignal' : 0,
                 'isData'   : 0 
             }



# HWW 



plot['qqH_hww'] = {
                  'nameHR' : 'qqH',
                  'color': 632+1, # kRed+1 
                  'isSignal' : 0,
                  'isData'   : 0
                  }


plot['ggH_hww'] = {
                  'nameHR' : 'ggH',
                  'color': 632, # kRed 
                  'isSignal' : 0,
                  'isData'   : 0
                  }
plot['DATA']  = { 
                 'nameHR' : 'Data',
                'color': 1 ,  
                'isSignal' : 0,
               'isData'   : 1 ,
               'isBlind'  : 1
          }
plot['WWewk']  = {
                  'nameHR' : 'WpWmJJ_EWK_noTop',
                  'isSignal' : 1,
                  'isData'   : 0 ,
                  'color': 8                                                                             
              }

