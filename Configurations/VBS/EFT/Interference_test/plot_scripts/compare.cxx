// run command:
// root -l -e ".x compare.cxx(0,500,25)" -q


// comparing only the ++ part of the samples, since the -- is missing from the powheg one!

void compare(int var_number,int m, int detajj) {

    bool normalize = false ;

    TString filename = "../rootFile_VBS_SS_interf_test_mar13/plots_VBS_SS_interf_test_mar13.root";

    TCanvas *c1 = new TCanvas("test","test",800,800);
    
    auto * spad1 = new TPad("spad1","The first subpad",0.0,0.54,1.0,1.0);
    spad1->Draw();
    spad1->cd();
    

    TString var ;
    TString plot_var ;

    if(var_number == 0) 
    {
        // mjj case
        var = "mjj_v2";
        plot_var = "m_{jj} [GeV]";
    }
    if (var_number == 1)
    {
        // detajj case
        var = "detajj";
        plot_var = "d#eta_{jj} [GeV]";
    }
    
    // setting up titles and cut names etc...
    TString title_name , cut;
    cut.Form("SS_sr_m%dd%dpp_emu",m,detajj);
    title_name.Form("SS sr emu | m_{jj}>%d GeV | d#eta_{jj}> %1.1f  ",m,(float)detajj/10.);
    
    cout << title_name << endl << cut << endl ;

    TFile *f = new TFile(filename);

    // needed to make correct error propagation in histogram operations
    TH1::SetDefaultSumw2(1);

    // EWK madgraph histogram    
    TH1D *histo_ewk_mg ;
    gDirectory->GetObject(cut + "/" + var + "/histo_WpWp_EWK_mg",histo_ewk_mg) ;

    float histo_ewk_mg_int = histo_ewk_mg->Integral();
    if (normalize) {
        // normalize histogram
        histo_ewk_mg->Scale(1./histo_ewk_mg_int);
    }

    histo_ewk_mg->SetLineColor(kBlue);
    histo_ewk_mg->SetLineWidth(2);

    // EWK powheg histogram
    TH1D *histo_ewk_ph ;
    gDirectory->GetObject(cut + "/" + var + "/histo_WpWp_EWK",histo_ewk_ph) ;

    float histo_ewk_ph_int = histo_ewk_ph->Integral();
    if (normalize) {
        // normalize histogram
        histo_ewk_ph->Scale(1./histo_ewk_ph_int);
    }

    // histo_ewk_ph->SetFillColor(kGreen);
    histo_ewk_ph->SetLineColor(kGreen);
    histo_ewk_ph->SetLineWidth(2);

    // draws
    
    histo_ewk_ph->Draw("HIST same");

    histo_ewk_mg->Draw("HIST same");
    histo_ewk_mg->GetXaxis()->SetTitle(plot_var);
    histo_ewk_mg->GetYaxis()->SetTitle("Events");
    
    // computing ratios...
    ofstream outfile;
    outfile.open("compare_log.txt",std::ios_base::app);

    outfile << title_name << "\t"
        // << "WpWpJJ_EWK_QCD\t" << ewk_qcd_int << endl
        // << "WpWpJJ_QCD\t" << qcd_int << endl
        // << "WpWpJJ_EWK\t" << ewk_int << endl 
        << "ratio M/P: " << histo_ewk_mg_int / histo_ewk_ph_int << endl ;
    

    // drawing ranges
    if(normalize){
        if (histo_ewk_ph->GetMaximum() < histo_ewk_mg->GetMaximum() ) {
            histo_ewk_ph->SetMaximum(histo_ewk_mg->GetMaximum()+0.1);
        }
        else
        {
            histo_ewk_ph->SetMaximum(histo_ewk_ph->GetMaximum()+0.1);
        }
    }
    else{
        if (histo_ewk_ph->GetMaximum() < histo_ewk_mg->GetMaximum() ) {
            histo_ewk_ph->SetMaximum(histo_ewk_mg->GetMaximum()+1);
        }
        else
        {
            histo_ewk_ph->SetMaximum(histo_ewk_ph->GetMaximum()+1);
        }
    }
    


    // ofstream outfile;
    // outfile.open("script_log.txt",std::ios_base::app);

    // outfile << title_name << endl 
    //     // << "WpWpJJ_EWK_QCD\t" << ewk_qcd_int << endl
    //     // << "WpWpJJ_QCD\t" << qcd_int << endl
    //     // << "WpWpJJ_EWK\t" << ewk_int << endl 
    //     << "interference: " << 100*(ewk_qcd_int - (ewk_int + qcd_int) ) / (ewk_int + qcd_int) << " %" << endl << endl;
    
    // madgraph
    TString legend_mg ;
    legend_mg.Form("WpWpJJ_EWK_madgraph [%3.1f]",histo_ewk_mg_int);
    // powheg
    TString legend_ph ;
    legend_ph.Form("WpWpJJ_EWK_powheg [%3.1f]",histo_ewk_ph_int);


    auto legend = new TLegend(0.6,0.7,0.88,0.88);
    //legend->SetHeader("Legend","C"); // option "C" allows to center the header
    legend->AddEntry(histo_ewk_ph,legend_ph,"f");
    legend->AddEntry(histo_ewk_mg,legend_mg,"f");
    legend->Draw();
    gPad->SetGrid();
    gStyle->SetOptStat(0000);


    /*****************************************/
    /********* ratio of histograms ***********/
    /*****************************************/
    
    // powheg / madgraph

    // pad settings...
    c1->cd();
    auto * spad2 = new TPad("spad2","The second subpad",0.0,0.27,1.0,0.54);
    spad2->Draw();
    spad2->cd();

    TH1D * h_ratio = (TH1D*) histo_ewk_ph->Clone();
    h_ratio->Divide(histo_ewk_mg);
    h_ratio->SetLineColor(kBlack);
    
    h_ratio->SetTitle("");
    // gStyle->SetOptTitle(0);
    h_ratio->GetYaxis()->SetRangeUser(0.,2.0);
    h_ratio->GetYaxis()->SetLabelSize(0.05);
    h_ratio->GetXaxis()->SetLabelSize(0.05);
    h_ratio->GetYaxis()->SetTitleSize(0.05);
    h_ratio->GetXaxis()->SetTitleSize(0.05);
    h_ratio->GetYaxis()->SetTitle("Ratio");
    h_ratio->GetYaxis()->SetTitleOffset(0.5);
    h_ratio->GetXaxis()->SetTitleOffset(1);
    h_ratio->GetXaxis()->SetTitle(plot_var);

    h_ratio->SetMarkerStyle(8);
    h_ratio->Draw();
    gPad->SetGrid();
    gStyle->SetOptStat("");

    TLine *l1 = new TLine(spad2->GetUxmin(),1.0,spad2->GetUxmax(),1.0);
    l1->SetLineWidth(2);
    l1->SetLineStyle(2);
    l1->SetLineColor(kGray+3);
    l1->Draw();

    /*****************************************/
    /********* diff. of histograms ***********/
    /*****************************************/

    // pad settings...
    c1->cd();
    auto * spad3 = new TPad("spad3","The third subpad",0.0,0.0,1.0,0.27);
    spad3->Draw();
    spad3->cd();

    TH1D * h_diff = (TH1D*) histo_ewk_ph->Clone();
    h_diff->Add(histo_ewk_mg,-1);
    // h_diff->Divide(h_sum); //...normalization? if you want you can..

    h_diff->SetLineColor(kBlack);
    
    h_diff->SetTitle("");
    //gStyle->SetOptTitle(0);
    //h_diff->GetYaxis()->SetRangeUser(-1,1);
    
    double range, aux = 0;
    float distance = 0.1 ;
    if(normalize){
        range = fabs(h_diff->GetMaximum()) + distance ; 
        aux   = fabs(h_diff->GetMinimum()) + distance ;
        if (range < aux) range = aux ;
    }
    else
    {
        distance = 0.5 ;
        range = fabs(h_diff->GetMaximum()) + distance ; 
        aux   = fabs(h_diff->GetMinimum()) + distance ;
        if (range < aux) range = aux ;
    }
    

    h_diff->GetYaxis()->SetRangeUser(-range,+range);    
    
    h_diff->GetYaxis()->SetLabelSize(0.05);
    h_diff->GetXaxis()->SetLabelSize(0.05);
    h_diff->GetYaxis()->SetTitleSize(0.05);
    h_diff->GetXaxis()->SetTitleSize(0.05);
    h_diff->GetYaxis()->SetTitle("Difference");
    h_diff->GetYaxis()->SetTitleOffset(0.5);
    h_diff->GetXaxis()->SetTitleOffset(1);
    h_diff->GetXaxis()->SetTitle(plot_var);

    h_diff->SetMarkerStyle(8);
    h_diff->Draw();
    gPad->SetGrid();
    gStyle->SetOptStat("");

    TLine *l2 = new TLine(spad3->GetUxmin(),0.0,spad3->GetUxmax(),0.0);
    l2->SetLineWidth(2);
    l2->SetLineStyle(2);
    l2->SetLineColor(kGray+3);
    l2->Draw();
   
    //final prints
    c1->Print(cut + "_" + var + ".png","png");
    if(normalize){
        c1->Print("norm_" + cut + "_" + var + ".png","png");
    }
    //log plots
    // spad1->SetLogy();
    // c1->Print("log_" + cut + "_" + var + ".png","png");
    return ;
}