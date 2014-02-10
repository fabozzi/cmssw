import FWCore.ParameterSet.Config as cms

from DQMOffline.PFTau.PFJetDQMAnalyzer_cfi import pfJetDQMAnalyzer

pfJetValidationEI = pfJetDQMAnalyzer.clone()
pfJetValidationEI.InputCollection = cms.InputTag('pfJetsEI')
pfJetValidationEI.MatchCollection = cms.InputTag('ak5PFJets')
pfJetValidationEI.BenchmarkLabel  = cms.string('PFJetValidationEI/CompWithPFJet')

from DQMOffline.PFTau.PFMETDQMAnalyzer_cfi import pfMETDQMAnalyzer
pfMETValidationEI = pfMETDQMAnalyzer.clone()
pfMETValidationEI.InputCollection = cms.InputTag('pfMetEI')
pfMETValidationEI.MatchCollection = cms.InputTag('pfMet')
pfMETValidationEI.BenchmarkLabel  = cms.string('PFMETValidationEI/CompWithPFMet')

pfAllElectrons = cms.EDFilter("PdgIdPFCandidateSelector",
                              pdgId = cms.vint32(11, -11),
                              src = cms.InputTag("particleFlow")
)

from DQMOffline.PFTau.PFElectronDQMAnalyzer_cfi import pfElectronDQMAnalyzer
pfElectronValidationEI = pfElectronDQMAnalyzer.clone()
pfElectronValidationEI.InputCollection = cms.InputTag('pfIsolatedElectronsEI')
pfElectronValidationEI.MatchCollection = cms.InputTag('pfAllElectrons')
pfElectronValidationEI.BenchmarkLabel  = cms.string('PFElectronValidationEI/CompWithPFElectron')

from DQM.Physics.susyDQM_cfi import *
susyDQM_EI = susyDQM.clone()
susyDQM_EI.moduleName = cms.untracked.string('Physics/SusyEI')
susyDQM_EI.muonCollection = cms.InputTag('pfIsolatedMuonsEI')
susyDQM_EI.electronCollection = cms.InputTag('pfIsolatedElectronsEI')
susyDQM_EI.jetCollection = cms.InputTag('pfJetsEI')
susyDQM_EI.metCollection = cms.InputTag('pfMetEI')


singleTopDQM_EI = cms.EDAnalyzer("SingleTopTChannelLeptonDQM",
  ## ------------------------------------------------------
  ## SETUP
  ##
  ## configuration of the MonitoringEnsemble(s)
  ## [mandatory] : optional PSets may be omitted
  ##
  setup = cms.PSet(
    ## sub-directory to write the monitor histograms to
    ## [mandatory] : should not be changed w/o explicit 
    ## communication to TopCom!
    directory = cms.string("Physics/TopEI/SingleTopDQM/"),
    ## [mandatory]
    sources = cms.PSet(
      muons = cms.InputTag("pfIsolatedMuonsEI"),
      elecs_gsf = cms.InputTag("gedGsfElectrons"),
      elecs = cms.InputTag("pfIsolatedElectronsEI"),
      jets  = cms.InputTag("pfJetsEI"),
      mets  = cms.VInputTag("met", "tcMet", "pfMetEI"),
      pvs   = cms.InputTag("offlinePrimaryVertices")
    ),
    ## [optional] : when omitted the verbosity level is set to STANDARD
    monitoring = cms.PSet(
      verbosity = cms.string("DEBUG")
    ),
  ),
  preselection = cms.PSet(
  ),
  selection = cms.VPSet(
    cms.PSet(
      label  = cms.string("empty:step0")
    ),
  )
)


dqmPhysicsEI = cms.Sequence( pfJetValidationEI *
                             pfMETValidationEI *
                             pfAllElectrons *
                             pfElectronValidationEI *
                             susyDQM_EI *
                             singleTopDQM_EI )

