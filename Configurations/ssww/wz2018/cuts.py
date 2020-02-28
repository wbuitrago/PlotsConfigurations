# cuts
# cuts = {}
#Different supercut used

#supercut for test on succesive selections

supercut='nLepton>2'

cuts['wz_inc_total'] ='wzinc && bVeto'
cuts['wz_inc_softmuonveto'] ='wzinc && bVeto && softmuon_veto'

cuts['wz_vbs_total'] ='wzinc && bVeto && twoJetOrMore && mjj>500 && jet_cuts'
cuts['wz_vbs_softmuonveto'] ='wzinc && bVeto && twoJetOrMore && mjj>500 && jet_cuts && softmuon_veto'
cuts['wz_vbs_eee'] ='wzinc && bVeto && twoJetOrMore && mjj>500 && jet_cuts && EEE'
cuts['wz_vbs_mee'] ='wzinc && bVeto && twoJetOrMore && mjj>500 && jet_cuts && MEE'
cuts['wz_vbs_mme'] ='wzinc && bVeto && twoJetOrMore && mjj>500 && jet_cuts && MME'
cuts['wz_vbs_mmm'] ='wzinc && bVeto && twoJetOrMore && mjj>500 && jet_cuts && MMM'

cuts['ZZ_inc_total'] ='zz && bVeto'
cuts['ZZ_inc_softmuonveto'] ='zz && bVeto && softmuon_veto'
cuts['ZZ_inc_eee'] ='zz && bVeto && EEE'
cuts['ZZ_inc_mee'] ='zz && bVeto && MEE'
cuts['ZZ_inc_mme'] ='zz && bVeto && MME'
cuts['ZZ_inc_mmm'] ='zz && bVeto && MMM'

cuts['ZZ_vbs_total'] ='zz && bVeto && twoJetOrMore && mjj>500 && jet_cuts'
cuts['ZZ_vbs_softmuonveto'] ='zz && bVeto && twoJetOrMore && mjj>500 && jet_cuts && softmuon_veto'
#cuts['ZZ_vbs_eee'] ='zz && bVeto && twoJetOrMore && mjj>500 && jet_cuts && EEE'
#cuts['ZZ_vbs_mee'] ='zz && bVeto && twoJetOrMore && mjj>500 && jet_cuts && MEE'
#cuts['ZZ_vbs_mme'] ='zz && bVeto && twoJetOrMore && mjj>500 && jet_cuts && MME'
#cuts['ZZ_vbs_mmm'] ='zz && bVeto && twoJetOrMore && mjj>500 && jet_cuts && MMM'