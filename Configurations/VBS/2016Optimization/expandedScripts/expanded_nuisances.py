# 
# Expanded version of samples.py 
# 
nuisances['lumi2016'] = { 
     'name'  :   'lumi_13TeV_2016' ,
     'type'  :   'lnN' ,
     'samples'  :  { 
            'DPS',
            'ZZ',
            'ChMisId',
            'Vg',
            'VVV',
            'ttbar',
            'WpWp_EWK',
            'WmWm_EWK',
            'WW_strong',
     },  
}  
   
 nuisances['QCDscale'] = { 
     'name'  :   'QCDscale' ,
     'type'  :   'lnN' ,
     'samples'  :  { 
            'DPS',
            'ZZ',
            'ChMisId',
            'Vg',
            'VVV',
            'ttbar',
            'WpWp_EWK',
            'WZ',
            'WmWm_EWK',
            'WW_strong',
     },  
}  
   
 nuisances['QCDscale_gg_accept'] = { 
     'name'  :   'QCDscale_gg_accept' ,
     'type'  :   'lnN' ,
     'samples'  :  { 
            'WpWp_EWK',
            'DY',
     },  
}  
   
 nuisances['QCDscale_qqbar_accept'] = { 
     'name'  :   'QCDscale_qqbar_accept' ,
     'type'  :   'lnN' ,
     'samples'  :  { 
            'lep_TT',
            'Vg',
     },  
}  
   
 nuisances['pdf'] = { 
     'name'  :   'pdf' ,
     'type'  :   'lnN' ,
     'samples'  :  { 
            'DPS',
            'ZZ',
            'ChMisId',
            'Vg',
            'VVV',
            'ttbar',
            'WpWp_EWK',
            'WZ',
            'WmWm_EWK',
            'WW_strong',
     },  
}  
   
 nuisances['WZ_norm'] = { 
     'name'  :   'WZ_norm' ,
     'type'  :   'lnN' ,
     'samples'  :  { 
            'WZ',
     },  
}  
   
 nuisances['charge_flip'] = { 
     'name'  :   'charge_flip' ,
     'type'  :   'lnN' ,
     'samples'  :  { 
            'ttbar',
            'ChMisId',
     },  
}  
   
 nuisances['fake_syst'] = { 
     'name'  :   'fake_syst' ,
     'type'  :   'lnN' ,
     'samples'  :  { 
            'Fake_lep',
     },  
}  
   
 nuisances['btagbc'] = { 
     'name'  :   'ICHEP_btag_bc' ,
     'kind'  :   'weight' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'DPS',
            'ZZ',
            'ChMisId',
            'Vg',
            'VVV',
            'ttbar',
            'WpWp_EWK',
            'WZ',
            'WmWm_EWK',
            'WW_strong',
     },  
}  
   
 nuisances['btagudsg'] = { 
     'name'  :   'ICHEP_btag_udsg' ,
     'kind'  :   'weight' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'DPS',
            'ZZ',
            'ChMisId',
            'Vg',
            'VVV',
            'ttbar',
            'WpWp_EWK',
            'WZ',
            'WmWm_EWK',
            'WW_strong',
     },  
}  
   
 nuisances['trigg'] = { 
     'name'  :   'trigger' ,
     'kind'  :   'weight' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'DPS',
            'ZZ',
            'ChMisId',
            'Vg',
            'VVV',
            'ttbar',
            'WpWp_EWK',
            'WZ',
            'WmWm_EWK',
            'WW_strong',
     },  
}  
   
 nuisances['idiso_ele'] = { 
     'name'  :   'idiso_ele' ,
     'kind'  :   'weight' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'DPS',
            'ZZ',
            'ChMisId',
            'Vg',
            'VVV',
            'ttbar',
            'WpWp_EWK',
            'WZ',
            'WmWm_EWK',
            'WW_strong',
     },  
}  
   
 nuisances['idiso_mu'] = { 
     'name'  :   'idiso_mu' ,
     'kind'  :   'weight' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'DPS',
            'ZZ',
            'ChMisId',
            'Vg',
            'VVV',
            'ttbar',
            'WpWp_EWK',
            'WZ',
            'WmWm_EWK',
            'WW_strong',
     },  
}  
   
 nuisances['jes'] = { 
     'name'  :   'scale_j' ,
     'kind'  :   'tree' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'DPS',
            'ZZ',
            'ChMisId',
            'Vg',
            'VVV',
            'ttbar',
            'WpWp_EWK',
            'WZ',
            'WmWm_EWK',
            'WW_strong',
     },  
     'folderUp'    :   '/gwteras/cms/store/group/OneLepton/Apr2017_summer16/lep2SelVBS__MCWeights__hadd__bSFL2pTEffCut__genMatchVariables__l2tightVBS__JESup__tightVbsSel/' ,
     'folderDown'  :   '/gwteras/cms/store/group/OneLepton/Apr2017_summer16/lep2SelVBS__MCWeights__hadd__bSFL2pTEffCut__genMatchVariables__l2tightVBS__JESdo__tightVbsSel/' ,
}  
   
 nuisances['electronpt'] = { 
     'name'  :   'scale_e' ,
     'kind'  :   'tree' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'DPS',
            'ZZ',
            'ChMisId',
            'Vg',
            'VVV',
            'ttbar',
            'WpWp_EWK',
            'WZ',
            'WmWm_EWK',
            'WW_strong',
     },  
     'folderUp'    :   '/gwteras/cms/store/group/OneLepton/Apr2017_summer16/lep2SelVBS__MCWeights__hadd__bSFL2pTEffCut__genMatchVariables__l2tightVBS__LepElepTCutup__tightVbsSel/' ,
     'folderDown'  :   '/gwteras/cms/store/group/OneLepton/Apr2017_summer16/lep2SelVBS__MCWeights__hadd__bSFL2pTEffCut__genMatchVariables__l2tightVBS__LepElepTCutdo__tightVbsSel/' ,
}  
   
 nuisances['muonpt'] = { 
     'name'  :   'scale_m' ,
     'kind'  :   'tree' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'DPS',
            'ZZ',
            'ChMisId',
            'Vg',
            'VVV',
            'ttbar',
            'WpWp_EWK',
            'WZ',
            'WmWm_EWK',
            'WW_strong',
     },  
     'folderUp'    :   '/gwteras/cms/store/group/OneLepton/Apr2017_summer16/lep2SelVBS__MCWeights__hadd__bSFL2pTEffCut__genMatchVariables__l2tightVBS__LepMupTCutup__tightVbsSel/' ,
     'folderDown'  :   '/gwteras/cms/store/group/OneLepton/Apr2017_summer16/lep2SelVBS__MCWeights__hadd__bSFL2pTEffCut__genMatchVariables__l2tightVBS__LepMupTCutdo__tightVbsSel/' ,
}  
   
 nuisances['met'] = { 
     'name'  :   'scale_met' ,
     'kind'  :   'tree' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'DPS',
            'ZZ',
            'ChMisId',
            'Vg',
            'VVV',
            'ttbar',
            'WpWp_EWK',
            'WZ',
            'WmWm_EWK',
            'WW_strong',
     },  
     'folderUp'    :   '/gwteras/cms/store/group/OneLepton/Apr2017_summer16/lep2SelVBS__MCWeights__hadd__bSFL2pTEffCut__genMatchVariables__l2tightVBS__METup__tightVbsSel/' ,
     'folderDown'  :   '/gwteras/cms/store/group/OneLepton/Apr2017_summer16/lep2SelVBS__MCWeights__hadd__bSFL2pTEffCut__genMatchVariables__l2tightVBS__METdo__tightVbsSel/' ,
}  
   
 nuisances['stat'] = { 
     'type'  :   'auto' ,
     'samples'  :  { 
     },  
}  
   
 