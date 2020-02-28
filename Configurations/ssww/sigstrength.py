import ROOT
from array import array

def change(bins,i):
    width=[2,2,2,2]
    xbin=[]
    #print(len(bins))
    for j in range(0,len(bins)-1):
        #print(bins[j],bins[j+1])
        xbin.append((bins[j]+bins[j+1])/2.+(i-1.5)*width[i])
    return array('f',xbin)
#without cr

variables = {
    'genmjj':{
        'xrange':['500','1000','1800','inf'],
        'xbin':array('f',[500,1000,1800,2500]),
        'ybin':array('f',[1., 1., 1.]),
        '2016_up':array('f',[0.982,0.537,0.472]),
        '2016_down':array('f',[1.011,0.487,0.380]),
        '2017_up':array('f',[1.435,0.624,1.201]),
        '2017_down':array('f',[1.553,0.606,0.445]),
        '2018_up':array('f',[1.080,0.473,1.057]),
        '2018_down':array('f',[1.143,0.448,0.399]),
        'total_up':array('f',[0.730,0.317,0.433]),
        'total_down':array('f',[0.745,0.309,0.274]),
    },
    'genmll':{
        'xrange':['20','120','220','inf'],
        'xbin':array('f',[20,120.,220.,350.]),
        'ybin':array('f',[1., 1., 1.]),
        '2016_up':array('f',[0.739,0.689,0.584]),
        '2016_down':array('f',[0.756,0.703,0.526]),
        '2017_up':array('f',[1.500,0.850,1.251]),
        '2017_down':array('f',[1.725,0.933,0.695]),
        '2018_up':array('f',[1.149,0.750,0.884]),
        '2018_down':array('f',[1.415,0.851,0.740]),
        'total_up':array('f',[0.675,0.470,0.485]),
        'total_down':array('f',[0.692,0.483,0.391]),
    },
    'genlep1pt':{
        'xrange':['30','70','120','inf'],
        'xbin':array('f',[30,70.,120.,200.]),
        'ybin':array('f',[1., 1., 1.]),
        '2016_up':array('f',[0.880,0.682,0.540]),
        '2016_down':array('f',[0.917,0.682,0.489]),
        '2017_up':array('f',[1.668,0.892,0.694]),
        '2017_down':array('f',[1.877,0.963,0.561]),
        '2018_up':array('f',[1.359,0.838,0.680]),
        '2018_down':array('f',[1.633,0.939,0.637]),
        'total_up':array('f',[0.790,0.501,0.400]),
        'total_down':array('f',[0.809,0.506,0.347]),
    },
    'genlep2pt':{
        'xrange':['30','45','70','120'],
        'xbin':array('f',[30,45.,70.,120.]),
        'ybin':array('f',[1., 1., 1.]),
        '2016_up':array('f',[0.715,0.695,0.629]),
        '2016_down':array('f',[0.746,0.695,0.546]),
        '2017_up':array('f',[1.470,0.890,0.640]),
        '2017_down':array('f',[1.751,0.994,0.614]),
        '2018_up':array('f',[1.072,0.823,0.713]),
        '2018_down':array('f',[1.296,0.925,0.738]),
        'total_up':array('f',[0.657,0.507,0.412]),
        'total_down':array('f',[0.672,0.508,0.383]),
    },
    'genjet1pt':{
        'xrange':['30','145','245','inf'],
        'xbin':array('f',[30,145.,245.,350.]),
        'ybin':array('f',[1., 1., 1.]),
        '2016_up':array('f',[1.012,0.578,0.926]),
        '2016_down':array('f',[1.065,0.539,0.414]),
        '2017_up':array('f',[1.392,0.689,1.115]),
        '2017_down':array('f',[1.519,0.689,0.545]),
        '2018_up':array('f',[1.276,0.568,0.983]),
        '2018_down':array('f',[1.394,0.567,0.505]),
        'total_up':array('f',[0.710,0.335,0.599]),
        'total_down':array('f',[0.702,0.317,0.287]),
    },
    'genjet2pt':{
        'xrange':['30','70','120','inf'],
        'xbin':array('f',[30,70.,120.,250.]),
        'ybin':array('f',[1., 1., 1.]),
        '2016_up':array('f',[1.040,0.674,0.560]),
        '2016_down':array('f',[1.071,0.641,0.391]),
        '2017_up':array('f',[2.037,0.838,0.661]),
        '2017_down':array('f',[2.391,0.861,0.470]),
        '2018_up':array('f',[1.704,0.812,0.573]),
        '2018_down':array('f',[2.106,0.864,0.457]),
        'total_up':array('f',[0.967,0.441,0.365]),
        'total_down':array('f',[0.941,0.418,0.267]),
    },
}

