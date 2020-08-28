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
            line = file.readline()
            while line:
                data_list.append(int(line))
                line = file.readline()
            self.data = data_list
            mean = self.calculate_mean()
            stdev = self.calculate_stdev(sample)
            
            
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
            








