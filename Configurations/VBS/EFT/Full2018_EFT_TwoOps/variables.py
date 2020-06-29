# variables

# variables = {}

#'fold' : # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow

###########################
##### LEPTON VARS #########
###########################

# variables['nLepton'] =  {   'name': 'nLepton',
#                             'range': (7,0,7),
#                             'xaxis': '# leptons',
#                             'fold': 3
# }

variables['events']  = {'name': '1',
                        'range' : (1,0,2),
                        'xaxis' : 'events',
                        'fold' : 3
                        }

variables['mll']  = {   'name'  : 'mll',            #   variable name
                        'range' : (4, 20. ,500),    #   variable range
                        'xaxis' : 'mll [GeV]',      #   x axis name
                        'fold'  : 3
                        }  
                                                                  
variables['pt1']  = {   'name'  : 'Alt$(Lepton_pt[0],-9999.)',
                        'range' : (4,30.,400.),
                        'xaxis' : 'p_{T} 1st lep [GeV]',
                        'fold'  : 3
                        }

variables['pt2']  = {   'name'  : 'Alt$(Lepton_pt[1],-9999.)',
                        'range' : (4,30.,180.),
                        'xaxis' : 'p_{T} 2nd lep [GeV]',
                        'fold'  : 3
                        }      


## eta leptons
# variables['eta_lep1'] = {   'name' : 'Alt$(Lepton_eta[0],-9999.)',
#                             'range': (20,-2.5,2.5),
#                             'xaxis': 'eta lep1',
#                             'fold' : 3
#                             }

# variables['eta_lep2'] = {   'name' : 'Alt$(Lepton_eta[1],-9999.)',
#                             'range': (20,-2.5,2.5),
#                             'xaxis': 'eta lep2',
#                             'fold' : 3
#                             }

variables['detall']  = {  'name' : 'fabs(Alt$(Lepton_eta[0],-9999.)-Alt$(Lepton_eta[1],9999.))',
                          'range': (5,0.0,5.0),
                          'xaxis': 'deta ll',
                          'fold' : 3
                          }                            

## phi leptons
    
variables['dphill'] = {     'name' : 'Alt$(dphill,-9999.)',
                            'range': (5,0,3.141592),
                            'xaxis': 'dphi ll',
                            'fold' : 3    
                            }                               

###########################
##### JETS   VARS #########
###########################

# variables['nJet']  = {      'name'  : 'nCleanJet',
#                             'range' : (7,0,7),
#                             'xaxis' : '# Clean Jets',
#                             'fold'  : 3
#                             }

variables['mjj']  =     {   'name' : 'mjj',
                            'range': (4,500.,2000.),
                            'xaxis': 'mjj [GeV]',
                            'fold' : 3
                            } 

# for low mjj control region
# variables['low_mjj']  = {   'name' : 'mjj',
#                             'range': (10,150,500.),
#                             'xaxis': 'mjj [GeV]',
#                             'fold' : 3
#                         }    

variables['jetpt1']  = {   'name'  : 'Alt$(CleanJet_pt[0],-9999.)',
                           'range' : (4,30.,800),
                           'xaxis' : 'p_{T} 1st jet [GeV]',
                           'fold'  : 3
                           }                      

variables['jetpt2']  = {   'name'  : 'Alt$(CleanJet_pt[1],-9999.)',
                           'range' : (3,30.,450),
                           'xaxis' : 'p_{T} 2nd jet [GeV]',
                           'fold'  : 3
                           }     

# eta
variables['etaj1'] = {  'name' : 'Alt$(CleanJet_eta[0],-9999.)',
                        'range': (5,-5,5),
                        'xaxis': 'eta j1',
                        'fold' : 3
                        }

variables['etaj2'] = {  'name' : 'Alt$(CleanJet_eta[1],-9999.)',
                        'range': (5,-5,5),
                        'xaxis': 'eta j2',
                        'fold' : 3
                        }      

