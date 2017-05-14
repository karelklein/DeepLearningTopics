## Blog-style post
- An unanimated pdf is available: GANs.pdf
- Corresponding python notebook: GANs.ipynb

## Code
- To run the GAN, simply run on command line:
	- python gan.py
- To save D an G losses, redirect output:
	- python gan.py > losses.txt
- To produce loss plots, run:
	- python plotloss.py <losses_file>

## Dependencies
- tensorflow
- numpy
- matplotlib

## Data
- MNIST data is automatically downloaded when running gan.py using the statement:
	- from tensorflow.examples.tutorials.mnist import input_data
- a copy of this data is stored in data/
