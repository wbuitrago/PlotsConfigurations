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

plot['SM']      = dict(nameHR="SM",      color=1,  isSignal=1, isData=0, scale=1.0, samples=['SM'])
plot['cqq11_LI'] = dict(nameHR="cqq11 LI", color=Azure,  isSignal=1, isData=0, scale=1.0, samples=['cqq11_LI'])
plot['cqq11_QU'] = dict(nameHR="cqq11 QU", color=Violet, isSignal=1, isData=0, scale=1.0, samples=['cqq11_QU'])
plot['cqq1_LI'] = dict(nameHR="cqq1 LI", color=Azure,  isSignal=1, isData=0, scale=1.0, samples=['cqq1_LI'])
plot['cqq1_QU'] = dict(nameHR="cqq1 QU", color=Violet, isSignal=1, isData=0, scale=1.0, samples=['cqq1_QU'])
plot['cqq31_LI'] = dict(nameHR="cqq31 LI", color=Azure,  isSignal=1, isData=0, scale=1.0, samples=['cqq31_LI'])
plot['cqq31_QU'] = dict(nameHR="cqq31 QU", color=Violet, isSignal=1, isData=0, scale=1.0, samples=['cqq31_QU'])
plot['cqq3_LI'] = dict(nameHR="cqq3 LI", color=Azure,  isSignal=1, isData=0, scale=1.0, samples=['cqq3_LI'])
plot['cqq3_QU'] = dict(nameHR="cqq3 QU", color=Violet, isSignal=1, isData=0, scale=1.0, samples=['cqq3_QU'])
plot['cHl3_LI'] = dict(nameHR="cHl3 LI", color=Azure,  isSignal=1, isData=0, scale=1.0, samples=['cHl3_LI'])
plot['cHl3_QU'] = dict(nameHR="cHl3 QU", color=Violet, isSignal=1, isData=0, scale=1.0, samples=['cHl3_QU'])
plot['cHq3_LI'] = dict(nameHR="cHq3 LI", color=Azure,  isSignal=1, isData=0, scale=1.0, samples=['cHq3_LI'])
plot['cHq3_QU'] = dict(nameHR="cHq3 QU", color=Violet, isSignal=1, isData=0, scale=1.0, samples=['cHq3_QU'])
plot['cll1_LI'] = dict(nameHR="cll1 LI", color=Azure,  isSignal=1, isData=0, scale=1.0, samples=['cll1_LI'])
plot['cll1_QU'] = dict(nameHR="cll1 QU", color=Violet, isSignal=1, isData=0, scale=1.0, samples=['cll1_QU'])
plot['WZ_EWK']  = dict(nameHR="WZ EWK",  color=Red,    isSignal=0, isData=0, scale=1.0, samples=['WZ_EWK'])

groupPlot['SM']      = dict(nameHR="SM",     isSignal=1, color= 1, samples=['SM'])
groupPlot['cqq11']   = dict(nameHR="cqq11",  isSignal=2, color=Red, samples=['SM','cqq11_LI','cqq11_QU'])
groupPlot['cqq1']    = dict(nameHR="cqq1",   isSignal=2, color=Orange, samples=['SM','cqq1_LI','cqq1_QU'])
groupPlot['cqq31']   = dict(nameHR="cqq31",  isSignal=2, color=Yellow, samples=['SM','cqq31_LI','cqq31_QU'])
groupPlot['cqq3']    = dict(nameHR="cqq3",   isSignal=2, color=Green, samples=['SM','cqq3_LI','cqq3_QU'])
groupPlot['cHl3']    = dict(nameHR="cHl3",   isSignal=2, color=Azure, samples=['SM','cHl3_LI','cHl3_QU'])
groupPlot['cHq3']    = dict(nameHR="cHq3",   isSignal=2, color=Blue, samples=['SM','cHq3_LI','cHq3_QU'])
groupPlot['cll1']    = dict(nameHR="cll1",   isSignal=2, color=Violet, samples=['SM','cll1_LI','cll1_QU'])

#groupPlot['WZ_EWK'] = dict(nameHR="WZ EWK", isSignal=2, color=2, samples=['WZ_EWK'])

# additional options
legend['lumi'] = 'L = 59.74/fb'
legend['sqrt'] = '#sqrt{s} = 13 TeV'
