# cuts

# Second lepton veto already done in post-processing 
#and Lepton WP setup in samples.py
supercut = '(   (abs(Lepton_pdgId[0])==11 && Lepton_pt[0]>35)\
             || (abs(Lepton_pdgId[0])==13 && Lepton_pt[0]>30 ) ) \
            && Alt$(Lepton_pt[1],0)<=10 && Alt$(Lepton_isLoose[1],1)> 0.5 \
            && vbs_0_pt_alt > 50 && vbs_1_pt_alt > 30 \
            && PuppiMET_pt > 30 \
            && deltaeta_vbs_alt >= 2.5  \
            && mjj_vbs_alt >= 500 \
            && Mtw_lep < 185 \
            '


# #########################################################################
# ###############|----------------------------------|######################
# ###############|          Resolved category       |######################
# ###############|----------------------------------|######################
# #########################################################################

cuts["res_sig_ele"] = 'VBS_category==1 \
                                && abs(Lepton_pdgId[0])==11 \
                                && vjet_0_pt_alt > 30 && vjet_1_pt_alt > 30 \
                                && mjj_vjet_alt > 65 && mjj_vjet_alt < 105 \
                                && bVeto \
                                && w_had_pt_alt < 200 \
                                '



cuts["res_sig_mu"] = 'VBS_category==1 \
                                && abs(Lepton_pdgId[0])==13 \
                                && vjet_0_pt_alt > 30 && vjet_1_pt_alt > 30 \
                                && mjj_vjet_alt > 65 && mjj_vjet_alt < 105 \
                                && bVeto \
                                && w_had_pt_alt < 200 \
                                '


##################################
# Woff shell, bveto ---> WJet region

cuts["res_wjetcr_ele"] = 'VBS_category==1 \
                                && abs(Lepton_pdgId[0])==11 \
                                && vjet_0_pt_alt > 30 && vjet_1_pt_alt > 30 \
                                && (mjj_vjet_alt <= 65 || mjj_vjet_alt >= 105) \
                                && bVeto \
                                && w_had_pt_alt < 200 \
                                '



cuts["res_wjetcr_mu"] = 'VBS_category==1 \
                                && abs(Lepton_pdgId[0])==13 \
                                && vjet_0_pt_alt > 30 && vjet_1_pt_alt > 30 \
                                && (mjj_vjet_alt <= 65 || mjj_vjet_alt >= 105) \
                                && bVeto \
                                && w_had_pt_alt < 200 \
                                '


# #########################################################################
# ###############|----------------------------------|######################
# ###############|          Boosted category       |######################
# ###############|----------------------------------|######################
# #########################################################################


cuts["boost_sig_ele"] = 'VBS_category==0 \
                            && abs(Lepton_pdgId[0])==11 \
                            && vjet_0_pt_alt > 200 \
                            && mjj_vjet_alt > 70 && mjj_vjet_alt < 120 \
                            && bVeto \
                            '


cuts["boost_sig_mu"] = 'VBS_category==0 \
                            && abs(Lepton_pdgId[0])==13 \
                            && vjet_0_pt_alt > 200 \
                            && mjj_vjet_alt > 70 && mjj_vjet_alt < 120 \
                            && bVeto \
                            '


# ###############################################
# # Wjets

cuts["boost_wjetcr_ele"] = 'VBS_category==0 \
                            && abs(Lepton_pdgId[0])==11 \
                            && vjet_0_pt_alt > 200 \
                            && (mjj_vjet_alt <= 70 || mjj_vjet_alt >= 120)  \
                            && bVeto \
                            '

cuts["boost_wjetcr_mu"] = 'VBS_category==0 \
                            && abs(Lepton_pdgId[0])==13 \
                            && vjet_0_pt_alt > 200 \
                            && (mjj_vjet_alt <= 70 || mjj_vjet_alt >= 120)  \
                            && bVeto \
                            '


# ###############################################
# #Top


### Top Tight region

cuts["res_topcr_ele"] = 'VBS_category==1 \
                                && abs(Lepton_pdgId[0])==11 \
                                && vjet_0_pt_alt > 30 && vjet_1_pt_alt > 30 \
                                && mjj_vjet_alt > 65 && mjj_vjet_alt < 105 \
                                && bReqTight \
                                && w_had_pt_alt < 200 \
                                '

cuts["res_topcr_mu"] = 'VBS_category==1 \
                                && abs(Lepton_pdgId[0])==13 \
                                && vjet_0_pt_alt > 30 && vjet_1_pt_alt > 30 \
                                && mjj_vjet_alt > 65 && mjj_vjet_alt < 105 \
                                && bReqTight \
                                && w_had_pt_alt < 200 \
                                '


# Tight top
cuts["boost_topcr_ele"] = 'VBS_category==0 \
                            && abs(Lepton_pdgId[0])==11 \
                            && vjet_0_pt_alt > 200 \
                            && mjj_vjet_alt > 70 && mjj_vjet_alt < 120 \
                            && bReqTight \
                            '


cuts["boost_topcr_mu"] = 'VBS_category==0 \
                            && abs(Lepton_pdgId[0])==13 \
                            && vjet_0_pt_alt > 200 \
                            && mjj_vjet_alt > 70 && mjj_vjet_alt < 120 \
                            && bReqTight \
                            '

