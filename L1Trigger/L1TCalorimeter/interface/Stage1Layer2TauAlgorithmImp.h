#ifndef Stage1Layer2TauAlgorithmImp_h
#define Stage1Layer2TauAlgorithmImp_h

#include "L1Trigger/L1TCalorimeter/interface/Stage1Layer2TauAlgorithm.h"
#include "L1Trigger/L1TCalorimeter/interface/Stage1Layer2JetAlgorithmImp.h"

//	This is the implementation of the Stage1Layer2TauAlgorithm abstract base class.
//	This class will be used to find sngle high pt tracks in heavy ion collisions.

namespace l1t {

  class Stage1Layer2SingleTrackHI : public Stage1Layer2TauAlgorithm {
  public:
    Stage1Layer2SingleTrackHI();
    virtual ~Stage1Layer2SingleTrackHI();
    virtual void processEvent(//const std::vector<l1t::CaloStage1> & clusters,
			      const std::vector<l1t::CaloEmCand> & clusters,
                              const std::vector<l1t::CaloRegion> & regions,
                              std::vector<l1t::Tau> * taus);

  /* private: */
  /*   double regionLSB_; */
 };

  class Stage1Layer2TauAlgorithmImpPP : public Stage1Layer2TauAlgorithm {
  public:
    Stage1Layer2TauAlgorithmImpPP(/*const CaloParams & dbPars*/);
    virtual ~Stage1Layer2TauAlgorithmImpPP();
    virtual void processEvent(const std::vector<l1t::CaloEmCand> & EMCands,
                              const std::vector<l1t::CaloRegion> & regions,
                              std::vector<l1t::Tau> * taus);

  private: 

    int AssociatedSecondRegionEt(int ieta, int iphi,
				 const std::vector<l1t::CaloRegion> & regions,
				 double& isolation) const;

    double JetIsolation(int et, int ieta, int iphi, 
			const std::vector<l1t::Jet> & jets) const;

    int tauSeed;
    double relativeIsolationCut;
    double relativeJetIsolationCut;
  };
}
#endif
