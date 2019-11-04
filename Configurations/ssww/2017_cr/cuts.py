# cuts
# cuts = {}
#Different supercut used

#supercut for test on succesive selections

# supercut='\
# nLepton>1 && nCleanJet > 1 &&\
# Alt$(Lepton_pt[0],0.)>30 && Alt$(Lepton_pt[1],0.)>30 && Alt$(Lepton_pt[2],0.)<10 && mjj >500 && detajj > 2.5\
# && abs(Alt$(CleanJet_eta[1],-9999.))<5 && abs(Alt$(CleanJet_eta[0],-9999.))<5\
# && fabs(Alt$(Lepton_eta[0],-9999.))<2.5 && fabs(Alt$(Lepton_eta[1],-9999.))<2.5 && Alt$(CleanJet_pt[0],-9999.) >30 && Alt$(CleanJet_pt[1],-9999.) >30'

supercut='\
mjj > 150'

## Signal regions
cuts['lowmjj'] = {
    'expr': 'ssww_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'jetpt30 && leppt30 && mjj < 500 && bVeto && softmuon_veto',
    }
}
cuts['lowmjj_ee'] = {
    'expr': 'ssww_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'jetpt30 && leppt30 && mjj < 500 && bVeto && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==11*11 && softmuon_veto',
    }
}
cuts['lowmjj_mm'] = {
    'expr': 'ssww_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'jetpt30 && leppt30 && mjj < 500 && bVeto && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==13*13 && softmuon_veto',
    }
}
cuts['lowmjj_me'] = {
    'expr': 'ssww_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'jetpt30 && leppt30 && mjj < 500 && bVeto && abs(Lepton_pdgId[0])==13 && abs(Lepton_pdgId[1])==11 && softmuon_veto',
    }
}
cuts['lowmjj_em'] = {
    'expr': 'ssww_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'jetpt30 && leppt30 && mjj < 500 && bVeto && abs(Lepton_pdgId[0])==11 && abs(Lepton_pdgId[1])==13 && softmuon_veto',
    }
}
cuts['top'] = {
    'expr': 'ssww_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'zlep_ww && jetpt30 && leppt30 && mjj > 500 && abs(detajj)>2.5 && (!bVeto||!softmuon_veto)',
    }
}
cuts['top_ee'] = {
    'expr': 'ssww_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'zlep_ww && jetpt30 && leppt30 && mjj > 500 && abs(detajj)>2.5 && (!bVeto||!softmuon_veto) && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==11*11',
    }
}
cuts['top_mm'] = {
    'expr': 'ssww_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'zlep_ww && jetpt30 && leppt30 && mjj > 500 && abs(detajj)>2.5 && (!bVeto||!softmuon_veto) && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==13*13',
    }
}
cuts['top_me'] = {
    'expr': 'ssww_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'zlep_ww && jetpt30 && leppt30 && mjj > 500 && abs(detajj)>2.5 && (!bVeto||!softmuon_veto)&& abs(Lepton_pdgId[0])==13 && abs(Lepton_pdgId[1])==11',
    }
}
cuts['top_em'] = {
    'expr': 'ssww_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'zlep_ww && jetpt30 && leppt30 && mjj > 500 && abs(detajj)>2.5 && (!bVeto||!softmuon_veto)&& abs(Lepton_pdgId[0])==11 && abs(Lepton_pdgId[1])==13',
    }
}
cuts['ssww'] = {
    'expr': 'ssww_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'zlep_ww && bVeto && jetpt30 && leppt30 && mjj > 500 && abs(detajj)>2.5 && softmuon_veto',
    }
}
cuts['ssww_ee'] = {
    'expr': 'ssww_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'zlep_ww && bVeto && jetpt30 && leppt30 && mjj > 500 && abs(detajj)>2.5 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==11*11 && softmuon_veto',
    }
}
cuts['ssww_mm'] = {
    'expr': 'ssww_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'zlep_ww && bVeto && jetpt30 && leppt30 && mjj > 500 && abs(detajj)>2.5 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==13*13 && softmuon_veto',
    }
}
cuts['ssww_me'] = {
    'expr': 'ssww_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'zlep_ww && bVeto && jetpt30 && leppt30 && mjj > 500 && abs(detajj)>2.5 && abs(Lepton_pdgId[0])==13 && abs(Lepton_pdgId[1])==11 && softmuon_veto',
    }
}
cuts['ssww_em'] = {
    'expr': 'ssww_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'zlep_ww && bVeto && jetpt30 && leppt30 && mjj > 500 && abs(detajj)>2.5 && abs(Lepton_pdgId[0])==11 && abs(Lepton_pdgId[1])==13 && softmuon_veto',
    }
}
'''
cuts['all'] = {
    'expr': 'wz_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'jetpt30',
        #'bveto_jetpt30_leppt1_ee' : ' bVeto && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==11*11',
        #'btag_jetpt30_leppt1_mumu' : ' bReq && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==13*13',
        #'bveto_jetpt30_leppt1_lowmjj' : ' bVeto && jetpt30 && leppt30 && mjj < 500',
        #'btag_jetpt30_leppt1_lowmjj' : ' bReq && jetpt30 && leppt30 && mjj < 500',
    }
}
cuts['eee'] = {
    'expr': 'wz_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'jetpt30 && abs(Alt$(Lepton_pdgId[0],0)*Alt$(Lepton_pdgId[1],0)*Alt$(Lepton_pdgId[2],0))==11*11*11',
        #'bveto_jetpt30_leppt1_ee' : ' bVeto && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==11*11',
        #'btag_jetpt30_leppt1_mumu' : ' bReq && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==13*13',
        #'bveto_jetpt30_leppt1_lowmjj' : ' bVeto && jetpt30 && leppt30 && mjj < 500',
        #'btag_jetpt30_leppt1_lowmjj' : ' bReq && jetpt30 && leppt30 && mjj < 500',
    }
}
cuts['mee'] = {
    'expr': 'wz_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'jetpt30 && abs(Alt$(Lepton_pdgId[0],0)*Alt$(Lepton_pdgId[1],0)*Alt$(Lepton_pdgId[2],0))==13*11*11',
        #'bveto_jetpt30_leppt1_ee' : ' bVeto && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==11*11',
        #'btag_jetpt30_leppt1_mumu' : ' bReq && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==13*13',
        #'bveto_jetpt30_leppt1_lowmjj' : ' bVeto && jetpt30 && leppt30 && mjj < 500',
        #'btag_jetpt30_leppt1_lowmjj' : ' bReq && jetpt30 && leppt30 && mjj < 500',
    }
}
cuts['mme'] = {
    'expr': 'wz_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'jetpt30 && abs(Alt$(Lepton_pdgId[0],0)*Alt$(Lepton_pdgId[1],0)*Alt$(Lepton_pdgId[2],0))==13*13*11',
        #'bveto_jetpt30_leppt1_ee' : ' bVeto && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==11*11',
        #'btag_jetpt30_leppt1_mumu' : ' bReq && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==13*13',
        #'bveto_jetpt30_leppt1_lowmjj' : ' bVeto && jetpt30 && leppt30 && mjj < 500',
        #'btag_jetpt30_leppt1_lowmjj' : ' bReq && jetpt30 && leppt30 && mjj < 500',
    }
}
cuts['mmm'] = {
    'expr': 'wz_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'jetpt30 && abs(Alt$(Lepton_pdgId[0],0)*Alt$(Lepton_pdgId[1],0)*Alt$(Lepton_pdgId[2],0))==13*13*13',
        #'bveto_jetpt30_leppt1_ee' : ' bVeto && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==11*11',
        #'btag_jetpt30_leppt1_mumu' : ' bReq && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==13*13',
        #'bveto_jetpt30_leppt1_lowmjj' : ' bVeto && jetpt30 && leppt30 && mjj < 500',
        #'btag_jetpt30_leppt1_lowmjj' : ' bReq && jetpt30 && leppt30 && mjj < 500',
    }
}
'''
'''
cuts['zz'] = {
    'expr': 'zz_region',
    # Define the sub-categorization of sr
    'categories' : {
        'jetpt50_leppt0' : 'jetpt50 && leppt0',
        'jetpt30_leppt0' : 'jetpt30 && leppt0',
        'jetpt30_leppt1' : 'jetpt30 && leppt30',
    }
}
'''
