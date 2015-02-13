physicsProcess='Zh'
globalTag='PHYS14_50_V2'

from WMCore.Configuration import Configuration
config = Configuration()

from CRABClient.UserUtilities import getUsernameFromSiteDB
username=getUsernameFromSiteDB()

config.section_("General")
config.General.requestName = 'SIM_'+physicsProcess

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step2.py'
config.JobType.allowNonProductionCMSSW = True
config.JobType.pyCfgParams = [ 'physicsProcess='+physicsProcess, 'globalTag='+globalTag ]

config.section_("Data")
if physicsProcess=='Zh':
    config.Data.inputDataset = '/Zh_m125_PtZ-200/xuchen-GEN-3f22eb42fbc8c953391827da6f10333b/USER'
if physicsProcess=='Zjets':
    config.Data.inputDataset = '/Zjets_m125_PtZ-200/jstupak-GEN-3f22eb42fbc8c953391827da6f10333b/USER'
config.Data.inputDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSReader/'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 10
config.Data.publication = True
config.Data.publishDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter/'
config.Data.publishDataName = 'GENSIM'
config.Data.outLFN = '/store/group/lpcmbja/noreplica/boostedGen/'+username
config.Data.ignoreLocality = True

config.section_("Site")
config.Site.storageSite = 'T3_US_FNALLPC'
