def get_mnist():
	import cPickle, gzip, numpy
	import os

	path = os.environ['DATASETS_PATH']
	path += '/mnist/'
	# Load the dataset
	f = gzip.open(path+'mnist.pkl.gz', 'rb')
	train_set, valid_set, test_set = cPickle.load(f)
	f.close()

	return (train_set, valid_set, test_set)