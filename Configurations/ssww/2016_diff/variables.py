# variables

#variables = {}

#'fold' : # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow

# variables['events']  = {   'name': '1',
# 'range' : (1,0,2),
# 'xaxis' : 'events',
# 'fold' : 3
# }
variables['mll']  = {   'name': 'mll',            #   variable name
                        'range' : ([20,120,220,320],),    #   variable range
                        'xaxis' : 'mll [GeV]',  #   x axis name
                        'fold' : 3
                        }
variables['mll_v2']  = {   'name': 'mll',            #   variable name
                        'range' : ([20,70,120,170,220,270,320],),    #   variable range
                        'xaxis' : 'mll [GeV]',  #   x axis name
                        'fold' : 3
                        }
variables['mjj']  = {  'name': 'mjj',
                       'range': ([500,1000,1800,2500],),  #for 500 < mjj < 1000
                       'xaxis': 'mjj [GeV]',
                       'fold': 3
                       }
variables['mjj_v2']  = {  'name': 'mjj',
                          'range': ([500,700,1000,1400,1800,2100,2500],),  #for 500 < mjj < 1000
                          'xaxis': 'mjj [GeV]',
                          'fold': 3
                          }
variables['mjj_low']  = {  'name': 'mjj',
                          'range': (10,150,500),  #for 500 < mjj < 1000
                          'xaxis': 'mjj [GeV]',
                          'fold': 3
                          }
variables['pt1']  = {   'name': 'Alt$(Lepton_pt[0],-9999.)',
                        'range' : ([30,70,120,270],),
                        'xaxis' : 'p_{T} 1st lep',
                        'fold'  : 3
                        }
variables['pt1_v2']  = {   'name': 'Alt$(Lepton_pt[0],-9999.)',
                           'range' : ([30,70,120,150,190,230,270],),
                           'xaxis' : 'p_{T} 1st lep',
                           'fold'  : 3
                           }

variables['pt2']  = {   'name': 'Alt$(Lepton_pt[1],-9999.)',
                        'range' : ([30,45,70,270],),
                        'xaxis' : 'p_{T} 2nd lep',
                        'fold'  : 3
                        }
variables['pt2_v2']  = {   'name': 'Alt$(Lepton_pt[1],-9999.)',
                           'range' : ([30,45,70,100,150,200,270],),
                           'xaxis' : 'p_{T} 2nd lep',
                           'fold'  : 3
                           }

variables['jetpt1']  = {   'name': 'Alt$(CleanJet_pt[0],-9999.)',
                           'range' : ([30,145,245,350],),
                           'xaxis' : 'p_{T} 1st jet',
                           'fold'  : 3
                           }
variables['jetpt1_v2']  = {   'name': 'Alt$(CleanJet_pt[0],-9999.)',
                           'range' : ([30,80,145,190,245,295,350],),
                           'xaxis' : 'p_{T} 1st jet',
                           'fold'  : 3
                           }
variables['jetpt2']  = {   'name': 'Alt$(CleanJet_pt[1],-9999.)',
                           'range' : ([30,70,120,270],),
                           'xaxis' : 'p_{T} 2nd jet',
                           'fold'  : 3
                           }
variables['jetpt2_v2']  = {   'name': 'Alt$(CleanJet_pt[1],-9999.)',
                           'range' : ([30,70,90,120,170,220,270],),
                           'xaxis' : 'p_{T} 2nd jet',
                           'fold'  : 3
                           }
