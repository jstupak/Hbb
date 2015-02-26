from os import system

ID='genTeleHiggsBugFix'
higgsCandSelection=1

jobs=[#'REQUESTNAME','INPUTDATASET','PUBLISHDATANAME','LBSPERJOB', 'input DBS', 'GT'],
    ['Zh_CSA14_40bx50',          '/ZH_HToBB_ZToLL_M-125_13TeV_powheg-herwigpp/Spring14miniaod-141029_PU40bx50_PLS170_V6AN2-v1/MINIAODSIM','CSA14-40bx50',        20, 'global', 'PLS170_V6AN1::All'],
    ['Zjets_CSA14_40bx50',       '/DYJetsToMuMu_PtZ-180_M-50_13TeV-madgraph/Spring14miniaod-141029_PU40bx50_PLS170_V6AN2-v1/MINIAODSIM',  'CSA14-40bx50',        20, 'global', 'PLS170_V6AN1::All'],
    ['Zh',                       '/Zh_m125_PtZ-200/jstupak-PHYS14_50_V2-MINIAODSIM-5aeef11518ff3267c48efc923ff0710e/USER',                'Private-40bx50',      20, 'phys03', 'PLS170_V6AN1::All'],
    ['Zjets',                    '/Zjets_m125_PtZ-200/jstupak-PHYS14_50_V2-MINIAODSIM-5aeef11518ff3267c48efc923ff0710e/USER',             'Private-40bx50',      20, 'phys03', 'PLS170_V6AN1::All'],
    ['Zjets_lowPt_CSA14_40bx50', '/DYToMuMu_M-50_Tune4C_13TeV-pythia8/Spring14miniaod-141029_PU40bx50_castor_PLS170_V6AN2-v1/MINIAODSIM', 'CSA14-40bx50-lowPt',  50, 'global', 'PLS170_V6AN1::All'],
     
    ['Zh_CSA14_20bx25',          '/ZH_HToBB_ZToLL_M-125_13TeV_powheg-herwigpp/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM',       'CSA14-20bx25',        20, 'global', 'PLS170_V7AN1::All'],
    ['Zh_PHYS14_20bx25',         '/ZH_HToBB_ZToLL_M-125_13TeV_powheg-herwigpp/Phys14DR-PU20bx25_tsg_PHYS14_25_V1-v1/MINIAODSIM',          'Phys14-20bx25',       20, 'global', 'PLS170_V7AN1::All'],
    ['Zh_PHYS14_40bx25',         '/ZH_HToBB_ZToLL_M-125_13TeV_powheg-herwigpp/Phys14DR-PU40bx25_tsg_PHYS14_25_V1-v2/MINIAODSIM',          'Phys14-40bx25',       20, 'global', 'PLS170_V7AN1::All'],
    ['Zjets_CSA14_20bx25',       '/DYJetsToMuMu_PtZ-180_M-50_13TeV-madgraph/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM',         'CSA14-20bx25',        20, 'global', 'PLS170_V7AN1::All'],
    ['Zjets_PHYS14_20bx25',      '/DYJetsToMuMu_PtZ-180_M-50_13TeV-madgraph/Phys14DR-PU20bx25_tsg_PHYS14_25_V1-v3/MINIAODSIM',            'Phys14-PU20bx25',     20, 'global', 'PLS170_V7AN1::All'],
    ['Zjets_PHYS14_40bx25',      '/DYJetsToMuMu_PtZ-180_M-50_13TeV-madgraph/Phys14DR-PU40bx25_tsg_PHYS14_25_V1-v1/MINIAODSIM',            'Phys14-PU40bx25',     20, 'global', 'PLS170_V7AN1::All'],
    ['Zjets_lowPt_PHYS14_20bx25','/DYToMuMu_M-50_Tune4C_13TeV-pythia8/Phys14DR-PU20bx25_castor_PHYS14_25_V1-v3/MINIAODSIM',               'Phys14-20bx25-lowPt', 50, 'global', 'PLS170_V7AN1::All'],
    ]
 
template='crab/crabTemplate.py'

#---------------------------------------------------------------------------------------------------------------------------------------------------

for job in jobs:
    requestName=job[0]+'_higgsCand'+str(higgsCandSelection)
    inputDS=job[1]
    publishDN=job[2]+'-higgsCand'+str(higgsCandSelection)+'-'+ID+'-HBB'
    LBs=str(job[3])
    dbsUrl=job[4]
    GT=job[5]
    
    config='python/'+requestName+'.py'
    system('cp '+template+' '+config)
    system('sed s%REQUESTNAME%'+requestName+'%g '+config+' --in-place')
    system('sed s%INPUTDATASET%'+inputDS+'%g '+config+' --in-place')
    system('sed s%PUBLISHDATANAME%'+publishDN+'%g '+config+' --in-place')
    system('sed s%LBSPERJOB%'+LBs+'%g '+config+' --in-place')
    system('sed s%DBSURL%'+dbsUrl+'%g '+config+' --in-place')
    system('sed s%GLOBALTAG%'+GT+'%g '+config+' --in-place')
    system('sed s%HIGGSCANDSEL%'+str(higgsCandSelection)+'%g '+config+' --in-place')

    system('crab submit '+config)
