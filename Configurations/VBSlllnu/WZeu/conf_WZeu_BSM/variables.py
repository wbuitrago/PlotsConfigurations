# variables

# variables = {}

# 'fold' : # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow

import math as mt
import numpy as np

variables['nJet'] = {
    'name'  : 'Sum$(CleanJet_pt>30)',
    'range' : (4,0,4),
    'xaxis' : 'njets',
    'fold'  : 3
}

variables['mlll'] = {
    'name'  : 'wz_var[0]',
    'range' : (list(np.logspace(mt.log(100,10), mt.log(700,10), 10+1)),),
    'xaxis' : 'm_{3l} [GeV]',
    'fold'  : 3
}

variables['ptlll'] = {
    'name'  : 'wz_var[1]',
    'range' : (list(np.logspace(mt.log(30,10), mt.log(500,10), 8+1)),),
    'xaxis' : 'p_{T}_{3l} [GeV]',
    'fold'  : 3
}

variables['ptl1'] = {
    'name'  : 'Alt$(Lepton_pt[0],-9999.)',
    'range' : (list(np.logspace(mt.log(30,10), mt.log(250,10), 7+1)),),
    'xaxis' : 'p_{T} 1st lep [GeV]',
    'fold'  : 3
}

variables['ptl1Z'] = {
    'name'  : 'wz_var[2]',
    'range' : (list(np.logspace(mt.log(30,10), mt.log(250,10), 7+1)),),
    'xaxis' : 'p_{T} 1st lep Z [GeV]',
    'fold'  : 3
}

variables['ptl2'] = {
    'name'  : 'Alt$(Lepton_pt[1],-9999.)',
    'range' : (list(np.logspace(mt.log(20,10), mt.log(200,10), 7+1)),),
    'xaxis' : 'p_{T} 2nd lep [GeV]',
    'fold'  : 3
}

variables['ptl2Z'] = {
    'name'  : 'wz_var[3]',
    'range' : (list(np.logspace(mt.log(20,10), mt.log(200,10), 7+1)),),
    'xaxis' : 'p_{T} 2nd lep Z [GeV]',
    'fold'  : 3
}


variables['ptl3'] = {
    'name'  : 'Alt$(Lepton_pt[2],-9999.)',
    'range' : (list(np.logspace(mt.log(10,10), mt.log(100,10), 7+1)),),
    'xaxis' : 'p_{T} 3rd lep [GeV]',
    'fold'  : 3
}

variables['ptlW'] = {
    'name'  : 'wz_var[4]',
    'range' : (list(np.logspace(mt.log(10,10), mt.log(100,10), 7+1)),),
    'xaxis' : 'p_{T} lep W [GeV]',
    'fold'  : 3
}

variables['etal1'] = {
    'name'  : 'Alt$(Lepton_eta[0],-9999.)',
    'range' : (6,-3.,3.),
    'xaxis' : 'eta lep1',
    'fold'  : 3
}

variables['etal1Z'] = {
    'name'  : 'wz_var[5]',
    'range' : (6,-3.,3.),
    'xaxis' : 'eta lep1 Z',
    'fold'  : 3
}

variables['etal2'] = {
    'name'  : 'Alt$(Lepton_eta[1],-9999.)',
    'range' : (6,-3.,3.),
    'xaxis' : 'eta lep2',
    'fold'  : 3
}

variables['etal2Z'] = {
    'name'  : 'wz_var[6]',
    'range' : (6,-3.,3.),
    'xaxis' : 'eta lep2 Z',
    'fold'  : 3
}

variables['etal3'] = {
    'name'  : 'Alt$(Lepton_eta[2],-9999.)',
    'range' : (6,-3.,3.),
    'xaxis' : 'eta lep3',
    'fold'  : 3
}

variables['etalW'] = {
    'name'  : 'wz_var[7]',
    'range' : (6,-3.,3.),
    'xaxis' : 'eta lep W',
    'fold'  : 3
}

variables['mjj'] = {
    'name'  : 'mjj',
    'range' : (list(np.logspace(mt.log(400,10), mt.log(3000,10), 7+1)),),
    'xaxis' : 'mjj [GeV]',
    'fold'  : 3
}

