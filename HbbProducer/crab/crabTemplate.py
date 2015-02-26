from WMCore.Configuration import Configuration
config = Configuration()
config.section_("General")
config.General.requestName = 'REQUESTNAME'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'test/HbbProducer_cfg.py'
config.JobType.allowNonProductionCMSSW = True
config.JobType.pyCfgParams = [ 'theGlobalTag=GLOBALTAG', 'higgsCandSelection=HIGGSCANDSEL' ]

config.section_("Data")
config.Data.inputDataset = 'INPUTDATASET'
config.Data.inputDBS = 'https://cmsweb.cern.ch/dbs/prod/DBSURL/DBSReader/'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = LBSPERJOB
config.Data.publication = True
config.Data.publishDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter/'
config.Data.publishDataName = 'PUBLISHDATANAME'
config.Data.outLFN = '/store/group/lpcmbja/noreplica/boostedGen/jstupak'
config.Data.ignoreLocality = True

config.section_("Site")
config.Site.storageSite = 'T3_US_FNALLPC'
