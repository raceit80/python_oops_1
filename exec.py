import math
import matplotlib.pyplot as plt
from gaussian import Gaussian


filepath = 'data/sample_weights.txt'

my_gaussian = Gaussian(100, 10)
my_gaussian.read_data_file(filepath,sample=True)
print("Standard deviation of sample is {}". format(my_gaussian.calculate_stdev(sample=True)))
print("Standard deviation of population is {}". format(my_gaussian.calculate_stdev(sample=False)))
print("Mean of sample is {}". format(my_gaussian.calculate_mean()))

print("PDF of value x= {} is {}".format(200.00, round(my_gaussian.pdf(200.00), 5)))

print("Plotting histogram of sample data \n")
my_gaussian.plot_histogram()

print("Plotting histogram of sample data and probility density fuction (pdf) \n")
my_gaussian.plot_histogram_pdf()