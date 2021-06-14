# plot configuration

# groupPlot = {}
#
# Groups of samples to improve the plots (merge different sample during plot).
# If not defined, normal plots is used
#

op='cHW'; 
k1=0.5; k2=1; k3=2; 

clin = ROOT.TColor.GetFreeColorIndex()
col1 = ROOT.TColor(clin, 0.44213725, 0.05882353, 0.4745098)
cquad = ROOT.TColor.GetFreeColorIndex()
col2 = ROOT.TColor(cquad, 0.0, 0.42745098, 0.23921569)
ceft1 = ROOT.TColor.GetFreeColorIndex()
col3 = ROOT.TColor(ceft1, 0.85490196078, 0.2431372549, 0.32156862745)
ceft2 = ROOT.TColor.GetFreeColorIndex()
col4 = ROOT.TColor(ceft2, 0.98431372549, 0.54509803921, 0.14117647058)
ceft3 = ROOT.TColor.GetFreeColorIndex()
col5 = ROOT.TColor(ceft3, 0.39215686274, 0.55294117647, 0.89803921568)
csm = ROOT.TColor.GetFreeColorIndex()
col6 = ROOT.TColor(csm, 0.63921568627, 0.4862745098, 0.25098039215)
cbkg = ROOT.kGray+1

#Signal
plot['sm']                        = dict(color=1, isSignal=1, isData=0, scale=1.0)
plot['sm_lin_quad_{}'.format(op)] = dict(color=1, isSignal=1, isData=0, scale=1.0)
plot['quad_{}'.format(op)]        = dict(color=1, isSignal=1, isData=0, scale=1.0)

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
    'color' : cbkg, 
    'samples' : ['WZ_QCD','VVV','ZZ4L','TTV','tZq','Vg', 'VgS1_H', 'VgS1_L','Fake']
}

groupPlot['SM'] = {
    'nameHR' : 'SM', 
    'isSignal' : 0, 
    'color' : csm, 
    'samples' : ['sm']
}

groupPlot['Sm_Lin_Quad'] = {
    'nameHR' : 'SM+Lin+Quad',
    'isSignal' : 2,
    'color' : clin,
    'samples' : ['sm_lin_quad_{}'.format(op)],
}

groupPlot['Quad'] = {
    'nameHR' : 'Quad',
    'isSignal' : 2,
    'color' : cquad,
    'samples' : ['quad_{}'.format(op)],
}

groupPlot['{}_1'.format(op)] = {
    'nameHR' : '{} = {}'.format(op,k1),
    'isSignal' : 2,
    'color' : ceft1,
    'samples' : ['sm','sm_lin_quad_{}'.format(op),'quad_{}'.format(op),'WZ_QCD','VVV','ZZ4L','TTV','tZq','Vg', 'VgS1_H', 'VgS1_L','Fake'],
    'scale' : { 
                'sm' : 1-k1, 
                'sm_lin_quad_{}'.format(op) : k1, 
                'quad_{}'.format(op) : k1*(k1-1),
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

groupPlot['{}_2'.format(op)] = {
    'nameHR' : '{} = {}'.format(op,k2),
    'isSignal' : 2,
    'color' : ceft2,
    'samples' : ['sm','sm_lin_quad_{}'.format(op),'quad_{}'.format(op),'WZ_QCD','VVV','ZZ4L','TTV','tZq','Vg', 'VgS1_H', 'VgS1_L','Fake'],
    'scale' : { 
                'sm' : 1-k2, 
                'sm_lin_quad_{}'.format(op) : k2, 
                'quad_{}'.format(op) : k2*(k2-1),
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

groupPlot['{}_3'.format(op)] = {
    'nameHR' : '{} = {}'.format(op,k3),
    'isSignal' : 2,
    'color' : ceft3,
    'samples' : ['sm','sm_lin_quad_{}'.format(op),'quad_{}'.format(op),'WZ_QCD','VVV','ZZ4L','TTV','tZq','Vg', 'VgS1_H', 'VgS1_L','Fake'],
    'scale' : {
                'sm' : 1-k3, 
                'sm_lin_quad_{}'.format(op) : k3, 
                'quad_{}'.format(op) : k3*(k3-1),
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
