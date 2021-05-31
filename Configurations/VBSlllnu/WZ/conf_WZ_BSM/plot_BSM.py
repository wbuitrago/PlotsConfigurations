# plot configuration

# groupPlot = {}
#
# Groups of samples to improve the plots (merge different sample during plot).
# If not defined, normal plots is used
#

Red=632; Violet=880; Green=416; Orange=800; Yellow=400; Azure=840; Blue=600; 

#Signal
plot['sm']     = dict(color=1, isSignal=1, isData=0, scale=1.0)

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

groupPlot['BKG'] = dict(nameHR='BKG', isSignal=0, color=ROOT.kGray+1, samples=['WZ_QCD','VVV','ZZ4L','TTV','tZq','Vg', 'VgS1_H', 'VgS1_L','Fake'])
groupPlot['SM']  = dict(nameHR="SM", isSignal=1, color=ROOT.kGray, samples=['sm'])

k1=0.1; k2=1; k3=10; 
cqq1_1=Red; cqq1_2=Violet; cqq1_3=Azure; 

#EFT components
plot['sm']                = dict(color=1, isSignal=1, isData=0, scale=1-k1)
plot['sm_lin_quad_cqq11'] = dict(color=1, isSignal=1, isData=0, scale=k1)
plot['quad_cqq11']        = dict(color=1, isSignal=1, isData=0, scale=k1*(k1-1))
groupPlot['cqq11_1']      = dict(nameHR='cqq1 = {}'.format(k1), isSignal=2, color=cqq1_1, samples=['sm','sm_lin_quad_cqq11','quad_cqq11'])

plot['sm']                = dict(color=1, isSignal=1, isData=0, scale=1-k2)
plot['sm_lin_quad_cqq11'] = dict(color=1, isSignal=1, isData=0, scale=k2)
plot['quad_cqq11']        = dict(color=1, isSignal=1, isData=0, scale=k2*(k2-1))
groupPlot['cqq11_2']      = dict(nameHR='cqq1 = {}'.format(k2), isSignal=2, color=cqq1_2, samples=['sm','sm_lin_quad_cqq11','quad_cqq11'])

plot['sm']                = dict(color=1, isSignal=1, isData=0, scale=1-k3)
plot['sm_lin_quad_cqq11'] = dict(color=1, isSignal=1, isData=0, scale=k3)
plot['quad_cqq11']        = dict(color=1, isSignal=1, isData=0, scale=k3*(k3-1))
groupPlot['cqq11_3']      = dict(nameHR='cqq1 = {}'.format(k3), isSignal=2, color=cqq1_3, samples=['sm','sm_lin_quad_cqq11','quad_cqq11'])

# additional options
legend['lumi'] = 'L = 59.74/fb'
legend['sqrt'] = '#sqrt{s} = 13 TeV'
