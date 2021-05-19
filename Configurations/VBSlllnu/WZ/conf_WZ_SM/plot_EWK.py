# plot configuration

# groupPlot = {}

Red=632; Violet=880; Green=416; Orange=800; Yellow=400; Azure=840; Blue=600; 

plot['WZ_EWK_off']  = dict(nameHR="WZ EWK off",  color=1, isSignal=1, isData=0, scale=1.0, samples=['WZ_EWK_off'])
plot['WZ_EWK_priv'] = dict(nameHR="WZ EWK priv", color=1, isSignal=0, isData=0, scale=1.0, samples=['WZ_EWK_priv'])

groupPlot['WZ_EWK_off']  = dict(nameHR="WZ EWK off",  isSignal=1, color=Green,  samples=['WZ_EWK_off'])
groupPlot['WZ_EWK_priv'] = dict(nameHR="WZ EWK priv", isSignal=2, color=Violet, samples=['WZ_EWK_priv'])

# additional options
legend['lumi'] = 'L = 59.74/fb'
legend['sqrt'] = '#sqrt{s} = 13 TeV'
