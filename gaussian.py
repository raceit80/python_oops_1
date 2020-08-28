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
            
    