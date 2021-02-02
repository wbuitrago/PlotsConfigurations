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
Red=632; Violet=880; Green=416; Orange=800; Yellow=400; Azure=860

plot['SM'] = dict(nameHR="SM", color=Green, isSignal=0, isData=0, scale=1.0, samples=['SM'])
plot['cqq1_LI'] = dict(nameHR="cqq1 LI", color=Azure, isSignal=0, isData=0, scale=1.0, samples=['cqq1_LI'])
plot['cqq1_QU'] = dict(nameHR="cqq1 QU", color=Violet, isSignal=0, isData=0, scale=1.0, samples=['cqq1_QU'])

groupPlot['SM'] = dict(nameHR="SM", color=Green, isSignal=0, isData=0, scale=1.0, samples=['SM'])
groupPlot['cqq1']  = dict(nameHR="cqq1", isSignal=0, color=Yellow, samples=['SM','cqq1_LI','cqq1_QU'])

# additional options
legend['lumi'] = 'L = 59.74/fb'
#legend['lumi'] = 'L = 137.19/fb'

legend['sqrt'] = '#sqrt{s} = 13 TeV'
