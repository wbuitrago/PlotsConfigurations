# cuts

cuts = {}
  
supercut = 'Lepton_pt[0] >= 25 && CleanJet_pt[1] >= 25'

cuts["no_cut"] = '1.'

'''
cuts["lept_pt25"] = 'Lepton_pt[0] >= 25'
cuts["Jet25_pt1"] = 'CleanJet_pt[0] >= 25'
cuts["Jet25_pt2"] = 'CleanJet_pt[1] >= 25'
cuts["Jet25_pt3"] = 'CleanJet_pt[2] >= 25'
cuts["Jet25_pt4"] = 'CleanJet_pt[3] >= 25'
cuts["Jet30_pt1"] = 'CleanJet_pt[0] >= 30'
cuts["Jet30_pt2"] = 'CleanJet_pt[1] >= 30'
cuts["Jet30_pt3"] = 'CleanJet_pt[2] >= 30 '
cuts["Jet30_pt4"] = 'CleanJet_pt[3] >= 30'

#cuts['btag_loose_1']  = 'Sum$(1*(Jet_btagDeepB[CleanJet_jetIdx[0]] > 0.1522)*(CleanJet_pt[0]>25))>=1'
#cuts['btag_medium_1']  = 'Sum$(1*(Jet_btagDeepB[CleanJet_jetIdx[0]] > 0.4941)*(CleanJet_pt[0]>25))>=1'
#cuts['btag_tight_1']  = 'Sum$(1*(Jet_btagDeepB[CleanJet_jetIdx[0]] > 0.8001)*(CleanJet_pt[0]>25))>=1'

cuts['btag_loose_2']  = '(1*(btagWeight_DeepCSVB[0]>loose)*CleanJet_pt[0]>25 + \
                        1*(btagWeight_DeepCSVB[1]>loose)*CleanJet_pt[1]>25 + \
                        1*(btagWeight_DeepCSVB[2]>loose)*CleanJet_pt[2]>25 + \
                        1*(btagWeight_DeepCSVB[3]>loose)*CleanJet_pt[3]>25 + \
                        1*(btagWeight_DeepCSVB[4]>loose)*CleanJet_pt[4]>25 + \
                        1*(btagWeight_DeepCSVB[5]>loose)*CleanJet_pt[5]>25 + \
                        1*(btagWeight_DeepCSVB[6]>loose)*CleanJet_pt[6]>25 + \
                        1*(btagWeight_DeepCSVB[7]>loose)*CleanJet_pt[7]>25 + \
                        1*(btagWeight_DeepCSVB[8]>loose)*CleanJet_pt[8]>25 + \
                        1*(btagWeight_DeepCSVB[9]>loose)*CleanJet_pt[9]>25)>=2'
cuts['btag_medium_2']  = '(1*(btagWeight_DeepCSVB[0]>medium)*CleanJet_pt[0]>25 + \
                        1*(btagWeight_DeepCSVB[1]>medium)*CleanJet_pt[1]>25 + \
                        1*(btagWeight_DeepCSVB[2]>medium)*CleanJet_pt[2]>25 + \
                        1*(btagWeight_DeepCSVB[3]>medium)*CleanJet_pt[3]>25 + \
                        1*(btagWeight_DeepCSVB[4]>medium)*CleanJet_pt[4]>25 + \
                        1*(btagWeight_DeepCSVB[5]>medium)*CleanJet_pt[5]>25 + \
                        1*(btagWeight_DeepCSVB[6]>medium)*CleanJet_pt[6]>25 + \
                        1*(btagWeight_DeepCSVB[7]>medium)*CleanJet_pt[7]>25 + \
                        1*(btagWeight_DeepCSVB[8]>medium)*CleanJet_pt[8]>25 + \
                        1*(btagWeight_DeepCSVB[9]>medium)*CleanJet_pt[9]>25)>=2'
cuts['btag_tight_2']  = '(1*(btagWeight_DeepCSVB[0]>tight)*CleanJet_pt[0]>25 + \
                        1*(btagWeight_DeepCSVB[1]>tight)*CleanJet_pt[1]>25 + \
                        1*(btagWeight_DeepCSVB[2]>tight)*CleanJet_pt[2]>25 + \
                        1*(btagWeight_DeepCSVB[3]>tight)*CleanJet_pt[3]>25 + \
                        1*(btagWeight_DeepCSVB[4]>tight)*CleanJet_pt[4]>25 + \
                        1*(btagWeight_DeepCSVB[5]>tight)*CleanJet_pt[5]>25 + \
                        1*(btagWeight_DeepCSVB[6]>tight)*CleanJet_pt[6]>25 + \
                        1*(btagWeight_DeepCSVB[7]>tight)*CleanJet_pt[7]>25 + \
                        1*(btagWeight_DeepCSVB[8]>tight)*CleanJet_pt[8]>25 + \
                        1*(btagWeight_DeepCSVB[9]>tight)*CleanJet_pt[9]>25)>=2'
'''
