# plot configuration

# groupPlot = {}

Red=632; Violet=880; Green=416; Orange=800; Yellow=400; Azure=840; Blue=600; 

plot['QCD_SM']      = dict(nameHR="WZ QCD priv", color=1,  isSignal=1, isData=0, scale=1.0, samples=['QCD_SM'])
plot['WZ_QCD']  = dict(nameHR="WZ QCD", color=Red,    isSignal=0, isData=0, scale=1.0, samples=['WZ_QCD'])

groupPlot['QCD_SM']     = dict(nameHR="WZ QCD priv", isSignal=1, color=Green, samples=['QCD_SM'])
groupPlot['WZ_QCD'] = dict(nameHR="WZ QCD", isSignal=2, color=Violet, samples=['WZ_QCD'])

# additional options
legend['lumi'] = 'L = 59.74/fb'
legend['sqrt'] = '#sqrt{s} = 13 TeV'
