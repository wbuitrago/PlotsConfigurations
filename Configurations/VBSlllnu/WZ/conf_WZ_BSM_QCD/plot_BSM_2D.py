# plot configuration

# groupPlot = {}
#
# Groups of samples to improve the plots (merge different sample during plot).
# If not defined, normal plots is used
#

op=['cHq1','cqq3']; 
k1=0.1; k2=0.8; 
op.sort()

# clin1 = ROOT.TColor.GetFreeColorIndex()
# col1 = ROOT.TColor(clin1, 0.443137255, 0.968627451, 0.623529412) # medium spring green
# cquad1 = ROOT.TColor.GetFreeColorIndex()
# col2 = ROOT.TColor(cquad1, 0.88627451, 0.42745098, 0.360784314) # terra cotta
# clin2 = ROOT.TColor.GetFreeColorIndex()
# col3 = ROOT.TColor(clin2, 0.933333333, 0.57254902, 0.760784314) # kobi
# cquad2 = ROOT.TColor.GetFreeColorIndex()
# col4 = ROOT.TColor(cquad2, 0.133333333, 0.682352941, 0.819607843) # pacific blue

clin1 = ROOT.TColor.GetFreeColorIndex()
col1 = ROOT.TColor(clin1, 0.243137255, 0.57254902, 0.8) # green blue crayola
cquad1 = ROOT.TColor.GetFreeColorIndex()
col2 = ROOT.TColor(cquad1, 0.88627451, 0.42745098, 0.360784314) # terra cotta
clin2 = ROOT.TColor.GetFreeColorIndex()
col3 = ROOT.TColor(clin2, 0.933333333, 0.57254902, 0.760784314) # kobi
cquad2 = ROOT.TColor.GetFreeColorIndex()
col4 = ROOT.TColor(cquad2, 0.0, 0.658823529, 0.470588235) # green munseil

# ceft1 = ROOT.TColor.GetFreeColorIndex()
# col5 = ROOT.TColor(ceft1, 0.070588235, 0.207843137, 0.356862745) # prussian blue

ceft1 = ROOT.TColor.GetFreeColorIndex()
col5 = ROOT.TColor(ceft1, 0.092, 0.262745098, 0.450980392) # indigo dye
ceft2 = ROOT.TColor.GetFreeColorIndex()
col6 = ROOT.TColor(ceft2, 0.639215686, 0.043137255, 0.215686275) # vivid burgundy
ceft3 = ROOT.TColor.GetFreeColorIndex()
col7 = ROOT.TColor(ceft3, 0.945098039, 0.560784314, 0.003921569) # carrot orange
ceft4 = ROOT.TColor.GetFreeColorIndex()
col8 = ROOT.TColor(ceft4, 0.596078431, 0.807843137, 0.0) # yellow green

csm = ROOT.TColor.GetFreeColorIndex()
col9 = ROOT.TColor(csm, 0.63921568627, 0.4862745098, 0.25098039215)
cbkg = ROOT.kGray+1

#Signal
plot['EW_sm']                        = dict(color=1, isSignal=1, isData=0, scale=1.0)
plot['QCD_sm']                       = dict(color=1, isSignal=1, isData=0, scale=1.0)
plot['sm_lin_quad_{}'.format(op[0])] = dict(color=1, isSignal=1, isData=0, scale=1.0)
plot['quad_{}'.format(op[0])]        = dict(color=1, isSignal=1, isData=0, scale=1.0)
plot['sm_lin_quad_{}'.format(op[1])] = dict(color=1, isSignal=1, isData=0, scale=1.0)
plot['quad_{}'.format(op[1])]        = dict(color=1, isSignal=1, isData=0, scale=1.0)
plot['sm_lin_quad_mixed_{}_{}'.format(op[0],op[1])] = dict(color=1, isSignal=1, isData=0, scale=1.0)

#Reducible Background
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
    'samples' : ['VVV','ZZ4L','TTV','tZq','Vg', 'VgS1_H', 'VgS1_L','Fake']
}

groupPlot['SM'] = {
    'nameHR' : 'SM', 
    'isSignal' : 0, 
    'color' : csm, 
    'samples' : ['EW_sm','QCD_sm']
}

# groupPlot['Sm_Lin_Quad_op1'] = {
#     'nameHR' : 'SM+Lin+Quad {}'.format(op[0]),
#     'isSignal' : 2,
#     'color' : clin1,
#     'samples' : ['sm_lin_quad_{}'.format(op[0])],
# }

# groupPlot['Quad_op1'] = {
#     'nameHR' : 'Quad {}'.format(op[0]),
#     'isSignal' : 2,
#     'color' : cquad1,
#     'samples' : ['quad_{}'.format(op[0])],
# }

# groupPlot['Sm_Lin_Quad_op2'] = {
#     'nameHR' : 'SM+Lin+Quad {}'.format(op[1]),
#     'isSignal' : 2,
#     'color' : clin2,
#     'samples' : ['sm_lin_quad_{}'.format(op[1])],
# }

