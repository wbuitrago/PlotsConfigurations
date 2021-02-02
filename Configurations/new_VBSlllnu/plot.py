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
#groupPlot['WZ_EWK']  = dict(nameHR="WZ EWK", isSignal=0, color=ROOT.kMagenta, samples=['WZ_EWK'])

plot['SM'] = dict(nameHR="SM", color=Green, isSignal=0, isData=0, scale=1.0, samples=['SM'])
plot['cqq1_LI'] = dict(nameHR="cqq1 LI", color=Azure, isSignal=0, isData=0, scale=1.0, samples=['cqq1_LI'])
plot['cqq1_QU'] = dict(nameHR="cqq1 QU", color=Violet, isSignal=0, isData=0, scale=1.0, samples=['cqq1_QU'])

# keys here must match keys in samples.py
##Fake and prompt substraction
plot['Fake']  = dict(color=Yellow, isSignal=0, isData=0, scale=1.0)

##Data
plot['DATA']  = dict(nameHR='Data', color=1, isSignal=0, isData=1, isBlind=0, scale=1.0)

# additional options
legend['lumi'] = 'L = 59.74/fb'
#legend['lumi'] = 'L = 137.19/fb'

legend['sqrt'] = '#sqrt{s} = 13 TeV'
