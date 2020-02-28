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
mll > 60'

## Signal regions
cuts['dy_mm'] = {
    'expr': 'dy_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'mll<120 && Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) == -13*13',
    }
}
cuts['dy_ee'] = {
    'expr': 'dy_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'mll<120 && Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) == -11*11',
    }
}
cuts['dy_veto_l3_mm'] = {
    'expr': 'dy_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'nLepton>1 && Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) == -13*13 && Alt$(Lepton_pt[2],0.)<10',
    }
}
cuts['dy_veto_l3_ee'] = {
    'expr': 'dy_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'nLepton>1 && Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) == -11*11 && Alt$(Lepton_pt[2],0.)<10',
    }
}

cuts['dy_jetpt_mm'] = {
    'expr': 'dy_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'nLepton>1 && Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) == -13*13 && Alt$(Lepton_pt[2],0.)<10 && nCleanJet >1 && jetpt30 && abs(Alt$(CleanJet_eta[0],-9999.)) < 4.7&& abs(Alt$(CleanJet_eta[1],-9999.)) < 4.7',
    }
}
cuts['dy_jetpt_ee'] = {
    'expr': 'dy_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'nLepton>1 && Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) == -11*11 && Alt$(Lepton_pt[2],0.)<10 && nCleanJet >1 && jetpt30 && abs(Alt$(CleanJet_eta[0],-9999.)) < 4.7&& abs(Alt$(CleanJet_eta[1],-9999.)) < 4.7',
    }
}

cuts['dy_dijet_mm'] = {
    'expr': 'dy_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'nLepton>1 && Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) == -13*13 && Alt$(Lepton_pt[2],0.)<10 && nCleanJet >1 && jetpt30 && abs(Alt$(CleanJet_eta[0],-9999.)) < 4.7&& abs(Alt$(CleanJet_eta[1],-9999.)) < 4.7 && mjj > 500 && abs(detajj)>2.5',
    }
}
cuts['dy_dijet_ee'] = {
    'expr': 'dy_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'nLepton>1 && Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) == -11*11 && Alt$(Lepton_pt[2],0.)<10 && nCleanJet >1 && jetpt30 && abs(Alt$(CleanJet_eta[0],-9999.)) < 4.7&& abs(Alt$(CleanJet_eta[1],-9999.)) < 4.7 && mjj > 500 && abs(detajj)>2.5',
    }
}

cuts['dy_bVeto_mm'] = {
    'expr': 'dy_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'nLepton>1 && Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) == -13*13 && Alt$(Lepton_pt[2],0.)<10 && nCleanJet >1 && jetpt30 && abs(Alt$(CleanJet_eta[0],-9999.)) < 4.7&& abs(Alt$(CleanJet_eta[1],-9999.)) < 4.7 && mjj > 500 && abs(detajj)>2.5 && bVeto',
    }
}
cuts['dy_bVeto_ee'] = {
    'expr': 'dy_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'nLepton>1 && Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) == -11*11 && Alt$(Lepton_pt[2],0.)<10 && nCleanJet >1 && jetpt30 && abs(Alt$(CleanJet_eta[0],-9999.)) < 4.7&& abs(Alt$(CleanJet_eta[1],-9999.)) < 4.7 && mjj > 500 && abs(detajj)>2.5 && bVeto',
    }
}

cuts['dy_tauVeto_mm'] = {
    'expr': 'dy_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'nLepton>1 && Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) == -13*13 && Alt$(Lepton_pt[2],0.)<10 && nCleanJet >1 && jetpt30 && abs(Alt$(CleanJet_eta[0],-9999.)) < 4.7&& abs(Alt$(CleanJet_eta[1],-9999.)) < 4.7 && mjj > 500 && abs(detajj)>2.5 && tauVeto_ww',
    }
}
cuts['dy_tauVeto_ee'] = {
    'expr': 'dy_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'nLepton>1 && Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) == -11*11 && Alt$(Lepton_pt[2],0.)<10 && nCleanJet >1 && jetpt30 && abs(Alt$(CleanJet_eta[0],-9999.)) < 4.7&& abs(Alt$(CleanJet_eta[1],-9999.)) < 4.7 && mjj > 500 && abs(detajj)>2.5 && tauVeto_ww',
    }
}

