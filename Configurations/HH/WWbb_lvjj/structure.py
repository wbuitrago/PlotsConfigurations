# structure configuration for datacard

structure = {}

###############
### SIGNAL ####
###############               
structure['HH'] = {
                'isSignal': 1,
                'isData': 0
                }

#####################
#### BACKGROUNDS ####
#####################  
structure['Wjets'] = {
		'isSignal': 0,
		'isData': 0
		}

structure['TT_semilep'] = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }

structure['DY'] = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }

structure['singleTop'] = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }
structure['ttbar'] = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }
structure['VV'] = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }
structure['VVV'] = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }

##############
#### DATA ####
##############
structure['DATA'] = {
                       	'isSignal' : 0,
                       	'isData'   : 1
		    }





