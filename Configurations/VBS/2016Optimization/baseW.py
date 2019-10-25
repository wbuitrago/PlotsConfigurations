import ROOT as rt
import sys

# Use: python2 path_to_baseW/baseW.py path_to_ntupla/ntupla
# It prints the cross section saved in the tree (fb). It works for miniAOD, updates needed for future ntuples
f = rt.TFile.Open( sys.argv[1] , "READ")
t1 = f.Get("latino")
h1= f.Get("totalEvents")
t1.GetEntry(0)
    
print sys.argv[1].split("_")[1]+" Cross Section: ",'%.4f'%(h1.GetEntries()*t1.baseW), "fb"
