import math
from gaussian import Gaussian


filepath = 'data/sample_weights.txt'

my_gaussian = Gaussian(140, 40)
my_gaussian.read_data_file(filepath,sample=True)



