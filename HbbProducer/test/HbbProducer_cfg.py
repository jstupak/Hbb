import FWCore.ParameterSet.Config as cms


process = cms.Process("Hbb")
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True),
                                     allowUnscheduled = cms.untracked.bool(True) 
                                     )

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000) )
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_1.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_10.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_100.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_101.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_102.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_103.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_104.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_105.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_106.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_107.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_108.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_109.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_11.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_110.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_111.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_112.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_113.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_114.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_115.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_116.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_117.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_118.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_119.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_12.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_120.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_121.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_122.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_123.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_124.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_125.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_126.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_127.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_128.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_129.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_13.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_130.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_131.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_132.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_133.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_134.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_135.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_136.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_137.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_138.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_139.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_14.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_140.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_141.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_142.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_143.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_144.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_145.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_146.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_147.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_148.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_149.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_15.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_150.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_151.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_152.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_153.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_154.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_155.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_156.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_157.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_158.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_159.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_16.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_160.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_161.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_162.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_163.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_164.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_165.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_166.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_167.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_168.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_169.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_17.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_170.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_171.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_172.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_173.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_174.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_175.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_176.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_177.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_178.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_179.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_18.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_180.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_181.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_182.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_183.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_184.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_185.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_186.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_187.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_188.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_189.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_19.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_190.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_191.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_192.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_193.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_194.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_195.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_196.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_197.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_198.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_199.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_2.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_20.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_200.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_201.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_202.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_203.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_204.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_205.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_206.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_207.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_208.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_209.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_21.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_210.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_211.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_212.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_213.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_214.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_215.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_216.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_217.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_218.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_219.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_22.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_220.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_221.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_222.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_223.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_224.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_225.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_226.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_227.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_228.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_229.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_23.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_230.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_231.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_232.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_233.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_234.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_235.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_236.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_237.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_238.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_239.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_24.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_240.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_241.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_242.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_243.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_244.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_245.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_246.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_247.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_248.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_249.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_25.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_26.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_27.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_28.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_29.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_3.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_30.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_31.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_32.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_33.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_34.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_35.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_36.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_37.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_38.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_39.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_4.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_40.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_41.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_42.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_43.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_44.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_45.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_46.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_47.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_48.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_49.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_5.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_50.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_51.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_52.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_53.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_54.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_55.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_56.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_57.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_58.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_59.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_6.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_60.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_61.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_62.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_63.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_64.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_65.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_66.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_67.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_68.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_69.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_7.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_70.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_71.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_72.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_73.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_74.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_75.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_76.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_77.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_78.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_79.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_8.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_80.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_81.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_82.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_83.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_84.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_85.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_86.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_87.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_88.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_89.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_9.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_90.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_91.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_92.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_93.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_94.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_95.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_96.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_97.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_98.root',
       '/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/ttbar_pT200_MINIAODSIM/150207_234828/0000/step5_99.root'
        #'file:/eos/uscms/store/user/jstupak/ZH_HToBB_ZToLL_M-125_13TeV_powheg-herwigpp/Spring14dr-PU_S14_POSTLS170_V6AN1-v1/140622_185946/0000/miniAOD-prod_PAT_1.root'
        )
                            )

#theGlobalTag='PHYS14_50_V2'
theGlobalTag='PLS170_V6AN1::All'   #PU_S14
#theGlobalTag='PLS170_V7AN1::All'   #PU20bx25

process.load("FWCore.MessageService.MessageLogger_cfi")

process.load('Hbb.HbbProducer.HbbProducer_cfi')

#####################################################################################################################################

process.load('PhysicsTools.PatAlgos.producersLayer1.patCandidates_cff')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.Geometry_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc')

#process.load('CondCore.DBCommon.CondDBSetup_cfi')

process.pfCHS = cms.EDFilter('CandPtrSelector', src = cms.InputTag('packedPFCandidates'), cut = cms.string('fromPV'))
process.pfNoMuonCHS =  cms.EDProducer("CandPtrProjector", src = cms.InputTag("pfCHS"), veto = cms.InputTag("selectedMuons"))
process.pfNoLeptonCHS = cms.EDProducer("CandPtrProjector", src = cms.InputTag("pfNoMuonCHS"), veto =  cms.InputTag("selectedElectrons"))

#2012 Tight muon: https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideMuonId#Tight_Muon
#missing dZ cut - JS
process.selectedMuons = cms.EDFilter("PATMuonSelector",
                                     src = cms.InputTag("slimmedMuons"),
                                     cut = cms.string('pt > 20. &'
                                                      'abs(eta) < 2.4 &'
                                                      'isGlobalMuon &'
                                                      'isPFMuon &'
                                                      #'globalTrack.normalizedChi2 < 10.0 &'
                                                      #'globalTrack.hitPattern.numberOfValidMuonHits > 0 &'
                                                      #'numberOfMatchedStations > 1 &'
                                                      #'abs(dB) < 0.2 &' #This was 0.02 before, ooops.  I think this is right - JS
                                                      #'innerTrack.hitPattern.numberOfValidPixelHits > 0 &'
                                                      #'innerTrack.hitPattern.trackerLayersWithMeasurement > 5 &'
                                                      '(pfIsolationR04.sumChargedHadronPt+ max(0.,pfIsolationR04.sumNeutralHadronEt+pfIsolationR04.sumPhotonEt-0.5*pfIsolationR04.sumPUPt))/pt < 0.2'
                                                      )
                                     )

