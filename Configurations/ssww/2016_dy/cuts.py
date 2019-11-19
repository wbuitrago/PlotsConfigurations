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
cuts['dy_vbs'] = {
    'expr': 'dy_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'nLepton>1 && (Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) == -13*13 || Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) == -11*11) && nCleanJet >1 && Alt$(Lepton_pt[2],0.)<10 && MET_pt>30 && mll > 20 && abs(Alt$(CleanJet_eta[0],-9999.)) < 4.7&& abs(Alt$(CleanJet_eta[1],-9999.)) < 4.7 && tauVeto_ww && zveto_ww && lep0eta && lep1eta && mll<120 && zlep_ww && bVeto && jetpt30 && mjj > 500 && abs(detajj)>2.5 && softmuon_veto',
    }
}
cuts['dy'] = {
    'expr': 'dy_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'mll<120 && (Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) == -13*13 || Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) == -11*11)',
    }
}
cuts['dy_em'] = {
    'expr': 'dy_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'mll<120 && (Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) == -13*11)',
    }
}
cuts['dy_twoJetOrMore'] = {
    'expr': 'dy_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'mll<120 && (Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) == -13*13 || Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) == -11*11) && twoJetOrMore',
    }
}
cuts['dy_oneJet'] = {
    'expr': 'dy_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'mll<120 && (Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) == -13*13 || Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) == -11*11) && oneJet',
    }
}
cuts['dy_zeroJet'] = {
    'expr': 'dy_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'mll<120 && (Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) == -13*13 || Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) == -11*11) && zeroJet',
    }
}
cuts['dy_ee'] = {
    'expr': 'dy_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : '(Lepton_pdgId[0] * Lepton_pdgId[1] == -11*11) && Lepton_pt[0]>25 && Lepton_pt[1]>13 && mll>60 && mll<120',
    }
}
cuts['dy_ee_twoJetOrMore'] = {
    'expr': 'dy_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : '(Lepton_pdgId[0] * Lepton_pdgId[1] == -11*11) && Lepton_pt[0]>25 && Lepton_pt[1]>13 && mll>60 && mll<120 && twoJetOrMore',
    }
}
cuts['dy_ee_oneJet'] = {
    'expr': 'dy_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : '(Lepton_pdgId[0] * Lepton_pdgId[1] == -11*11) && Lepton_pt[0]>25 && Lepton_pt[1]>13 && mll>60 && mll<120 && oneJet',
    }
}
cuts['dy_ee_zeroJet'] = {
    'expr': 'dy_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : '(Lepton_pdgId[0] * Lepton_pdgId[1] == -11*11) && Lepton_pt[0]>25 && Lepton_pt[1]>13 && mll>60 && mll<120 && zeroJet',
    }
}
cuts['dy_mm'] = {
    'expr': 'dy_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : '(Lepton_pdgId[0] * Lepton_pdgId[1] == -13*13) && mll>60 && mll<120',
    }
}
cuts['dy_mm_twoJetOrMore'] = {
    'expr': 'dy_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : '(Lepton_pdgId[0] * Lepton_pdgId[1] == -13*13) && mll>60 && mll<120 && twoJetOrMore',
    }
}
cuts['dy_mm_oneJet'] = {
    'expr': 'dy_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : '(Lepton_pdgId[0] * Lepton_pdgId[1] == -13*13) && mll>60 && mll<120 && oneJet',
    }
}
cuts['dy_mm_zeroJet'] = {
    'expr': 'dy_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : '(Lepton_pdgId[0] * Lepton_pdgId[1] == -13*13) && mll>60 && mll<120 && zeroJet',
    }
}
