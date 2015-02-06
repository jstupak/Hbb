from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'GEN_Zjets'

config.section_("JobType")
config.JobType.pluginName = 'PrivateMC'
config.JobType.generator = 'lhe'
config.JobType.psetName = 'step1.py'
config.JobType.allowNonProductionCMSSW = True
config.JobType.inputFiles = ['/eos/uscms/store/user/lpcmbja/noreplica/boostedGen/Zjets/lhe/unweighted_events.1.lhe']
                            # '/eos/uscms/store/user/lpcmbja/noreplica/boostedGen/Zh/lhe/unweighted_events.2.lhe',
                            # '/eos/uscms/store/user/lpcmbja/noreplica/boostedGen/Zh/lhe/unweighted_events.3.lhe',
                            # '/eos/uscms/store/user/lpcmbja/noreplica/boostedGen/Zh/lhe/unweighted_events.4.lhe',
                            # '/eos/uscms/store/user/lpcmbja/noreplica/boostedGen/Zh/lhe/unweighted_events.5.lhe',
                            # '/eos/uscms/store/user/lpcmbja/noreplica/boostedGen/Zh/lhe/unweighted_events.6.lhe',
                            # '/eos/uscms/store/user/lpcmbja/noreplica/boostedGen/Zh/lhe/unweighted_events.7.lhe',
                            # '/eos/uscms/store/user/lpcmbja/noreplica/boostedGen/Zh/lhe/unweighted_events.8.lhe',
                            # '/eos/uscms/store/user/lpcmbja/noreplica/boostedGen/Zh/lhe/unweighted_events.9.lhe',
                            # '/eos/uscms/store/user/lpcmbja/noreplica/boostedGen/Zh/lhe/unweighted_events.10.lhe']

config.section_("Data")
config.Data.primaryDataset ='CRAB_PrivateMC'
#config.Data.inputDataset = '/QCD_Pt-470to600_Tune4C_13TeV_pythia8/Spring14dr-castor_PU_S14_POSTLS170_V6-v1/AODSIM'
#config.Data.dbsUrl = 'https://cmsweb.cern.ch/dbs/prod/global/DBSReader/'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 20
config.Data.totalUnits = 5000
config.Data.publication = True
config.Data.publishDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter/'
config.Data.publishDataName = 'Zjets_pT200_GEN'
#config.Data.outlfn = '/store/group/lpcmbja/noreplica/boostedGen/Zh/GEN/'
config.Data.outLFN = '/store/user/bparida/GEN/Zjets'
config.Data.ignoreLocality = True

config.section_("Site")
config.Site.storageSite = 'T3_US_FNALLPC'
