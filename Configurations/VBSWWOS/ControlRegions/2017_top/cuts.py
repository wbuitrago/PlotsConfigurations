# cuts

#cuts = {}
    

#cuts['first']  = 'mll<50'
#cuts['second'] = 'mll>=50'
### supercut is added to all the other cuts


supercut = 'mll>50  \
            && ptll > 30 \
            && (Alt$(Lepton_pdgId[0]*Lepton_pdgId[1],0)==-11*13 || Alt$(Lepton_pdgId[0]*Lepton_pdgId[1],0)==-11*11 || Alt$(Lepton_pdgId[0]*Lepton_pdgId[1],0)==-13*13)\
            && Lepton_pt[0]>25 \
            && Lepton_pt[1]>13 \
            && (nLepton>=2 && Alt$(Lepton_pt[2],0)<10) \
            && nCleanJet >=2 \
            && (abs(CleanJet_eta[0]) <= 2.5 || abs(CleanJet_eta[0]) >= 3.2) \
            && (abs(CleanJet_eta[1]) <= 2.5 || abs(CleanJet_eta[1]) >= 3.2)  \
            && (MET_pt > 20 || PuppiMET_pt>20) \
           '


     


##top control regions     
cuts['top']  =             'mjj>500 \
                            && detajj > 3.5 \
                             && Alt$(CleanJet_pt[0],0.)>30 && Alt$(CleanJet_pt[1],0.)>30 && (Alt$(Jet_btagDeepB[0],0.)> 0.4941 || Alt$(Jet_btagDeepB[1],0.)> 0.4941)  \
                               && (   ( Alt$(CleanJet_pt[2],0.) < 20 || Alt$(Jet_btagDeepB[2],0.)< 0.4941 ) \
                                      && ( Alt$(CleanJet_pt[3],0.) < 20 || Alt$(Jet_btagDeepB[3],0.)< 0.4941 ) \
                                      && ( Alt$(CleanJet_pt[4],0.) < 20 || Alt$(Jet_btagDeepB[4],0.)< 0.4941 ) \
                                      && ( Alt$(CleanJet_pt[5],0.) < 20 || Alt$(Jet_btagDeepB[5],0.)< 0.4941 ) \
                                      && ( Alt$(CleanJet_pt[6],0.) < 20 || Alt$(Jet_btagDeepB[6],0.)< 0.4941  ) \
                                      && ( Alt$(CleanJet_pt[7],0.) < 20 || Alt$(Jet_btagDeepB[7],0.)< 0.4941  ) \
                                      && ( Alt$(CleanJet_pt[8],0.) < 20 || Alt$(Jet_btagDeepB[8],0.)< 0.4941 ) \
                                      && ( Alt$(CleanJet_pt[9],0.) < 20 || Alt$(Jet_btagDeepB[9],0.)< 0.4941  ) \
                                  ) \
                                  '           
cuts['top_me']  =          'mjj>500 \
                            && detajj > 3.5 \
                            && Alt$(Lepton_pdgId[0]*Lepton_pdgId[1],0)==-11*13 \
                            && Alt$(CleanJet_pt[0],0.)>30 && Alt$(CleanJet_pt[1],0.)>30 && (Alt$(Jet_btagDeepB[0],0.)> 0.4941 || Alt$(Jet_btagDeepB[1],0.)> 0.4941)  \
                            && (   ( Alt$(CleanJet_pt[2],0.) < 20 || Alt$(Jet_btagDeepB[2],0.)< 0.4941 ) \
                                      && ( Alt$(CleanJet_pt[3],0.) < 20 || Alt$(Jet_btagDeepB[3],0.)< 0.4941 ) \
                                      && ( Alt$(CleanJet_pt[4],0.) < 20 || Alt$(Jet_btagDeepB[4],0.)< 0.4941 ) \
                                      && ( Alt$(CleanJet_pt[5],0.) < 20 || Alt$(Jet_btagDeepB[5],0.)< 0.4941 ) \
                                      && ( Alt$(CleanJet_pt[6],0.) < 20 || Alt$(Jet_btagDeepB[6],0.)< 0.4941  ) \
                                      && ( Alt$(CleanJet_pt[7],0.) < 20 || Alt$(Jet_btagDeepB[7],0.)< 0.4941  ) \
                                      && ( Alt$(CleanJet_pt[8],0.) < 20 || Alt$(Jet_btagDeepB[8],0.)< 0.4941 ) \
                                      && ( Alt$(CleanJet_pt[9],0.) < 20 || Alt$(Jet_btagDeepB[9],0.)< 0.4941  ) \
                                  ) \
                                  '                    
