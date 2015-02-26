#ifndef Hbb_HbbProducer_HbbTuple_h
#define Hbb_HbbProducer_HbbTuple_h

#include "TLorentzVector.h"

#include "DataFormats/PatCandidates/interface/Jet.h"

#include <string>

namespace Hbb
{

  //---------------------------------------------------------------------------------

  struct Object
  {
    TLorentzVector lv;

  Object() :
    lv(TLorentzVector())
    {
    }

  Object(TLorentzVector theLV) : lv(TLorentzVector())
    {
      lv.SetPtEtaPhiM(theLV.Pt(), theLV.Eta(), theLV.Phi(), theLV.M());
    }

  Object(double pT, double eta, double phi, double m) : lv(TLorentzVector())
    {
      lv.SetPtEtaPhiM(pT, eta, phi, m);
    }

  };

  //---------------------------------------------------------------------------------
  
  struct GenParticle:Object
  {
    int pdgId, status, motherId;
    std::vector<int> daughterIds;
    
  GenParticle() : Object()
      {
	this->initialize();
      }

  GenParticle(TLorentzVector theLV) : Object(theLV)
      {
	lv.SetPtEtaPhiM(theLV.Pt(), theLV.Eta(), theLV.Phi(), theLV.M());
	this->initialize();
      }

  GenParticle(double pT, double eta, double phi, double m) : Object(pT, eta, phi, m)
      {
	lv.SetPtEtaPhiM(pT, eta, phi, m);
	this->initialize();
      }

    void initialize(){
      pdgId=-9999;
      status=-9999;
      motherId=-9999;
      daughterIds=std::vector<int>();
    }

  };
  
  //---------------------------------------------------------------------------------
  
  struct SubJet:Object
  {
    float area, R;
    
    
  SubJet() : Object()
      {
	this->initialize();
      }
    
  SubJet(TLorentzVector theLV) : Object(theLV)
    {
      this->initialize();
    }
    
  SubJet(double pT, double eta, double phi, double m) : Object(pT, eta, phi, m)
      {
	this->initialize();
      }
    
    void initialize(){
      area=-9999;
      R=-9999;
    }

  };
  
  //---------------------------------------------------------------------------------

  struct Jet:Object
  {
    float area, R;
    float tau1, tau2, tau3;
    float prunedMass, trimmedMass, filteredMass, mdtMass, butterMass;
    float qJetsVolatility;
    float csv;
    float Nconstit;

    std::vector<SubJet> trimmedSubJets;
    std::vector<SubJet> filteredSubJets;
    std::vector<SubJet> prunedSubJets;
    std::vector<SubJet> mdtSubJets;
    std::vector<SubJet> butterSubJets;
    
  Jet() : Object()
      {
	this->initialize();
      }

  Jet(pat::Jet input) : Object(input.pt(), input.eta(), input.phi(), input.mass())
      {
	this->initialize();
	this->area = input.jetArea();
	this->csv = input.bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags");
      }
    
  Jet(TLorentzVector theLV) : Object(theLV)
    {
      this->initialize();
    }
    
  Jet(double pT, double eta, double phi, double m) : Object(pT, eta, phi, m)
      {
	this->initialize();
      }
    
    void initialize(){
      area=-9999;
      R=-9999;
      tau1=-9999; 
      tau2=-9999;
      tau3=-9999;
      prunedMass=-9999;
      trimmedMass=-9999;
      filteredMass=-9999;
      mdtMass=-9999;
      butterMass=-9999;
      qJetsVolatility=-9999;
      csv=-9999;
      Nconstit=-9999;
    }
    
  };
  
  //---------------------------------------------------------------------------------

  struct Lepton:Object
  {
    int charge;
    double isolation;
    
  Lepton() : Object(),
      charge(-9999), isolation(-9999)
      {
      }

  };

  //---------------------------------------------------------------------------------
  
