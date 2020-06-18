import sys
import os
import argparse
from ROOT import gROOT, gStyle
from ROOT import TFile, TCanvas, TGraph,TGraphErrors, TH1F,TMultiGraph, TLegend, TF1, TColor


def doWWComb( file_list, output):

    gStyle.SetOptFit(0)
    gStyle.SetOptStat(0)
    gROOT.SetBatch(1)
    ypoint=[10,6,3.84,1,0.1,0.02,0.1,0.4,1,3.84,6,10]
    xpoint=[-7,-6,-5.28,-3.67,-2,-1, 1,2,2.68, 4.22,4.8,6]
    grWW=TGraph()
    #for i in range(len(xpoint)):
    #  grWW.SetPoint(i,xpoint[i],ypoint[i])


    color=[601,417,920,633,910,433,400,619,1,922]
    mg = TMultiGraph()
    leg = TLegend(0.6,0.77,0.89,0.89)
    if not os.path.exists("/eos/user/f/fcetorel/www/VBS_OS/test/2018/eft_v6_180520/WWinc/mll_ll.root"): 
      print '>>> This File does not exist -->  /eos/user/f/fcetorel/www/VBS_OS/test/2018/eft_v6_180520/WWinc/mll_ll.root... check path ... '
      return 0
    print '>>> Opening File :' , "/eos/user/f/fcetorel/www/VBS_OS/test/2018/eft_v6_180520/WWinc/mll_ll.root"
    inFile = TFile.Open ("/eos/user/f/fcetorel/www/VBS_OS/test/2018/eft_v6_180520/WWinc/mll_ll.root" ," READ ")

    c1 = inFile.Get("cc");
    gr = c1.GetListOfPrimitives().FindObject("gr")  
    gr.SetLineColor(1)
    mg.Add(gr)
    leg.AddEntry(gr,"WW inclusive","l")   
   
    for iFile in file_list:
       
        if not os.path.exists(iFile['path']): 
            print '>>> This File does not exist -->  '+iFile['path']+'... check path ... '
            continue
        print '>>> Opening File :' , iFile['path']
        inFile = TFile.Open ( iFile['path'] ," READ ")

        c1 = inFile.Get("cc");
        gr = c1.GetListOfPrimitives().FindObject("gr")

        xaxis = gr.GetXaxis().GetTitle()
        yaxis = gr.GetYaxis().GetTitle()

        gr.SetLineColor(iFile['color'])
        mg.Add(gr)
        leg.AddEntry(gr,iFile['legend'],"l")
       

    #grWW= TGraph(4,xpoint,ypoint)
    #grWW.SetLineColor(1)
    #grWW.SetLineWidth(2)
    #mg.Add(grWW)
    #leg.AddEntry(grWW,"WW inclusive","l")

    c = TCanvas()
    c.cd() 
    c.SetGrid()
    mg.Draw("al")
    line1 = TF1("line1","pol0",-100,100)
    line1.FixParameter(0,1.)
    line1.SetLineWidth(2)
    line1.SetLineStyle(2)
    line1.SetLineColor(2)
    line1.Draw("same")
  
    line2 = TF1("line2","pol0",-100,100)
    line2.FixParameter(0,3.84)
    line2.SetLineWidth(2)
    line2.SetLineStyle(2)
    line2.SetLineColor(2)
    line2.Draw("same") 


    mg.SetTitle(";" +xaxis+";" +yaxis)
    mg.GetXaxis().SetRangeUser(-7,7)
    mg.GetYaxis().SetRangeUser(0,10)

    leg.SetNColumns(2)
    leg.SetBorderSize(0)
    leg.Draw("same")
    c.SaveAs(output+"HWWcombined10.png")
    c.SaveAs(output+"HWWcombined10.root")


def doSuperTGraph( data, canvas, obj):
    xmin=-1.8
    xmax=1.8
    gStyle.SetOptFit(0)
    gStyle.SetOptStat(0)
    gROOT.SetBatch(1)

    color=[601,417,920,633,910,433,400,619,1,922]
    mg = TMultiGraph();
    leg = TLegend(0.58,0.75,0.89,0.89);
    i=0
    for ivar in data['var']:

       
        if not os.path.exists(data['fold']+"/"+ivar+"_ll.root"): 
            continue
        print '>>> Opening File :' , data['fold']+"/"+ivar+"_ll.root"
        inFile = TFile.Open ( data['fold']+"/"+ivar+"_ll.root" ," READ ")

        c1 = inFile.Get(canvas);
        gr = c1.GetListOfPrimitives().FindObject(obj)

        xaxis = gr.GetXaxis().GetTitle()
        yaxis = gr.GetYaxis().GetTitle()

        gr.SetLineColor(color[i])
        mg.Add(gr)
        leg.AddEntry(gr,ivar,"l")
        i=i+1
        print i
    

    c = TCanvas()
    c.cd() 
    c.SetGrid()
    mg.Draw("al")
    line1 = TF1("line1","pol0",-100,100)
    line1.FixParameter(0,1.)
    line1.SetLineWidth(2)
    line1.SetLineStyle(2)
    line1.SetLineColor(2)
    line1.Draw("same")
  
    line2 = TF1("line2","pol0",-100,100)
    line2.FixParameter(0,3.84)
    line2.SetLineWidth(2)
    line2.SetLineStyle(2)
    line2.SetLineColor(2)
    line2.Draw("same") 


    mg.SetTitle(";" +xaxis+";" +yaxis)
    mg.GetYaxis().SetRangeUser(0,10)

    leg.SetNColumns(2)
    leg.SetBorderSize(0)
    leg.Draw("same")
    c.SaveAs(data['fold']+"combined10.png")
    c.SaveAs(data['fold']+"combined10.pdf")
    c.SaveAs(data['fold']+"combined10.root")



