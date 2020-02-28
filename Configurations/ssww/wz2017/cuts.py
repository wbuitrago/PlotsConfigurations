# cuts
# cuts = {}
#Different supercut used

#supercut for test on succesive selections

supercut='nLepton>2'

cuts['wz_inc_total'] ='wzinc && bVeto'
cuts['wz_inc_softmuonveto'] ='wzinc && bVeto && softmuon_veto'

cuts['wz_vbs_total'] ='wzinc && bVeto && twoJetOrMore && mjj>500 && jet_cuts && jeteta_exclude2'
cuts['wz_vbs_softmuonveto'] ='wzinc && bVeto && twoJetOrMore && mjj>500 && jet_cuts && softmuon_veto && jeteta_exclude2'
cuts['wz_vbs_eee'] ='wzinc && bVeto && twoJetOrMore && mjj>500 && jet_cuts && EEE && jeteta_exclude2'
cuts['wz_vbs_mee'] ='wzinc && bVeto && twoJetOrMore && mjj>500 && jet_cuts && MEE && jeteta_exclude2'
cuts['wz_vbs_mme'] ='wzinc && bVeto && twoJetOrMore && mjj>500 && jet_cuts && MME && jeteta_exclude2'
cuts['wz_vbs_mmm'] ='wzinc && bVeto && twoJetOrMore && mjj>500 && jet_cuts && MMM && jeteta_exclude2'

cuts['ZZ_inc_total'] ='zz && bVeto && jeteta_exclude2'
cuts['ZZ_inc_softmuonveto'] ='zz && bVeto && softmuon_veto && jeteta_exclude2'
cuts['ZZ_inc_eee'] ='zz && bVeto && EEE && jeteta_exclude2'
cuts['ZZ_inc_mee'] ='zz && bVeto && MEE && jeteta_exclude2'
cuts['ZZ_inc_mme'] ='zz && bVeto && MME && jeteta_exclude2'
cuts['ZZ_inc_mmm'] ='zz && bVeto && MMM && jeteta_exclude2'

cuts['ZZ_vbs_total'] ='zz && bVeto && twoJetOrMore && mjj>500 && jet_cuts && jeteta_exclude2'
cuts['ZZ_vbs_softmuonveto'] ='zz && bVeto && twoJetOrMore && mjj>500 && jet_cuts && softmuon_veto && jeteta_exclude2'