  struct Electron:Lepton
  {
  Electron() : Lepton()
      {
      }

  };
  
  //---------------------------------------------------------------------------------
  
  struct Muon:Lepton
  {
  Muon() : Lepton()
      {
      }

  };

  //---------------------------------------------------------------------------------

  struct Tau:Lepton
  {
  Tau() : Lepton()
      {
      }

  };

  //---------------------------------------------------------------------------------

  struct V:Object {
    std::vector<Object> daughters;

  V() : Object()
      {
        this->initialize();
      }

  V(TLorentzVector theLV) : Object(theLV)
    {
      lv.SetPtEtaPhiM(theLV.Pt(), theLV.Eta(), theLV.Phi(), theLV.M());
      this->initialize();
    }

  V(double pT, double eta, double phi, double m) : Object(pT, eta, phi, m)
      {
        lv.SetPtEtaPhiM(pT, eta, phi, m);
        this->initialize();
      }

    void initialize(){
      daughters=std::vector<Object>();
    }
  };

  //---------------------------------------------------------------------------------

  struct Higgs:Object {
    std::vector<Jet> daughters;
    float csv; 
  
  Higgs() : Object()
      {
	this->initialize();
      }

  Higgs(TLorentzVector theLV) : Object(theLV)
    {
      lv.SetPtEtaPhiM(theLV.Pt(), theLV.Eta(), theLV.Phi(), theLV.M());
      this->initialize();
    }

  Higgs(double pT, double eta, double phi, double m) : Object(pT, eta, phi, m)
      {
        lv.SetPtEtaPhiM(pT, eta, phi, m);
        this->initialize();
      }
    
    void initialize(){
      csv=-9999;
    }
  };

  //---------------------------------------------------------------------------------
  struct MET:Object
  {
  };

  //---------------------------------------------------------------------------------

  struct Tuple
  {
    int eventClassification;
    float rho;
    
    double pull, genPull;
    
    std::vector<Jet> AK4PFCHS;
    std::vector<Jet> AK8PFCHS;
    std::vector<Jet> AK10PFCHS;
    std::vector<Jet> AK12PFCHS;
    std::vector<Jet> AK15PFCHS;

    std::vector<Electron> Electrons;
    std::vector<Muon> Muons;
    std::vector<Tau> Taus;

    V theVstar;
    V theV;
    Higgs theHiggs;

    std::vector<Higgs> TeleHiggs;
    std::vector<Higgs> genTeleHiggs;

    GenParticle genVstar;
    GenParticle genV;
    GenParticle genHiggs;
    GenParticle genLepton;
    GenParticle genAntiLepton;
    GenParticle genNeutrino;
    GenParticle genAntiNeutrino;
    GenParticle genB;
    GenParticle genAntiB;
    std::vector<GenParticle> genParticles;
    
  Tuple() : 
    eventClassification(-9999), rho(-9999), pull(-9999), genPull(-9999),
      AK4PFCHS(std::vector<Jet>()), AK8PFCHS(std::vector<Jet>()), AK10PFCHS(std::vector<Jet>()), AK12PFCHS(std::vector<Jet>()), AK15PFCHS(std::vector<Jet>()),
      Electrons(std::vector<Electron>()), Muons(std::vector<Muon>()),Taus(std::vector<Tau>()),
      TeleHiggs(std::vector<Higgs>()), genTeleHiggs(std::vector<Higgs>()),
      genParticles(std::vector<GenParticle>())
    {
    }
  };
  
  typedef std::vector<Object> ObjectCollection;
  typedef std::vector<Jet> JetCollection;
  typedef std::vector<Electron> ElectronCollection;
  typedef std::vector<Muon> MuonCollection;
  typedef std::vector<Tau> TauCollection;
  typedef std::vector<Tuple> TupleCollection;
  typedef std::vector<Higgs> HiggsCollection;
}

#endif

/*  LocalWords:  ifndef
 */
