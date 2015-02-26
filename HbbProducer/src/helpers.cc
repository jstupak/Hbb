#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/Math/interface/deltaPhi.h"

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

double getPull(reco::Jet j1, reco::Jet j2){

  //recalculate j1 from charged constituents
  TLorentzVector j1_lv;
  int nConst=0;
  reco::Jet::Constituents constituents=j1.getJetConstituents();
  for(auto constituentItr=constituents.begin(); constituentItr!=constituents.end(); ++constituentItr){
    edm::Ptr<reco::Candidate> constituent=*constituentItr;
    if(constituent->charge()==0 || constituent->pt()==0) continue;
    nConst++;

    TLorentzVector t_lv;
    t_lv.SetPtEtaPhiM(constituent->pt(), constituent->eta(), constituent->phi(), constituent->mass());
    j1_lv+=t_lv;
  }
  if(j1_lv.Pt()==0 || nConst<2) return -9999;

  //calculate pull vector
  double pullPhi=0;
  double pullY=0;
  for(auto constituentItr=constituents.begin(); constituentItr!=constituents.end(); ++constituentItr){
    edm::Ptr<reco::Candidate> constituent=*constituentItr;
    if(constituent->charge()==0 || constituent->pt()==0) continue;

    double dY=constituent->y()-j1_lv.Rapidity();
    double dPhi=reco::deltaPhi(constituent->phi(), j1_lv.Phi());
    pullPhi += constituent->pt() * sqrt(pow(dPhi,2) + pow(dY,2)) * dPhi;
    pullY   += constituent->pt() * sqrt(pow(dPhi,2) + pow(dY,2)) * dY;
  }
  pullPhi=pullPhi/j1_lv.Pt();
  pullY  =pullY  /j1_lv.Pt();
  double pullTheta=atan2(pullPhi,pullY);

  //recalculate j2 from charged constituents  
  TLorentzVector j2_lv;
  nConst=0;
  constituents=j2.getJetConstituents();
  for(auto constituentItr=constituents.begin(); constituentItr!=constituents.end(); ++constituentItr){
    edm::Ptr<reco::Candidate> constituent=*constituentItr;
    if(constituent->charge()==0 || constituent->pt()==0) continue;
    nConst++;

    TLorentzVector t_lv;
    t_lv.SetPtEtaPhiM(constituent->pt(), constituent->eta(), constituent->phi(), constituent->mass());
    j2_lv+=t_lv;
  }
  if(j2_lv.Pt()==0 || nConst<2) return -9999;

  double deltaY=j2_lv.Rapidity()-j1_lv.Rapidity();
  double deltaPhi=reco::deltaPhi(j2_lv.Phi(),j1_lv.Phi());
  double deltaTheta=atan2(deltaPhi,deltaY);

  return reco::deltaPhi(pullTheta,deltaTheta);
}
