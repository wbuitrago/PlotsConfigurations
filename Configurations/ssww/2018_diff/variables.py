# variables

#variables = {}

#'fold' : # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow

# variables['events']  = {   'name': '1',
# 'range' : (1,0,2),
# 'xaxis' : 'events',
# 'fold' : 3
# }

variables['mll']  = {   'name': 'mll',            #   variable name
                        'range' : (4, 0. ,500),    #   variable range
                        'xaxis' : 'mll [GeV]',  #   x axis name
                        'fold' : 3
                        }
variables['mjj']  = {  'name': 'mjj',
                       'range': ([500,800,1100,1500,2000],),  #for 500 < mjj < 1000
                       'xaxis': 'mjj [GeV]',
                       'fold': 3
                       }
variables['mjj_v2']  = {  'name': 'mjj',
                          'range': (10,150,500),  #for 500 < mjj < 1000
                          'xaxis': 'mjj [GeV]',
                          'fold': 3
                          }
variables['pt1']  = {   'name': 'Alt$(Lepton_pt[0],-9999.)',
                        'range' : (10,30.,350),
                        'xaxis' : 'p_{T} 1st lep',
                        'fold'  : 3
                        }
variables['pt1_v2']  = {   'name': 'Alt$(Lepton_pt[0],-9999.)',
                           'range' : (16,30.,350),
                           'xaxis' : 'p_{T} 1st lep',
                           'fold'  : 3
                           }

variables['pt2']  = {   'name': 'Alt$(Lepton_pt[1],-9999.)',
                        'range' : (10,30.,350),
                        'xaxis' : 'p_{T} 2nd lep',
                        'fold'  : 3
                        }
variables['pt2_v2']  = {   'name': 'Alt$(Lepton_pt[1],-9999.)',
                           'range' : (16,30.,350),
                           'xaxis' : 'p_{T} 2nd lep',
                           'fold'  : 3
                           }

variables['jetpt1']  = {   'name': 'Alt$(Jet_pt[0],-9999.)',
                           'range' : (10,30.,350),
                           'xaxis' : 'p_{T} 1st jet',
                           'fold'  : 3
                           }

variables['jetpt2']  = {   'name': 'Alt$(Jet_pt[1],-9999.)',
                           'range' : (10,30.,350),
                           'xaxis' : 'p_{T} 2nd jet',
                           'fold'  : 3
                           }