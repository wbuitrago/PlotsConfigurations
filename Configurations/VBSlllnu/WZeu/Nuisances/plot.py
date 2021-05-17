# plot configuration

# groupPlot = {}

Red=632; Violet=880; Green=416; Orange=800; Yellow=400; Azure=840; Blue=600; 

plot['WZ_QCD']  = dict(nameHR="WZ QCD", color=1,  isSignal=1, isData=0, scale=1.0, samples=['WZ_SM'])
plot['WZ_EWK']  = dict(nameHR="WZ EWK", color=Red,    isSignal=0, isData=0, scale=1.0, samples=['WZ_EWK'])

groupPlot['WZ_QCD'] = dict(nameHR="WZ QCD", isSignal=1, color=Green, samples=['WZ_QCD'])
groupPlot['WZ_EWK'] = dict(nameHR="WZ EWK", isSignal=2, color=Violet, samples=['WZ_EWK'])

# additional options
legend['lumi'] = 'L = 59.74/fb'
legend['sqrt'] = '#sqrt{s} = 13 TeV'
