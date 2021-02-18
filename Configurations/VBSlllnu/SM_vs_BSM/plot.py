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

plot['sm']                = dict(nameHR="SM",      color=1,  isSignal=1, isData=0, scale=1.0, samples=['sm'])
plot['sm_lin_quad_cqq11'] = dict(nameHR="cqq11", color=Azure,  isSignal=1, isData=0, scale=1.0)
plot['sm_lin_quad_cqq1']  = dict(nameHR="cqq1", color=Azure,  isSignal=1, isData=0, scale=1.0)
plot['sm_lin_quad_cqq31'] = dict(nameHR="cqq31", color=Azure,  isSignal=1, isData=0, scale=1.0)
plot['sm_lin_quad_cqq3']  = dict(nameHR="cqq3", color=Azure,  isSignal=1, isData=0, scale=1.0)
plot['sm_lin_quad_cW']    = dict(nameHR="cW", color=Azure,  isSignal=1, isData=0, scale=1.0)
plot['sm_lin_quad_cHl3']  = dict(nameHR="cHl3", color=Azure,  isSignal=1, isData=0, scale=1.0)
plot['sm_lin_quad_cHq3']  = dict(nameHR="cHq3", color=Azure,  isSignal=1, isData=0, scale=1.0)
plot['sm_lin_quad_cll1']  = dict(nameHR="cll1", color=Azure,  isSignal=1, isData=0, scale=1.0)

groupPlot['sm']      = dict(nameHR="SM", isSignal=1, color= 1, samples=['sm'])
groupPlot['cqq11']   = dict(nameHR="cqq11", isSignal=2, color=Red, samples=['sm_lin_quad_cqq11'])
groupPlot['cqq1']    = dict(nameHR="cqq1", isSignal=2, color=Orange, samples=['sm_lin_quad_cqq11'])
groupPlot['cqq31']   = dict(nameHR="cqq31", isSignal=2, color=Yellow, samples=['sm_lin_quad_cqq31'])
groupPlot['cqq3']    = dict(nameHR="cqq3", isSignal=2, color=Green, samples=['sm_lin_quad_cqq3'])
groupPlot['cHl3']    = dict(nameHR="cHl3", isSignal=2, color=Azure, samples=['sm_lin_quad_cHl3'])
groupPlot['cHq3']    = dict(nameHR="cHq3", isSignal=2, color=Blue, samples=['sm_lin_quad_cHq3'])
groupPlot['cll1']    = dict(nameHR="cll1", isSignal=2, color=Violet, samples=['sm_lin_quad_cll1'])

#groupPlot['WZ_EWK'] = dict(nameHR="WZ EWK", isSignal=2, color=2, samples=['WZ_EWK'])

# additional options
legend['lumi'] = 'L = 59.74/fb'
legend['sqrt'] = '#sqrt{s} = 13 TeV'
