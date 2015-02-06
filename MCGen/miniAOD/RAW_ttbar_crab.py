from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'RAW_ttbar'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step3.py'
config.JobType.allowNonProductionCMSSW = True

config.section_("Data")
config.Data.inputDataset = '/CRAB_PrivateMC/bparida-ttbar_pT200_GENSIM-30c9d67a08465e3004357085aff9e730/USER'
config.Data.inputDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSReader/'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = True
config.Data.publishDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter/'
config.Data.publishDataName = 'ttbar_pT200_RAW'
config.Data.outLFN = '/store/user/bparida/RAW'
config.Data.ignoreLocality = True

config.section_("Site")
config.Site.storageSite = 'T3_US_FNALLPC'
