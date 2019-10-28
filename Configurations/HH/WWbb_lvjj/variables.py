# variables

#variables = {}
    

variables['events']  = {   'name': '1',      
                        'range' : (1000,0,1000),  
                        'xaxis' : 'events', 
                        'fold' : 3
                        }

################
#### LEPTON ####
################

variables['btagging_loose']  = {   'name': 'Sum$(1*(Jet_btagDeepB[CleanJet_jetIdx[0]] > 0.1522)*(CleanJet_pt[0]>30))',
                        'range' : (5,-0.5,4.5),   
                        'xaxis' : 'lepton pt (GeV)',
                       'fold'  : 3                         
                        }
variables['btagging_medium']  = {   'name': 'Sum$(1*(Jet_btagDeepB[CleanJet_jetIdx[0]] > 0.4941)*(CleanJet_pt[0]>30))',
                        'range' : (5,-0.5,4.5),   
                        'xaxis' : 'lepton pt (GeV)',
                        'fold'  : 3                         
                        }
variables['btagging_tight']  = {   'name': 'Sum$(1*(Jet_btagDeepB[CleanJet_jetIdx[0]] > 0.8001)*(CleanJet_pt[0]>30))',
                        'range' : (5,-0.5,4.5),   
                        'xaxis' : 'lepton pt (GeV)',
                        'fold'  : 3                         
                        }
'''
variables['lepton_pt']  = {   'name': 'Lepton_pt[0]',     
                        'range' : (50,0,200),   
                        'xaxis' : 'lepton pt (GeV)',
                        'fold'  : 3                         
                        }

variables['lepton_eta'] = {   'name': 'abs(Lepton_eta[0])',      
                        'range' : (50,0,2.5),  
                        'xaxis' : 'Lepton #eta', 
                        'fold' : 3
                        }

###########
### JET ###
###########

variables['nJets'] = {   'name': 'Sum$(CleanJet_pt>= 30)',      
                        'range' : (10,0,10),  
                        'xaxis' : 'nJets >= 30 GeV', 
                        'fold' : 3
                        }
variables['Jet1_pt'] = {   'name': 'abs(CleanJet_pt[0])',      
                        'range' : (40,0,300),  
                        'xaxis' : 'Jet 1st pt', 
                        'fold' : 3
                        }
variables['Jet2_pt'] = {   'name': 'abs(CleanJet_pt[1])',      
                        'range' : (40,0,200),  
                        'xaxis' : 'Jet 2nd pt', 
                        'fold' : 3
                        }
variables['Jet3_pt'] = {   'name': 'abs(CleanJet_pt[2])',      
                        'range' : (40,0,160),  
                        'xaxis' : 'Jet 3rd pt', 
                        'fold' : 3
                        }
variables['Jet4_pt'] = {   'name': 'abs(CleanJet_pt[3])',      
                        'range' : (30,0,120),  
                        'xaxis' : 'Jet 4th pt', 
                        'fold' : 3
                        }
###########
### MET ###
###########

variables['PuppiMET'] = {   'name': 'PuppiMET_pt',      
                        'range' : (30,0,250),  
                        'xaxis' : 'PuppiMET_pt', 
                        'fold' : 3
                        }
variables['MET_pt'] = {   'name': 'MET_pt',      
                        'range' : (30,0,250),  
                        'xaxis' : 'MET_pt', 
                        'fold' : 3
                        }
variables['nbjet_medium']  = {
                        'name': '1*(Jet_btagDeepB[CleanJet_Idx[0]]>0.4941)+1*(Jet_btagDeepB[CleanJet_Idx[1]]>0.4941)+1*(Jet_btagDeepB[CleanJet_Idx[2]]>0.4941)+1*(Jet_btagDeepB[CleanJet_Idx[3]]>0.4941)+1*(Jet_btagDeepB[CleanJet_Idx[4]]>0.4941)+1*(Jet_btagDeepB[CleanJet_Idx[5]]>0.4941)',
                        'range' : (10,0,10),
                        'xaxis' : 'nbjet_loose',
                        'fold'  : 3
                        }
'''
