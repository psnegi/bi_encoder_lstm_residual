MAX_SENTENCE_LEN = 160
EMBED_LEN = 300
EMBED_FILE = 'data/glove.42B.300d.txt' #  also change the EMBED_LEN when changing this
TRAIN_BATCH_SIZE = 256
VALIDATION_BATCH_SIZE = 16
TRAIN_FILES = ['data/train.tfrecords']
VALIDATION_FILES = ['data/validation_v1.tfrecords']
NUM_EPOCHS = 2
CHECKPOINT_FILE = 'checkpoints/390.ckpt'
VOCABULARY = 'data/vocabulary.json'
