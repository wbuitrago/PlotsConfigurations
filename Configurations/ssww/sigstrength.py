import ROOT
from array import array

def change(bins,i):
    width=[20,20,20,20]
    xbin=[]
    #print(len(bins))
    for j in range(0,len(bins)-1):
        #print(bins[j],bins[j+1])
        xbin.append((bins[j]+bins[j+1])/2.+(i-1.5)*width[i])
    return array('f',xbin)
variables = {
    'genmjj':{
        'xrange':['500','1000','1500','inf'],
        'xbin':array('f',[500,1000,1500,2000]),
        'ybin':array('f',[1., 1., 1.]),
        '2016_up':array('f',[2.491,1.642,3.226]),
        '2016_down':array('f',[2.524,1.462,0.885]),
        '2017_up':array('f',[3.346,1.746,3.113]),
        '2017_down':array('f',[3.445,1.596,0.931]),
        '2018_up':array('f',[2.256,1.383,3.005]),
        '2018_down':array('f',[2.074,1.294,0.766]),
        'total_up':array('f',[1.659,0.895,2.813]),
        'total_down':array('f',[1.570,0.844,0.553]),
    },
    'genmll':{
        'xrange':['20','120','250','inf'],
        'xbin':array('f',[20,120.,250.,400.]),
        'ybin':array('f',[1., 1., 1.]),
        '2016_up':array('f',[1.213,1.234,1.542]),
        '2016_down':array('f',[1.232,1.235,1.222]),
        '2017_up':array('f',[2.428,1.525,1.998]),
        '2017_down':array('f',[2.880,1.708,1.769]),
        '2018_up':array('f',[1.775,1.332,2.023]),
        '2018_down':array('f',[2.157,1.507,1.997]),
        'total_up':array('f',[1.078,0.841,1.108]),
        'total_down':array('f',[1.065,0.821,0.928]),
    },
    'genlep1pt':{
        'xrange':['30','120','250','inf'],
        'xbin':array('f',[30,120.,250.,400.]),
        'ybin':array('f',[1., 1., 1.]),
        '2016_up':array('f',[0.998,1.519,5.125]),
        '2016_down':array('f',[1.043,1.366,3.400]),
        '2017_up':array('f',[1.452,1.681,6.288]),
        '2017_down':array('f',[1.499,1.582,4.216]),
        '2018_up':array('f',[1.265,1.431,4.909]),
        '2018_down':array('f',[1.337,1.364,3.566]),
        'total_up':array('f',[0.800,0.939,3.158]),
        'total_down':array('f',[0.777,0.880,2.157]),
    },
    'genjet1pt':{
        'xrange':['30','120','250','inf'],
        'xbin':array('f',[30,120.,250.,400.]),
        'ybin':array('f',[1., 1., 1.]),
        '2016_up':array('f',[3.632,0.973,1.449]),
        '2016_down':array('f',[3.667,0.943,0.798]),
        '2017_up':array('f',[5.407,1.322,1.628]),
        '2017_down':array('f',[5.902,1.405,0.942]),
        '2018_up':array('f',[4.399,1.084,1.372]),
        '2018_down':array('f',[4.821,1.191,0.906]),
        'total_up':array('f',[2.853,0.700,0.900]),
        'total_down':array('f',[2.822,0.691,0.533]),
    },
    'genjet2pt':{
        'xrange':['30','120','250','inf'],
        'xbin':array('f',[30,120.,250.,400.]),
        'ybin':array('f',[1., 1., 1.]),
        '2016_up':array('f',[1.623,0.847,2.569]),
        '2016_down':array('f',[1.686,0.759,1.374]),
        '2017_up':array('f',[1.919,1.030,2.242]),
        '2017_down':array('f',[1.889,0.956,1.473]),
        '2018_up':array('f',[1.889,0.862,2.119]),
        '2018_down':array('f',[2.078,0.862,1.438]),
        'total_up':array('f',[1.172,0.543,1.391]),
        'total_down':array('f',[1.150,0.514,0.871]),
    },
}
'''
'genlep2pt':{
    'xrange':['30','120','250','inf'],
    'xbin':array('f',[30,120.,250.,400.]),
    'ybin':array('f',[1., 1., 1.]),
    '2016_up':array('f',[0.1,0.1,0.1]),
    '2016_down':array('f',[0.1,0.1,0.1]),
    '2017_up':array('f',[0.1,0.1,0.1]),
    '2017_down':array('f',[0.1,0.1,0.1]),
    '2018_up':array('f',[0.1,0.1,0.1]),
    '2018_down':array('f',[0.1,0.1,0.1]),
    'total_up':array('f',[0.1,0.1,0.1]),
    'total_down':array('f',[0.1,0.1,0.1]),
},
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
        gr[i]=ROOT.TGraphAsymmErrors(len(variables[ivar]['ybin']),change(variables[ivar]['xbin'],i),variables[ivar]['ybin'],ex,ex,variables[ivar][year[i]+'_up'],variables[ivar][year[i]+'_down'])
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
    gr[0].GetHistogram().SetMaximum(6)
    gr[0].GetHistogram().SetMinimum(-4)
    gr[0].Draw("APE")

    #print(variables[ivar]['xbin'][1],gr[0].GetHistogram().GetMinimum(),variables[ivar]['xbin'][1],gr[0].GetHistogram().GetMaximum())
    l1=ROOT.TLine(variables[ivar]['xbin'][1],gr[0].GetHistogram().GetMinimum(),variables[ivar]['xbin'][1],gr[0].GetHistogram().GetMaximum())
    l2=ROOT.TLine(variables[ivar]['xbin'][-2],gr[0].GetHistogram().GetMinimum(),variables[ivar]['xbin'][-2],gr[0].GetHistogram().GetMaximum())
    l1.SetLineStyle(7)
    l2.SetLineStyle(7)
    l1.Draw("SAME")
    l2.Draw("SAME")

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