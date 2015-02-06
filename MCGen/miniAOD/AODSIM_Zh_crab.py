from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'AODSIM_Zh'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step4.py'
config.JobType.allowNonProductionCMSSW = True

config.section_("Data")
config.Data.inputDataset = '/CRAB_PrivateMC/bparida-Zh_pT200_RAW-e3ad8888848d2e90bbd6e6e99f286155/USER'
config.Data.inputDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSReader/'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = True
config.Data.publishDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter/'
config.Data.publishDataName = 'Zh_pT200_AODSIM'
config.Data.outLFN = '/store/user/bparida/AODSIM'
config.Data.ignoreLocality = True

config.section_("Site")
config.Site.storageSite = 'T3_US_FNALLPC'
