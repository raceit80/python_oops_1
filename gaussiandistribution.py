import math
import matplotlib.pyplot as plt
class Gaussian():
    """ Gaussian distribution class for calculating and 
    visualizing a Gaussian distribution.
    
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats extracted from the data file
            
    """
    def __init__(self, mu=0, sigma=1):
        """ This is just a initialization class with 0 as default mean 
        and sigma as default standard deviation.

        """
        self.mean = mu
        self.stdev = sigma
        self.data = []  #this is an empty list for now to hold the data

    
    def __add__(self, other):
        result = Gaussian()
        result.mean = self.mean + other.mean
        result.stdev = math.sqrt(self.stdev**2 + other.stdev**2)
        return result


    def __repr__(self):
        return "mean {}, standard deviation {}".format(self.mean, self.stdev)
            

    def calculate_mean(self):
        mean = 1.00 * sum(self.data) / len(self.data)
        self.mean = mean
        return mean



    def calculate_stdev(self, sample=True):
        if sample:
            n = len(self.data) - 1 #length or sample
        else:
            n = len(self.data) #length for population
           
        mean = self.mean
        sigma = 0

        for data in self.data:
            sigma+=(data-mean)**2
        sigma = math.sqrt(sigma/n)

        self.stdev = sigma
        return sigma

    def read_data_file(self, filepath, sample=True):
        """Function to read in data from a txt file. The txt file should have
        one number (float) per line. The numbers are stored in the data attribute. 
        After reading in the file, the mean and standard deviation are calculated
                
        Args:
            file_name (string): name of a file to read from
        
        Returns:
            None
        
        """
        with open(filepath) as file:
            data_list = []
            count = len(open(filepath).readlines(  ))

            while count>0:
                line = float(str(file.readline().strip("\n")))
                data_list.append(line)
                count-=1
                
            file.close()
            self.data = data_list
            self.mean = self.calculate_mean()
            self.stdev = self.calculate_stdev(sample)

    def plot_histogram(self):
        plt.hist(self.data)
        plt.xlabel('Weight of males in USA')
        plt.ylabel('Count')
        plt.savefig('data/results/histogram.png')
        plt.show()

    def pdf(self, x):
        mean = self.mean
        stdev = self.stdev
        pdf = (1 /(2*(math.pi)* stdev**2)**0.5 ) * math.exp(-1 * (x-mean)**2 / 2*stdev**2) * 1.00000
        return pdf

    def plot_histogram_pdf(self, n_spaces=50):
        mu = self.mean
        sigma = self.stdev

        min_value = min(self.data)
        max_value = max(self.data)

        interval = 1.0 * (max_value-min_value)/n_spaces

        x = []
        y = []

        for i in range(n_spaces):
            tmp = min_value + interval * i
            x.append(tmp)
            y.append(self.pdf(tmp))
        
        # make the plots
        fig, axes = plt.subplots(2,sharex=True)
        fig.subplots_adjust(hspace=.5)
        axes[0].hist(self.data, density=True)
        axes[0].set_title('Normed Histogram of Data')
        axes[0].set_ylabel('Density')

        axes[1].plot(x, y)
        axes[1].set_title('Normal Distribution for \n Sample Mean and Sample Standard Deviation')
        axes[0].set_ylabel('Density')
        plt.savefig('data/results/pdf_histogram.png')
        plt.show()

        return x, y
