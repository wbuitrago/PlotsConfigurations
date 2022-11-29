import ROOT
import argparse


if __name__ == "__main__":
   parser = argparse.ArgumentParser(description='Command line parser for model testing')
   parser.add_argument('-f', "--file",    dest='file',     help='the root file with distributions of eFT reweighting weights', required = True)
   parser.add_argument('-c', "--cut",     dest='cut',      help='The name of the cut you want to compute quantiles on as expressed in the Latinos framework', required = True)
   parser.add_argument('-v', "--variable",    dest='variable',     help='The name of the variable TDrectory as defined in the variables.py', required = True)
   parser.add_argument('-s', "--sample",    dest='sample',     help='The name of the sample you want to extract the quantiles as defined in the samples.py', required = True)
   args = parser.parse_args()

   ROOT.gROOT.SetBatch(1)
   ROOT.TH1.SetDefaultSumw2(True)
   ROOT.gStyle.SetOptStat(0)

   f = ROOT.TFile(args.file)
   t = f.Get(args.cut + "/" + args.variable + "/tree_" + args.sample)

   shapes = [i.GetName() for i in t.GetListOfBranches()]

   out = "wplots"

   for s in shapes:

      h = ROOT.TH1D("h_{}".format(s), "h_{}".format(s), 100, t.GetMinimum(s)-0.1, t.GetMaximum(s)+0.1)
      h.GetXaxis().SetTitle("Weight")
      h.GetYaxis().SetTitle("Events")
      t.Draw("{} >> h_{}".format(s, s), "1==1")
      c = ROOT.TCanvas("c_{}".format(s), "c_{}".format(s), 1000, 1000)

      h.Draw("hist")
      c.Draw()

      c.Print("wplots/{}.png".format(s))
      c.Print("wplots/{}.pdf".format(s))

      c.SetLogy()
      c.Print("wplots/{}_log.png".format(s))
      c.Print("wplots/{}_log.pdf".format(s))
