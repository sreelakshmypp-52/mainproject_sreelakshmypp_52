# -*- coding: utf-8 -*-
class DefaultMovieDialogConfig():
    buckets=[(10,10),(15,15),(20,20),(40,40)]
    
    steps_per_checkpoint=100
    max_steps=20000
    
    max_vocabulary_size=2000
    
    size=512
    num_layers=4
    max_gradient_norm=5.0
    batch_size=64
    learning_rate=0.5
    learning_rate_decay_factor=0.99
    
    use_Istm=True
    use_rms_prop=False
    
    projection_bias=0.0

