#!/bin/bash
trained=trained_network.pt

rm dataset_vc2022_test_utt_length.dic
# copy synthesis using PPG in this directory
export TEMP_PPG=/home/smg/miao/voice_priacy/Voice-Privacy-Challenge-2020-master/baseline/exp/models/1_asr_am/exp/nnet3_cleaned/ppg_train-clean-100/ppg; python main.py --inference --module-config config_test --output-dir output --trained-model ${trained}                    
  
#rm dataset_vc2022_test_utt_length.dic
#export TEMP_PPG=/home/smg/wang/WORK/WORK/WORK/voice-privacy-challenge-2019/train/DATA/tmp; python main.py --inference --module-config config_test --output-dir output-orig-ppg --trained-model ${trained}

