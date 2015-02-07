from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'GEN_ttbar'

config.section_("JobType")
config.JobType.pluginName = 'PrivateMC'
config.JobType.generator = 'lhe'
config.JobType.psetName = 'step1.py'
config.JobType.allowNonProductionCMSSW = True
config.JobType.inputFiles = ['/eos/uscms/store/user/lpcmbja/noreplica/boostedGen/ttbar/lhe/unweighted_events.1.lhe']
                             '/eos/uscms/store/user/lpcmbja/noreplica/boostedGen/ttbar/lhe/unweighted_events.2.lhe',
                             '/eos/uscms/store/user/lpcmbja/noreplica/boostedGen/ttbar/lhe/unweighted_events.3.lhe',
                             '/eos/uscms/store/user/lpcmbja/noreplica/boostedGen/ttbar/lhe/unweighted_events.4.lhe',
                             '/eos/uscms/store/user/lpcmbja/noreplica/boostedGen/ttbar/lhe/unweighted_events.5.lhe',
                             '/eos/uscms/store/user/lpcmbja/noreplica/boostedGen/ttbar/lhe/unweighted_events.6.lhe',
                             '/eos/uscms/store/user/lpcmbja/noreplica/boostedGen/ttbar/lhe/unweighted_events.7.lhe',
                             '/eos/uscms/store/user/lpcmbja/noreplica/boostedGen/ttbar/lhe/unweighted_events.8.lhe',
                             '/eos/uscms/store/user/lpcmbja/noreplica/boostedGen/ttbar/lhe/unweighted_events.9.lhe',
                             '/eos/uscms/store/user/lpcmbja/noreplica/boostedGen/ttbar/lhe/unweighted_events.10.lhe']

config.section_("Data")
config.Data.primaryDataset ='ttbar_PtLL-200'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 250
config.Data.totalUnits = 100000
config.Data.publication = True
config.Data.publishDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter/'
config.Data.publishDataName = 'GEN'
config.Data.outlfn = '/store/group/lpcmbja/noreplica/boostedGen/ttbar/GEN/'
config.Data.ignoreLocality = True

config.section_("Site")
config.Site.storageSite = 'T3_US_FNALLPC'
