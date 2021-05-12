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
plot['sm']        = dict(color=Azure, isSignal=1, isData=0, scale=1.0)

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

plot['DATA']      = dict(nameHR='Data', color=1, isSignal=0, isData=1, isBlind=1, scale=1.0)

groupPlot['ZZ']    = dict(nameHR="ZZ", isSignal=0, color=ROOT.kMagenta-10, samples=['ZZ4L','ggZZ'])
groupPlot['WpWp']    = dict(nameHR="W^{#pm}W^{#pm}", isSignal=0, color=ROOT.kOrange+1, samples=['SSWW','WpWp_QCD'])
groupPlot['WZ_QCD']  = dict(nameHR="WZ QCD", isSignal=0, color=ROOT.kMagenta, samples=['WZ_QCD'])
groupPlot['VVV']     = dict(nameHR='VVV', isSignal=0, color=ROOT.kSpring-9, samples=['VVV'])
groupPlot['TTV']     = dict(nameHR='TTV', isSignal=0, color=ROOT.kGray+5, samples=['TTV','tZq'])
groupPlot['DPS']     = dict(nameHR='DPS', isSignal=0, color=ROOT.kGray, samples=['DPS'])
groupPlot['Vg']      = dict(nameHR="V#gamma", isSignal=0, color=ROOT.kCyan-7, samples=['Vg', 'VgS1_H', 'VgS1_L'])
groupPlot['Fake']    = dict(nameHR='non-Prompt', isSignal=0, color=ROOT.kYellow-4, samples=['Fake'])
groupPlot['sm']      = dict(nameHR="WZ EWK", isSignal=0, color=ROOT.kRed, samples=['sm'])

# additional options
legend['lumi'] = 'L = 59.74/fb'
legend['sqrt'] = '#sqrt{s} = 13 TeV'
