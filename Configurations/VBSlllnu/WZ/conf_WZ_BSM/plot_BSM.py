# plot configuration

# groupPlot = {}
#
# Groups of samples to improve the plots (merge different sample during plot).
# If not defined, normal plots is used
#

Red=632; Violet=880; Green=416; Orange=800; Yellow=400; Azure=840; Blue=600; 
k1=0.5; k2=1; k3=2; 
color_1=Red; color_2=Violet; color_3=Azure; color_sm=ROOT.kGray+1; color_bkg=ROOT.kGray+2; 

#Signal
plot['sm']                = dict(color=1, isSignal=1, isData=0, scale=1.0)
plot['sm_lin_quad_cqq11'] = dict(color=1, isSignal=1, isData=0, scale=1.0)
plot['quad_cqq11']        = dict(color=1, isSignal=1, isData=0, scale=1.0)

#Reducible Background
plot['WZ_QCD'] = dict(color=1, isSignal=0, isData=0, scale=1.0)
plot['ZZ4L']   = dict(color=1, isSignal=0, isData=0, scale=1.0) 
plot['ggZZ']   = dict(color=1, isSignal=0, isData=0, scale=1.0)
plot['TTV']    = dict(color=1, isSignal=0, isData=0, scale=1.0)
plot['tZq']    = dict(color=1, isSignal=0, isData=0, scale=1.0)
plot['Vg']     = dict(color=1, isSignal=0, isData=0, scale=1.0)
plot['VgS1_H'] = dict(color=1, isSignal=0, isData=0, scale=1.0)
plot['VgS1_L'] = dict(color=1, isSignal=0, isData=0, scale=1.0)
plot['VVV']    = dict(color=1, isSignal=0, isData=0, scale=1.0)
plot['Fake']   = dict(color=1, isSignal=0, isData=0, scale=1.0)

groupPlot['BKG'] = {
    'nameHR' : 'BKG',
    'isSignal' : 0, 
    'color' : color_bkg, 
    'samples' : ['WZ_QCD','VVV','ZZ4L','TTV','tZq','Vg', 'VgS1_H', 'VgS1_L','Fake']
}

groupPlot['SM'] = {
    'nameHR' : 'SM', 
    'isSignal' : 2, 
    'color' : color_sm, 
    'samples' : ['sm']
}

groupPlot['cqq11_1'] = {
    'nameHR' : 'cqq11 1= {}'.format(k1),
    'isSignal' : 2,
    'color' : color_1,
    'samples' : ['sm','sm_lin_quad_cqq11','quad_cqq11','WZ_QCD','VVV','ZZ4L','TTV','tZq','Vg', 'VgS1_H', 'VgS1_L','Fake'],
    'scale' : { 
                'sm' : 1-k1, 
                'sm_lin_quad_cqq11' : k1, 
                'quad_cqq11' : k1*(k1-1),
                'WZ_QCD' : 1,
                'VVV' : 1,
                'ZZ4L' : 1,
                'TTV' : 1,
                'tZq' : 1,
                'Vg' : 1,
                'VgS1_H' : 1, 
                'VgS1_L' : 1,
                'Fake' : 1,
              },
}

groupPlot['cqq11_2'] = {
    'nameHR' : 'cqq11 = {}'.format(k2),
    'isSignal' : 2,
    'color' : color_2,
    'samples' : ['sm','sm_lin_quad_cqq11','quad_cqq11','WZ_QCD','VVV','ZZ4L','TTV','tZq','Vg', 'VgS1_H', 'VgS1_L','Fake'],
    'scale' : { 
                'sm' : 1-k2, 
                'sm_lin_quad_cqq11' : k2, 
                'quad_cqq11' : k2*(k2-1),
                'WZ_QCD' : 1,
                'VVV' : 1,
                'ZZ4L' : 1,
                'TTV' : 1,
                'tZq' : 1,
                'Vg' : 1,
                'VgS1_H' : 1, 
                'VgS1_L' : 1,
                'Fake' : 1,
              },
}

groupPlot['cqq11_3'] = {
    'nameHR' : 'cqq11 = {}'.format(k3),
    'isSignal' : 2,
    'color' : color_3,
    'samples' : ['sm','sm_lin_quad_cqq11','quad_cqq11','WZ_QCD','VVV','ZZ4L','TTV','tZq','Vg', 'VgS1_H', 'VgS1_L','Fake'],
    'scale' : {
                'sm' : 1-k3, 
                'sm_lin_quad_cqq11' : k3, 
                'quad_cqq11' : k3*(k3-1),
                'WZ_QCD' : 1,
                'VVV' : 1,
                'ZZ4L' : 1,
                'TTV' : 1,
                'tZq' : 1,
                'Vg' : 1,
                'VgS1_H' : 1, 
                'VgS1_L' : 1,
                'Fake' : 1,
              },
}

# additional options
legend['lumi'] = 'L = 59.74/fb'
legend['sqrt'] = '#sqrt{s} = 13 TeV'
