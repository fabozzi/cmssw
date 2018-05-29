# import the definition of the steps and input files:
from Configuration.PyReleaseValidation.relval_steps import *

# here only define the workflows as a combination of the steps defined above:
workflows = Matrix()

###### reminiAOD 2017 #######
# reminiaod wf on 94X MC noPU
workflows[100.10] = ['', ['ADDMonoJet_d3MD3_13_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.11] = ['', ['BeamHalo_13_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.12] = ['', ['BuMixing_13_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.13] = ['', ['DisplacedSUSY_stopToBottom_13_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.14] = ['', ['EtaBToJpsiJpsi_13_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.15] = ['', ['H125GGgluonfusion_13_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.16] = ['', ['HSCPstop_M_200_13_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.17] = ['', ['Higgs200ChargedTaus_13_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.18] = ['', ['HydjetQ_MinBias_XeXe_5442GeV_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.19] = ['', ['JpsiMuMu_Pt-8_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.20] = ['', ['MinBias_13_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.21] = ['', ['NuGun_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.22] = ['', ['PhiToMuMu_13_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.23] = ['', ['PhotonJets_Pt_10_13_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.24] = ['', ['QCD_FlatPt_15_3000HS_13_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.25] = ['', ['QCD_Pt_3000_3500_13_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.26] = ['', ['QCD_Pt_600_800_13_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.27] = ['', ['QCD_Pt_80_120_13_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.28] = ['', ['QQH1352T_13_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.29] = ['', ['RSGravitonToGaGa_13_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.30] = ['', ['RSKKGluon_m3000GeV_13_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.31] = ['', ['SMS-T1tttt_13_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.32] = ['', ['SingleElectronPt10_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.33] = ['', ['SingleElectronPt1000_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.34] = ['', ['SingleElectronPt35_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.35] = ['', ['SingleGammaPt10_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.36] = ['', ['SingleGammaPt35_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.37] = ['', ['SingleMuPt1_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.38] = ['', ['SingleMuPt10_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.39] = ['', ['SingleMuPt100_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.40] = ['', ['SingleMuPt1000_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.41] = ['', ['TTbarLepton_13_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.42] = ['', ['TTbar_13_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.43] = ['', ['TenE_0_200_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.44] = ['', ['TenTau_15_500_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.45] = ['', ['Upsilon1SToMuMu_13_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.46] = ['', ['WE_13_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.47] = ['', ['WM_13_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.48] = ['', ['Wjet_Pt_3000_3500_13_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.49] = ['', ['Wjet_Pt_80_120_13_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.50] = ['', ['WpM_13_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.51] = ['', ['WpToENu_M-2000_13_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.52] = ['', ['ZEE_13_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.53] = ['', ['ZMM_13_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.54] = ['', ['ZTT_13_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.55] = ['', ['ZpEE_2250_13_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.56] = ['', ['ZpMM_13_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.57] = ['', ['ZpMM_2250_13_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[100.58] = ['', ['ZpTT_1500_13_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]


# reminiaod wf on 94X MC PU
workflows[101.10] = ['', ['H125GGgluonfusion_13PU_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[101.11] = ['', ['Higgs200ChargedTaus_13PU_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[101.12] = ['', ['NuGunPU_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[101.13] = ['', ['QCD_FlatPt_15_3000HS_13PU_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[101.14] = ['', ['QQH1352T_13PU_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[101.15] = ['', ['SMS-T1tttt_13PU_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[101.16] = ['', ['TTbarLepton_13PU_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[101.17] = ['', ['TTbar_13PU_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[101.18] = ['', ['TenE_0_200PU_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[101.19] = ['', ['TenTau_15_500PU_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[101.20] = ['', ['ZEE_13PU_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[101.21] = ['', ['ZMM_13PU_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[101.22] = ['', ['ZTT_13PU_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]
workflows[101.23] = ['', ['ZpTT_1500_13PU_94XrmIN','REMINIAOD_mc2017','HARVESTUP17_REMINIAOD_mc2017']]



# reminiaod wf on 94X data

workflows[102.10] = ['',['RunDoubleEG2017B_rm','REMINIAOD_data2017','HARVEST2017_REMINIAOD_data2017']]
workflows[102.11] = ['',['RunDoubleMuon2017B_rm','REMINIAOD_data2017','HARVEST2017_REMINIAOD_data2017']]
workflows[102.12] = ['',['RunHLTPhysics2017B_rm','REMINIAOD_data2017','HARVEST2017_REMINIAOD_data2017']]
workflows[102.13] = ['',['RunJetHT2017B_rm','REMINIAOD_data2017','HARVEST2017_REMINIAOD_data2017']]
workflows[102.14] = ['',['RunMET2017B_rm','REMINIAOD_data2017','HARVEST2017_REMINIAOD_data2017']]
workflows[102.15] = ['',['RunMuOnia2017B_rm','REMINIAOD_data2017','HARVEST2017_REMINIAOD_data2017']]
workflows[102.16] = ['',['RunMuonEG2017B_rm','REMINIAOD_data2017','HARVEST2017_REMINIAOD_data2017']]
workflows[102.17] = ['',['RunSingleElectron2017B_rm','REMINIAOD_data2017','HARVEST2017_REMINIAOD_data2017']]
workflows[102.18] = ['',['RunSingleMuon2017B_rm','REMINIAOD_data2017','HARVEST2017_REMINIAOD_data2017']]
workflows[102.19] = ['',['RunSinglePhoton2017B_rm','REMINIAOD_data2017','HARVEST2017_REMINIAOD_data2017']]
workflows[102.20] = ['',['RunZeroBias2017B_rm','REMINIAOD_data2017','HARVEST2017_REMINIAOD_data2017']]
workflows[102.21] = ['',['RunDoubleEG2017C_rm','REMINIAOD_data2017','HARVEST2017_REMINIAOD_data2017']]
workflows[102.22] = ['',['RunDoubleMuon2017C_rm','REMINIAOD_data2017','HARVEST2017_REMINIAOD_data2017']]
workflows[102.23] = ['',['RunHLTPhysics2017C_rm','REMINIAOD_data2017','HARVEST2017_REMINIAOD_data2017']]
workflows[102.24] = ['',['RunJetHT2017C_rm','REMINIAOD_data2017','HARVEST2017_REMINIAOD_data2017']]
workflows[102.25] = ['',['RunMET2017C_rm','REMINIAOD_data2017','HARVEST2017_REMINIAOD_data2017']]
workflows[102.26] = ['',['RunMuOnia2017C_rm','REMINIAOD_data2017','HARVEST2017_REMINIAOD_data2017']]
workflows[102.27] = ['',['RunMuonEG2017C_rm','REMINIAOD_data2017','HARVEST2017_REMINIAOD_data2017']]
workflows[102.28] = ['',['RunSingleElectron2017C_rm','REMINIAOD_data2017','HARVEST2017_REMINIAOD_data2017']]
workflows[102.29] = ['',['RunSingleMuon2017C_rm','REMINIAOD_data2017','HARVEST2017_REMINIAOD_data2017']]
workflows[102.30] = ['',['RunSinglePhoton2017C_rm','REMINIAOD_data2017','HARVEST2017_REMINIAOD_data2017']]
workflows[102.31] = ['',['RunZeroBias2017C_rm','REMINIAOD_data2017','HARVEST2017_REMINIAOD_data2017']]
workflows[102.32] = ['',['RunNoBPTX2017C_rm','REMINIAOD_data2017','HARVEST2017_REMINIAOD_data2017']]


############################

# reminiaod wf on 80X MC noPU
workflows[103.10] = ['', ['ADDMonoJet_d3MD3_13_80XrmIN','REMINIAOD_mc2016']]
workflows[103.11] = ['', ['BeamHalo_13_80XrmIN','REMINIAOD_mc2016']]
workflows[103.12] = ['', ['DisplacedSUSY_stopToBottom_13_80XrmIN','REMINIAOD_mc2016']]
workflows[103.13] = ['', ['EtaBToJpsiJpsi_13_80XrmIN','REMINIAOD_mc2016']]
workflows[103.14] = ['', ['H125GGgluonfusion_13_80XrmIN','REMINIAOD_mc2016']]
workflows[103.15] = ['', ['HSCPstop_M_200_13_80XrmIN','REMINIAOD_mc2016']]
workflows[103.16] = ['', ['Higgs200ChargedTaus_13_80XrmIN','REMINIAOD_mc2016']]
workflows[103.17] = ['', ['JpsiMuMu_Pt-15_80XrmIN','REMINIAOD_mc2016']]
workflows[103.18] = ['', ['MinBias_13_80XrmIN','REMINIAOD_mc2016']]
workflows[103.19] = ['', ['NuGun_80XrmIN','REMINIAOD_mc2016']]
workflows[103.20] = ['', ['PhiToMuMu_13_80XrmIN','REMINIAOD_mc2016']]
workflows[103.21] = ['', ['PhotonJets_Pt_10_13_80XrmIN','REMINIAOD_mc2016']]
workflows[103.22] = ['', ['QCD_FlatPt_15_3000HS_13_80XrmIN','REMINIAOD_mc2016']]
workflows[103.23] = ['', ['QCD_Pt_3000_3500_13_80XrmIN','REMINIAOD_mc2016']]
workflows[103.24] = ['', ['QCD_Pt_600_800_13_80XrmIN','REMINIAOD_mc2016']]
workflows[103.25] = ['', ['QCD_Pt_80_120_13_80XrmIN','REMINIAOD_mc2016']]
workflows[103.26] = ['', ['QQH1352T_13_80XrmIN','REMINIAOD_mc2016']]
workflows[103.27] = ['', ['RSGravitonToGaGa_13_80XrmIN','REMINIAOD_mc2016']]
workflows[103.28] = ['', ['RSKKGluon_m3000GeV_13_80XrmIN','REMINIAOD_mc2016']]
workflows[103.29] = ['', ['SMS-T1tttt_13_80XrmIN','REMINIAOD_mc2016']]
workflows[103.30] = ['', ['SingleElectronPt10_80XrmIN','REMINIAOD_mc2016']]
workflows[103.31] = ['', ['SingleElectronPt1000_80XrmIN','REMINIAOD_mc2016']]
workflows[103.32] = ['', ['SingleElectronPt35_80XrmIN','REMINIAOD_mc2016']]
workflows[103.33] = ['', ['SingleGammaPt10_80XrmIN','REMINIAOD_mc2016']]
workflows[103.34] = ['', ['SingleGammaPt35_80XrmIN','REMINIAOD_mc2016']]
workflows[103.35] = ['', ['SingleMuPt1_80XrmIN','REMINIAOD_mc2016']]
workflows[103.36] = ['', ['SingleMuPt10_80XrmIN','REMINIAOD_mc2016']]
workflows[103.37] = ['', ['SingleMuPt100_80XrmIN','REMINIAOD_mc2016']]
workflows[103.38] = ['', ['SingleMuPt1000_80XrmIN','REMINIAOD_mc2016']]
workflows[103.39] = ['', ['TTbarLepton_13_80XrmIN','REMINIAOD_mc2016']]
workflows[103.40] = ['', ['TTbar_13_80XrmIN','REMINIAOD_mc2016']]
workflows[103.41] = ['', ['Upsilon1SToMuMu_13_80XrmIN','REMINIAOD_mc2016']]
workflows[103.42] = ['', ['WE_13_80XrmIN','REMINIAOD_mc2016']]
workflows[103.43] = ['', ['WM_13_80XrmIN','REMINIAOD_mc2016']]
workflows[103.44] = ['', ['Wjet_Pt_3000_3500_13_80XrmIN','REMINIAOD_mc2016']]
workflows[103.45] = ['', ['Wjet_Pt_80_120_13_80XrmIN','REMINIAOD_mc2016']]
workflows[103.46] = ['', ['WpM_13_80XrmIN','REMINIAOD_mc2016']]
workflows[103.47] = ['', ['WpToENu_M-2000_13_80XrmIN','REMINIAOD_mc2016']]
workflows[103.48] = ['', ['ZEE_13_80XrmIN','REMINIAOD_mc2016']]
workflows[103.49] = ['', ['ZMM_13_80XrmIN','REMINIAOD_mc2016']]
workflows[103.50] = ['', ['ZTT_13_80XrmIN','REMINIAOD_mc2016']]
workflows[103.51] = ['', ['ZpEE_2250_13_80XrmIN','REMINIAOD_mc2016']]
workflows[103.52] = ['', ['ZpMM_13_80XrmIN','REMINIAOD_mc2016']]
workflows[103.53] = ['', ['ZpMM_2250_13_80XrmIN','REMINIAOD_mc2016']]
workflows[103.54] = ['', ['ZpTT_1500_13_80XrmIN','REMINIAOD_mc2016']]

# reminiaod wf on 80X MC PU
workflows[104.10] = ['', ['H125GGgluonfusion_13PU_80XrmIN','REMINIAOD_mc2016']]
workflows[104.11] = ['', ['NuGunPU_80XrmIN','REMINIAOD_mc2016']]
workflows[104.12] = ['', ['QQH1352T_13PU_80XrmIN','REMINIAOD_mc2016']]
workflows[104.13] = ['', ['SMS-T1tttt_13PU_80XrmIN','REMINIAOD_mc2016']]
workflows[104.14] = ['', ['TTbar_13PU_80XrmIN','REMINIAOD_mc2016']]
workflows[104.15] = ['', ['ZpMM_13PU_80XrmIN','REMINIAOD_mc2016']]
workflows[104.16] = ['', ['ZpEE_2250_13PU_80XrmIN','REMINIAOD_mc2016']]
workflows[104.17] = ['', ['ZEE_13PU_80XrmIN','REMINIAOD_mc2016']]
workflows[104.18] = ['', ['ZMM_13PU_80XrmIN','REMINIAOD_mc2016']]
workflows[104.19] = ['', ['ZTT_13PU_80XrmIN','REMINIAOD_mc2016']]
workflows[104.20] = ['', ['ZpTT_1500_13PU_80XrmIN','REMINIAOD_mc2016']]

# reminiaod wf on 80X data
workflows[105.10] = ['',['RunDoubleEG2016B_rm','REMINIAOD_data2016_HIPM']]
workflows[105.11] = ['',['RunDoubleMuon2016B_rm','REMINIAOD_data2016_HIPM']]
workflows[105.12] = ['',['RunHLTPhysics2016B_rm','REMINIAOD_data2016_HIPM']]
workflows[105.13] = ['',['RunJetHT2016B_rm','REMINIAOD_data2016_HIPM']]
workflows[105.14] = ['',['RunMET2016B_rm','REMINIAOD_data2016_HIPM']]
workflows[105.15] = ['',['RunMuOnia2016B_rm','REMINIAOD_data2016_HIPM']]
workflows[105.16] = ['',['RunMuonEG2016B_rm','REMINIAOD_data2016_HIPM']]
workflows[105.17] = ['',['RunSingleElectron2016B_rm','REMINIAOD_data2016_HIPM']]
workflows[105.18] = ['',['RunSingleMuon2016B_rm','REMINIAOD_data2016_HIPM']]
workflows[105.19] = ['',['RunSinglePhoton2016B_rm','REMINIAOD_data2016_HIPM']]
workflows[105.20] = ['',['RunZeroBias2016B_rm','REMINIAOD_data2016_HIPM']]

workflows[105.21] = ['',['RunDoubleEG2016E_rm','REMINIAOD_data2016_HIPM']]
workflows[105.22] = ['',['RunDoubleMuon2016E_rm','REMINIAOD_data2016_HIPM']]
workflows[105.23] = ['',['RunHLTPhysics2016E_rm','REMINIAOD_data2016_HIPM']]
workflows[105.24] = ['',['RunJetHT2016E_rm','REMINIAOD_data2016_HIPM']]
workflows[105.25] = ['',['RunMET2016E_rm','REMINIAOD_data2016_HIPM']]
workflows[105.26] = ['',['RunMuonEG2016E_rm','REMINIAOD_data2016_HIPM']]
workflows[105.27] = ['',['RunSingleElectron2016E_rm','REMINIAOD_data2016_HIPM']]
workflows[105.28] = ['',['RunSingleMuon2016E_rm','REMINIAOD_data2016_HIPM']]
workflows[105.29] = ['',['RunSinglePhoton2016E_rm','REMINIAOD_data2016_HIPM']]
workflows[105.30] = ['',['RunZeroBias2016E_rm','REMINIAOD_data2016_HIPM']]

from Configuration.PyReleaseValidation.relval_input_reminiaod import *


