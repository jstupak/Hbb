#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/Jet.h"

#include "Hbb/HbbProducer/interface/HbbTuple.h"

using namespace std;

typedef edm::Handle< edm::View< pat::Jet > > h_patJets;
typedef vector<Hbb::Jet> v_HbbJets;

void getHiggsCandidate(h_patJets inputJets, pat::Jet &d1, pat::Jet &d2, int method=0){

  if(method==0){
    double maxPT2=0;
    for(auto jet1=inputJets->begin(); jet1!=inputJets->end(); ++jet1){
      for(auto jet2=jet1+1; jet2!=inputJets->end() && jet1!=inputJets->end()-1; ++jet2){
	double pT2=pow(jet1->px()+jet2->px(),2)+pow(jet1->py()+jet2->py(),2);
	if (pT2>maxPT2){
	  d1=*jet1;
	  d2=*jet2;
	}
      }
    }
  }
  else{
    vector<double> maxCSV(2,-9999);
    for(auto jet=inputJets->begin(); jet!=inputJets->end(); ++jet){
      double csv=jet->bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags");
      if (csv>maxCSV[0]){
	maxCSV[1]=maxCSV[0];
	maxCSV[0]=csv;
	d2=d1;
	d1=*jet;
      }
      else {
	if (csv>maxCSV[1]) {
	  maxCSV[1]=csv;
	  d2=*jet;
	}
      }
    }
  }
}

//DO NOT USE ME - NOT MAINTAINED
void getHiggsCandidate(vector<Hbb::Jet> inputJets, pair<int,int> &leadingSubleadingIndex, int method=0){
  double maxPT2=0;
  for(unsigned int jet1=0; jet1<inputJets.size(); jet1++){
     for(unsigned int jet2=jet1+1; jet2<inputJets.size() && jet1<inputJets.size()-1; jet2++){
      double pT2=pow(inputJets[jet1].lv.Px()+inputJets[jet2].lv.Px(),2)+
         pow(inputJets[jet1].lv.Py()+inputJets[jet2].lv.Py(),2);
      if (pT2>maxPT2){
         leadingSubleadingIndex=make_pair(jet1,jet2);
      }
    }
  }
}



double getPull(pat::Jet j1, pat::Jet j2){

  double pullPhi=0;
  double pullY=0;
  
  reco::Jet::Constituents constituents=j1.getJetConstituents();
  
  for(auto constituentItr=constituents.begin(); constituentItr!=constituents.end(); ++constituentItr){
    edm::Ptr<reco::Candidate> constituent=*constituentItr;
    
    double deltaY=constituent->y()-j1.y();
    double deltaPhi=constituent->phi()-j1.phi();
    pullPhi += constituent->pt() * sqrt( pow(deltaY,2) + pow(deltaPhi,2) ) * deltaPhi;
    pullY   += constituent->pt() * sqrt( pow(deltaY,2) + pow(deltaPhi,2) ) * deltaY;
  }
  pullPhi=pullPhi/j1.pt();
  pullY  =pullY  /j1.pt();
  double pullTheta=atan(pullPhi/pullY);

  double deltaY=j1.y()-j2.y();
  double deltaPhi=j1.phi()-j2.phi();
  double deltaTheta=atan(deltaPhi/deltaY);
  
  return acos(cos(pullTheta-deltaTheta));
}
