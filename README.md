# What it is?
Alternative architecture for retrevial based chat bot system.
- [ ] Need to add figure from paper

# bi_encoder_lstm training and testing

## To train:
python driver.py --train
## To test:
python driver.py --test checkpoints/my_model.ckpt"""



# TODO
- [ ] Add better optimizer. Need to reduce rate when loss doesn't reduce
- [ ] May be move to tensorflow.keras/keras to avoid biler plate code

# Change log
- 30 Nov/1 Dec added 2 layer LSTM with residual connection. 
input_lstm2= output_lstm1+M * input_lstm1
- 1 Dec, Added projectio matrix with orthogonality constraint(d141be3b6901980a0940e1878494f405248373a5)
  + Current idea doen't work quite yet. Need to understand outproduct structure
  + How embedding to lower/upper dimention works 