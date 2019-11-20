import ROOT
from array import array

def change(bins,i):
    width=[5,5,5,5]
    xbin=[]
    #print(len(bins))
    for j in range(0,len(bins)-1):
        #print(bins[j],bins[j+1])
        xbin.append((bins[j]+bins[j+1])/2.+(i-1.5)*width[i])
    return array('f',xbin)
variables = {
    'genmjj':{
        'xrange':['500','1000','1800','inf'],
        'xbin':array('f',[500,1000,1800,2500]),
        'ybin':array('f',[1., 1., 1.]),
        '2016_up':array('f',[1.030,0.665,5.087]),
        '2016_down':array('f',[1.077,0.595,0.521]),
        '2017_up':array('f',[2.313,1.373,9.000]),
        '2017_down':array('f',[2.345,1.257,1.271]),
        '2018_up':array('f',[1.593,1.023,8.096]),
        '2018_down':array('f',[1.483,0.945,0.941]),
        'total_up':array('f',[0.803,0.496,3.957]),
        'total_down':array('f',[0.721,0.450,0.459]),
    },
    'genmll':{
        'xrange':['20','120','220','inf'],
        'xbin':array('f',[20,120.,220.,350.]),
        'ybin':array('f',[1., 1., 1.]),
        '2016_up':array('f',[0.735,0.707,0.647]),
        '2016_down':array('f',[0.746,0.706,0.480]),
        '2017_up':array('f',[1.492,0.857,0.804]),
        '2017_down':array('f',[1.760,0.944,0.669]),
        '2018_up':array('f',[1.127,0.702,0.849]),
        '2018_down':array('f',[1.359,0.772,0.768]),
        'total_up':array('f',[0.664,0.448,0.472]),
        'total_down':array('f',[0.651,0.459,0.365]),
    },
    'genlep1pt':{
        'xrange':['30','70','120','inf'],
        'xbin':array('f',[30,70.,120.,200.]),
        'ybin':array('f',[1., 1., 1.]),
        '2016_up':array('f',[0.962,0.712,0.573]),
        '2016_down':array('f',[0.966,0.675,0.453]),
        '2017_up':array('f',[1.598,0.825,0.612]),
        '2017_down':array('f',[1.663,0.810,0.510]),
        '2018_up':array('f',[1.289,0.736,0.577]),
        '2018_down':array('f',[1.395,0.755,0.512]),
        'total_up':array('f',[0.784,0.462,0.370]),
        'total_down':array('f',[0.762,0.445,0.311]),
    },
    'genlep2pt':{
        'xrange':['30','45','70','120'],
        'xbin':array('f',[30,45.,70.,120.]),
        'ybin':array('f',[1., 1., 1.]),
        '2016_up':array('f',[0.718,0.686,0.727]),
        '2016_down':array('f',[0.729,0.656,0.498]),
        '2017_up':array('f',[1.416,0.864,0.630]),
        '2017_down':array('f',[1.658,0.942,0.563]),
        '2018_up':array('f',[0.955,0.704,0.676]),
        '2018_down':array('f',[1.049,0.720,0.620]),
        'total_up':array('f',[0.618,0.457,0.420]),
        'total_down':array('f',[0.602,0.441,0.349]),
    },
    'genjet1pt':{
        'xrange':['30','145','245','inf'],
        'xbin':array('f',[30,145.,245.,350.]),
        'ybin':array('f',[1., 1., 1.]),
        '2016_up':array('f',[1.106,0.647,0.925]),
        '2016_down':array('f',[1.131,0.599,0.451]),
        '2017_up':array('f',[1.589,0.722,0.867]),
        '2017_down':array('f',[1.637,0.724,0.468]),
        '2018_up':array('f',[1.354,0.562,0.724]),
        '2018_down':array('f',[1.439,0.581,0.439]),
        'total_up':array('f',[0.801,0.363,0.483]),
        'total_down':array('f',[0.779,0.353,0.276]),
    },
    'genjet2pt':{
        'xrange':['30','70','120','inf'],
        'xbin':array('f',[30,70.,120.,250.]),
        'ybin':array('f',[1., 1., 1.]),
        '2016_up':array('f',[1.658,1.303,0.746]),
        '2016_down':array('f',[1.607,1.243,0.623]),
        '2017_up':array('f',[3.017,1.017,0.531]),
        '2017_down':array('f',[2.975,1.015,0.453]),
        '2018_up':array('f',[2.442,1.005,0.499]),
        '2018_down':array('f',[2.585,1.138,0.502]),
        'total_up':array('f',[1.001,0.583,0.305]),
        'total_down':array('f',[0.933,0.565,0.262]),
    },
}

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
    gr[0].GetHistogram().SetMaximum(3)
    gr[0].GetHistogram().SetMinimum(-1)
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