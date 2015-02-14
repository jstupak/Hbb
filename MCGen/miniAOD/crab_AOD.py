physicsProcess='Zh'
globalTag='PHYS14_50_V2'

from CRABClient.UserUtilities import getUsernameFromSiteDB
username=getUsernameFromSiteDB()

from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'AOD_'+physicsProcess

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step4.py'
config.JobType.allowNonProductionCMSSW = True
config.JobType.pyCfgParams = [ 'physicsProcess='+physicsProcess, 'globalTag='+globalTag ]

config.section_("Data")
if physicsProcess=='Zh':
    config.Data.inputDataset = '/Zh_m125_PtZ-200/jstupak-RAW-637d1501b11ffc3149a6110710d366a6/USER'
if physicsProcess=='Zjets':
    config.Data.inputDataset = '/Zjets_m125_PtZ-200/jstupak-RAW-637d1501b11ffc3149a6110710d366a6/USER'
config.Data.inputDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSReader/'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 10
config.Data.publication = True
config.Data.publishDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter/'
config.Data.publishDataName = 'AODSIM'
config.Data.outLFN = '/store/group/lpcmbja/noreplica/boostedGen/'+username
config.Data.ignoreLocality = True

config.section_("Site")
config.Site.storageSite = 'T3_US_FNALLPC'
