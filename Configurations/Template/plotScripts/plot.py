# Htautau

import ROOT 
c1 = ROOT.TColor.GetFreeColorIndex()
blue = ROOT.TColor(c1, 0.34117647058, 0.72156862745, 1)

c2 = ROOT.TColor.GetFreeColorIndex()
brown = ROOT.TColor(c2, 0.71372549019, 0.42745098039, 0.05098039215)

c3 = ROOT.TColor.GetFreeColorIndex()
yellow = ROOT.TColor(c3, 0.98431372549, 0.69411764705, 0.23529411764)

c4 = ROOT.TColor.GetFreeColorIndex()
red = ROOT.TColor(c4, 0.99607843137,0.40784313725 ,0.27843137254 )

plot['ewk_SSWW'] = {
                  'nameHR' : 'SSWW',
                  'color': c1, 
                  'isSignal' : 1,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }

# HWW 

plot['ewk_OSWW'] = {
                  'nameHR' : 'OSWW',
                  'color': c2, # kRed+3 
                  'isSignal' : 1,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }

plot['ewk_WZ'] = {
                  'nameHR' : 'WZ',
                  'color': c3, # kRed+4
                  'isSignal' : 1,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }

plot['ewk_ZZ'] = {
                  'nameHR' : 'ZZ',
                  'color': c4, # kRed+2 
                  'isSignal' : 1,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }


plot['qqH_hww'] = {
                  'nameHR' : 'VBF',
                  'color': 600, # kRed+1 
                  'isSignal' : 1,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }


plot['ggH_hww'] = {
                  'nameHR' : 'ggH',
                  'color': 418, # kRed 
                  'isSignal' : 1,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }

plot['bbH_hww'] = {
                  'nameHR' : 'b#bar{b}H',
                  'color': 434, # kRed+5 
                  'isSignal' : 1,
                  'isData'   : 0,
                  'scale'    : 1    #
                  }

plot['ttH_hww'] = {
                  'nameHR' : 't#bar{t}H',
                  'color': 400, # kRed+5 
                  'isSignal' : 1,
                  'isData'   : 0,
                  'scale'    : 1    #
                 } 