#process.muonMatch.match='packedGenParticles'


##**** Electron definition from https://github.com/cms-sw/cmssw/blob/CMSSW_7_3_X/PhysicsTools/PatAlgos/test/miniAOD/example_ei.py - IB
process.selectedElectrons = cms.EDFilter("PATElectronSelector", 
                                         src = cms.InputTag("slimmedElectrons"), 
                                         cut = cms.string('abs(eta)<2.5 &'
                                                          'pt>20. &'
                                                          'gsfTrack.isAvailable() &'
                                                          'gsfTrack.hitPattern().numberOfLostHits(\'MISSING_INNER_HITS\') < 2 &'
                                                          '(pfIsolationVariables().sumChargedHadronPt+max(0.,pfIsolationVariables().sumNeutralHadronEt+pfIsolationVariables().sumPhotonEt-0.5*pfIsolationVariables().sumPUPt))/pt < 0.2'))


process.load('RecoJets.Configuration.RecoPFJets_cff')
process.load('RecoJets.Configuration.RecoGenJets_cff')
process.fixedGridRhoFastjetAll.pfCandidatesTag = 'packedPFCandidates'

process.ak4PFJets.src = 'packedPFCandidates'
process.ak4PFJetsCHS.src = 'pfNoLeptonCHS'
process.ak4PFJets.doAreaFastjet = True
process.ak4PFJetsCHS.doAreaFastjet = True

process.ak8PFJetsCHS  = process.ak4PFJetsCHS.clone(rParam = 0.8)
process.ak10PFJetsCHS = process.ak4PFJetsCHS.clone(rParam = 1.0)
process.ak12PFJetsCHS = process.ak4PFJetsCHS.clone(rParam = 1.2)
process.ak15PFJetsCHS = process.ak4PFJetsCHS.clone(rParam = 1.5)

process.ak4GenJets.src = 'packedGenParticles'
process.ak3GenJets  = process.ak4GenJets.clone(rParam = 0.3)
process.ak8GenJets  = process.ak4GenJets.clone(rParam = 0.8)
process.ak10GenJets = process.ak4GenJets.clone(rParam = 1.0)
process.ak12GenJets = process.ak4GenJets.clone(rParam = 1.2)
process.ak15GenJets = process.ak4GenJets.clone(rParam = 1.5)

process.ak8PFJetsCHSPruned.src = 'pfNoLeptonCHS'
process.ak8PFJetsCHSTrimmed.src = 'pfNoLeptonCHS'
process.ak8PFJetsCHSFiltered.src = 'pfNoLeptonCHS'

process.ak10PFJetsCHSPruned = process.ak8PFJetsCHSPruned.clone(rParam = 1)
process.ak10PFJetsCHSTrimmed = process.ak8PFJetsCHSTrimmed.clone(rParam = 1)
process.ak10PFJetsCHSFiltered = process.ak8PFJetsCHSFiltered.clone(rParam = 1)

process.ak12PFJetsCHSPruned = process.ak8PFJetsCHSPruned.clone(rParam = 1.2)
process.ak12PFJetsCHSTrimmed = process.ak8PFJetsCHSTrimmed.clone(rParam = 1.2)
process.ak12PFJetsCHSFiltered = process.ak8PFJetsCHSFiltered.clone(rParam = 1.2)

process.ak15PFJetsCHSPruned = process.ak8PFJetsCHSPruned.clone(rParam = 1.5)
process.ak15PFJetsCHSTrimmed = process.ak8PFJetsCHSTrimmed.clone(rParam = 1.5)
process.ak15PFJetsCHSFiltered = process.ak8PFJetsCHSFiltered.clone(rParam = 1.5)

from PhysicsTools.PatAlgos.tools.jetTools import addJetCollection
from PhysicsTools.PatAlgos.tools.jetTools import switchJetCollection