variables['ptj1'] = {
    'name'  : 'Alt$(CleanJet_pt[0],-9999.)',
    'range' : (list(np.logspace(mt.log(50,10), mt.log(700,10), 7+1)),),
    'xaxis' : 'p_{T} 1st jet [GeV]',
    'fold'  : 3
}

variables['ptj2'] = {
    'name'  : 'Alt$(CleanJet_pt[1],-9999.)',
    'range' : (list(np.logspace(mt.log(30,10), mt.log(400,10), 7+1)),),
    'xaxis' : 'p_{T} 2nd jet [GeV]',
    'fold'  : 3
}

variables['etaj1'] = {
    'name'  : 'Alt$(CleanJet_eta[0],-9999.)',
    'range' : (10,-4,4),
    'xaxis' : 'eta j1',
    'fold'  : 3
}

variables['etaj2'] = {
    'name'  : 'Alt$(CleanJet_eta[1],-9999.)',
    'range' : (10,-4,4),
    'xaxis' : 'eta j2',
    'fold'  : 3
}

variables['detajj'] = {
    'name'  : 'detajj',
    'range' : (10,2.5,8),
    'xaxis' : 'deta jj',
    'fold'  : 3
}

variables['dphijj'] = {
    'name'  : 'dphijj',
    'range' : (10,0.0,3.141592),
    'xaxis' : 'dphi jj',
    'fold'  : 3
}

variables['met'] = {
    'name'  : 'MET_pt',
    'range' : (list(np.logspace(mt.log(20,10), mt.log(400,10), 10+1)),),
    'xaxis' : 'met [GeV]', 
    'fold'  : 3
}

variables['Zlep1'] = {
    'name'  : 'zlep1',
    'range': (8,-1.,1.),
    'xaxis' : 'Z^{lep}_{1}',
    'fold'  : 3
}

variables['Zlep2'] = {
    'name': 'zlep2',
    'range': (8,-1.,1.),
    'xaxis': 'Z^{lep}_{2}',
    'fold': 3
}

variables['mZ'] = {
    'name'  : 'wz_var[8]',
    'range' : (10,85,100),
    'xaxis' : 'm_{ll} Z [GeV]',
    'fold'  : 3
}

variables['ptZ'] = {
    'name'  : 'wz_var[9]',
    'range' : (list(np.logspace(mt.log(30,10), mt.log(500,10), 8+1)),),
    'xaxis' : 'p_{T} Z [GeV]',
    'fold'  : 3
}

variables['mWZ'] = {
    'name'  : 'wz_var[10]',
    'range' : (list(np.logspace(mt.log(170,10), mt.log(2500,10), 10+1)),),
    'xaxis' : 'm_{WZ} [GeV]',
    'fold'  : 3
}

variables['deltaetaWZ'] = {
    'name'  : 'wz_var[11]',
    'range' : (10,0,8),
    'xaxis' : '#delta#eta_{WZ}',
    'fold'  : 3
}

variables['deltaphiWZ'] = {
    'name'  : 'wz_var[12]',
    'range' : (10,0,3.14),
    'xaxis' : '#delta#phi_{WZ}',
    'fold'  : 3
}

variables['Philanes'] = {
    'name'  : 'wz_var[13]',
    'range' : (10,0,3.14),
    'xaxis' : '#delta#Phi_{planes}',
    'fold'  : 3
}

variables['ThetaWZ'] = {
    'name'  : 'wz_var[14]',
    'range' : (10,0,3.14),
    'xaxis' : '#Theta_{WZ}',
    'fold'  : 3
}

variables['ThetalW'] = {
    'name'  : 'wz_var[15]',
    'range' : (10,0,3.14),
    'xaxis' : '#Theta_{lW}',
    'fold'  : 3
}

variables['ThetalZ'] = {
    'name'  : 'wz_var[16]',
    'range' : (10,0,3.14),
    'xaxis' : '#Theta_{lZ}',
    'fold'  : 3
}