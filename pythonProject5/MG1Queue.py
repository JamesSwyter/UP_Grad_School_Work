from BaseQueue import BaseQueue
from numbers import Number
import math


class MG1Queue(BaseQueue):

    def __init__(self, lamda, mu, sigma=0.0):
        """
        BaseQueue constructor tests lamda, mu for validity and assigns the variables
        :param lamda: arrival rate
        :param mu: service rate
        :param sigma: service time standard deviation
        """

        self._sigma = sigma

        if not isinstance(sigma, Number) or sigma < 0:
            self._sigma = math.nan

        super().__init__(lamda, mu)

    @property
    def sigma(self):
        """
        Getter function returns sigma when called
        :return: self._sigma, which is service time standard deviation
        """
        return self._sigma

    @sigma.setter
    def sigma(self, sigma):
        """
        Setter function sets the value of self._sigma, checks for validity and feasibility
        :param sigma: service time standard deviation
        """

        self._sigma = sigma

        # Check for validity
        if not isinstance(sigma, Number) or sigma < 0:
            self._sigma = math.nan

        self._recalc_needed = True

    def _calc_metrics(self):
        """
        Function calculates the values of lq, the average number of customers waiting, and p0, the probability
        of an empty queue.
        """

        self._p0 = 1 - self.ro

        lq_num = self.ro ** 2 + ((self._lamda ** 2) * self._sigma ** 2)
        lq_denom = 2 * (1 - self.ro)

        self._lq = lq_num / lq_denom

        self._recalc_needed = False

    def is_valid(self):
        """
        Boolean function determining if the given queue is valid
        :return: True if the queue is valid, false otherwise
        """

        if not super().is_valid():
            return False

        # Tests sigma for validity
        if math.isnan(self._sigma):
            return False

        # If the inputs have passed all tests, the queue is valid
        return True

    def __str__(self):
        """
        Function returns all the relevant queue metrics
        :return: f string with all the metrics
        """

        a = super().__str__()
        a = f"sigma: {self._sigma}\n" + a
        return a
