# -*- coding: utf-8 -*-
class TestConfig:
    buckets=[(10,10),(15,15),(20,20),(40,40)]
    steps_per_checkpoint=20
    max_step=100
    max_vocabulary_size=10000
    
    
    size= 12
    num_layers=1
    max_gradient_norm=5.0
    batch_size=64
    learning_rate=0.5
    leraing_rate_decay_factor=0.59
    
    use_Istm=False
    use_rms_prop=False
    
    
class DefaultPtConfig():
    buckets=[(10,10),(15,15),(20,20),(40,40)]
    steps_per_checkpoint=100
    max_steps=20000
    
    
     