cuts['dy_softmuonVeto_mm'] = {
    'expr': 'dy_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'nLepton>1 && Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) == -13*13 && Alt$(Lepton_pt[2],0.)<10 && nCleanJet >1 && jetpt30 && abs(Alt$(CleanJet_eta[0],-9999.)) < 4.7&& abs(Alt$(CleanJet_eta[1],-9999.)) < 4.7 && mjj > 500 && abs(detajj)>2.5 && softmuon_veto',
    }
}
cuts['dy_softmuonVeto_ee'] = {
    'expr': 'dy_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'nLepton>1 && Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) == -11*11 && Alt$(Lepton_pt[2],0.)<10 && nCleanJet >1 && jetpt30 && abs(Alt$(CleanJet_eta[0],-9999.)) < 4.7&& abs(Alt$(CleanJet_eta[1],-9999.)) < 4.7 && mjj > 500 && abs(detajj)>2.5 && softmuon_veto',
    }
}

cuts['dy_zepp_mm'] = {
    'expr': 'dy_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'nLepton>1 && Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) == -13*13 && Alt$(Lepton_pt[2],0.)<10 && nCleanJet >1 && jetpt30 && abs(Alt$(CleanJet_eta[0],-9999.)) < 4.7&& abs(Alt$(CleanJet_eta[1],-9999.)) < 4.7 && mjj > 500 && abs(detajj)>2.5 && zlep_ww',
    }
}
cuts['dy_zepp_ee'] = {
    'expr': 'dy_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'nLepton>1 && Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) == -11*11 && Alt$(Lepton_pt[2],0.)<10 && nCleanJet >1 && jetpt30 && abs(Alt$(CleanJet_eta[0],-9999.)) < 4.7&& abs(Alt$(CleanJet_eta[1],-9999.)) < 4.7 && mjj > 500 && abs(detajj)>2.5 && zlep_ww',
    }
}

cuts['dy_met_mm'] = {
    'expr': 'dy_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'nLepton>1 && Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) == -13*13 && Alt$(Lepton_pt[2],0.)<10 && nCleanJet >1 && jetpt30 && abs(Alt$(CleanJet_eta[0],-9999.)) < 4.7&& abs(Alt$(CleanJet_eta[1],-9999.)) < 4.7 && mjj > 500 && abs(detajj)>2.5 && MET_pt>30',
    }
}
cuts['dy_met_ee'] = {
    'expr': 'dy_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'nLepton>1 && Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) == -11*11 && Alt$(Lepton_pt[2],0.)<10 && nCleanJet >1 && jetpt30 && abs(Alt$(CleanJet_eta[0],-9999.)) < 4.7&& abs(Alt$(CleanJet_eta[1],-9999.)) < 4.7 && mjj > 500 && abs(detajj)>2.5 && MET_pt>30',
    }
}

cuts['dy_vbs_mm'] = {
    'expr': 'dy_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'nLepton>1 && Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) == -13*13 && nCleanJet >1 && Alt$(Lepton_pt[2],0.)<10 && MET_pt>30 && mll > 20 && abs(Alt$(CleanJet_eta[0],-9999.)) < 4.7&& abs(Alt$(CleanJet_eta[1],-9999.)) < 4.7 && tauVeto_ww && mll<120 && zlep_ww && bVeto && jetpt30 && mjj > 500 && abs(detajj)>2.5 && softmuon_veto',
    }
}
cuts['dy_vbs_ee'] = {
    'expr': 'dy_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'nLepton>1 && Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) == -11*11 && nCleanJet >1 && Alt$(Lepton_pt[2],0.)<10 && MET_pt>30 && mll > 20 && abs(Alt$(CleanJet_eta[0],-9999.)) < 4.7&& abs(Alt$(CleanJet_eta[1],-9999.)) < 4.7 && tauVeto_ww && mll<120 && zlep_ww && bVeto && jetpt30 && mjj > 500 && abs(detajj)>2.5 && softmuon_veto',
    }
}