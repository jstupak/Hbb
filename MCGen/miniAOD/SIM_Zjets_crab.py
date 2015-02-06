from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'SIM_Zjets'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step2.py'
config.JobType.allowNonProductionCMSSW = True

config.section_("Data")
config.Data.inputDataset = '/CRAB_PrivateMC/bparida-Zjets_pT200_GEN-3f22eb42fbc8c953391827da6f10333b/USER'
config.Data.inputDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSReader/'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = True
config.Data.publishDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter/'
config.Data.publishDataName = 'Zjets_pT200_GENSIM'
config.Data.outLFN = '/store/user/bparida/GENSIM'
config.Data.ignoreLocality = True

config.section_("Site")
config.Site.storageSite = 'T3_US_FNALLPC'
