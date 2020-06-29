# variables

# variables = {}

#'fold' : # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow

###########################
##### LEPTON VARS #########
###########################

variables['nLepton'] =  {   'name': 'nLepton',
                            'range': (7,0,7),
                            'xaxis': '# leptons',
                            'fold': 3
}

variables['mll']  = {   'name': 'mll',            #   variable name
                        'range' : (25, 0. ,500),    #   variable range
                        'xaxis' : 'mll [GeV]',  #   x axis name
                        'fold' : 3
                        }

# zoom around Z0
# variables['mll_v2']  = {    'name': 'mll',              #   variable name
#                             'range' : (100, 50 ,150),    #   variable range
#                             'xaxis' : 'mll [GeV]',      #   x axis name
#                             'fold' : 3
#                             }                        

variables['pt1']  = {   'name': 'Alt$(Lepton_pt[0],-9999.)',
                        'range' : (15,0.,300.),
                        'xaxis' : 'p_{T} 1st lep',
                        'fold'  : 3
                        }


variables['pt2']  = {   'name': 'Alt$(Lepton_pt[1],-9999.)',
                        'range' : (15,0.,300.),
                        'xaxis' : 'p_{T} 2nd lep',
                        'fold'  : 3
                        }      

# eta leptons
variables['eta_lep1'] = {   'name': 'Alt$(Lepton_eta[0],-9999.)',
                            'range': (20,-5,5),
                            'xaxis': 'eta_lep1',
                            'fold': 3
                            }

variables['eta_lep2'] = {   'name': 'Alt$(Lepton_eta[1],-9999.)',
                            'range': (20,-5,5),
                            'xaxis': 'eta_lep2',
                            'fold': 3
                            }

variables['detall']  = {  'name': 'Alt$(abs(Lepton_eta[0]-Lepton_eta[1]),-9999.)',
                          'range': (20,0.0,10.0),
                          'xaxis': 'deta_ll',
                          'fold': 3
                          }                            

# phi leptons
       
variables['phi_lep1'] = {   'name': 'Alt$(Lepton_phi[0],-9999.)',
                            'range': (20,0,2*3.14159),
                            'xaxis': 'phi_lep1',
                            'fold': 3
}

variables['phi_lep2'] = {   'name': 'Alt$(Lepton_phi[1],-9999.)',
                            'range': (20,0,2*3.14159),
                            'xaxis': 'phi_lep2',
                            'fold': 3  
                            }               

variables['dphill'] = {     'name': 'Alt$(dphill,-9999.)',
                            'range': (10,0,3.14159),
                            'xaxis': 'dphill',
                            'fold': 3    
                            }                               


###########################
##### JETS   VARS #########
###########################

variables['nJet']  = {      'name': 'nCleanJet',
                            'range' : (7,0,7),
                            'xaxis' : 'nCleanJet',
                            'fold' : 3
                            }

variables['mjj']  = {  'name': 'mjj',
                       'range': (25,0.,500.),
                       'xaxis': 'mjj [GeV]',
                       'fold': 3
                       }


variables['jetpt1']  = {   'name': 'Alt$(CleanJet_pt[0],-9999.)',
                           'range' : (20,0.,350),
                           'xaxis' : 'p_{T} 1st jet',
                           'fold'  : 3
                           }

variables['jetpt2']  = {   'name': 'Alt$(CleanJet_pt[1],-9999.)',
                           'range' : (20,0.,350),
                           'xaxis' : 'p_{T} 2nd jet',
                           'fold'  : 3
                           }     

# eta
variables['etaj1'] = {  'name': 'Alt$(CleanJet_eta[0],-9999.)',
                        'range': (20,-5,5),
                        'xaxis': 'etaj1',
                        'fold': 3
                        }

variables['etaj2'] = {  'name': 'Alt$(CleanJet_eta[1],-9999.)',
                        'range': (20,-5,5),
                        'xaxis': 'etaj2',
                        'fold': 3
                        }      

variables['detajj']  = {  'name': 'detajj',
                          'range': (20,0.0,10.0),
                          'xaxis': 'detajj',
                          'fold': 3
                          }

variables['Clean_detajj']  = {  'name': 'Alt$(abs(CleanJet_eta[0]-CleanJet_eta[1]),-9990.)',
                                'range': (20,0.0,10.0),
                                'xaxis': 'detajj',
                                'fold': 3
                                }                          

# phi jets
       
variables['phi_j1'] = {   'name': 'Alt$(CleanJet_phi[0],-9999.)',
                            'range': (20,0,2*3.14159),
                            'xaxis': 'phi_j1',
                            'fold': 3
}

variables['phi_j2'] = { 'name': 'Alt$(CleanJet_phi[1],-9999.)',
                        'range': (20,0,2*3.14159),
                        'xaxis': 'phi_j2',
                        'fold': 3  
                        }                             

variables['dphijj']  = {    'name': 'Alt$(abs(abs(abs(CleanJet_phi[0]-CleanJet_phi[1])-pi)-pi),-9999.)',
                            'range': (10,0.0,3.14159),
                            'xaxis': 'dphijj',
                            'fold': 3
                            }                                                                 


###########################
##### MET    VARS #########
###########################

variables['met']  = {   'name': 'MET_pt',            #   variable name
                        'range' : (20,0,200),        #   variable range
                        'xaxis' : 'pfmet [GeV]',     #   x axis name
                        'fold' : 3
                        }





















                        