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
    directory = cms.string("Physics/TopEI/TopDiLeptonDQM/"),

    ## [mandatory]
    sources = cms.PSet(
      muons = cms.InputTag("pfIsolatedMuonsEI"),
      elecs = cms.InputTag("pfIsolatedElectronsEI"),
      jets  = cms.InputTag("pfJetsEI"),
      mets  = cms.VInputTag("met", "tcMet", "pfMetEI")
      ),
    ## [optional] : when omitted the verbosity level is set to STANDARD
    monitoring = cms.PSet(
      verbosity = cms.string("DEBUG")
    ),
  ),
  ## [mandatory] : but may be empty
  ##
  preselection = cms.PSet(
  ),
  selection = cms.VPSet(
    cms.PSet(
      ## [mandatory] : 'jets' defines the objects to
      ## select on, 'step0' labels the histograms;
      ## instead of 'step0' you can choose any label
      label  = cms.string("empty:step0")
    ),
  )
)


dqmPhysicsEI = cms.Sequence( pfJetValidationEI *
                             pfMETValidationEI *
                             pfElectronValidationEI *
                             susyDQM_EI *
                             topDiLeptonOfflineDQM_EI )

