# plot configuration



# groupPlot = {}
# 
# Groups of samples to improve the plots.
# If not defined, normal plots is used
#




#BKG

groupPlot['TTToSemilepton']  = {    
				  'nameHR' : 'tt_semileptonic',
				  'isSignal' : 0,
				  'color' : 860,
			  	  'samples' : ['TT']
			       }	

groupPlot['Wjets']  = {
                        'nameHR' : 'W+Jets',
                        'isSignal' : 0,
                        'color': 418,
                        'samples'  : ['Wjets']
                     }

groupPlot['TT_leptonic']  = {
                        'nameHR' : 'tt_leptonic',
                        'isSignal' : 0,
                        'color': 797,
                        'samples'  : ['TT_leptonic']
                     }


groupPlot['SingleTop']  = {
                        'nameHR' : 'SingleTop',
                        'isSignal' : 0,
                        'color': 617,
                        'samples'  : ['SingleTop']
                     }

groupPlot['WZ_WW_WWZ_WWW_DY_ZZ']  = {
                        'nameHR' : 'DY, WZ, WW, WWW, WWZ, ZZ',
                        'isSignal' : 0,
                        'color': 432,
                        'samples'  : ['WZ','DY','WW', 'WWW', 'WWZ','ZZ']
                     }
#groupPlot['WWW']  = {
#                        'nameHR' : 'WWW',
#                        'isSignal' : 0,
#                        'color': 880,
#                        'samples'  : ['WWW']
#                     }

#groupPlot['WWZ']  = {
#                        'nameHR' : 'WWZ',
#                        'isSignal' : 0,
#                        'color': 617,
#                        'samples'  : ['WWZ']
#                     }
#groupPlot['WZ']  = {
#                        'nameHR' : 'WZ',
#                        'isSignal' : 0,
#                        'color': 921,
#                        'samples'  : ['WZ']
#                     }

#groupPlot['ZZ']  = {
#                        'nameHR' : 'ZZ',
#                        'isSignal' : 0,
#                        'color': 815,
#                        'samples'  : ['ZZ']
#                     }
#groupPlot['DY_ZZ']  = {
#                        'nameHR' : 'DY and ZZ',
#                        'isSignal' : 0,
#                        'color': 432,
#                        'samples'  : ['DY', 'ZZ']
#                     }


#SIGNAL
groupPlot['HH']  = {
                        'nameHR' : 'HH',
                        'isSignal' : 1,
                        'color': 632,
                        'samples'  : ['HH']
                   }



#DATA
#groupPlot['DATA']  = {
#			'nameHR' : 'DATA',
#			'isSignal' : 0,
#                	'color': 1,
#                        'samples'  : ['DATA']
#		     }	



#plot = {}

# keys here must match keys in samples.py    
#                    

#BKG

plot['TT']  = {
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

plot['TT_leptonic']  = {
                  'color': 797,
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.   ,
                  }


plot['SingleTop']  = {
                  'color': 617,
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.   ,
                  }

plot['WW']  = {
                  'color': 432,
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.   ,
                  }
plot['WWW']  = {
                  'color': 432,
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.   ,
                  }
plot['WWZ']  = {
                  'color': 432,
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.   ,
                  }
plot['WZ']  = {
                  'color': 432,
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.   ,
                  }
plot['DY']  = {
                  'color': 432,
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.   ,
                  }

plot['ZZ']  = {
                  'color': 432,
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.   ,
                  }


#SIGNAL
plot['HH']  = {
                  'color': 632,
                  'isSignal' : 1,
                  'isData'   : 0,
                  'scale'    : 1.  ,
              }


#DATA
#plot['DATA']  = { 
#                  'nameHR' : 'Data',
#                  'color': 1 ,  
#                  'isSignal' : 0,
#                  'isData'   : 1 ,
#                  'isBlind'  : 0,
#		  'scale' : 1.
#                }






#legend['lumi'] = 'L = 6.3/fb'
legend['lumi'] = 'L = 35.9/fb'
legend['sqrt'] = '#sqrt{s} = 13 TeV'




