# variables

#variables = {}

#'fold' : # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow

variables['events']  = {   'name': '1',
'range' : (1,0,2),
'xaxis' : 'events',
'fold' : 3
}

variables['nJet']  = {   'name': 'Sum$(CleanJet_pt>30)',
                            'range' : (6,0,6),
                            'xaxis' : 'njets',
                            'fold' : 3
                            }


variables['nLepton'] =  {
    'name': '1*(Alt$(Lepton_pt[0],0.)>20) + 1*(Alt$(Lepton_pt[1],0.)>20) + 1*(Alt$(Lepton_pt[2],0.)>20)+ 1*(Alt$(Lepton_pt[3],0.)>20) + 1*(Alt$(Lepton_pt[4],0.)>20)',
    'range': (5,0,5),
    'xaxis': '# leptons',
    'fold': 3
}

#2 Jets

variables['jetpt1']  = {   'name': 'Alt$(CleanJet_pt[0],-9999.)',
                           'range' : (15,0.,200),
                           'xaxis' : 'p_{T} 1st jet',
                           'fold'  : 3
                           }

variables['jetpt2']  = {   'name': 'Alt$(CleanJet_pt[1],-9999.)',
                           'range' : (15,0.,150),
                           'xaxis' : 'p_{T} 2nd jet',
                           'fold'  : 3
                           }


#Eta 2 Jets

variables['etaj1'] = {  'name': 'Alt$(Jet_eta[0],-9999.)',
                        'range': (10,-5,5),
                        'xaxis': 'etaj1',
                        'fold': 3
                        }

variables['etaj2'] = {         'name': 'Alt$(Jet_eta[1],-9999.)',
                               'range': (10,-5,5),
                               'xaxis': 'etaj2',
                               'fold': 3
                               }

#Eta for each lepton

variables['eta1'] = {  'name': 'Lepton_eta[0]',
                        'range': (10,-5,5),
                        'xaxis': 'etaj1',
                        'fold': 3
                        }

variables['eta2'] = {  'name': 'Lepton_eta[1]',
                        'range': (10,-5,5),
                        'xaxis': 'etaj1',
                        'fold': 3
                        }

variables['eta3'] = {  'name': 'Lepton_eta[2]',
                        'range': (10,-5,5),
                        'xaxis': 'etaj1',
                        'fold': 3
                        }

variables['eta4'] = {  'name': 'Lepton_eta[3]',
                        'range': (10,-5,5),
                        'xaxis': 'etaj1',
                        'fold': 3
                        }


# Zeppenfeld Variable in the moment is only defined for the 4 leptons


variables['Zlep1']  = {  'name': '(Alt$(Lepton_eta[0],-9999.) - (Alt$(Jet_eta[0],-9999.)+Alt$(Jet_eta[1],-9999.))/2)/detajj',
                         'range': (10,-1.5,1.5),
                         'xaxis': 'Z^{lep}_{1}',
                         'fold': 3
                         }

variables['Zlep2']  = {  'name': '(Alt$(Lepton_eta[1],-9999.) - (Alt$(Jet_eta[0],-9999.)+Alt$(Jet_eta[1],-9999.))/2)/detajj',
                         'range': (10,-1.5,1.5),
                         'xaxis': 'Z^{lep}_{2}',
                         'fold': 3
                         }

variables['Zlep3']  = {  'name': '(Alt$(Lepton_eta[2],-9999.) - (Alt$(Jet_eta[0],-9999.)+Alt$(Jet_eta[1],-9999.))/2)/detajj',
                         'range': (10,-1.5,1.5),
                         'xaxis': 'Z^{lep}_{3}',
                         'fold': 3
                         }

variables['Zlep4']  = {  'name': '(Alt$(Lepton_eta[3],-9999.) - (Alt$(Jet_eta[0],-9999.)+Alt$(Jet_eta[1],-9999.))/2)/detajj',
                         'range': (10,-1.5,1.5),
                         'xaxis': 'Z^{lep}_{4}',
                         'fold': 3
                         }



variables['mjj']  = {  'name': 'mjj', # for ZZCR in paper  WW (AN-19-089) pg 37 1D
                       'range': ([500, 800, 1200, 1800, 3000],),
                       'xaxis': 'mjj [GeV]',
                       'fold': 3,
                       }

variables['pt1']  = {   'name': 'Alt$(Lepton_pt[0],-9999.)',
                        'range' : (20,0.,250),
                        'xaxis' : 'p_{T} 1st lep',
                        'fold'  : 3
                        }

variables['pt2']  = {   'name': 'Alt$(Lepton_pt[1],-9999.)',
                        'range' : (20,0.,250),
                        'xaxis' : 'p_{T} 2nd lep',
                        'fold'  : 3
                        }

variables['pt3']  = {   'name': 'Alt$(Lepton_pt[2],-9999.)',
                        'range' : (20,0.,250),
                        'xaxis' : 'p_{T} 3th lep',
                        'fold'  : 3
                        }

variables['pt4']  = {   'name': 'Alt$(Lepton_pt[3],-9999.)',
                        'range' : (20,0.,250),
                        'xaxis' : 'p_{T} 4th lep',
                        'fold'  : 3
                        }



# I follow woth the same detajj because have the same selection (Cuts) for all signals reported in ww article (Check Well With Patrizia this Variable)
variables['detajj']  = {  'name': 'detajj',
                          'range': (16,0.0,8.0),
                          'xaxis': 'detajj',
                          'fold': 3,
                          }



###############################################################################
#Variables to plot

variables = {k:v for k,v in variables.items() if k in ['events', 'jetpt1', 'jetpt2', 'etaj1', 'etaj2', 'eta1', 'eta2', 'eta3', 'eta4', 'Zlep1', 'Zlep2', 'Zlep3', 'Zlep4', 'mjj', 'pt1', 'pt2', 'pt3', 'pt4',  'detajj', 'nJet']}
