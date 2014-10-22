import FWCore.ParameterSet.Config as cms

process = cms.Process('TESTING')

process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContentCosmics_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.EDMtoMEAtRunEnd_cff')
process.load('Configuration.StandardSequences.HarvestingCosmics_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

#process.load("DQMServices.Components.DQMEnvironment_cfi")
process.load("DQMServices.Components.MEtoEDMConverter_cfi")

process.load('HLTriggerOffline.SUSYBSM.SusyExoValidation_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.source = cms.Source("PoolSource",
    #secondaryFileNames = cms.untracked.vstring(),
    #fileNames = cms.untracked.vstring('file:/home/users/jgran/hltDQM/CMSSW_7_1_7/src/HLTriggerOffline/SUSYBSM/qcd-pt-300to470-muenriched-edm-file1-reco-test10evts-1a.root'),
    #fileNames = cms.untracked.vstring('file:/hadoop/cms/store/user/owen/qcd-300to470-muenriched/post-reco-000.root')
    #fileNames = cms.untracked.vstring('file:/tmp/pablom/QCD_Pt-300to470.root'),
    fileNames = cms.untracked.vstring( 
        #'file:///afs/cern.ch/work/a/aelwood/alphat/trigger/hltSkims/DY_withmuon1.root',
        #'file:///afs/cern.ch/work/a/aelwood/alphat/trigger/hltSkims/Susy_withmuon1.root',
        #'file:///afs/cern.ch/work/a/aelwood/alphat/trigger/hltSkim.root',
        'file:///afs/cern.ch/user/a/aelwood/alphat/hlt/CMSSW_7_2_0/src/HLTTest/hltSkim.root'
    )


    #processingMode = cms.untracked.string('RunsAndLumis')
    )



from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:startup', '')

process.out = cms.OutputModule("PoolOutputModule",
        outputCommands = cms.untracked.vstring(
           'drop *',
           'keep *_MEtoEDMConverter_*_*'
        ),
    fileName = cms.untracked.string('testout.root'),
    )


process.HLTSusyExoValSeq = cms.Sequence( process.SUSY_HLT_HT200_alphaT0p57 
         + process.SUSY_HLT_HT250_alphaT0p55 
         + process.SUSY_HLT_HT300_alphaT0p53 
         + process.SUSY_HLT_HT350_alphaT0p52 
         + process.SUSY_HLT_HT400_alphaT0p51 
        )
#process.HLTSusyExoValSeq = cms.Sequence(process.SUSY_HLT_InclusiveHT_aux350 + process.SUSY_HLT_InclusiveHT_aux600)

process.run_module = cms.Path(process.HLTSusyExoValSeq+process.MEtoEDMConverter)
#process.run_module = cms.Path(process.HLTSusyExoValSeq)
#process.dqmsave_step = cms.Path(process.dqmSaver)
#process.schedule = cms.Schedule(process.run_module,process.dqmsave_step)
process.outpath = cms.EndPath(process.out)
process.schedule = cms.Schedule(process.run_module, process.outpath)

#process.analyzerpath = cms.Path(
#    process.HLTSusyExoValSeq 
#)

