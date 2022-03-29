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

supercut = 'nLepton>=1  && Lepton_pt[0]>25 \
            && Alt$(Lepton_pt[1],0)<=15 && Alt$(Lepton_isLoose[1],1)> 0.5 \
            && (  Alt$(Lepton_isTightElectron_mvaFall17V1Iso_WP90[1], 0) < 0.5 \
            && Alt$(Lepton_isTightMuon_cut_Tight_HWWW[1],0) < 0.5 )  \
            '

cuts['Z'] = '1'

cuts['ele'] = 'abs(Lepton_pdgId[0])==11 \
                '


cuts['mu'] = 'abs(Lepton_pdgId[0])==13 \
             '    

cuts['horn_ele'] = '((Alt$(abs(CleanJet_eta[0]), 3) <2.5) || (Alt$(abs(CleanJet_eta[0]), 0) > 3.))\
                    && ((Alt$(abs(CleanJet_eta[1]), 3) <2.5) || (Alt$(abs(CleanJet_eta[1]), 0) >3.))\
                    && Alt$(abs(Lepton_pdgId[0]),0) == 11'

cuts['horn_mu'] = '((Alt$(abs(CleanJet_eta[0]), 3) <2.5) || (Alt$(abs(CleanJet_eta[0]), 0) > 3.))\
                    && ((Alt$(abs(CleanJet_eta[1]), 3) <2.5) || (Alt$(abs(CleanJet_eta[1]), 0) >3.))\
                    && Alt$(abs(Lepton_pdgId[0]),0) == 13'

                    
# Top control region
cuts['topcr_ele']  = '((zeroJet && !bVeto) || bReqTight) \
                      && Alt$(abs(Lepton_pdgId[0]),0) == 11'

cuts['topcr_mu']  = '((zeroJet && !bVeto) || bReqTight) \
                      && Alt$(abs(Lepton_pdgId[0]),0) == 13'


## Fake CR
cuts['FakeCR_ele']  = '(mtw1 <= 40.) \
                       && PuppiMET_pt<=40. \
                       && bVeto \
                       && detajj < 4. \
                       && CleanJet_pt[1]>60. \
                       && Alt$(abs(Lepton_pdgId[0]),0) == 11'

cuts['FakeCR_mu']  = '(mtw1 <= 40.) \
                       && PuppiMET_pt<=40. \
                       && bVeto\
                       && detajj < 4. \
                       && CleanJet_pt[1]>60. \
                       && Alt$(abs(Lepton_pdgId[0]),0) == 13'

##WJets PU CR
cuts['WJetsPUCR_ele']  = 'detajj >= 4. \
                       && CleanJet_pt[1]<=60.\
                       && bVeto \
                       && mtw1 > 40. \
                       && PuppiMET_pt>40. \
                       && Alt$(abs(Lepton_pdgId[0]),0) == 11'

##WJets PU CR
cuts['WJetsPUCR_mu']  = 'detajj >= 4. \
                       && CleanJet_pt[1]<=60.\
                       && bVeto \
                       && mtw1 > 40. \
                       && PuppiMET_pt>40. \
                       && Alt$(abs(Lepton_pdgId[0]),0) == 13'


#cuts['E1'] = 'Lepton_pt[0] >= 30. \
#            && Alt$(CleanJet_pt[1], 0) > 30. \
#            && CleanJet_pt[0] > 100. \
#            && mjj >= 500. \
#            && detajj > 2. \
#            && Lepton_eta[0] > -2 && Lepton_eta[0] < 2'





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


