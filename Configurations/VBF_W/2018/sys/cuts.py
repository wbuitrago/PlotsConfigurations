# cuts

# Second lepton veto already done in post-processing 
#and Lepton WP setup in samples.py
# supercut = 'Lepton_pt[0]>25 \
#             && Alt$(Lepton_pt[1],0)<=15 && Alt$(Lepton_isLoose[1],1)> 0.5 \
#             && (  Alt$(Lepton_isTightElectron_mvaFall17V1Iso_WP90[1], 0) < 0.5 \
#             && Alt$(Lepton_isTightMuon_cut_Tight_HWWW[1],0) < 0.5 ) \
#             && Alt$(CleanJet_pt[1],0) >30. \
#             && (Alt$(CleanJet_pt[0],0) > 40.)
#             && mjj>400.\
#             && (detajj > 2.)
#             && ((Alt$(abs(CleanJet_eta[0]), 3) <2.5) || (Alt$(abs(CleanJet_eta[0]), 0) > 3.))\
#             && ((Alt$(abs(CleanJet_eta[1]), 3) <2.5) || (Alt$(abs(CleanJet_eta[1]), 0) >3.))\
#            '

supercut = '((Alt$(abs(CleanJet_eta[0]), 3) <2.5) || (Alt$(abs(CleanJet_eta[0]), 0) > 3.))\
             && ((Alt$(abs(CleanJet_eta[1]), 3) <2.5) || (Alt$(abs(CleanJet_eta[1]), 0) >3.))\
            '

# skim: 
# '"(Alt$(Lepton_pt[0],0) > 25.) && 
# (Alt$(CleanJet_pt[1], 0) > 30.) && 
# (Alt$(CleanJet_pt[0],0) > 40.) && (mjj >= 400.) && 
# (detajj > 2.) && (Alt$(Lepton_eta[0],-3) > -2.) && 
# (Alt$(Lepton_eta[0],3) < 2.) && Alt$(Lepton_pt[1],0)<=15. && 
# Alt$(Lepton_isLoose[1],1)> 0.5 && (
#   Alt$(Lepton_isTightElectron_mvaFall17V1Iso_WP90[1], 0) < 0.5 && 
# Alt$(Lepton_isTightMuon_cut_Tight_HWWW[1],0) < 0.5 )"',

cuts['Z'] = '1'

cuts['do_or_do_not'] = 'Lepton_isTightElectron_mvaFall17V1Iso_WP90[0] > 0.5\
                        || Lepton_isTightMuon_cut_Tight_HWWW[0] > 0.5'

#cuts['ANWJets'] = 'PuppiMET_pt>50. \
#                    && CleanJet_pt[1]>60. \
#                    && bVeto \
#                    && mtw1 < 50. \
#                   '

# cuts['ele_HWJ'] = '(abs(Lepton_pdgId[0])==11) \
#                     && CleanJet_pt[1]>70. \
#                     && CleanJet_pt[0]<100. \
#                     && bVeto \
#                     && mtw1 > 60. \
#                     && mjj <= 750. \
#                     '

# cuts['ele_PUWJ'] = '(abs(Lepton_pdgId[0])==11) \
#                     && detajj >= 5. \
#                     && CleanJet_pt[1]<=50.\
#                     && bVeto \
#                     && PuppiMET_pt>70. \
#                     && mtw1>50. \
#                     && CleanJet_pt[0]<70. \
#                     '

cuts['mu_HWJ'] = '(abs(Lepton_pdgId[0])==13) \
                    && CleanJet_pt[1]>70. \
                    && CleanJet_pt[0]<100. \
                    && bVeto \
                    && mtw1 > 60. \
                    && mjj <= 750. \
                    '

cuts['mu_PUWJ'] = '(abs(Lepton_pdgId[0])==13) \
                    && detajj >= 5. \
                    && CleanJet_pt[1]<=50.\
                    && bVeto \
                    && PuppiMET_pt>70. \
                    && mtw1>50. \
                    && CleanJet_pt[0]<70. \
                    '

#cuts['horn'] = '((Alt$(abs(CleanJet_eta[0]), 3) <2.5) || (Alt$(abs(CleanJet_eta[0]), 0) > 3.))\
#                && ((Alt$(abs(CleanJet_eta[1]), 3) <2.5) || (Alt$(abs(CleanJet_eta[1]), 0) >3.))\
#                '

# cuts['massiro'] = 'CleanJet_pt[1] < 70. \
#                 && bVeto \
#                 && PuppiMET_pt > 70. \
#                 '
                    
# # Top control region
# cuts['topcr']  = '((zeroJet && !bVeto) || bReqTight) \
#                     '

# cuts['skimR'] = 'Lepton_pt[0] >= 30. \
#               && Alt$(CleanJet_pt[1], 0) > 30. \
#               && CleanJet_pt[0] > 100. \
#               && mjj >= 500. \
#               && detajj > 2. \
#               && Lepton_eta[0] > -2 && Lepton_eta[0] < 2'

## Fake CR
cuts['ele_FakeCR_isT']  = '(abs(Lepton_pdgId[0])==11) \
                      && detajj < 5. \
                      && bVeto\
                      && mtw1<50. \
                      && Lepton_isTightElectron_mvaFall17V1Iso_WP90[0] < 0.5 \
                      && CleanJet_pt[1]<70.  \
                     '
    
cuts['ele_FakeCR']  = '(abs(Lepton_pdgId[0])==11) \
                      && detajj < 5. \
                      && bVeto\
                      && mtw1<50. \
                      && CleanJet_pt[1]<70.  \
                     '

cuts['mu_FakeCR_isT']  = '(abs(Lepton_pdgId[0])==13) \
                      && detajj < 5. \
                      && bVeto\
                      && mtw1<50. \
                      && Lepton_isTightMuon_cut_Tight_HWWW[0] < 0.5 \
                      && CleanJet_pt[1]<70.  \
                     '
    
cuts['mu_FakeCR']  = '(abs(Lepton_pdgId[0])==13) \
                      && detajj < 5. \
                      && bVeto\
                      && mtw1<50. \
                      && CleanJet_pt[1]<70.  \
                     '

##WJets PU CR
#cuts['WJetsPUCR']  = 'detajj >= 5. \
#                       && CleanJet_pt[1]<=50.\
#                       && bVeto \
#                       && PuppiMET_pt>70. \
#                      '

#cuts['WJetsPUCRphi']  = 'detajj >= 5. \
#                       && CleanJet_pt[1]<=50.\
#                       && bVeto \
#                       && PuppiMET_pt>70. \
#                       && Dphilep1met>0.5'

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


