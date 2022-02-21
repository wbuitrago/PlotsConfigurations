# cuts
# Looking only at FatJet category with two jets of 30 JeV
# Removing events with the two highest pt jets are between [2.5,3.2] eta

supercut = '(nLepton==1 && Lepton_pt[0]>30 ) \
            && (  Lepton_isTightElectron_mvaFall17V2Iso_WP90[0] > 0.5 \
                    || Lepton_isTightMuon_cut_Tight_HWWW[0] > 0.5) \
            && multiJet \
            && mjj>200 && abs(CleanJet_eta[0])<4.7 && abs(CleanJet_eta[1])<4.7 \
            && CleanJet_pt[0]>50 && CleanJet_pt[1]>30 \
           '
# Vbs jets are the jets extracted by MaxMjj association from the CleanJet after FatJet cleaning

cuts["fatjet_ele"] = 'abs(Lepton_pdgId[0])==11 \
                        && Lepton_pt[0] >= 40 \
                        '

cuts["fatjet_mu"] = 'abs(Lepton_pdgId[0])==13  \
                        && Lepton_pt[0] >= 30 \
                        '

cuts["fatjet_ele_looseVBS"] = 'abs(Lepton_pdgId[0])==11 \
                        && Lepton_pt[0] >= 40 \
                        && mjj_vbs >=300    \
                        && deltaeta_vbs >= 2  \
                        '

cuts["fatjet_mu_looseVBS"] = 'abs(Lepton_pdgId[0])==13 \
                        && Lepton_pt[0] >= 30 \
                        && mjj_vbs >=300    \
                        && deltaeta_vbs >= 2  \
                        '