'''
# with cr
variables = {
    'genmjj':{
        'xrange':['500','1000','1800','inf'],
        'xbin':array('f',[500,1000,1800,2500]),
        'ybin':array('f',[1., 1., 1.]),
        '2016_up':array('f',[0.860,0.524,0.472]),
        '2016_down':array('f',[0.833,0.468,0.379]),
        '2017_up':array('f',[1.031,0.578,1.188]),
        '2017_down':array('f',[1.033,0.539,0.443]),
        '2018_up':array('f',[0.776,0.440,0.992]),
        '2018_down':array('f',[0.768,0.409,0.390]),
        'total_up':array('f',[0.506,0.293,0.424]),
        'total_down':array('f',[0.501,0.283,0.270]),
    },
    'genmll':{
        'xrange':['20','120','220','inf'],
        'xbin':array('f',[20,120.,220.,350.]),
        'ybin':array('f',[1., 1., 1.]),
        '2016_up':array('f',[0.663,0.620,0.567]),
        '2016_down':array('f',[0.629,0.586,0.497]),
        '2017_up':array('f',[0.977,0.646,1.130]),
        '2017_down':array('f',[0.986,0.629,0.585]),
        '2018_up':array('f',[0.684,0.563,0.797]),
        '2018_down':array('f',[0.691,0.544,0.558]),
        'total_up':array('f',[0.433,0.355,0.449]),
        'total_down':array('f',[0.426,0.346,0.338]),
    },
    'genlep1pt':{
        'xrange':['30','70','120','inf'],
        'xbin':array('f',[30,70.,120.,200.]),
        'ybin':array('f',[1., 1., 1.]),
        '2016_up':array('f',[0.785,0.622,0.520]),
        '2016_down':array('f',[0.751,0.586,0.461]),
        '2017_up':array('f',[1.149,0.708,0.621]),
        '2017_down':array('f',[1.154,0.689,0.481]),
        '2018_up':array('f',[0.815,0.617,0.561]),
        '2018_down':array('f',[0.812,0.599,0.465]),
        'total_up':array('f',[0.513,0.383,0.349]),
        'total_down':array('f',[0.500,0.373,0.295]),
    },
    'genlep2pt':{
        'xrange':['30','45','70','120'],
        'xbin':array('f',[30,45.,70.,120.]),
        'ybin':array('f',[1., 1., 1.]),
        '2016_up':array('f',[0.633,0.633,0.615]),
        '2016_down':array('f',[0.606,0.594,0.529]),
        '2017_up':array('f',[0.943,0.702,0.599]),
        '2017_down':array('f',[0.952,0.675,0.538]),
        '2018_up':array('f',[0.645,0.616,0.604]),
        '2018_down':array('f',[0.638,0.591,0.556]),
        'total_up':array('f',[0.419,0.391,0.373]),
        'total_down':array('f',[0.403,0.372,0.338]),
    },
    'genjet1pt':{
        'xrange':['30','145','245','inf'],
        'xbin':array('f',[30,145.,245.,350.]),
        'ybin':array('f',[1., 1., 1.]),
        '2016_up':array('f',[1.069,0.608,1.429]),
        '2016_down':array('f',[1.151,0.560,0.415]),
        '2017_up':array('f',[1.876,0.744,1.531]),
        '2017_down':array('f',[2.285,0.767,0.602]),
        '2018_up':array('f',[1.641,0.613,1.476]),
        '2018_down':array('f',[2.020,0.629,0.588]),
        'total_up':array('f',[0.977,0.380,1.297]),
        'total_down':array('f',[0.976,0.355,0.304]),
    },
    'genjet2pt':{
        'xrange':['30','70','120','inf'],
        'xbin':array('f',[30,70.,120.,250.]),
        'ybin':array('f',[1., 1., 1.]),
        '2016_up':array('f',[1.060,0.684,0.589]),
        '2016_down':array('f',[1.106,0.646,0.405]),
        '2017_up':array('f',[2.062,0.902,0.672]),
        '2017_down':array('f',[2.515,0.944,0.536]),
        '2018_up':array('f',[1.711,0.848,0.611]),
        '2018_down':array('f',[2.134,0.901,0.476]),
        'total_up':array('f',[0.983,0.465,0.442]),
        'total_down':array('f',[0.973,0.438,0.270]),
    },
}
'''
c1 = ROOT.TCanvas("c1","A Simple Graph Example",200,10,500,300)
gr=[0,0,0,0]
ex=array('f',[0., 0., 0.])
year=['2016','2017','2018','total']
for ivar in variables:
    for i in range(0,4):
        '''
        print(len(variables[ivar]['ybin']))
        print(change(variables[ivar]['xbin'],i))
        print(variables[ivar]['ybin'])
        print(ex)
        print(ex)
        print(variables[ivar][year[i]+'_up'])
        print(variables[ivar][year[i]+'_down'])
        '''
        gr[i]=ROOT.TGraphAsymmErrors(len(variables[ivar]['ybin']),change(variables[ivar]['xbin'],i),variables[ivar]['ybin'],ex,ex,variables[ivar][year[i]+'_down'],variables[ivar][year[i]+'_up'])
    c1.Clear()
    c1.cd()
    c1.SetGridy()
    ROOT.gStyle.SetOptStat(0)

    gr[0].SetLineColor(ROOT.kBlue)
    gr[0].SetMarkerColor(ROOT.kBlue)
    gr[0].SetMarkerStyle(20)
    gr[0].GetXaxis().SetLimits(variables[ivar]['xbin'][0],variables[ivar]['xbin'][-1])
    gr[0].GetXaxis().SetTitle(ivar+' [GeV]')
    gr[0].GetYaxis().SetTitle('#mu')
    gr[0].GetHistogram().SetMaximum(3.)
    gr[0].GetHistogram().SetMinimum(-1.)
    gr[0].Draw("APE")

    #print(variables[ivar]['xbin'][1],gr[0].GetHistogram().GetMinimum(),variables[ivar]['xbin'][1],gr[0].GetHistogram().GetMaximum())
    l1=ROOT.TLine(variables[ivar]['xbin'][1],gr[0].GetHistogram().GetMinimum(),variables[ivar]['xbin'][1],gr[0].GetHistogram().GetMaximum())
    l2=ROOT.TLine(variables[ivar]['xbin'][-2],gr[0].GetHistogram().GetMinimum(),variables[ivar]['xbin'][-2],gr[0].GetHistogram().GetMaximum())
    l1.SetLineStyle(7)
    l2.SetLineStyle(7)
    l1.Draw("SAME")
    l2.Draw("SAME")

    l3=ROOT.TLine(variables[ivar]['xbin'][0],1,variables[ivar]['xbin'][-1],1)
    l4=ROOT.TLine(variables[ivar]['xbin'][0],0,variables[ivar]['xbin'][-1],0)
    l5=ROOT.TLine(variables[ivar]['xbin'][0],2,variables[ivar]['xbin'][-1],2)
    l3.SetLineStyle(1)
    l4.SetLineStyle(1)
    l5.SetLineStyle(1)
    l3.SetLineWidth(1)
    l4.SetLineWidth(1)
    l5.SetLineWidth(1)
    l3.SetLineColor(ROOT.kBlack)
    l4.SetLineColor(ROOT.kBlack)
    l5.SetLineColor(ROOT.kBlack)
    l3.Draw("SAME")
    l4.Draw("SAME")
    l5.Draw("SAME")

    gr[0].Draw("PE")

    gr[1].SetLineColor(ROOT.kRed)
    gr[1].SetMarkerColor(ROOT.kRed)
    gr[1].SetMarkerStyle(20)
    gr[1].Draw("PE")

    gr[2].SetLineColor(ROOT.kGreen)
    gr[2].SetMarkerColor(ROOT.kGreen)
    gr[2].SetMarkerStyle(20)
    gr[2].Draw("PE")

    gr[3].SetLineColor(ROOT.kBlack)
    gr[3].SetMarkerColor(ROOT.kBlack)
    gr[3].SetMarkerStyle(20)
    gr[3].Draw("PE")



    leg1 = ROOT.TLegend(0.2, 0.83, 0.38, 0.90)
    leg1.AddEntry(gr[0], "2016")
    leg2 = ROOT.TLegend(0.35, 0.83, 0.53, 0.90)
    leg2.AddEntry(gr[1], "2017")
    leg3 = ROOT.TLegend(0.50, 0.83, 0.68, 0.90)
    leg3.AddEntry(gr[2], "2018")
    leg4 = ROOT.TLegend(0.65, 0.83, 0.85, 0.90)
    leg4.AddEntry(gr[3], "combine")
    leg1.SetFillStyle(0)
    leg1.SetLineWidth(0)
    leg2.SetFillStyle(0)
    leg2.SetLineWidth(0)
    leg3.SetFillStyle(0)
    leg3.SetLineWidth(0)
    leg4.SetFillStyle(0)
    leg4.SetLineWidth(0)
    leg1.Draw()
    leg2.Draw()
    leg3.Draw()
    leg4.Draw()

    c1.SaveAs("signal_strength_"+ivar+".pdf")