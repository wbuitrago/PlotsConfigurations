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
groupPlot['ZZ']  = dict(nameHR="ZZ", isSignal=0, color=ROOT.kMagenta - 10, samples=['ZZ4L','ggZZ'])
groupPlot['WZ_QCD']  = dict(nameHR="WZ QCD", isSignal=0, color=ROOT.kRed, samples=['WZ_QCD'])
groupPlot['WZ_EWK']  = dict(nameHR="WZ EWK", isSignal=0, color=ROOT.kMagenta, samples=['WZ_EWK'])
groupPlot['VVV']  = dict(nameHR='VVV', isSignal=0, color=ROOT.kSpring - 9, samples=['VVV'])
groupPlot['TVX']  = dict(nameHR='TVX', isSignal=0, color=ROOT.kGray, samples=['TVX'])
groupPlot['DPS']  = dict(nameHR='DPS', isSignal=0, color=ROOT.kGray + 5, samples=['DPS'])
groupPlot['Vg']  = dict(nameHR="V#gamma", isSignal=0, color=ROOT.kCyan - 7, samples=['Vg', 'VgS1_H','VgS1_L'])
groupPlot['WpWp_QCD']  = dict(nameHR="W^{#pm}W^{#pm} QCD", isSignal=0, color=ROOT.kViolet - 4, samples=['WpWp_QCD'])
groupPlot['non-prompt']  = dict(nameHR='non-Prompt', isSignal=0, color=ROOT.kYellow - 4, samples=['Fake_lep'])
groupPlot['WpWp_EWK']  = dict(nameHR="W^{#pm}W^{#pm} EWK", isSignal=0, color=ROOT.kBlue - 7, samples=['WpWp_EWK'])
groupPlot['Wrong-sign']  = dict(nameHR="mischarge", isSignal=0, color=ROOT.kOrange, samples=['WW','Top','DY','Higgs'])
#groupPlot['quadratic']  = dict(nameHR="W^{#pm}W^{#pm} EWK bsm", isSignal=0, color=ROOT.kBlue, samples=['quadratic'])
#plot = {}

# keys here must match keys in samples.py
##Fake and prompt substraction
plot['Fake_lep']  = dict(color=Yellow, isSignal=0, isData=0, scale=1.0)
##Signal
plot['DY']  = dict(color=Orange - 4, isSignal=0, isData=0, scale=1.0) #
plot['WW']  = dict(color=Orange - 4, isSignal=0, isData=0, scale=1.0) #
plot['Top']  = dict(color=Orange - 4, isSignal=0, isData=0, scale=1.0) #
plot['Higgs']  = dict(color=Orange - 4, isSignal=0, isData=0, scale=1.0) #
plot['WpWp_EWK']  = dict(color=Azure + 4, isSignal=0, isData=0, scale=1.0) # WpWpJJ_EWK_powheg WpWp_EWK
plot['WpWp_QCD']  = dict(color=Violet, isSignal=0, isData=0, scale=1.0)
#plot['WpWpJJ_QCD']  = dict(color=Violet, isSignal=0, isData=0, scale=1.0)
plot['Vg']  = dict(color=Orange + 10, isSignal=0, isData=0, scale=1.0)
plot['VgS1_H']  = dict(color=Orange + 10, isSignal=0, isData=0, scale=1.0) # VgS VgS1 VgS2
plot['VgS1_L']  = dict(color=Orange + 10, isSignal=0, isData=0, scale=1.0) # VgS VgS1 VgS2
##Reducible Background
##VV plot
plot['ZZ4L']  = dict(color=Violet + 10, isSignal=0, isData=0, scale=1.0)
plot['ggZZ']  = dict(color=Violet + 10, isSignal=0, isData=0, scale=1.0)
plot['WZ_QCD']  = dict(color=Violet + 10, isSignal=0, isData=0, scale=1.0) # WZ_QCD WZ_QCD_powheg WZ_QCD_AMCNLO
plot['WZ_EWK']  = dict(color=Violet + 10, isSignal=0, isData=0, scale=1.0)
plot['DPS']  = dict(color=Violet + 10, isSignal=0, isData=0, scale=1.0)
##VVV
plot['VVV']  = dict(color=Green, isSignal=0, isData=0, scale=1.0)
plot['TVX']  = dict(color=Green + 10, isSignal=0, isData=0, scale=1.0)
##Data
plot['DATA']  = dict(nameHR='Data', color=1, isSignal=0, isData=1, isBlind=0, scale=1.0)

# additional options
legend['lumi'] = 'L = 59.74/fb'
#legend['lumi'] = 'L = 137.19/fb'

legend['sqrt'] = '#sqrt{s} = 13 TeV'
