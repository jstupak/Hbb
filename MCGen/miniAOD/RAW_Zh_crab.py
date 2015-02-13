physicsProcess='Zh'
globalTag='PHYS14_50_V2'

from CRABClient.UserUtilities import getUsernameFromSiteDB
username=getUsernameFromSiteDB()

from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'RAW_'+physicsProcess

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step3.py'
config.JobType.allowNonProductionCMSSW = True
config.JobType.pyCfgParams = [ 'physicsProcess='+physicsProcess, 'globalTag='+globalTag ]

config.section_("Data")
if physicsProcess=='Zh':
    config.Data.inputDataset = '/Zh_m125_PtZ-200/jstupak-GENSIM-18b392c6220e732772ac7ab670c61bc1/USER'
if physicsProcess=='Zjets':
    config.Data.inputDataset = ''
if physicsProcess=='ttbar':
    config.Data.inputDataset = ''
config.Data.inputDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSReader/'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 10
config.Data.publication = True
config.Data.publishDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter/'
config.Data.publishDataName = 'RAW'
config.Data.outLFN = '/store/group/lpcmbja/noreplica/boostedGen/'+username
config.Data.ignoreLocality = True

config.section_("Site")
config.Site.storageSite = 'T3_US_FNALLPC'
