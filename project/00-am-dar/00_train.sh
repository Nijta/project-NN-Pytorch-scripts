#!/bin/bash
########################
# Usage:
#   1. please check that config.py has been properly configured
#   2. $: bash 00_train.sh > /dev/null 2>&1 &
#   3. please check log_train and log_err to monitor the training 
#      process
#   
########################

log_train_name=log_train
log_err_name=log_err

python main.py --sampler block_shuffle_by_length --model-forward-with-target --num-workers 3 --epochs 200 --no-best-epochs 50 --batch-size 32 --optimizer AdamW --lr 0.0001 --shuffle --seed 1000 --model-forward-with-file-name --cudnn-deterministic-toggle --cudnn-benchmark-toggle >${log_train_name} 2>${log_err_name}
