# bi_encoder_lstm

# To train:
python driver.py --train
# To test:
python driver.py --test checkpoints/my_model.ckpt"""

#@TODO
- [ ] Add better optimizer. Need to reduce rate when loss doesn't reduce
- [ ] May be move to tensorflow.keras/keras to avoid biler plate code

# Change log
- 30 Nov/1 Dec added 2 layer LSTM with residual connection. 
input_lstm2= output_lstm1+M@input_lstm1