# groupPlot['Quad_op2'] = {
#     'nameHR' : 'Quad {}'.format(op[1]),
#     'isSignal' : 2,
#     'color' : cquad2,
#     'samples' : ['quad_{}'.format(op[1])],
# }

j=k1; l=k1; 
groupPlot['{}_{}_1'.format(op[0],op[1])] = {
    'nameHR' : '{}={} {}={}'.format(op[0],j,op[1],l),
    'isSignal' : 2,
    'color' : ceft1,
    'samples' : ['EW_sm','QCD_sm','sm_lin_quad_{}'.format(op[0]),'quad_{}'.format(op[0]),'sm_lin_quad_{}'.format(op[1]),'quad_{}'.format(op[1]),'sm_lin_quad_mixed_{}_{}'.format(op[0],op[1]),'WZ_QCD','VVV','ZZ4L','TTV','tZq','Vg', 'VgS1_H', 'VgS1_L','Fake'],
    'scale' : { 
                'EW_sm' : 1-j,
                'QCD_sm' : 1-j,
                'sm_lin_quad_{}'.format(op[0]) : j, 
                'quad_{}'.format(op[0]) : j*(j-1),
                'sm_lin_quad_{}'.format(op[1]) : l, 
                'quad_{}'.format(op[1]) : l*(l-1),
                'sm_lin_quad_mixed_{}_{}'.format(op[0],op[1]) : 2*j*l,
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

j=k1; l=k2; 
groupPlot['{}_{}_2'.format(op[0],op[1])] = {
    'nameHR' : '{}={} {}={}'.format(op[0],j,op[1],l),
    'isSignal' : 2,
    'color' : ceft2,
    'samples' : ['EW_sm','QCD_sm','sm_lin_quad_{}'.format(op[0]),'quad_{}'.format(op[0]),'sm_lin_quad_{}'.format(op[1]),'quad_{}'.format(op[1]),'sm_lin_quad_mixed_{}_{}'.format(op[0],op[1]),'WZ_QCD','VVV','ZZ4L','TTV','tZq','Vg', 'VgS1_H', 'VgS1_L','Fake'],
    'scale' : { 
                'EW_sm' : 1-j,
                'QCD_sm' : 1-j,
                'sm_lin_quad_{}'.format(op[0]) : j, 
                'quad_{}'.format(op[0]) : j*(j-1),
                'sm_lin_quad_{}'.format(op[1]) : l, 
                'quad_{}'.format(op[1]) : l*(l-1),
                'sm_lin_quad_mixed_{}_{}'.format(op[0],op[1]) : 2*j*l,
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

j=k2; l=k1; 
groupPlot['{}_{}_3'.format(op[0],op[1])] = {
    'nameHR' : '{}={} {}={}'.format(op[0],j,op[1],l),
    'isSignal' : 2,
    'color' : ceft3,
    'samples' : ['EW_sm','QCD_sm','sm_lin_quad_{}'.format(op[0]),'quad_{}'.format(op[0]),'sm_lin_quad_{}'.format(op[1]),'quad_{}'.format(op[1]),'sm_lin_quad_mixed_{}_{}'.format(op[0],op[1]),'WZ_QCD','VVV','ZZ4L','TTV','tZq','Vg', 'VgS1_H', 'VgS1_L','Fake'],
    'scale' : { 
                'EW_sm' : 1-j,
                'QCD_sm' : 1-j,
                'sm_lin_quad_{}'.format(op[0]) : j, 
                'quad_{}'.format(op[0]) : j*(j-1),
                'sm_lin_quad_{}'.format(op[1]) : l, 
                'quad_{}'.format(op[1]) : l*(l-1),
                'sm_lin_quad_mixed_{}_{}'.format(op[0],op[1]) : 2*j*l,
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

j=k2; l=k2; 
groupPlot['{}_{}_4'.format(op[0],op[1])] = {
    'nameHR' : '{}={} {}={}'.format(op[0],j,op[1],l),
    'isSignal' : 2,
    'color' : ceft4,
    'samples' : ['EW_sm','QCD_sm','sm_lin_quad_{}'.format(op[0]),'quad_{}'.format(op[0]),'sm_lin_quad_{}'.format(op[1]),'quad_{}'.format(op[1]),'sm_lin_quad_mixed_{}_{}'.format(op[0],op[1]),'WZ_QCD','VVV','ZZ4L','TTV','tZq','Vg', 'VgS1_H', 'VgS1_L','Fake'],
    'scale' : { 
                'EW_sm' : 1-j,
                'QCD_sm' : 1-j,
                'sm_lin_quad_{}'.format(op[0]) : j, 
                'quad_{}'.format(op[0]) : j*(j-1),
                'sm_lin_quad_{}'.format(op[1]) : l, 
                'quad_{}'.format(op[1]) : l*(l-1),
                'sm_lin_quad_mixed_{}_{}'.format(op[0],op[1]) : 2*j*l,
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
