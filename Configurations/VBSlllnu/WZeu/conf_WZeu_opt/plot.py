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
plot['sm']                = dict(color=Azure, isSignal=1, isData=0, scale=1.0)

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

#BSM
plot['sm_lin_quad_cqq11'] = dict(nameHR="cqq11", color=Azure,  isSignal=1, isData=0, scale=1.0)
plot['sm_lin_quad_cqq1']  = dict(nameHR="cqq1", color=Azure,  isSignal=1, isData=0, scale=1.0)
plot['sm_lin_quad_cqq31'] = dict(nameHR="cqq31", color=Azure,  isSignal=1, isData=0, scale=1.0)
plot['sm_lin_quad_cqq3']  = dict(nameHR="cqq3", color=Azure,  isSignal=1, isData=0, scale=1.0)
plot['sm_lin_quad_cW']    = dict(nameHR="cW", color=Azure,  isSignal=1, isData=0, scale=1.0)
plot['sm_lin_quad_cHl3']  = dict(nameHR="cHl3", color=Azure,  isSignal=1, isData=0, scale=1.0)
plot['sm_lin_quad_cHq3']  = dict(nameHR="cHq3", color=Azure,  isSignal=1, isData=0, scale=1.0)
plot['sm_lin_quad_cll1']  = dict(nameHR="cll1", color=Azure,  isSignal=1, isData=0, scale=1.0)

#groupPlot['cqq11']   = dict(nameHR="cqq11", isSignal=0, color=ROOT.kGreen, samples=['sm_lin_quad_cqq11'])
groupPlot['cqq1']    = dict(nameHR="cqq1", isSignal=0, color=ROOT.kGreen, samples=['sm_lin_quad_cqq11'])
#groupPlot['cqq31']   = dict(nameHR="cqq31", isSignal=0, color=ROOT.kCyan, samples=['sm_lin_quad_cqq31'])
groupPlot['cqq3']    = dict(nameHR="cqq3", isSignal=0, color=ROOT.kCyan, samples=['sm_lin_quad_cqq3'])
groupPlot['cW']      = dict(nameHR="cW", isSignal=0, color=ROOT.kOrange+1, samples=['sm_lin_quad_cW'])
groupPlot['cHl3']    = dict(nameHR="cHl3", isSignal=0, color=ROOT.kYellow, samples=['sm_lin_quad_cHl3'])
groupPlot['cHq3']    = dict(nameHR="cHq3", isSignal=0, color=ROOT.kMagenta, samples=['sm_lin_quad_cHq3'])
groupPlot['cll1']    = dict(nameHR="cll1", isSignal=0, color=ROOT.kMagenta-9, samples=['sm_lin_quad_cll1'])

groupPlot['SIG']     = dict(nameHR="SIG", isSignal=1, color=ROOT.kRed, samples=['sm'])
groupPlot['BKG']     = dict(nameHR="BKG", isSignal=0, color=ROOT.kBlue, samples=['ZZ4L','ggZZ','SSWW','WpWp_QCD','WZ_QCD','VVV','TTV','tZq','DPS','Vg', 'VgS1_H', 'VgS1_L','Fake'])

# additional options
legend['lumi'] = 'L = 59.74/fb'
legend['sqrt'] = '#sqrt{s} = 13 TeV'
