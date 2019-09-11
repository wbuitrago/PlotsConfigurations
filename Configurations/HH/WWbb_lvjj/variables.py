# variables

#variables = {}
    
   
variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                        'fold' : 3
                        }
    
################
#### LEPTON ####
################

variables['lepton_pt']  = {   'name': 'Lepton_pt[0]',     
                        'range' : (50,0,300),   
                        'xaxis' : 'lepton pt (GeV)',
                        'fold'  : 3                         
                        }

#variables['lepton_eta'] = {   'name': 'abs(Lepton_eta[0])',      
#                        'range' : (50,0,2.5),  
#                        'xaxis' : 'Lepton #eta', 
#                        'fold' : 3
#                        }

###########
### JET ###
###########

#variables['nJets'] = {   'name': 'Sum$(CleanJet_pt[CleanJet] >= 30)',      
#                        'range' : (10,0,10),  
#                        'xaxis' : 'nJets >= 30 GeV', 
#                        'fold' : 3
#                        }

#variables['Jet1_pt'] = {   'name': 'abs(CleanJet_pt[CleanJet[0]])',      
#                        'range' : (60,0,500),  
#                        'xaxis' : 'Jet 1st pt', 
#                        'fold' : 3
#                        }

#variables['Jet2_pt'] = {   'name': 'abs(CleanJet_pt[CleanJet[1]])',      
#                        'range' : (60,0,500),  
#                        'xaxis' : 'Jet 2nd pt', 
#                        'fold' : 3
#                        }

#variables['Jet3_pt'] = {   'name': 'abs(CleanJet_pt[CleanJet[2]])',      
#                        'range' : (60,0,500),  
#                        'xaxis' : 'Jet 3rd pt', 
#                        'fold' : 3
#                        }
#variables['Jet4_pt'] = {   'name': 'abs(CleanJet_pt[CleanJet[3]])',      
#                        'range' : (60,0,500),  
#                        'xaxis' : 'Jet 4th pt', 
#                        'fold' : 3
#                        }

###########
### MET ###
###########

#variables['PuppiMET'] = {   'name': 'PuppiMET_pt',      
#                        'range' : (60,0,500),  
#                        'xaxis' : 'PuppiMET_pt', 
#                        'fold' : 3
#                        }

#variables['MET_pt'] = {   'name': 'MET_pt',      
#                        'range' : (60,0,500),  
#                        'xaxis' : 'MET_pt', 
#                        'fold' : 3
#                        }

#variables['nbjet_medium']  = {
#                        'name': '1*(Jet_btagDeepB>0.6324)+1*(Jet_btagDeepB>0.6324)+1*(Jet_btagDeepB>0.6324)+1*(Jet_btagDeepB>0.6324)+1*(Jet_btagDeepB>0.6324)+1*(Jet_btagDeepB>0.6324)',
#                        'range' : (10,0,10),
#                        'xaxis' : 'nbjet_loose',
#                        'fold'  : 3
#                        }
