# variables

#'fold' : # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow

#variables = {}
    


variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                        'fold' : 3
                        }


# define some interesting variables, for example mll (invariant mass of the two leptons)
# lepton pt etc. etc.
# see on thesis to choose other good variables..

variables['mll']  = {   'name': 'mll',            #   variable name
                        'range' : (50, 0. ,500),    #   variable range
                        'xaxis' : 'mll [GeV]',  #   x axis name
                        'fold' : 3
                        }  

variables['pt1']  = {   'name': 'Alt$(Lepton_pt[0],-9999.)',
                        'range' : (20,0.,200),
                        'xaxis' : 'p_{T} 1st lep',
                        'fold'  : 3
                        }

variables['pt2']  = {   'name': 'Alt$(Lepton_pt[0],-9999.)',
                        'range' : (15,0.,150),
                        'xaxis' : 'p_{T} 2nd lep',
                        'fold'  : 3
                        }    
                        
                                                                                

# lepton charge product -> defined to see how many events are SS or OS
# leptons Id:   e-/+  -> +/-11
#               mu-/+ -> +/-13

variables['lep_charge_prod'] = {  'name'  : '(Lepton_pdgId[0]*Lepton_pdgId[1])/abs(Lepton_pdgId[0]*Lepton_pdgId[1])',    #   variable name
                                        'range' : (2,-1.1,1.1),                                 #   variable range
                                        'xaxis' : 'Lepton Charge Product',                      #   x axis name
                                      }


