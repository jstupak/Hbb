events=100000
physicsProcess='Zh'
globalTag='PHYS14_50_V2'

from WMCore.Configuration import Configuration
config = Configuration()

from CRABClient.UserUtilities import getUsernameFromSiteDB
username=getUsernameFromSiteDB()

config.section_("General")
config.General.requestName = 'GEN_'+physicsProcess

config.section_("JobType")
config.JobType.pluginName = 'PrivateMC'
config.JobType.generator = 'lhe'
config.JobType.psetName = 'step1.py'
config.JobType.allowNonProductionCMSSW = True
config.JobType.pyCfgParams = [ 'physicsProcess='+physicsProcess, 'globalTag='+globalTag ]

config.section_("Data")
if physicsProcess=='Zh': config.Data.primaryDataset = 'Zh_m125_PtZ-200'
elif physicsProcess=='Zjets': config.Data.primaryDataset = 'Zjets_PtZ-200'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = events
config.Data.totalUnits = events
config.Data.publication = True
config.Data.publishDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter/'
config.Data.publishDataName = 'GEN'
config.Data.outLFN = '/store/group/lpcmbja/noreplica/boostedGen/'+username
config.Data.ignoreLocality = True

config.section_("Site")
config.Site.storageSite = 'T3_US_FNALLPC'
