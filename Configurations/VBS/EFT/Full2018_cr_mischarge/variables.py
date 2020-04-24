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

variables['mll']  = {   'name'  : 'mll',            #   variable name
                        'range' : (25, 15 ,500),    #   variable range
                        'xaxis' : 'mll [GeV]',      #   x axis name
                        'fold'  : 3
                        }  

variables['mll_v3']  = {    'name'  : 'mll',            #   variable name
                            'range' : (25, 75 ,105),    #   variable range
                            'xaxis' : 'mll [GeV]',      #   x axis name
                            'fold'  : 0
                        }                                                                         

variables['pt1']  = {   'name'  : 'Alt$(Lepton_pt[0],-9999.)',
                        'range' : (25,25,300.),
                        'xaxis' : 'p_{T} 1st lep [GeV]',
                        'fold'  : 3
                    }

variables['pt2']  = {   'name'  : 'Alt$(Lepton_pt[1],-9999.)',
                        'range' : (25,25,300.),
                        'xaxis' : 'p_{T} 2nd lep [GeV]',
                        'fold'  : 3
                    }      

## eta leptons
variables['eta_lep1'] = {   'name' : 'Alt$(Lepton_eta[0],-9999.)',
                            'range': (20,-2.5,2.5),
                            'xaxis': 'eta lep1',
                            'fold' : 3
                            }

variables['eta_lep2'] = {   'name' : 'Alt$(Lepton_eta[1],-9999.)',
                            'range': (20,-2.5,2.5),
                            'xaxis': 'eta lep2',
                            'fold' : 3
                            }

variables['detall']  = {  'name' : 'fabs(Alt$(Lepton_eta[0],-9999.)-Alt$(Lepton_eta[1],9999.))',
                          'range': (20,0.0,5.0),
                          'xaxis': 'deta ll',
                          'fold' : 3
                          }                            

## phi leptons
       
variables['phi_lep1'] = {   'name' : 'Alt$(Lepton_phi[0],-9999.)',
                            'range': (20,-3.141592,3.141592),
                            'xaxis': 'phi lep1',
                            'fold' : 3
}

variables['phi_lep2'] = {   'name' : 'Alt$(Lepton_phi[1],-9999.)',
                            'range': (20,-3.141592,3.141592),
                            'xaxis': 'phi lep2',
                            'fold' : 3  
                            }               

variables['dphill'] = {     'name' : 'Alt$(dphill,-9999.)',
                            'range': (20,0,3.141592),
                            'xaxis': 'dphi ll',
                            'fold' : 3    
                            }                               

###########################
##### JETS   VARS #########
###########################

variables['nJet']  = {      'name'  : 'nCleanJet',
                            'range' : (7,0,7),
                            'xaxis' : '# Clean Jets',
                            'fold'  : 3
                            }

variables['mjj']  = {  'name' : 'mjj',
                       'range': (25,0.,1000.),
                       'xaxis': 'mjj [GeV]',
                       'fold' : 3
                       } 
                   

variables['jetpt1']  = {   'name'  : 'Alt$(CleanJet_pt[0],-9999.)',
                           'range' : (25,30.,300),
                           'xaxis' : 'p_{T} 1st jet [GeV]',
                           'fold'  : 3
                           }

variables['jetpt2']  = {   'name'  : 'Alt$(CleanJet_pt[1],-9999.)',
                           'range' : (25,30.,200),
                           'xaxis' : 'p_{T} 2nd jet [GeV]',
                           'fold'  : 3
                           }     

# eta jets
variables['etaj1'] = {  'name' : 'Alt$(CleanJet_eta[0],-9999.)',
                        'range': (20,-5,5),
                        'xaxis': 'eta j1',
                        'fold' : 3
                        }

variables['etaj2'] = {  'name' : 'Alt$(CleanJet_eta[1],-9999.)',
                        'range': (20,-5,5),
                        'xaxis': 'eta j2',
                        'fold' : 3
                        }      

# variables['detajj']  = {  'name' : 'detajj',
#                           'range': (4,2.5,9.0),
#                           'xaxis': 'deta jj',
#                           'fold' : 3
#                           }

# variables['detajj_v1']  = { 'name' : 'detajj',
#                             'range': ([2.5,3.5,5.0,6.5,9.0],),
#                             'xaxis': 'deta jj v1',
#                             'fold' : 3
#                             }                          

# phi jets
       
variables['phi_j1'] = {     'name' : 'Alt$(CleanJet_phi[0],-9999.)',
                            'range': (20,-3.141592,3.141592),
                            'xaxis': 'phi j1',
                            'fold' : 3
                    }

variables['phi_j2'] = { 'name' : 'Alt$(CleanJet_phi[1],-9999.)',
                        'range': (20,-3.141592,3.141592),
                        'xaxis': 'phi j2',
                        'fold' : 3  
                        }                             

variables['dphijj']  = {    'name' : 'my_dphijj' ,
                            'range': (20,0.0,3.141592),
                            'xaxis': 'dphi jj',
                            'fold' : 3
                        }      
                                                                                 

###########################
##### MET    VARS #########
###########################

variables['met']  = {           'name'  : 'MET_pt',         #  variable name
                                'range' : (20,30,250),       #  variable range
                                'xaxis' : 'met [GeV]',      #  x axis name
                                'fold'  : 3
                    }

###########################
##### bTag Variables ######
###########################

variables['Jet_btagDeepB_0']  = {   'name'  : 'Jet_btagDeepB[CleanJet_jetIdx[0]]',   
                                    'range' : (10,0,1),        
                                    'xaxis' : 'Jet_btagDeepB_0',     
                                    'fold'  : 3
                                }

variables['Jet_btagDeepB_1']  = {   'name'  : 'Jet_btagDeepB[CleanJet_jetIdx[1]]',   
                                    'range' : (10,0,1),        
                                    'xaxis' : 'Jet_btagDeepB_1',     
                                    'fold'  : 3
                                }

# # # one only for the first two jets. It gives the btag variable for the most central of the first two CleanJets
# variables['central_jet_btag']  = {   'name'  : 'central_jet_btag',
#                                 'range' : (10,0,1),        
#                                 'xaxis' : 'central_jet_btag_var',     
#                                 'fold'  : 3
#                             }


#############################
#### Zeppenfeld Variable ####
#############################                     
                        
# variables['Zlep1']  = {  'name': 'zlep1',
#                          'range': (10,-1.5,1.5),
#                          'xaxis': 'Z^{lep}_{1}',
#                          'fold': 3
#                          }

# variables['Zlep1_sr']  = {  'name': 'zlep1',
#                             'range': (5,-0.75,0.75),
#                             'xaxis': 'Z^{lep}_{1}',
#                             'fold': 3
#                          }

# variables['Zlep2']  = {  'name': 'zlep2',
#                          'range': (10,-1.5,1.5),
#                          'xaxis': 'Z^{lep}_{2}',
#                          'fold': 3
#                          }

###############################
### control var for pt veto ###
###############################

# variables['pt3']  = {   'name'  : 'Alt$(Lepton_pt[2],-9999.)',
#                         'range' : (25,0.,100.),
#                         'xaxis' : 'p_{T} 3rd lep [GeV]',
#                         'fold'  : 3
#                         }  
