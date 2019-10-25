# plot configuration



groupPlot = {}



#####################
#### BACKGROUNDS ####
#####################
groupPlot['TT_semilep']  = {    
				  'nameHR' : 'tt_semilep',
				  'isSignal' : 0,
				  'color' : 860,
			  	  'samples' : ['TT_semilep']
			       }	

groupPlot['Wjets']  = {
                        'nameHR' : 'W+Jets',
                        'isSignal' : 0,
                        'color': 418,
                        'samples'  : ['Wjets']
                     }

groupPlot['ttbar']  = {
                        'nameHR' : 'ttbar',
                        'isSignal' : 0,
                        'color': 797,
                        'samples'  : ['ttbar']
                     }


groupPlot['singleTop']  = {
                        'nameHR' : 'SingleTop',
                        'isSignal' : 0,
                        'color': 617,
                        'samples'  : ['singleTop']
                     }

groupPlot['DY_VV_VVV']  = {
                        'nameHR' : 'DY, VV, VVV',
                        'isSignal' : 0,
                        'color': 1,
                        'samples'  : ['DY','VV', 'VVV']
                     }

'''
groupPlot['DY']  = {
                        'nameHR' : 'Drell-Yan',
                        'isSignal' : 0,
                        'color': 432,
                        'samples'  : ['DY']
                     }
'''
###############
### SIGNAL ####
###############
groupPlot['HH']  = {
                        'nameHR' : 'HH',
                        'isSignal' : 1,
                        'color': 632,
                        'samples'  : ['HH']
                   }



plot = {}

#####################
#### BACKGROUNDS ####
#####################
plot['TT_semilep']  = {
                  'color': 860,    
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.   ,
              }

plot['Wjets']  = {
                  'color': 418,
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.   ,
                  }

plot['ttbar']  = {
                  'color': 797,
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.   ,
                  }


plot['singleTop']  = {
                  'color': 617,
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.   ,
                  }

plot['VV']  = {
                  'color': 1,
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.   ,
                  }
plot['VVV']  = {
                  'color': 1,
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.   ,
                  }
plot['DY']  = {
                  'color': 1,#432,
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.   ,
                  }

###############
### SIGNAL ####
###############
plot['HH']  = {
                  'color': 632,
                  'isSignal' : 1,
                  'isData'   : 0,
                  'scale'    : 1.  ,
              }


##############
#### DATA ####
##############
'''
plot['DATA']  = { 
                  'nameHR' : 'Data',
                  'color': 1 ,  
                  'isSignal' : 0,
                  'isData'   : 1 ,
                  'isBlind'  : 0,
		            'scale' : 1.
                }
'''





#legend['lumi'] = 'L = 6.3/fb'
legend['lumi'] = 'L = 41.5/fb'
legend['sqrt'] = '#sqrt{s} = 13 TeV'




