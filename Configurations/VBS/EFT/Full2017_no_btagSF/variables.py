# variables

# 'fold' : # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow

# variables = {}
    
variables['events']  = {  'name': '1',      
                          'range' : (1,0,2),  
                          'xaxis' : 'events', 
                          'fold' : 3
                          }

# lepton charge product -> defined to see how many events are SS or OS
# leptons Id:   e-/+  -> +/-11
#               mu-/+ -> +/-13
variables['lep_charge_prod'] = {  'name'  : '(Lepton_pdgId[0]*Lepton_pdgId[1])/abs(Lepton_pdgId[0]*Lepton_pdgId[1])',    #   variable name
                                  'range' : (2,-1.1,1.1),                                 #   variable range
                                  'xaxis' : 'Lepton Charge Product',                      #   x axis name
                                  }


# kinematic variables
variables['detajj'] = { 'name': 'detajj',
                        'range': (10,0,10),
                        'xaxis': '#Delta #eta_{jj}',
                        'fold': 3
                        }

variables['mll']  = {   'name': 'mll',            #   variable name
                        'range' : (50,0,500),  #   variable range
                        'xaxis' : 'mll [GeV]',    #   x axis name
                        'fold' : 3
                        }  


variables['mjj'] = {  'name': 'mjj',
                      'range': (25,0,2500),
                      'xaxis': 'm_jj [GeV]',
                      'fold': 3
                      }

# jets pt
variables['jet_pt1'] = {  'name': 'Jet_pt[0]',
                          'range': (50,0,500),
                          'xaxis': 'p_{T} 1st jet [GeV]',
                          'fold': 3
                          }

variables['jet_pt2'] = {  'name': 'Jet_pt[1]',
                          'range': (50,0,500),
                          'xaxis': 'p_{T} 2nd jet [GeV]',
                          'fold': 3
                          }

# leptons pt
variables['pt1']  = {   'name': 'Alt$(Lepton_pt[0],-9999.)',
                        'range' : (30,0,300),
                        'xaxis' : 'p_{T} 1st lep [GeV]',
                        'fold'  : 3
                        }

variables['pt2']  = {   'name': 'Alt$(Lepton_pt[1],-9999.)',
                        'range' : (30,0,300),
                        'xaxis' : 'p_{T} 2nd lep [GeV]',
                        'fold'  : 3
                        }    
                        