cuts['top_ee']  = 'mjj>500 \
                   && detajj > 3.5 \
                   && Alt$(Lepton_pdgId[0]*Lepton_pdgId[1],0)==-11*11 \
                   && Alt$(CleanJet_pt[0],0.)>30 && Alt$(CleanJet_pt[1],0.)>30 && (Alt$(Jet_btagDeepB[0],0.)> 0.4941 || Alt$(Jet_btagDeepB[1],0.)> 0.4941)  \
                   && (   ( Alt$(CleanJet_pt[2],0.) < 20 || Alt$(Jet_btagDeepB[2],0.)< 0.4941 ) \
                                      && ( Alt$(CleanJet_pt[3],0.) < 20 || Alt$(Jet_btagDeepB[3],0.)< 0.4941 ) \
                                      && ( Alt$(CleanJet_pt[4],0.) < 20 || Alt$(Jet_btagDeepB[4],0.)< 0.4941 ) \
                                      && ( Alt$(CleanJet_pt[5],0.) < 20 || Alt$(Jet_btagDeepB[5],0.)< 0.4941 ) \
                                      && ( Alt$(CleanJet_pt[6],0.) < 20 || Alt$(Jet_btagDeepB[6],0.)< 0.4941  ) \
                                      && ( Alt$(CleanJet_pt[7],0.) < 20 || Alt$(Jet_btagDeepB[7],0.)< 0.4941  ) \
                                      && ( Alt$(CleanJet_pt[8],0.) < 20 || Alt$(Jet_btagDeepB[8],0.)< 0.4941 ) \
                                      && ( Alt$(CleanJet_pt[9],0.) < 20 || Alt$(Jet_btagDeepB[9],0.)< 0.4941  ) \
                                  ) \
                                  '   
cuts['top_mm']  = 'mjj>500 \
                   && detajj > 3.5 \
                   && Alt$(Lepton_pdgId[0]*Lepton_pdgId[1],0)==-13*13 \
                   && Alt$(CleanJet_pt[0],0.)>30 && Alt$(CleanJet_pt[1],0.)>30 && (Alt$(Jet_btagDeepB[0],0.)> 0.4941 || Alt$(Jet_btagDeepB[1],0.)> 0.4941)  \
                   && (   ( Alt$(CleanJet_pt[2],0.) < 20 || Alt$(Jet_btagDeepB[2],0.)< 0.4941 ) \
                                      && ( Alt$(CleanJet_pt[3],0.) < 20 || Alt$(Jet_btagDeepB[3],0.)< 0.4941 ) \
                                      && ( Alt$(CleanJet_pt[4],0.) < 20 || Alt$(Jet_btagDeepB[4],0.)< 0.4941 ) \
                                      && ( Alt$(CleanJet_pt[5],0.) < 20 || Alt$(Jet_btagDeepB[5],0.)< 0.4941 ) \
                                      && ( Alt$(CleanJet_pt[6],0.) < 20 || Alt$(Jet_btagDeepB[6],0.)< 0.4941  ) \
                                      && ( Alt$(CleanJet_pt[7],0.) < 20 || Alt$(Jet_btagDeepB[7],0.)< 0.4941  ) \
                                      && ( Alt$(CleanJet_pt[8],0.) < 20 || Alt$(Jet_btagDeepB[8],0.)< 0.4941 ) \
                                      && ( Alt$(CleanJet_pt[9],0.) < 20 || Alt$(Jet_btagDeepB[9],0.)< 0.4941  ) \
                                  ) \
                                  '    
