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


topDiLeptonOfflineDQM_EI = cms.EDAnalyzer("TopDiLeptonOfflineDQM",
  setup = cms.PSet(
    directory = cms.string("Physics/TopEI/TopDiLeptonDQM/"),
    sources = cms.PSet(
      muons = cms.InputTag("pfIsolatedMuonsEI"),
      elecs = cms.InputTag("pfIsolatedElectronsEI"),
      jets  = cms.InputTag("pfJetsEI"),
      mets  = cms.VInputTag("met", "tcMet", "pfMetEI")
      ),
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
                             pfElectronValidationEI *
                             susyDQM_EI *
                             topDiLeptonOfflineDQM_EI )

