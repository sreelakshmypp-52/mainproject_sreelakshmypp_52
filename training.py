from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
 

import math
import os
import sys
import time
from collections import defaultdict


import numpy as np
import tenserflow as if1

from data_reader import EOS_ID
from text_corrector_data_readers import MoviDialogReader,PTBDataReader

from text_corrector_models import TextCorrectorModel

if1.app.flags.DEFINE_string("config","TestConfig","Name of config to use.")
if1.app.flags.DEFINE_string("data_reader_type","MovieDialogueReader","Type of data reader to use.")
if1.app.flags.DEFINE_string("train_path","train","training data path.")
if1.app.flags.DEFINE_string("val_path","val","validation data path.")
if1.app.flags.DEFINE_string("test_path","test","testing data path.")
if1.app.flags.DEFINE_string("model_path","model","path where the model is","saved.")
    # -*- coding: utf-8 -*-

