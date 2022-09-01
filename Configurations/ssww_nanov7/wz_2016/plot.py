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
#groupPlot['ZZ']  = dict(nameHR="ZZ", isSignal=0, color=ROOT.kBlue-10, samples=['ZZ4L','ggZZ'])
#groupPlot['VVV']  = dict(nameHR='VVV', isSignal=0, color=ROOT.kBlue-9, samples=['VVV'])
#groupPlot['TTV']  = dict(nameHR='TVX', isSignal=0, color=ROOT.kBlue-7, samples=['ttV','tZq'])
#groupPlot['Vg']  = dict(nameHR="V#gamma", isSignal=0, color=ROOT.kCyan+2, samples=['Vg', 'VgS1_H'])#,'VgS1_L'])
#groupPlot['non-prompt']  = dict(nameHR='Non-prompt', isSignal=0, color=ROOT.kCyan, samples=['Fake'])
#groupPlot['WZ_QCD']  = dict(nameHR="WZ QCD", isSignal=0, color=ROOT.kGreen, samples=['WZ_QCD_powheg'])
#groupPlot['WZ_EWK']  = dict(nameHR="WZ EWK", isSignal=0, color=ROOT.kYellow, samples=['WZ_EWK'])
#groupPlot['DPS']  = dict(nameHR='DPS', isSignal=0, color=ROOT.kYellow-9, samples=['DPS'])
#groupPlot['WpWp_QCD']  = dict(nameHR="QCD W^{#pm}W^{#pm}", isSignal=0, color=ROOT.kOrange+0, samples=['WpWp_QCD'])
#groupPlot['SSWW_EW']  = dict(nameHR='EW W^{#pm}W^{#pm}', isSignal=0, color=ROOT.kMagenta, samples=['SSWW_EW'])

groupPlot['others']  = dict(nameHR='Other bkgs.', isSignal=0, color=ROOT.kBlue-10, samples=['SSWW_QCD','ZZ4L','ggZZ','Vg','VgS','DPS','VVV'])
groupPlot['tVx']  = dict(nameHR="ttV+tZq", isSignal=0, color=ROOT.kGreen, samples=['ttV','tZq'])
groupPlot['WZ_QCD']  = dict(nameHR="QCD W^{#pm}Z", isSignal=0, color=ROOT.kYellow, samples=['WZ_QCD_powheg'])
#groupPlot['SSWW_QCD']  = dict(nameHR='QCD W^{#pm}W^{#pm}', isSignal=0, color=ROOT.kMagenta, samples=['WpWp_QCD'])
#groupPlot['chargeflip']  = dict(nameHR="Wrong sign", isSignal=0, color=ROOT.kOrange, samples=['WW','ggWW','DY','top','higgs'])
groupPlot['non-prompt']  = dict(nameHR='Non-prompt', isSignal=0, color=ROOT.kCyan, samples=['Fake'])
groupPlot['WZ_EW']  = dict(nameHR="EW W^{#pm}Zjj", isSignal=0, color=ROOT.kOrange, samples=['WZ_EW'])
groupPlot['SSWW_EW']  = dict(nameHR='EW W^{#pm}W^{#pm}jj', isSignal=0, color=ROOT.kMagenta-10, samples=['SSWW_EW'])
#plot = {}

# keys here must match keys in samples.py
##Fake and prompt substraction
plot['Fake']  = dict(color=Yellow, isSignal=0, isData=0, scale=1.0)
##Signal
plot['SSWW_EW']   = dict(color=ROOT.kRed+0, isSignal=1, isData=0, scale=1.0)
plot['SSWW_QCD']  = dict(color=ROOT.kGreen, isSignal=0, isData=0, scale=1.0)
plot['WZ_EW']  = dict(color=ROOT.kGreen, isSignal=0, isData=0, scale=1.0)
plot['WZ_QCD_powheg']  = dict(color=ROOT.kGreen, isSignal=0, isData=0, scale=1.0)
plot['ZZ4L']  = dict(color=ROOT.kGreen, isSignal=0, isData=0, scale=1.0)
plot['ggZZ']  = dict(color=ROOT.kGreen, isSignal=0, isData=0, scale=1.0)
plot['ttV']  = dict(color=ROOT.kGreen, isSignal=0, isData=0, scale=1.0)
plot['tZq']  = dict(color=ROOT.kGreen, isSignal=0, isData=0, scale=1.0)
plot['Vg']  = dict(color=ROOT.kGreen, isSignal=0, isData=0, scale=1.0)
plot['VgS']  = dict(color=ROOT.kGreen, isSignal=0, isData=0, scale=1.0)
plot['DPS']  = dict(color=ROOT.kGreen, isSignal=0, isData=0, scale=1.0)
plot['VVV']  = dict(color=ROOT.kGreen, isSignal=0, isData=0, scale=1.0)
plot['Fake']  = dict(color=ROOT.kGreen, isSignal=0, isData=0, scale=1.0)
#wrong-sign
#plot['WW']  = dict(color=Green + 10, isSignal=0, isData=0, scale=1.0)
#plot['ggWW']  = dict(color=Green + 10, isSignal=0, isData=0, scale=1.0)
#plot['top']  = dict(color=Green + 10, isSignal=0, isData=0, scale=1.0)
#plot['DY']  = dict(color=Green + 10, isSignal=0, isData=0, scale=1.0)
#plot['higgs']  = dict(color=Green + 10, isSignal=0, isData=0, scale=1.0)
##Data
plot['DATA']  = dict(nameHR='Data', color=1, isSignal=0, isData=1, isBlind=0,scale=1.0)

# additional options
legend['lumi'] = 'L = 35.92/fb'
# legend['lumi'] = 'L = 137/fb'

legend['sqrt'] = '#sqrt{s} = 13 TeV'
