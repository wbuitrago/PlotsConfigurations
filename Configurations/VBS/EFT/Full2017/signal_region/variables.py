# variables

# variables = {}

#'fold' : # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow

variables['nJet']  = {      'name': 'nCleanJet',
                            'range' : (7,0,7),
                            'xaxis' : 'nCleanJet',
                            'fold' : 3
                            }

variables['nLepton'] =  {   'name': 'nLepton',
                            'range': (7,0,7),
                            'xaxis': '# leptons',
                            'fold': 3
}

variables['mll']  = {   'name': 'mll',            #   variable name
                        'range' : (50, 0. ,500),    #   variable range
                        'xaxis' : 'mll [GeV]',  #   x axis name
                        'fold' : 3
                        }


variables['mjj']  = {  'name': 'mjj',
                       'range': (50,0.,500.),
                       'xaxis': 'mjj [GeV]',
                       'fold': 3
                       }

variables['pt1']  = {   'name': 'Alt$(Lepton_pt[0],-9999.)',
                        'range' : (30,0.,300.),
                        'xaxis' : 'p_{T} 1st lep',
                        'fold'  : 3
                        }


variables['pt2']  = {   'name': 'Alt$(Lepton_pt[1],-9999.)',
                        'range' : (30,0.,300.),
                        'xaxis' : 'p_{T} 2nd lep',
                        'fold'  : 3
                        }


variables['jetpt1']  = {   'name': 'Alt$(CleanJet_pt[0],-9999.)',
                           'range' : (35,0.,350),
                           'xaxis' : 'p_{T} 1st jet',
                           'fold'  : 3
                           }

variables['jetpt2']  = {   'name': 'Alt$(CleanJet_pt[1],-9999.)',
                           'range' : (35,0.,350),
                           'xaxis' : 'p_{T} 2nd jet',
                           'fold'  : 3
                           }

variables['met']  = {   'name': 'MET_pt',            #   variable name
                        'range' : (20,0,200),        #   variable range
                        'xaxis' : 'pfmet [GeV]',     #   x axis name
                        'fold' : 3
                        }

variables['etaj1'] = {  'name': 'Alt$(CleanJet_eta[0],-9999.)',
                        'range': (20,-5,5),
                        'xaxis': 'etaj1',
                        'fold': 3
                        }

variables['etaj2'] = {         'name': 'Alt$(CleanJet_eta[1],-9999.)',
                               'range': (20,-5,5),
                               'xaxis': 'etaj2',
                               'fold': 3
                               }

variables['detajj']  = {  'name': 'detajj',
                          'range': (20,0.0,10.0),
                          'xaxis': 'detajj',
                          'fold': 3
                          }


variables['dphijj']  = {  'name': 'abs(Alt$(CleanJet_phi[0],-9999.)-Alt$(CleanJet_phi[1],-9999.))',
                          'range': (20,0.0,6.2832),
                          'xaxis': 'dphijj',
                          'fold': 3
                          }