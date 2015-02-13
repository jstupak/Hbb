import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing ('analysis')

options.register ('physicsProcess',
                  '', # default value
                  VarParsing.VarParsing.multiplicity.singleton,
                  VarParsing.VarParsing.varType.string,
                  "The physics process (Zh, Zjets, ttbar)")

options.register ('globalTag',
                  '', # default value
                  VarParsing.VarParsing.multiplicity.singleton,
                  VarParsing.VarParsing.varType.string,
                  "The global tag")

options.parseArguments()

#if not options.physicsProcess: options.physicsProcess='Zh'
#if not options.globalTag: options.globalTag='PHYS14_50_V2'

# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step1 --filein file:/eos/uscms/store/user/lpcmbja/noreplica/boostedGen/Zh/lhe/unweighted_events.1.lhe --fileout file:step1.root --mc --eventcontent LHE --datatier GEN --conditions PHYS14_50_V2 --step NONE --python_filename step1.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 10000
import FWCore.ParameterSet.Config as cms

process = cms.Process('LHE')

# import of standard configurations
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100000)
)

# Input source
process.source = cms.Source("LHESource",
    fileNames = cms.untracked.vstring('root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.1.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.2.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.3.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.4.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.5.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.6.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.7.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.8.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.9.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.10.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.11.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.12.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.13.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.14.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.15.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.16.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.17.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.18.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.19.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.20.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.21.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.22.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.23.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.24.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.25.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.26.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.27.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.28.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.29.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.30.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.31.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.32.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.33.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.34.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.35.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.36.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.37.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.38.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.39.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.40.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.41.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.42.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.43.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.44.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.45.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.46.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.47.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.48.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.49.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.50.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.51.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.52.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.53.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.54.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.55.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.56.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.57.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.58.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.59.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.60.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.61.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.62.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.63.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.64.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.65.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.66.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.67.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.68.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.69.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.70.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.71.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.72.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.73.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.74.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.75.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.76.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.77.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.78.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.79.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.80.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.81.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.82.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.83.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.84.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.85.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.86.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.87.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.88.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.89.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.90.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.91.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.92.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.93.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.94.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.95.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.96.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.97.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.98.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.99.lhe',
                                      'root://cmsxrootd.fnal.gov//store/user/lpcmbja/noreplica/boostedGen/'+options.physicsProcess+'/lhe/unweighted_events.100.lhe',
                                      )
                            )

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.19 $'),
    annotation = cms.untracked.string('step1 nevts:10000'),
    name = cms.untracked.string('Applications')
)

# Output definition

process.LHEoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.LHEEventContent.outputCommands,
    fileName = cms.untracked.string('file:step1.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN')
    )
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, options.globalTag, '')

# Path and EndPath definitions
process.LHEoutput_step = cms.EndPath(process.LHEoutput)

# Schedule definition
process.schedule = cms.Schedule(process.LHEoutput_step)

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions

