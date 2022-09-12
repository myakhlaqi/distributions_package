import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution

class Binomial(Distribution):
    """ Binomial distribution class for calculating and
    visualizing a Binomial distribution.

    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring

    """
    #       A binomial distribution is defined by two variables:
    #           the probability of getting a positive outcome
    #           the number of trials

    #       If you know these two values, you can calculate the mean and the standard deviation
    #
    #       For example, if you flip a fair coin 25 times, p = 0.5 and n = 25
    #       You can then calculate the mean and standard deviation with the following formula:
    #           mean = p * n
    #           standard deviation = sqrt(n * p * (1 - p))
    
    def __init__(self, p, n):
        Distribution.__init__(self, p * n, math.sqrt(n * p * (1 - p)))
        self.p = p
        self.n = n
        


    def calculate_mean(self):
        """Function to calculate the mean from p and n

        Args:
            None

        Returns:
            float: mean of the data set

        """
        self.mean = self.p * self.n
        self.stdev = math.sqrt(self.n * self.p * (1 - self.p))
        return self.mean


    def calculate_stdev(self):
        """Function to calculate the standard deviation from p and n.

        Args:
            None

        Returns:
            float: standard deviation of the data set

        """
        self.stdev = math.sqrt(self.n * self.p * (1 - self.p))
        return self.stdev


    #           

    #
    #           defined previously.
    def replace_stats_with_data(self):
        """Function to calculate p and n from the data set. The function updates the p and n variables of the object.

        Args:
            None

        Returns:
            float: the p value
            float: the n value

        """
        self.n = len(self.data)
        self.p = self.data.count(1)/self.n
        return (self.p, self.n)

    
    def plot_bar(self):
        """Function to output a histogram of the instance variable data using
        matplotlib pyplot library.

        Args:
            None

        Returns:
            None
        """
        plt.hist(self.data)
        plt.title('Histogram of Data')
        plt.xlabel('data')
        plt.ylabel('count')


    def pdf(self, k):
        """Probability density function calculator for the binomial distribution.

        Args:
            k (float): point for calculating the probability density function


        Returns:
            float: probability density function output
        """
        pdf_value = ((math.factorial(self.n)*1.0)/(math.factorial(k) *
                     math.factorial(self.n - k)))*(self.p ** k * (1 - self.p) ** (self.n - k))
        return pdf_value

    def plot_histogram_pdf(self, n_spaces=50):
        """Function to plot the pdf of the binomial distribution
        Args:
            None
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
        """
        mu = self.mean
        sigma = self.stdev
        # calculates the interval between x values
        interval = self.n / n_space
        x = []
        y = []
        # calculate the x values to visualize
        for i in range(n_spaces):
            tmp = interval*i
            x.append(tmp)
            y.append(self.pdf(tmp))
        # make the plots
        fig, axes = plt.subplots(2, sharex=True)
        fig.subplots_adjust(hspace=.5)
        axes[0].hist(self.data, density=True)
        axes[0].set_title('Binomial Histogram of Data')
        axes[0].set_ylabel('Density')
        axes[1].plot(x, y)
        axes[1].set_title(
            'Binomial Distribution for \n Sample Mean and Sample Standard Deviation')
        axes[0].set_ylabel('Density')
        plt.show()
        return x, y

      # k = 0 to k = n

      #   density function for every value of k.

      #   Be sure to label the bar chart with a title, x label and y label

      #   This method should also return the x and y values used to make the chart
      #   The x and y values should be stored in separate lists

    # write a method to output the sum of two binomial distributions. Assume both distributions have the same p value.
    def __add__(self, other):
        """Function to add together two Binomial distributions with equal p

        Args:
            other (Binomial): Binomial instance

        Returns:
            Binomial: Binomial distribution

        """

        try:
            assert self.p == other.p, 'p values are not equal'
            result = Binomial(self.p, self.n + other.n)
            result.stdev = result.calculate_stdev
            result.mean = result.calculate_mean
            return result
        except AssertionError as error:
            raise

        # TODO: Define addition for two binomial distributions. Assume that the
        # p values of the two distributions are the same. The formula for
        # summing two binomial distributions with different p values is more complicated,
        # so you are only expected to implement the case for two distributions with equal p.

        # the try, except statement above will raise an exception if the p values are not equal

        # Hint: When adding two binomial distributions, the p value remains the same
        #   The new n value is the sum of the n values of the two distributions.

    # use the __repr__ magic method to output the characteristics of the binomial distribution object.
    def __repr__(self):
        """Function to output the characteristics of the Binomial instance

        Args:
            None

        Returns:
            string: characteristics of the Binomial object

        """
        # return 'x ~ Bin({0:.2f} , {0:d})'.format(self.p, self.n)
        return 'mean {0;d}, standard deviation {1:.2f}, p {2:.2f}, n {3:d}'.format(
            self.mean, self.stdev, self.p, self.n
        )
        # TODO: 
        #       mean 5, standard deviation 4.5, p .8, n 20
        #
        #       with the values replaced by whatever the actual distributions values are
        #       The method should return a string in the expected format

        pass