addJetCollection(
    process,
    labelName = 'AK4PFCHS',
    jetSource = cms.InputTag('ak4PFJetsCHS'),
    algo = 'ak4',
    rParam = 0.4,
    jetCorrections = ('AK4PFchs', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute']), 'None'),
    trackSource = cms.InputTag('unpackedTracksAndVertices'),
    pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
    svSource = cms.InputTag('slimmedSecondaryVertices'),
    pfCandidates = cms.InputTag('packedPFCandidates'),
    btagDiscriminators = ['pfCombinedSecondaryVertexBJetTags', 'pfCombinedInclusiveSecondaryVertexV2BJetTags'],
    genJetCollection=cms.InputTag('ak4GenJets'),
    )

addJetCollection(
    process,
    labelName = 'AK8PFCHS',
    jetSource = cms.InputTag('ak8PFJetsCHS'),
    algo = 'ak8',
    rParam = 0.8,
    jetCorrections = ('AK8PFchs', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute']), 'None'),
    trackSource = cms.InputTag('unpackedTracksAndVertices'),
    pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
    svSource = cms.InputTag('slimmedSecondaryVertices'),
    pfCandidates = cms.InputTag('packedPFCandidates'),
    btagDiscriminators = ['pfCombinedSecondaryVertexBJetTags', 'pfCombinedInclusiveSecondaryVertexV2BJetTags'],
    genJetCollection=cms.InputTag('ak4GenJets'),
    )

addJetCollection(
    process,
    labelName = 'AK10PFCHS',
    jetSource = cms.InputTag('ak10PFJetsCHS'),
    algo = 'ak10',
    rParam = 1.0,
    jetCorrections = ('AK10PFchs', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute']), 'None'),
    trackSource = cms.InputTag('unpackedTracksAndVertices'),
    pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
    svSource = cms.InputTag('slimmedSecondaryVertices'),
    pfCandidates = cms.InputTag('packedPFCandidates'),
    btagDiscriminators = ['pfCombinedSecondaryVertexBJetTags', 'pfCombinedInclusiveSecondaryVertexV2BJetTags'],
    genJetCollection=cms.InputTag('ak4GenJets'),
    )

addJetCollection(
    process,
    labelName = 'AK12PFCHS',
    jetSource = cms.InputTag('ak12PFJetsCHS'),
    algo = 'ak12',
    rParam = 1.2,
    jetCorrections = ('AK10PFchs', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute']), 'None'),
    trackSource = cms.InputTag('unpackedTracksAndVertices'),
    pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
    svSource = cms.InputTag('slimmedSecondaryVertices'),
    pfCandidates = cms.InputTag('packedPFCandidates'),
    btagDiscriminators = ['pfCombinedSecondaryVertexBJetTags', 'pfCombinedInclusiveSecondaryVertexV2BJetTags'],
    genJetCollection=cms.InputTag('ak4GenJets'),
    )

addJetCollection(
    process,
    labelName = 'AK15PFCHS',
    jetSource = cms.InputTag('ak15PFJetsCHS'),
    algo = 'ak15',
    rParam = 1.5,
    jetCorrections = ('AK10PFchs', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute']), 'None'),
    trackSource = cms.InputTag('unpackedTracksAndVertices'),
    pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
    svSource = cms.InputTag('slimmedSecondaryVertices'),
    pfCandidates = cms.InputTag('packedPFCandidates'),
    btagDiscriminators = ['pfCombinedSecondaryVertexBJetTags', 'pfCombinedInclusiveSecondaryVertexV2BJetTags'],
    genJetCollection=cms.InputTag('ak4GenJets'),
    )

switchJetCollection(
    process,
    jetSource = cms.InputTag('ak4PFJets'),
    algo = 'ak4',
    rParam = 0.4,
    jetCorrections = ('AK4PF', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute']), 'Type-1'),
    trackSource = cms.InputTag('unpackedTracksAndVertices'),
    pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
    svSource = cms.InputTag('slimmedSecondaryVertices'),
    pfCandidates = cms.InputTag('packedPFCandidates'),
    #btagDiscriminators = ['pfCombinedSecondaryVertexBJetTags', 'pfCombinedInclusiveSecondaryVertexV2BJetTags'],   #this breaks the config
    genJetCollection=cms.InputTag('ak4GenJets'),
    )

for module in [process.patJetsAK4PFCHS, process.patJetsAK8PFCHS, process.patJetsAK10PFCHS, process.patJetsAK12PFCHS, process.patJetsAK15PFCHS]:
    module.addJetCharge   = False
    module.addBTagInfo    = True   
    module.getJetMCFlavour = False
    module.addAssociatedTracks = False

for module in [process.patJetPartonMatch, process.patJetPartonMatchAK4PFCHS, process.patJetPartonMatchAK8PFCHS, process.patJetPartonMatchAK10PFCHS, process.patJetPartonMatchAK12PFCHS, process.patJetPartonMatchAK15PFCHS]:
    module.matched='prunedGenParticles'

for module in [process.patJetCorrFactors, process.patJetCorrFactorsAK4PFCHS, process.patJetCorrFactorsAK8PFCHS, process.patJetCorrFactorsAK10PFCHS, process.patJetCorrFactorsAK12PFCHS, process.patJetCorrFactorsAK15PFCHS]:
    module.primaryVertices = 'offlineSlimmedPrimaryVertices'

process.load('RecoBTag.Configuration.RecoBTag_cff')
process.load('RecoJets.Configuration.RecoJetAssociations_cff')
process.load('PhysicsTools.PatAlgos.slimming.unpackedTracksAndVertices_cfi')
#process.load('CondCore.DBCommon.CondDBSetup_cfi')
#process.load('RecoBTag.SecondaryVertex.combinedSecondaryVertexES_cfi')
process.load('RecoBTag.SecondaryVertex.combinedSecondaryVertexBJetTags_cfi')

process.inclusiveCandidateVertexFinder.primaryVertices = 'offlineSlimmedPrimaryVertices'
process.inclusiveCandidateVertexFinder.tracks = 'packedPFCandidates'

process.candidateVertexArbitrator.primaryVertices = 'offlineSlimmedPrimaryVertices'
process.candidateVertexArbitrator.tracks = 'packedPFCandidates'

#process.inclusiveVertexFinder.primaryVertices='offlineSlimmedPrimaryVertices'
#process.inclusiveVertexFinder.tracks='unpackedTracksAndVertices'

#process.trackVertexArbitrator.primaryVertices='offlineSlimmedPrimaryVertices'
#process.trackVertexArbitrator.tracks='unpackedTracksAndVertices'

process.ak4JetTracksAssociatorAtVertexPF.jets = cms.InputTag('ak4PFJets')
process.ak4JetTracksAssociatorAtVertexPF.tracks = cms.InputTag('unpackedTracksAndVertices')

process.ak4JetTracksAssociatorAtVertexPFCHS=process.ak4JetTracksAssociatorAtVertexPF.clone(jets = cms.InputTag('ak4PFJetsCHS'), coneSize = 0.4)
process.ak8JetTracksAssociatorAtVertexPFCHS=process.ak4JetTracksAssociatorAtVertexPF.clone(jets = cms.InputTag('ak8PFJetsCHS'), coneSize = 0.8)
process.ak10JetTracksAssociatorAtVertexPFCHS=process.ak4JetTracksAssociatorAtVertexPF.clone(jets = cms.InputTag('ak10PFJetsCHS'), coneSize = 1)
process.ak12JetTracksAssociatorAtVertexPFCHS=process.ak4JetTracksAssociatorAtVertexPF.clone(jets = cms.InputTag('ak12PFJetsCHS'), coneSize = 1.2)
process.ak15JetTracksAssociatorAtVertexPFCHS=process.ak4JetTracksAssociatorAtVertexPF.clone(jets = cms.InputTag('ak15PFJetsCHS'), coneSize = 1.5)

#These may be important
#process.impactParameterTagInfos.primaryVertex = cms.InputTag('unpackedTracksAndVertices')
#process.inclusiveSecondaryVertexFinderTagInfos.extSVCollection = cms.InputTag('unpackedTracksAndVertices','secondary','')

#process.pfCombinedInclusiveSecondaryVertexV2.trackMultiplicityMin = 1

#process.secondaryVertexTagInfosAK4PFCHS.trackSelection.jetDeltaRMax = 0.4
#process.secondaryVertexTagInfosAK4PFCHS.vertexCuts.maxDeltaRToJetAxis = 0.4
#process.pfCombinedInclusiveSecondaryVertexV2AK4PFCHS=process.pfCombinedInclusiveSecondaryVertexV2.clone()
#process.pfCombinedInclusiveSecondaryVertexV2AK4PFCHS.trackSelection.jetDeltaRMax = 0.4
#process.pfCombinedInclusiveSecondaryVertexV2AK4PFCHS.trackPseudoSelection.jetDeltaRMax = 0.4
#process.combinedInclusiveSecondaryVertexV2BJetTagsAK4PFCHS.jetTagComputer = 'pfCombinedInclusiveSecondaryVertexV2AK4PFCHS'

from RecoJets.JetProducers.SubJetParameters_cfi import SubJetParameters


addJetCollection(
    process,
    labelName = 'AK8PFCHSFiltered',
    jetSource = cms.InputTag('ak8PFJetsCHSFiltered'),
    jetCorrections = ('AK8PFchs', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute']), 'None'),
    trackSource = cms.InputTag('unpackedTracksAndVertices'),
    pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
    svSource = cms.InputTag('slimmedSecondaryVertices'),
    pfCandidates = cms.InputTag('packedPFCandidates'),
    btagDiscriminators = ['pfCombinedSecondaryVertexBJetTags', 'pfCombinedInclusiveSecondaryVertexV2BJetTags'],
    genJetCollection=cms.InputTag('ak4GenJets'),
    getJetMCFlavour = False
    )

addJetCollection(
    process,
    labelName = 'AK8PFCHSFilteredSubjets',
    jetSource = cms.InputTag('ak8PFJetsCHSFiltered','SubJets'),
    jetCorrections = ('AK8PFchs', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute']), 'None'),
    trackSource = cms.InputTag('unpackedTracksAndVertices'),
    pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
    svSource = cms.InputTag('slimmedSecondaryVertices'),
    pfCandidates = cms.InputTag('packedPFCandidates'),
    btagDiscriminators = ['pfCombinedSecondaryVertexBJetTags', 'pfCombinedInclusiveSecondaryVertexV2BJetTags'],
    genJetCollection=cms.InputTag('ak4GenJets'),
    getJetMCFlavour = False,
    )

process.patJetsAK8PFCHSFilteredPacked = cms.EDProducer("BoostedJetMerger",
                                                       jetSrc=cms.InputTag("patJetsAK8PFCHSFiltered" ),
                                                       subjetSrc=cms.InputTag("patJetsAK8PFCHSFilteredSubjets")
                                                       )
addJetCollection(
    process,
    labelName = 'AK10PFCHSFiltered',
    jetSource = cms.InputTag('ak10PFJetsCHSFiltered'),
    jetCorrections = ('AK10PFchs', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute']), 'None'),
    trackSource = cms.InputTag('unpackedTracksAndVertices'),
    pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
    svSource = cms.InputTag('slimmedSecondaryVertices'),
    pfCandidates = cms.InputTag('packedPFCandidates'),
    btagDiscriminators = ['pfCombinedSecondaryVertexBJetTags', 'pfCombinedInclusiveSecondaryVertexV2BJetTags'],
    genJetCollection=cms.InputTag('ak4GenJets'),
    getJetMCFlavour = False
    )                                                  

addJetCollection(
    process,
    labelName = 'AK10PFCHSFilteredSubjets',
    jetSource = cms.InputTag('ak10PFJetsCHSFiltered','SubJets'),
    jetCorrections = ('AK10PFchs', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute']), 'None'),
    trackSource = cms.InputTag('unpackedTracksAndVertices'),
    pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
    svSource = cms.InputTag('slimmedSecondaryVertices'),
    pfCandidates = cms.InputTag('packedPFCandidates'),
    btagDiscriminators = ['pfCombinedSecondaryVertexBJetTags', 'pfCombinedInclusiveSecondaryVertexV2BJetTags'],
    genJetCollection=cms.InputTag('ak4GenJets'),
    getJetMCFlavour = False,
    )

process.patJetsAK10PFCHSFilteredPacked = cms.EDProducer("BoostedJetMerger",
                                                        jetSrc=cms.InputTag("patJetsAK10PFCHSFiltered" ),
                                                        subjetSrc=cms.InputTag("patJetsAK10PFCHSFilteredSubjets")
                                                        )

addJetCollection(
    process,
    labelName = 'AK12PFCHSFiltered',
    jetSource = cms.InputTag('ak12PFJetsCHSFiltered'),
    jetCorrections = ('AK10PFchs', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute']), 'None'),
    trackSource = cms.InputTag('unpackedTracksAndVertices'),
    pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
    svSource = cms.InputTag('slimmedSecondaryVertices'),
    pfCandidates = cms.InputTag('packedPFCandidates'),
    btagDiscriminators = ['pfCombinedSecondaryVertexBJetTags', 'pfCombinedInclusiveSecondaryVertexV2BJetTags'],
    genJetCollection=cms.InputTag('ak4GenJets'),
    getJetMCFlavour = False
    )

addJetCollection(
    process,
    labelName = 'AK12PFCHSFilteredSubjets',
    jetSource = cms.InputTag('ak12PFJetsCHSFiltered','SubJets'),
    jetCorrections = ('AK10PFchs', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute']), 'None'),
    trackSource = cms.InputTag('unpackedTracksAndVertices'),
    pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
    svSource = cms.InputTag('slimmedSecondaryVertices'),
    pfCandidates = cms.InputTag('packedPFCandidates'),
    btagDiscriminators = ['pfCombinedSecondaryVertexBJetTags', 'pfCombinedInclusiveSecondaryVertexV2BJetTags'],
    genJetCollection=cms.InputTag('ak4GenJets'),
    getJetMCFlavour = False,
    )

process.patJetsAK12PFCHSFilteredPacked = cms.EDProducer("BoostedJetMerger",
                                                        jetSrc=cms.InputTag("patJetsAK12PFCHSFiltered" ),
                                                        subjetSrc=cms.InputTag("patJetsAK12PFCHSFilteredSubjets")
                                                        )

addJetCollection(
    process,
    labelName = 'AK15PFCHSFiltered',
    jetSource = cms.InputTag('ak15PFJetsCHSFiltered'),
    jetCorrections = ('AK10PFchs', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute']), 'None'),
    trackSource = cms.InputTag('unpackedTracksAndVertices'),
    pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
    svSource = cms.InputTag('slimmedSecondaryVertices'),
    pfCandidates = cms.InputTag('packedPFCandidates'),
    btagDiscriminators = ['pfCombinedSecondaryVertexBJetTags', 'pfCombinedInclusiveSecondaryVertexV2BJetTags'],
    genJetCollection=cms.InputTag('ak4GenJets'),
    getJetMCFlavour = False
    )

addJetCollection(
    process,
    labelName = 'AK15PFCHSFilteredSubjets',
    jetSource = cms.InputTag('ak15PFJetsCHSFiltered','SubJets'),
    jetCorrections = ('AK10PFchs', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute']), 'None'),
    trackSource = cms.InputTag('unpackedTracksAndVertices'),
    pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
    svSource = cms.InputTag('slimmedSecondaryVertices'),
    pfCandidates = cms.InputTag('packedPFCandidates'),
    btagDiscriminators = ['pfCombinedSecondaryVertexBJetTags', 'pfCombinedInclusiveSecondaryVertexV2BJetTags'],
    genJetCollection=cms.InputTag('ak4GenJets'),
    getJetMCFlavour = False,
    )

process.patJetsAK15PFCHSFilteredPacked = cms.EDProducer("BoostedJetMerger",
                                                        jetSrc=cms.InputTag("patJetsAK15PFCHSFiltered" ),
                                                        subjetSrc=cms.InputTag("patJetsAK15PFCHSFilteredSubjets")
                                                        )

for module in [process.patJetPartonMatchAK8PFCHSFiltered, process.patJetPartonMatchAK10PFCHSFiltered, process.patJetPartonMatchAK12PFCHSFiltered, process.patJetPartonMatchAK15PFCHSFiltered,
               process.patJetPartonMatchAK8PFCHSFilteredSubjets, process.patJetPartonMatchAK10PFCHSFilteredSubjets, process.patJetPartonMatchAK12PFCHSFilteredSubjets, process.patJetPartonMatchAK15PFCHSFilteredSubjets]:
    module.matched='prunedGenParticles'

for module in [process.patJetCorrFactorsAK8PFCHSFiltered, process.patJetCorrFactorsAK10PFCHSFiltered, process.patJetCorrFactorsAK12PFCHSFiltered, process.patJetCorrFactorsAK15PFCHSFiltered,
               process.patJetCorrFactorsAK8PFCHSFilteredSubjets, process.patJetCorrFactorsAK10PFCHSFilteredSubjets, process.patJetCorrFactorsAK12PFCHSFilteredSubjets, process.patJetCorrFactorsAK15PFCHSFilteredSubjets]:
    module.primaryVertices = 'offlineSlimmedPrimaryVertices'
    
for module in [process.patJetGenJetMatchAK8PFCHSFiltered, process.patJetGenJetMatchAK10PFCHSFiltered, process.patJetGenJetMatchAK12PFCHSFiltered, process.patJetGenJetMatchAK15PFCHSFiltered,
               process.patJetGenJetMatchAK8PFCHSFilteredSubjets, process.patJetGenJetMatchAK10PFCHSFilteredSubjets, process.patJetGenJetMatchAK12PFCHSFilteredSubjets, process.patJetGenJetMatchAK15PFCHSFilteredSubjets]:
    module.matched = 'ak3GenJets'


#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

process.selectedPatJetsAK4PFCHS = cms.EDFilter("PATJetSelector",
                                               src = cms.InputTag("patJetsAK4PFCHS"),
                                               cut = cms.string("pt > 20.0 &"
                                                                "abs(eta) < 2.5")
                                               )
process.selectedPatJetsAK8PFCHS =process.selectedPatJetsAK4PFCHS.clone(cut="pt > 150.0", src="patJetsAK8PFCHS")
process.selectedPatJetsAK10PFCHS=process.selectedPatJetsAK4PFCHS.clone(cut="pt > 150.0", src="patJetsAK10PFCHS")
process.selectedPatJetsAK12PFCHS=process.selectedPatJetsAK4PFCHS.clone(cut="pt > 150.0", src="patJetsAK12PFCHS")
process.selectedPatJetsAK15PFCHS=process.selectedPatJetsAK4PFCHS.clone(cut="pt > 150.0", src="patJetsAK15PFCHS")

process.selectedPatJetsAK8PFCHSFilteredPacked =process.selectedPatJetsAK4PFCHS.clone(cut="pt > 150.0", src="patJetsAK8PFCHSFilteredPacked")
process.selectedPatJetsAK10PFCHSFilteredPacked=process.selectedPatJetsAK4PFCHS.clone(cut="pt > 150.0", src="patJetsAK10PFCHSFilteredPacked")
process.selectedPatJetsAK12PFCHSFilteredPacked=process.selectedPatJetsAK4PFCHS.clone(cut="pt > 150.0", src="patJetsAK12PFCHSFilteredPacked")
process.selectedPatJetsAK15PFCHSFilteredPacked=process.selectedPatJetsAK4PFCHS.clone(cut="pt > 150.0", src="patJetsAK15PFCHSFilteredPacked")

from PhysicsTools.SelectorUtils.pfJetIDSelector_cfi import pfJetIDSelector
process.goodPatJetsAK4PFCHS = cms.EDFilter("PFJetIDSelectionFunctorFilter",
                                           filterParams = pfJetIDSelector.clone(),
                                           src = cms.InputTag("selectedPatJetsAK4PFCHS")
                                           )
process.goodPatJetsAK8PFCHS=process.goodPatJetsAK4PFCHS.clone(src="selectedPatJetsAK8PFCHS")
process.goodPatJetsAK10PFCHS=process.goodPatJetsAK4PFCHS.clone(src="selectedPatJetsAK10PFCHS")
process.goodPatJetsAK12PFCHS=process.goodPatJetsAK4PFCHS.clone(src="selectedPatJetsAK12PFCHS")
process.goodPatJetsAK15PFCHS=process.goodPatJetsAK4PFCHS.clone(src="selectedPatJetsAK15PFCHS")

process.goodPatJetsAK8PFCHSFilteredPacked =process.goodPatJetsAK4PFCHS.clone(src="selectedPatJetsAK8PFCHSFilteredPacked")
process.goodPatJetsAK10PFCHSFilteredPacked=process.goodPatJetsAK4PFCHS.clone(src="selectedPatJetsAK10PFCHSFilteredPacked")
process.goodPatJetsAK12PFCHSFilteredPacked=process.goodPatJetsAK4PFCHS.clone(src="selectedPatJetsAK12PFCHSFilteredPacked")
process.goodPatJetsAK15PFCHSFilteredPacked=process.goodPatJetsAK4PFCHS.clone(src="selectedPatJetsAK15PFCHSFilteredPacked")

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#JECs for telescoping

process.load('JetMETCorrections/Configuration/JetCorrectionServices_cff')
#process.load('JetMETCorrections/Configuration/JetCorrectionProducers_cff')

#L1Offset correction is bad, we want L1Fastjet
process.ak1PFchsL1Fastjet   = process.ak4PFCHSL1Fastjet.clone( algorithm = 'AK1PFchs' )
process.ak2PFchsL1Fastjet   = process.ak4PFCHSL1Fastjet.clone( algorithm = 'AK2PFchs' )
process.ak3PFchsL1Fastjet   = process.ak4PFCHSL1Fastjet.clone( algorithm = 'AK3PFchs' )
process.ak4PFchsL1Fastjet   = process.ak4PFCHSL1Fastjet.clone( algorithm = 'AK4PFchs' )
process.ak5PFchsL1Fastjet   = process.ak4PFCHSL1Fastjet.clone( algorithm = 'AK5PFchs' )
process.ak6PFchsL1Fastjet   = process.ak4PFCHSL1Fastjet.clone( algorithm = 'AK6PFchs' )
process.ak7PFchsL1Fastjet   = process.ak4PFCHSL1Fastjet.clone( algorithm = 'AK7PFchs' )
process.ak8PFchsL1Fastjet   = process.ak4PFCHSL1Fastjet.clone( algorithm = 'AK8PFchs' )
process.ak9PFchsL1Fastjet   = process.ak4PFCHSL1Fastjet.clone( algorithm = 'AK9PFchs' )
process.ak10PFchsL1Fastjet  = process.ak4PFCHSL1Fastjet.clone( algorithm = 'AK10PFchs')

process.ak1PFchsL2Relative  = process.ak4PFCHSL2Relative.clone( algorithm = 'AK1PFchs' )
process.ak2PFchsL2Relative  = process.ak4PFCHSL2Relative.clone( algorithm = 'AK2PFchs' )
process.ak3PFchsL2Relative  = process.ak4PFCHSL2Relative.clone( algorithm = 'AK3PFchs' )
process.ak4PFchsL2Relative  = process.ak4PFCHSL2Relative.clone( algorithm = 'AK4PFchs' )
process.ak5PFchsL2Relative  = process.ak4PFCHSL2Relative.clone( algorithm = 'AK5PFchs' )
process.ak6PFchsL2Relative  = process.ak4PFCHSL2Relative.clone( algorithm = 'AK6PFchs' )
process.ak7PFchsL2Relative  = process.ak4PFCHSL2Relative.clone( algorithm = 'AK7PFchs' )
process.ak8PFchsL2Relative  = process.ak4PFCHSL2Relative.clone( algorithm = 'AK8PFchs' )
process.ak9PFchsL2Relative  = process.ak4PFCHSL2Relative.clone( algorithm = 'AK9PFchs' )
process.ak10PFchsL2Relative = process.ak4PFCHSL2Relative.clone( algorithm = 'AK10PFchs')

process.ak1PFCHSL3Absolute  = process.ak4PFCHSL3Absolute.clone( algorithm = 'AK1PFchs' )
process.ak2PFCHSL3Absolute  = process.ak4PFCHSL3Absolute.clone( algorithm = 'AK2PFchs' )
process.ak3PFCHSL3Absolute  = process.ak4PFCHSL3Absolute.clone( algorithm = 'AK3PFchs' )
process.ak4PFCHSL3Absolute  = process.ak4PFCHSL3Absolute.clone( algorithm = 'AK4PFchs' )
process.ak5PFCHSL3Absolute  = process.ak4PFCHSL3Absolute.clone( algorithm = 'AK5PFchs' )
process.ak6PFCHSL3Absolute  = process.ak4PFCHSL3Absolute.clone( algorithm = 'AK6PFchs' )
process.ak7PFCHSL3Absolute  = process.ak4PFCHSL3Absolute.clone( algorithm = 'AK7PFchs' )
process.ak8PFCHSL3Absolute  = process.ak4PFCHSL3Absolute.clone( algorithm = 'AK8PFchs' )
process.ak9PFCHSL3Absolute  = process.ak4PFCHSL3Absolute.clone( algorithm = 'AK9PFchs' )
process.ak10PFCHSL3Absolute = process.ak4PFCHSL3Absolute.clone( algorithm = 'AK10PFchs')

process.ak1PFCHSL1L2L3      = process.ak4PFCHSL1L2L3.clone( correctors = ['ak1PFchsL1Fastjet', 'ak1PFchsL2Relative', 'ak1PFCHSL3Absolute'] )
process.ak2PFCHSL1L2L3      = process.ak4PFCHSL1L2L3.clone( correctors = ['ak2PFchsL1Fastjet', 'ak2PFchsL2Relative', 'ak2PFCHSL3Absolute'] )
process.ak3PFCHSL1L2L3      = process.ak4PFCHSL1L2L3.clone( correctors = ['ak3PFchsL1Fastjet', 'ak3PFchsL2Relative', 'ak3PFCHSL3Absolute'] )
process.ak4PFCHSL1L2L3      = process.ak4PFCHSL1L2L3.clone( correctors = ['ak4PFchsL1Fastjet', 'ak4PFchsL2Relative', 'ak4PFCHSL3Absolute'] )
process.ak5PFCHSL1L2L3      = process.ak4PFCHSL1L2L3.clone( correctors = ['ak5PFchsL1Fastjet', 'ak5PFchsL2Relative', 'ak5PFCHSL3Absolute'] )
process.ak6PFCHSL1L2L3      = process.ak4PFCHSL1L2L3.clone( correctors = ['ak6PFchsL1Fastjet', 'ak6PFchsL2Relative', 'ak6PFCHSL3Absolute'] )
process.ak7PFCHSL1L2L3      = process.ak4PFCHSL1L2L3.clone( correctors = ['ak7PFchsL1Fastjet', 'ak7PFchsL2Relative', 'ak7PFCHSL3Absolute'] )
process.ak8PFCHSL1L2L3      = process.ak4PFCHSL1L2L3.clone( correctors = ['ak8PFchsL1Fastjet', 'ak8PFchsL2Relative', 'ak8PFCHSL3Absolute'] )
process.ak9PFCHSL1L2L3      = process.ak4PFCHSL1L2L3.clone( correctors = ['ak9PFchsL1Fastjet', 'ak9PFchsL2Relative', 'ak9PFCHSL3Absolute'] )
process.ak10PFCHSL1L2L3     = process.ak4PFCHSL1L2L3.clone( correctors = ['ak10PFchsL1Fastjet','ak10PFchsL2Relative','ak10PFCHSL3Absolute'])

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
#process.load('RecoJets.JetProducers.jettoolbox_cff')
"""
process.NjettinessAK10=process.NjettinessAK8.clone(src="ak10PFJetsCHS", cone=1.0)
process.NjettinessAK12=process.NjettinessAK8.clone(src="ak12PFJetsCHS", cone=1.2)
process.NjettinessAK15=process.NjettinessAK8.clone(src="ak15PFJetsCHS", cone=1.5)

process.RandomNumberGeneratorService=process.RandomNumberGeneratorService.clone(QJetsAdderAK10 = cms.PSet(initialSeed = cms.untracked.uint32(14)),
                                                                                QJetsAdderAK12 = cms.PSet(initialSeed = cms.untracked.uint32(31)),
                                                                                QJetsAdderAK15 = cms.PSet(initialSeed = cms.untracked.uint32(420)))

process.QJetsAdderAK10=process.QJetsAdderAK8.clone(src="ak10PFJetsCHS", jetRad=1.0)
process.QJetsAdderAK12=process.QJetsAdderAK8.clone(src="ak12PFJetsCHS", jetRad=1.2)
process.QJetsAdderAK15=process.QJetsAdderAK8.clone(src="ak15PFJetsCHS", jetRad=1.5)

process.AK8PFJetsCHSPrunedLinks=process.ak8PFJetsCHSPrunedLinks.clone()
process.AK10PFJetsCHSPrunedLinks=process.AK8PFJetsCHSPrunedLinks.clone(src="ak10PFJetsCHS", matched="ak10PFJetsCHSPruned", distMax=1.0)
process.AK12PFJetsCHSPrunedLinks=process.AK8PFJetsCHSPrunedLinks.clone(src="ak12PFJetsCHS", matched="ak12PFJetsCHSPruned", distMax=1.2)
process.AK15PFJetsCHSPrunedLinks=process.AK8PFJetsCHSPrunedLinks.clone(src="ak15PFJetsCHS", matched="ak15PFJetsCHSPruned", distMax=1.5)

process.AK8PFJetsCHSTrimmedLinks=process.ak8PFJetsCHSTrimmedLinks.clone()
process.AK10PFJetsCHSTrimmedLinks=process.AK8PFJetsCHSTrimmedLinks.clone(src="ak10PFJetsCHS", matched="ak10PFJetsCHSTrimmed", distMax=1.0)
process.AK12PFJetsCHSTrimmedLinks=process.AK8PFJetsCHSTrimmedLinks.clone(src="ak12PFJetsCHS", matched="ak12PFJetsCHSTrimmed", distMax=1.2)
process.AK15PFJetsCHSTrimmedLinks=process.AK8PFJetsCHSTrimmedLinks.clone(src="ak15PFJetsCHS", matched="ak15PFJetsCHSTrimmed", distMax=1.5)

process.AK8PFJetsCHSFilteredLinks=process.ak8PFJetsCHSFilteredLinks.clone()
process.AK10PFJetsCHSFilteredLinks=process.AK8PFJetsCHSFilteredLinks.clone(src="ak10PFJetsCHS", matched="ak10PFJetsCHSFiltered", distMax=1.0)
process.AK12PFJetsCHSFilteredLinks=process.AK8PFJetsCHSFilteredLinks.clone(src="ak12PFJetsCHS", matched="ak12PFJetsCHSFiltered", distMax=1.2)
process.AK15PFJetsCHSFilteredLinks=process.AK8PFJetsCHSFilteredLinks.clone(src="ak15PFJetsCHS", matched="ak15PFJetsCHSFiltered", distMax=1.5)

process.patJetsAK8PFCHS.userData.userFloats.src += ['NjettinessAK8:tau1','NjettinessAK8:tau2','NjettinessAK8:tau3',
                                                    'QJetsAdderAK8:QjetsVolatility',
                                                    'AK8PFJetsCHSPrunedLinks','AK8PFJetsCHSTrimmedLinks','AK8PFJetsCHSFilteredLinks']

process.patJetsAK10PFCHS.userData.userFloats.src += ['NjettinessAK10:tau1','NjettinessAK10:tau2','NjettinessAK10:tau3',
                                                    'QJetsAdderAK10:QjetsVolatility',
                                                    'AK10PFJetsCHSPrunedLinks','AK10PFJetsCHSTrimmedLinks','AK10PFJetsCHSFilteredLinks']

process.patJetsAK12PFCHS.userData.userFloats.src += ['NjettinessAK12:tau1','NjettinessAK12:tau2','NjettinessAK12:tau3',
                                                    'QJetsAdderAK12:QjetsVolatility',
                                                    'AK12PFJetsCHSPrunedLinks','AK12PFJetsCHSTrimmedLinks','AK12PFJetsCHSFilteredLinks']

process.patJetsAK15PFCHS.userData.userFloats.src += ['NjettinessAK15:tau1','NjettinessAK15:tau2','NjettinessAK15:tau3',
                                                    'QJetsAdderAK15:QjetsVolatility',
                                                    'AK15PFJetsCHSPrunedLinks','AK15PFJetsCHSTrimmedLinks','AK15PFJetsCHSFilteredLinks']
"""
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                                                             
process.load('FWCore.MessageLogger.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 10
process.MessageLogger.suppressWarning = cms.untracked.vstring('ecalLaserCorrFilter','manystripclus53X','toomanystripclus53X')
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
process.options.allowUnscheduled = cms.untracked.bool(True)

process.out = cms.OutputModule("PoolOutputModule",
                               fileName = cms.untracked.string('Hbb.root'),
                               outputCommands = cms.untracked.vstring(['keep *_HbbProducer_*_*',
                                                                       ])
)

process.end = cms.EndPath(process.out)

#  LocalWords:  pfNoMuonCHS