variables['detajj']  = {  'name' : 'detajj',
                          'range': (5,2.5,9.0),
                          'xaxis': 'deta jj',
                          'fold' : 3
                          }
                       
# phi jets

variables['dphijj']  = {    'name' : 'my_dphijj' ,
                            'range': (5,0.0,3.141592),
                            'xaxis': 'dphi jj',
                            'fold' : 3
                        }                                                     

###########################
##### MET    VARS #########
###########################

variables['met']  = {           'name'  : 'MET_pt',         #  variable name
                                'range' : (4,30,400),       #  variable range
                                'xaxis' : 'met [GeV]',      #  x axis name
                                'fold'  : 3
                    }   

################################
###### 2D distributions ########
################################

variables['mllVSmjj']  = {  'name'  : 'mll:mjj',            #   variable name
                            'range' : (3,500,2000,4, 20. ,500),    #   variable range
                            'xaxis' : 'mll:mjj',      #   x axis name
                            'fold'  : 3
                        }  
                                                                  
variables['pt1VSmjj']  = {  'name'  : 'Lepton_pt[0]:mjj',
                            'range' : (3,500,2000,4,30.,400.),
                            'xaxis' : 'pt1:mjj',
                            'fold'  : 3
                        }

variables['pt2VSmjj']  = {  'name'  : 'Lepton_pt[1]:mjj',
                            'range' : (3,500,2000,4,30.,180.),
                            'xaxis' : 'pt2:mjj',
                            'fold'  : 3
                        }      

variables['detallVSmjj']  = {   'name' : 'fabs(Alt$(Lepton_eta[0],-9999.)-Alt$(Lepton_eta[1],9999.)) : mjj',
                                'range': (3,500,2000,5,0.0,5.0),
                                'xaxis': 'detall:mjj',
                                'fold' : 3
                            }                            

    
variables['dphillVSmjj'] = {    'name' : 'Alt$(dphill,-9999.):mjj',
                                'range': (3,500,2000,5,0,3.141592),
                                'xaxis': 'dphill:mjj',
                                'fold' : 3    
                            }                               
                            
variables['jetpt1VSmjj']  = {   'name'  : 'Alt$(CleanJet_pt[0],-9999.):mjj',
                           'range' : (3,500,2000,4,30.,800),
                           'xaxis' : 'jetpt1:mjj',
                           'fold'  : 3
                           }                      

variables['jetpt2VSmjj']  = {   'name'  : 'Alt$(CleanJet_pt[1],-9999.):mjj',
                           'range' : (3,500,2000,3,30.,450),
                           'xaxis' : 'jetpt2:mjj',
                           'fold'  : 3
                           }     

variables['etaj1VSmjj'] = {  'name' : 'Alt$(CleanJet_eta[0],-9999.):mjj',
                            'range': (3,500,2000,5,-5,5),
                            'xaxis': 'etaj1:mjj',
                            'fold' : 3
                        }

variables['etaj2VSmjj'] = {  'name' : 'Alt$(CleanJet_eta[1],-9999.):mjj',
                            'range': (3,500,2000,5,-5,5),
                            'xaxis': 'etaj2:mjj',
                            'fold' : 3
                        }      

variables['detajjVSmjj']  = {    'name' : 'detajj:mjj',
                                'range': (3,500,2000,5,2.5,9.0),
                                'xaxis': 'detajj:mjj',
                                'fold' : 3
                            }
                       

# phi jets

variables['dphijjVSmjj']  = {    'name' : 'my_dphijj:mjj' ,
                            'range': (3,500,2000,5,0.0,3.141592),
                            'xaxis': 'dphijj:mjj',
                            'fold' : 3
                        }                                                     

###########################
##### MET    VARS #########
###########################

variables['metVSmjj']  = {      'name'  : 'MET_pt:mjj',         #  variable name
                                'range' : (3,500,2000,4,30,400),       #  variable range
                                'xaxis' : 'met:mjj',      #  x axis name
                                'fold'  : 3
                    }



