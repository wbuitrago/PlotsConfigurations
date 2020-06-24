## variabeadines
import numpy as np
## variabeadines
from itertools import chain

###########################
##### LEPTON VARS #########
###########################

# variables['nLepton'] =  {   'name': 'nLepton',
#                             'range': (7,0,7),
#                             'xaxis': '# leptons',
#                             'fold': 3
# }
variables['mll']  = {    'name'  : 'mll',            #   variable name
                            'range' : ([20,80,140,240,500],),    #   variable range
                            'xaxis' : 'mll v1 [GeV]',      #   x axis name
                            'fold'  : 3
                            }

variables['Lepton_pt1']  = {   'name'  : 'Lepton_pt[0]',
                        'range' : (5,30.,300.),
                        'xaxis' : 'p_{T} 1st lep [GeV]',
                        'fold'  : 3
                        }

variables['Lepton_pt2']  = {   'name'  : 'Lepton_pt[1]',
                        'range' : (5,30.,200.),
                        'xaxis' : 'p_{T} 2nd lep [GeV]',
                        'fold'  : 3
                        }
## eta leptons
variables['Lepton_eta1'] = {   'name' : 'Lepton_eta[0]',
                            'range': (20,-2.5,2.5),
                            'xaxis': 'eta lep1',
                            'fold' : 3
                        }
variables['Lepton_eta2'] = {   'name' : 'Lepton_eta[1]',
                            'range': (20,-2.5,2.5),
                            'xaxis': 'eta lep2',
                            'fold' : 3
                        }

variables['detall']  = {  'name' : 'abs(detall)',
                        'range': (5,0.0,5.0),
                        'xaxis': 'deta ll',
                        'fold' : 3
                        }

## phi leptons
variables['Lepton_phi1'] = {   'name' : 'Lepton_phi[0]',
                            'range': (10,-3.141592,3.141592),
                            'xaxis': 'phi lep1',
                            'fold' : 3
}

variables['Lepton_phi2'] = {   'name' : 'Lepton_phi[1]',
                            'range': (10,-3.141592,3.141592),
                            'xaxis': 'phi lep2',
                            'fold' : 3
                            }

variables['dphill'] = {     'name' : 'dphill',
                            'range': (5,0,3.141592),
                            'xaxis': 'dphi ll',
                            'fold' : 3
                            }


###########################
##### JETS   VARS #########
###########################

# variables['nJet']  = {      'name'  : 'nCleanJet',
#                             'range' : (7,2,7),
#                             'xaxis' : '# Clean Jets',
#                             'fold'  : 3
#                             }
variables['nJets'] = {   'name': 'Sum(CleanJet_pt >= 30)',      
                        'range' : (4,2,6),  
                        'xaxis' : 'nJets >= 30 GeV', 
                        'fold' : 3
                        }

variables['mjj']  = {   'name' : 'mjj',
                        'range': ([500,800,1100,1500,2000,3000],),
                        'xaxis': 'mjj [GeV]',
                        'fold' : 3
                    }
variables['Jet_pt1']  = {   'name'  : 'Alt(CleanJet_pt,0,-999)',
                            'range' : ([30,80,120,150,200,300],),
                            'xaxis' : 'p_{T} 1st jet [GeV]',
                            'fold'  : 3
                        }
variables['Jet_pt2']  = {   'name'  : 'Alt(CleanJet_pt,1,-999)',
                            'range' : ([30,70,100,130,200],),
                            'xaxis' : 'p_{T} 2nd jet [GeV]',
                            'fold'  : 3
                        }
# eta
variables['Jet_eta1'] = {  'name' : 'Alt(CleanJet_eta,0,-999)',
                        'range': (10,-5,5),
                        'xaxis': 'eta j1',
                        'fold' : 3
                    }
variables['Jet_eta2'] = {  'name' : 'Alt(CleanJet_eta,1,-999)',
                        'range': (10,-5,5),
                        'xaxis': 'eta j2',
                        'fold' : 3
                    }

variables['detajj']  = {  'name' : 'detajj',
                            'range': (5,2.5,9.0),
                            'xaxis': 'deta jj',
                            'fold' : 3
                        }
# phi jets

variables['Jet_phi1'] = {     'name' : 'Alt(CleanJet_phi,0,-999)',
                            'range': (10,-3.141592,3.141592),
                            'xaxis': 'phi_j1',
                            'fold' : 3
                    }

variables['Jet_phi2'] = { 'name' : 'Alt(CleanJet_phi,1,-999)',
                        'range': (10,-3.141592,3.141592),
                        'xaxis': 'phi_j2',
                        'fold' : 3
                        }

variables['dphijj']  = {    'name' : 'dphijj' ,
                            'range': (5,0.0,3.141592),
                            'xaxis': 'dphi jj',
                            'fold' : 3
                            }

###########################
##### MET    VARS #########
###########################

variables['met']  = {   'name'  : 'MET_pt',         #  variable name
                        'range' : (5,30,300),       #  variable range
                        'xaxis' : 'met [GeV]',      #  x axis name
                        'fold'  : 3
                        }
variables['MET_significance']  = {  'name'  : 'MET_significance',
                                    'range' : (10,0.,1.),
                                    'xaxis' : 'MET_significance',
                                    'fold'  : 3
                    }

#variables['DNNScore'] = {
#    'name': 'DNNScore',
#    'range': ([0.1,0.2,0.3,0.4,0.5,0.55, 0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1],),
#    'xaxis': 'DNN output',
#    'fold': 3 ,
#}
###########################
##### bTag Variables ######
###########################

# variables['Jet_btagDeepB_0']  = {   'name'  : 'Jet_btagDeepB[CleanJet_jetIdx[0]]',
#                                     'range' : (10,0,1),
#                                     'xaxis' : 'Jet_btagDeepB_0',
#                                     'fold'  : 3
#                                 }

# variables['Jet_btagDeepB_1']  = {   'name'  : 'Jet_btagDeepB[CleanJet_jetIdx[1]]',
#                                     'range' : (10,0,1),
#                                     'xaxis' : 'Jet_btagDeepB_1',
#                                     'fold'  : 3
#                                 }

# # one only for the first two jets. It gives the btag variable for the most central of the first two CleanJets
# variables['my_btag_var']  = {   'name'  : '(fabs(CleanJet_eta[0]) <= fabs(CleanJet_eta[1])) * Jet_btagDeepB[CleanJet_jetIdx[0]] + (fabs(CleanJet_eta[0]) > fabs(CleanJet_eta[1])) * Jet_btagDeepB[CleanJet_jetIdx[1]]',
#                                 'range' : (10,0,1),
#                                 'xaxis' : 'central_jet_btag_var',
#                                 'fold'  : 3
#                             }


#############################
#### Zeppenfeld Variable ####
#############################

variables['zlep1']  = {  'name': 'abs((Lepton_eta[0] - (Alt(CleanJet_eta,0,-999)+Alt(CleanJet_eta,1,-999))/2)/detajj)',
                            'range': (10,0,1.5),
                            'xaxis': 'Z^{lep}_{1}',
                            'fold': 3
                            }

variables['Zlep2']  = {  'name': 'abs((Lepton_eta[1] - (Alt(CleanJet_eta,0,-999)+Alt(CleanJet_eta,1,-999))/2)/detajj)',
                        'range': (10,0,1.5),
                        'xaxis': 'Z^{lep}_{2}',
                        'fold': 3
                        }