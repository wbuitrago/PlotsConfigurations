# cuts

# Second lepton veto already done in post-processing 
#and Lepton WP setup in samples.py
#supercut = '(   (abs(Lepton_pdgId[0])==11 && Lepton_pt[0]>35)\
#             || (abs(Lepton_pdgId[0])==13 && Lepton_pt[0]>30 ) ) \
#            && Alt$(Lepton_pt[1],0)<=10 && Alt$(Lepton_isLoose[1],1)> 0.5 \
#            && vbs_0_pt > 50 && vbs_1_pt > 30 \
#            && PuppiMET_pt > 30 \
#            && deltaeta_vbs >= 2.5  \
#            && mjj_vbs >= 500 \
#            && Mtw_lep < 185 \
#            '

supercut = '1'

########prova
#cuts["fatjet_ele"] = 'abs(Lepton_pdgId[0])==11 \
#                        && Lepton_pt[0] >= 40 \
#                        '


cuts['Z'] = '1'

#cuts['A1'] = 'Lepton_pt[0] >= 30. \
#            '

#cuts['A2'] = 'Alt$(CleanJet_pt[1], 0) > 30. \
#            '

cuts['A'] = 'Lepton_pt[0] >= 30. \
            && Alt$(CleanJet_pt[1], 0) > 30. \
            '     


cuts['B1'] = 'Lepton_pt[0] >= 30. \
            && Alt$(CleanJet_pt[1], 0) > 30. \
            && CleanJet_pt[0] > 100.'

cuts['B2'] = 'Lepton_pt[0] >= 30. \
            && Alt$(CleanJet_pt[1], 0) > 30. \
            && CleanJet_pt[0] > 100. \
            && CleanJet_pt[1] > 50.'


cuts['C1'] = 'Lepton_pt[0] >= 30. \
            && Alt$(CleanJet_pt[1], 0) > 30. \
            && CleanJet_pt[0] > 100. \
            && mjj >= 500.'

cuts['C2'] = 'Lepton_pt[0] >= 30. \
            && Alt$(CleanJet_pt[1], 0) > 30. \
            && CleanJet_pt[0] > 100. \
            && CleanJet_pt[1] > 50. \
            && mjj >= 500.'


cuts['D1'] = 'Lepton_pt[0] >= 30. \
            && Alt$(CleanJet_pt[1], 0) > 30. \
            && CleanJet_pt[0] > 100. \
            && mjj >= 500. \
            && detajj > 2.'

cuts['D2'] = 'Lepton_pt[0] >= 30. \
            && Alt$(CleanJet_pt[1], 0) > 30. \
            && CleanJet_pt[0] > 100. \
            && CleanJet_pt[1] > 50. \
            && mjj >= 500. \
            && detajj > 1.'


cuts['E1'] = 'Lepton_pt[0] >= 30. \
            && Alt$(CleanJet_pt[1], 0) > 30. \
            && CleanJet_pt[0] > 100. \
            && mjj >= 500. \
            && detajj > 2. \
            && Lepton_eta[0] > -2 && Lepton_eta[0] < 2'

cuts['E2'] = 'Lepton_pt[0] >= 30. \
            && Alt$(CleanJet_pt[1], 0) > 30. \
            && CleanJet_pt[0] > 100. \
            && CleanJet_pt[1] > 50. \
            && mjj >= 500. \
            && detajj > 1. \
            && Lepton_eta[0] > -2 && Lepton_eta[0] < 2'




#cuts['B'] = 'Lepton_pt[0] >= 30. \
#            && Alt$(CleanJet_pt[1], 0) > 30. \
#            && mjj >= 200.'

#cuts['C'] = 'Lepton_pt[0] >= 30. \
#            && Alt$(CleanJet_pt[1], 0) > 30. \
#            && mjj >= 400'

#cuts['D'] = 'Lepton_pt[0] >= 30. \
#            && Alt$(CleanJet_pt[1], 0) > 30. \
#            && mjj >= 200. \
#            && detajj >= 1'

#cuts['E'] = 'Lepton_pt[0] >= 30 \
#            && Alt$(CleanJet_pt[1], 0) > 30. \
#            && mjj >= 200 \
#            && detajj >= 2'


############ 
## Signal

#cuts["res_onshell"] = 'VBS_category==1 \
#                      && vjet_0_pt > 30 && vjet_1_pt > 30 \
#                      && mjj_vjet > 65 && mjj_vjet < 105 \
#                      && w_had_pt < 200 \
#                      && veto_fatjet_180 \
#                      '

#cuts["boost_onshell"] = 'VBS_category==0 \
#                            && w_had_pt >= 200 \
#                            && mjj_vjet > 70 && mjj_vjet < 115 \
#                            '


###############
##### Offshell

#cuts["res_offshell"] = 'VBS_category==1 \
#                                && vjet_0_pt > 30 && vjet_1_pt > 30 \
#                                && mjj_vjet> 40 && (mjj_vjet <= 65 || mjj_vjet >= 105) \
#                                && w_had_pt < 200 \
#                                && veto_fatjet_180 \
#                                '

#cuts["boost_offshell"] = 'VBS_category==0 \
#                             && w_had_pt >= 200 \
#                            && mjj_vjet > 40 && (mjj_vjet <= 70 || mjj_vjet >= 115)  \
#                            '


