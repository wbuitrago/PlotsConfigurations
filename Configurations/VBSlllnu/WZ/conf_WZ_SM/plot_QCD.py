# plot configuration

# groupPlot = {}

Red=632; Violet=880; Green=416; Orange=800; Yellow=400; Azure=840; Blue=600; 

plot['WZ_QCD_off']  = dict(nameHR="WZ QCD off",  color=1, isSignal=1, isData=0, scale=1.0, samples=['WZ_QCD_off'])
plot['WZ_QCD_priv'] = dict(nameHR="WZ QCD priv", color=1, isSignal=0, isData=0, scale=1.0, samples=['WZ_QCD_priv'])

groupPlot['WZ_QCD_off']  = dict(nameHR="WZ QCD off",  isSignal=2, color=Blue,  samples=['WZ_QCD_off'])
groupPlot['WZ_QCD_priv'] = dict(nameHR="WZ QCD priv", isSignal=2, color=Azure, samples=['WZ_QCD_priv'])

# additional options
legend['lumi'] = 'L = 59.74/fb'
legend['sqrt'] = '#sqrt{s} = 13 TeV'
