{
      vector<int> veci;
        veci.push_back(1);
          veci.push_back(2);
            veci.push_back(3);

              vector<int>::iterator it;
              int z0lepton2_idx=2;
              cout<<veci.size()<<endl;
                for(it = veci.begin(); it!=veci.end();){
                        if(*it==z0lepton2_idx){
                                    it=veci.erase(it);
                                        }else{
                                                    ++it;
                                                        }
                          }
                cout<<veci.size()<<endl;
}
