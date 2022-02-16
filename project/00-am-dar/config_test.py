#!/usr/bin/env python
"""
config.py

To merge different corpora (or just one corpus), 

*_set_name are lists
*_list are lists of lists
*_dirs are lists of lists

"""

__author__ = "Xin Wang"
__email__ = "wangxin@nii.ac.jp"
__copyright__ = "Copyright 2020, Xin Wang"

#########################################################
## Configuration for training stage
#########################################################

# Name of datasets
#  after data preparation, trn/val_set_name are used to save statistics 
#  about the data sets
trn_set_name = ['dataset_vc2022_trn']
val_set_name = ['dataset_vc2022_val']

# for convenience
tmp = '/home/smg/wang/WORK/WORK/WORK/voice-privacy-challenge-2022/baseline1/data'

# File lists (text file, one data name per line, without name extension)
# trin_file_list: list of files for training set
trn_list = [tmp + '/scp/train.lst']
# val_file_list: list of files for validation set. It can be None
val_list = [tmp + '/scp/dev.lst']

# Directories for input features
# input_dirs = [path_of_feature_1, path_of_feature_2, ..., ]
#  we assume train and validation data are put in the same sub-directory
input_dirs = [[tmp + '/ppg', tmp + '/xvector', tmp + '/f0']]

# Dimensions of input features
# input_dims = [dimension_of_feature_1, dimension_of_feature_2, ...]
input_dims = [256, 512, 1]

# File name extension for input features
# input_exts = [name_extention_of_feature_1, ...]
# Please put ".f0" as the last feature
input_exts = ['.ppg', '.xvector', '.f0']

# Temporal resolution for input features
# input_reso = [reso_feature_1, reso_feature_2, ...]
#  for waveform modeling, temporal resolution of input acoustic features
#  may be = waveform_sampling_rate * frame_shift_of_acoustic_features
#  for example, 80 = 16000 Hz * 5 ms 
input_reso = [1, 1, 1]

# Whether input features should be z-normalized
# input_norm = [normalize_feature_1, normalize_feature_2]
input_norm = [True, True, True]
    
# Similar configurations for output features
output_dirs = [[tmp + '/mel']]
output_dims = [80]
output_exts = ['.mel']
output_reso = [1]
output_norm = [True]

# Waveform sampling rate
#  wav_samp_rate can be None if no waveform data is used
wav_samp_rate = None

# Truncating input sequences so that the maximum length = truncate_seq
#  When truncate_seq is larger, more GPU mem required
# If you don't want truncating, please truncate_seq = None
truncate_seq = None

# Minimum sequence length
#  If sequence length < minimum_len, this sequence is not used for training
#  minimum_len can be None
minimum_len = None
    
# Optional argument
#  Just a buffer for convenience
#  It can contain anything
optional_argument = ['']

# Data transformation function, you can import here
#  these functions are applied before casting np.array data into tensor arrays
#  
#input_trans_fns = [[func_for_mel, fun_for_f0]]
#output_trans_fns = [[func_for_wav]]


#########################################################
## Configuration for inference stage
#########################################################
# similar options to training stage

import os

test_set_name = ['dataset_vc2022_test']

# List of test set data
# for convenience, you may directly load test_set list here
test_list = [['1040_133433_000019_000000', '1088_134315_000068_000000', 
              '1098_133695_000014_000003', '1183_133256_000077_000000']]

# Directories for input features
# input_dirs = [path_of_feature_1, path_of_feature_2, ..., ]
#  we assume train and validation data are put in the same sub-directory
test_input_dirs = input_dirs
test_input_dirs[0][0] = os.getenv('TEMP_PPG')

# Directories for output features, which are []
test_output_dirs = output_dirs


# Data transformation function, you can import here
#  these functions are applied before casting np.array data into tensor arrays
#
#test_input_trans_fns = [[func_for_mel, fun_for_f0]]
#test_output_trans_fns = [[func_for_wav]]
