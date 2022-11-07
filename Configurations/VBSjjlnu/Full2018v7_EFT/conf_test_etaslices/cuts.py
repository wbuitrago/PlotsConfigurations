# cuts

# Second lepton veto already done in post-processing 
#and Lepton WP setup in samples.py
supercut = '(   (abs(Lepton_pdgId[0])==11 && Lepton_pt[0]>35)\
             || (abs(Lepton_pdgId[0])==13 && Lepton_pt[0]>30 ) ) \
            && Alt$(Lepton_pt[1],0)<=10 && Alt$(Lepton_isLoose[1],1)> 0.5 \
            && vbs_0_pt > 50 && vbs_1_pt > 30 \
            && PuppiMET_pt > 30 \
            && deltaeta_vbs >= 2.5  \
            && mjj_vbs >= 500 \
            && Mtw_lep < 185 \
            '


# #########################################################################
# ###############|----------------------------------|######################
# ###############|          Resolved category       |######################
# ###############|----------------------------------|######################
# #########################################################################


##################################
# Woff shell, bveto ---> WJet region

cuts["res_wjetcr_ele"] = 'VBS_category==1 \
                                && abs(Lepton_pdgId[0])==11 \
                                && vjet_0_pt > 30 && vjet_1_pt > 30 \
                                && (mjj_vjet <= 65 || mjj_vjet >= 105) \
                                && bVeto \
                                && w_had_pt < 200 \
                                '



cuts["res_wjetcr_mu"] = 'VBS_category==1 \
                                && abs(Lepton_pdgId[0])==13 \
                                && vjet_0_pt > 30 && vjet_1_pt > 30 \
                                && (mjj_vjet <= 65 || mjj_vjet >= 105) \
                                && bVeto \
                                && w_had_pt < 200 \
                                '



### Top Tight region

cuts["res_topcr_ele"] = 'VBS_category==1 \
                                && abs(Lepton_pdgId[0])==11 \
                                && vjet_0_pt > 30 && vjet_1_pt > 30 \
                                && mjj_vjet > 65 && mjj_vjet < 105 \
                                && bReqTight \
                                && w_had_pt < 200 \
                                '

cuts["res_topcr_mu"] = 'VBS_category==1 \
                                && abs(Lepton_pdgId[0])==13 \
                                && vjet_0_pt > 30 && vjet_1_pt > 30 \
                                && mjj_vjet > 65 && mjj_vjet < 105 \
                                && bReqTight \
                                && w_had_pt < 200 \
                                '


eta_regions = [0, 1, 1.5, 2,2.5,3, 3.5, 4,5]

for i in range(len(eta_regions)-1):
    for cut in ["res_wjetcr_ele", "res_wjetcr_mu","res_topcr_ele", "res_topcr_mu"]:
        cuts["{}_eta{}-{}".format(cut, eta_regions[i], eta_regions[i+1])] = \
            "(" + cuts[cut] + ") * (abs(vbs_0_eta)> {})*(abs(vbs_0_eta) <= {}) ".format(eta_regions[i], eta_regions[i+1])

