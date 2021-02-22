# plot configuration

# groupPlot = {}
#
# Groups of samples to improve the plots.
# If not defined, normal plots is used
#

# groupPlot = {}
#
# Groups of samples to improve the plots (merge different sample during plot).
# If not defined, normal plots is used
#
Red=632; Violet=880; Green=416; Orange=800; Yellow=400; Azure=840; Blue=600; 

#Signal
plot['sm']                = dict(nameHR="SM", color=Azure,  isSignal=1, isData=0, scale=1.0, samples=['sm'])
#plot['sm_lin_quad_cqq11'] = dict(nameHR="cqq11", color=Azure,  isSignal=1, isData=0, scale=1.0)
#plot['sm_lin_quad_cqq1']  = dict(nameHR="cqq1", color=Azure,  isSignal=1, isData=0, scale=1.0)
#plot['sm_lin_quad_cqq31'] = dict(nameHR="cqq31", color=Azure,  isSignal=1, isData=0, scale=1.0)
#plot['sm_lin_quad_cqq3']  = dict(nameHR="cqq3", color=Azure,  isSignal=1, isData=0, scale=1.0)
#plot['sm_lin_quad_cW']    = dict(nameHR="cW", color=Azure,  isSignal=1, isData=0, scale=1.0)
#plot['sm_lin_quad_cHl3']  = dict(nameHR="cHl3", color=Azure,  isSignal=1, isData=0, scale=1.0)
#plot['sm_lin_quad_cHq3']  = dict(nameHR="cHq3", color=Azure,  isSignal=1, isData=0, scale=1.0)
#plot['sm_lin_quad_cll1']  = dict(nameHR="cll1", color=Azure,  isSignal=1, isData=0, scale=1.0)

#Reducible Background
plot['SSWW']      = dict(color=Azure, isSignal=0, isData=0, scale=1.0) 
plot['WpWp_QCD']  = dict(color=Azure, isSignal=0, isData=0, scale=1.0)
plot['WZ_QCD']    = dict(color=Azure, isSignal=0, isData=0, scale=1.0)
plot['ZZ4L']      = dict(color=Azure, isSignal=0, isData=0, scale=1.0) 
plot['ggZZ']      = dict(color=Azure, isSignal=0, isData=0, scale=1.0)
plot['TTV']       = dict(color=Azure, isSignal=0, isData=0, scale=1.0)
plot['tZq']       = dict(color=Azure, isSignal=0, isData=0, scale=1.0)
plot['Vg']        = dict(color=Azure, isSignal=0, isData=0, scale=1.0)
plot['VgS1_H']    = dict(color=Azure, isSignal=0, isData=0, scale=1.0)
plot['VgS1_L']    = dict(color=Azure, isSignal=0, isData=0, scale=1.0)
plot['DPS']       = dict(color=Azure, isSignal=0, isData=0, scale=1.0)
plot['VVV']       = dict(color=Azure, isSignal=0, isData=0, scale=1.0)
plot['Fake']      = dict(color=Azure, isSignal=0, isData=0, scale=1.0)
plot['DATA']      = dict(nameHR='Data', color=1, isSignal=0, isData=1, isBlind=0, scale=1.0)

groupPlot['sm']      = dict(nameHR="SM", isSignal=1, color= 1, samples=['sm'])
#groupPlot['cqq11']   = dict(nameHR="cqq11", isSignal=2, color=Red, samples=['sm_lin_quad_cqq11'])
#groupPlot['cqq1']    = dict(nameHR="cqq1", isSignal=2, color=Orange, samples=['sm_lin_quad_cqq11'])
#groupPlot['cqq31']   = dict(nameHR="cqq31", isSignal=2, color=Yellow, samples=['sm_lin_quad_cqq31'])
#groupPlot['cqq3']    = dict(nameHR="cqq3", isSignal=2, color=Green, samples=['sm_lin_quad_cqq3'])
#groupPlot['cW']      = dict(nameHR="cW", isSignal=2, color=Green+5, samples=['sm_lin_quad_cW'])
#groupPlot['cHl3']    = dict(nameHR="cHl3", isSignal=2, color=Azure, samples=['sm_lin_quad_cHl3'])
#groupPlot['cHq3']    = dict(nameHR="cHq3", isSignal=2, color=Blue, samples=['sm_lin_quad_cHq3'])
#groupPlot['cll1']    = dict(nameHR="cll1", isSignal=2, color=Violet, samples=['sm_lin_quad_cll1'])

groupPlot['WpWp']    = dict(nameHR="W^{#pm}W^{#pm}", isSignal=0, color=ROOT.kViolet-4, samples=['SSWW','WpWp_QCD'])
groupPlot['ZZ']      = dict(nameHR="ZZ", isSignal=0, color=ROOT.kMagenta-10, samples=['ZZ4L','ggZZ'])
groupPlot['WZ_QCD']  = dict(nameHR="WZ QCD", isSignal=0, color=ROOT.kRed, samples=['WZ_QCD'])
groupPlot['VVV']     = dict(nameHR='VVV', isSignal=0, color=ROOT.kSpring-9, samples=['VVV'])
groupPlot['TTV']     = dict(nameHR='TTV', isSignal=0, color=ROOT.kGray, samples=['TTV','tZq'])
groupPlot['DPS']     = dict(nameHR='DPS', isSignal=0, color=ROOT.kGray+5, samples=['DPS'])
groupPlot['Vg']      = dict(nameHR="V#gamma", isSignal=0, color=ROOT.kCyan-7, samples=['Vg', 'VgS1_H', 'VgS1_L'])

groupPlot['Fake']  = dict(nameHR='non-Prompt', isSignal=0, color=ROOT.kYellow-4, samples=['Fake'])

# additional options
legend['lumi'] = 'L = 59.74/fb'
legend['sqrt'] = '#sqrt{s} = 13 TeV'
