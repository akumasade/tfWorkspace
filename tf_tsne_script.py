import numpy as np
import matplotlib.pyplot as plt
#import pyfits
from astropy.io import fits

hdulist = fits.open('./Hewett_090816_matchDR7all_wclusters_weightsonly.fits')
#print hdulist[1].data.tolist()
data = np.asarray(hdulist[1].data.tolist())
#X = data[:20000]
X = data
print X.shape
print X

import tensorflow as tf
import os
from tensorflow.contrib.tensorboard.plugins import projector
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

LOG_DIR = 'Hewett_tsne'

embedding_var = tf.Variable(tf.truncated_normal([9, 3]), name='embedding')
data = tf.Variable(X, name='Weights')



with tf.Session() as sess:
    saver = tf.train.Saver([data])

    sess.run(data.initializer)
    saver.save(sess, os.path.join(LOG_DIR, 'Hewett.ckpt'))