def doSuperTGraphAll( file_list, canvas, obj, output):

    gStyle.SetOptFit(0)
    gStyle.SetOptStat(0)
    gROOT.SetBatch(1)

    mg = TMultiGraph();
    leg = TLegend(0.58,0.75,0.89,0.89);

    for iFile in file_list:
       
        if not os.path.exists(iFile['path']): 
            print '>>> This File does not exist -->  '+iFile['path']+'... check path ... '
            continue
        print '>>> Opening File :' , iFile['path']
        inFile = TFile.Open ( iFile['path'] ," READ ")

        c1 = inFile.Get(canvas);
        gr = c1.GetListOfPrimitives().FindObject(obj)

        xaxis = gr.GetXaxis().GetTitle()
        yaxis = gr.GetYaxis().GetTitle()

        gr.SetLineColor(iFile['color'])
        mg.Add(gr)
        leg.AddEntry(gr,iFile['legend'],"l")
    

    c = TCanvas()
    c.cd() 
    c.SetGrid()
    mg.Draw("al")
    line1 = TF1("line1","pol0",-100,100)
    line1.FixParameter(0,1.)
    line1.SetLineWidth(2)
    line1.SetLineStyle(2)
    line1.SetLineColor(2)
    line1.Draw("same")
  
    line2 = TF1("line2","pol0",-100,100)
    line2.FixParameter(0,3.84)
    line2.SetLineWidth(2)
    line2.SetLineStyle(2)
    line2.SetLineColor(2)
    line2.Draw("same") 
 


    mg.SetTitle(";" +xaxis+";" +yaxis)
    mg.GetYaxis().SetRangeUser(0,10)

    leg.SetNColumns(2)
    leg.SetBorderSize(0)
    leg.Draw("same")
    c.SaveAs(output+"10.png")
    c.SaveAs(output+"10.pdf")
    c.SaveAs(output+"10.root")

#parse arguments --> From command line options
parser = argparse.ArgumentParser()
parser.add_argument('--doComparison',          action='store_true',      default=False,      help='do comparison between OS,SS and comb')
parser.add_argument('--doWW',          action='store_true',      default=False,      help='do comparison between OS,SS and comb and WWinc')
parser.add_argument('--doOneChannel',          action='store_true',    default=False,      help='do only one channel, remember to selct it!')
parser.add_argument('-d', '--date'    , type=str   ,   help='date')
parser.add_argument('-o', '--outdir'   ,   default="/eos/user/f/fcetorel/www/VBS_OS/test/2018/",      type=str,      help='output base folder')
parser.add_argument('-c', '--channel'   , nargs='+' , defalult=""  help='Choose the year you want to run on. Default is all.')
args = parser.parse_args()



fold=args.outdir+"eft_v6_"+args.date
output=fold+"/combined/"
file_list=[]

variables_os=["ptll_var","mjjVSmTi"]
variables_ss=["pt1","pt1VSmjj"]

for varos in variables_os:
  for varss in variables_ss:
    data1 = {
        'path' : fold+'OSSF_SSDF/'+str(varos)+'_'+str(varss)+'_ll.root',
        'color' : 619, #kMagenta+3
        'legend' : 'combined',
        'fold' : fold+"/OSSF_SSDF/",
        'var' : ["ptll_pt1","ptll_pt1VSmjj","mjjVSmTi_pt1","mjjVSmTi_pt1VSmjj"]
           }
    data2 = {
        'path' : fold+'SF/'+str(varos)+'_ll.root',
        'color' : 413, #kGreen-3
        'legend' : 'OS',
        'fold' : fold+"/SF/",
        'var': ["pt1","pt2","ptll","detall","mll","mjj","mjjVSmTi","mjjVSmll","mllSF","ptll_var"]
           }
    data3 = {
        'path' : fold+'SSDF/'+str(varss)+'_ll.root',
        'color' : 867, #kAzure+7
        'legend' : 'SS',
        'fold' : fold+"/SSDF/",
         'var': ["pt1","pt1VSmjj"]
           }
    if args.doComparison:
      file_list = [data1,data2, data3]
      doSuperTGraphAll(file_list, "cc", "gr" ,output+str(varos)+'_'+str(varss))

    if args.doWW:
      file_list = [data1,data2, data3]
      doWWComb(file_list,output+str(varos)+'_'+str(varss))

if args.doOneChannel:
  if "comb" in args.channel: file_list.append(data1)
  if "OS" in args.channel: file_list.append(data2)  
  if "SS" in args.channel: file_list.append(data3)
  for data in file_list:
    try: 
      os.mkdir(data['fold']) 
    except OSError as error: 
      print(error) 
    doSuperTGraph(data, "cc", "gr" )


        





