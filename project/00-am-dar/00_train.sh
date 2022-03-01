#!/bin/bash
########################
# Usage:
#   1. please check that config.py has been properly configured
#   2. $: bash 00_train.sh > /dev/null 2>&1 &
#   3. please check log_train and log_err to monitor the training 
#      process
#   
########################

export PYTHONPATH=$PWD/../../:$PYTHONPATH

#config_file="/home/bsrivast/nijta/pytorch-nii/project-NN-Pytorch-scripts/project/00-am-dar/config_libritts100.py"

TEMP_TESTSET_NAME="dataset_libritts100_test"
TEMP_TESTSET_DIR="/home/bsrivast/nijta/pytorch-nii/exp/am_nsf_data_pytorch_16k/test_libritts_16k"
TEMP_TESTSET_LST="${TEMP_TESTSET_DIR}/../train_libritts_16k/scp/test.lst"
TEMP_TESTSET_PPG="${TEMP_TESTSET_DIR}/ppg"
TEMP_TESTSET_XVEC="${TEMP_TESTSET_DIR}/xvector"
TEMP_TESTSET_F0="${TEMP_TESTSET_DIR}/f0"

model_out_dir="models/libritts100"
mkdir -p ${model_out_dir}

log_train_name=${model_out_dir}/log_train_libritts100
log_err_name=${model_out_dir}/log_err_libritts100


python main.py --sampler block_shuffle_by_length \
	--model-forward-with-target --num-workers 3 \
	--epochs 200 --no-best-epochs 50 --batch-size 32 \
	--optimizer AdamW --lr 0.0001 --shuffle --seed 1000 \
	--model-forward-with-file-name \
	--cudnn-deterministic-toggle \
	--cudnn-benchmark-toggle \
	--save-trained-name ${model_out_dir}/trained_model \
	--save-model-ext ".pth" >${log_train_name} 2>${log_err_name}

	#--module-config ${config_file} >${log_train_name} 2>${log_err_name}
