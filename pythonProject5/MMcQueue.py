import math
from numbers import Number
from BaseQueue import BaseQueue


class MMcQueue(BaseQueue):

    def __init__(self, lamda, mu, c):
        """
        MMcQueue constructor tests lamda, mu and c for validity and assigns the variables
        :param lamda: arrival rate
        :param mu: service rate
        :param c: amount of servers
        """

        # Assign c, call super constructor to assign lamda and mu
        self._c = c
        super().__init__(lamda, mu)

        # Run c through validity test
        if not isinstance(self._c, Number) or self._c <= 0:
            self._c = math.nan

        # Recalc is needed since lamda and mu have been changed
        self._recalc_needed = True

    @property
    def c(self):
        """
        Getter function returns c when called
        :return: self._c, which is number of servers
        """
        return self._c

    @c.setter
    def c(self, c):
        """
        Setter function sets the value of self._c, checks for validity and feasibility
        :param c: number of servers
        """

        self._c = c

        # Tests c for validity
        if not isinstance(self._c, Number) or self._c <= 0:
            self._c = math.nan

        self._recalc_needed = True

    @property
    def ro(self):
        """
        Getter function calculates and returns ro when called
        :return: ro, system utilization
        """

        ro = self.r / self._c

        return ro

    def _calc_metrics(self):
        """
        Function calculates and sets the values of lq, the average number of customers waiting, and p0, the probability
        of an empty queue.
        """

        wlamda = self._simplify_lamda(self._lamda)

        # Calculate p0 and lq if there are multiple servers
        if self._c > 1:

            list_for_p0 = []

            for n in range(0, int(self._c)):
                term1 = (self.r ** n) / math.factorial(n)
                list_for_p0.append(term1)

            term2 = (self.r ** self._c) / (math.factorial(self._c) * (1 - self.ro))

            self._p0 = 1 / (sum(list_for_p0) + term2)

            lq_num = self.r ** self._c * self.ro * self._p0
            lq_denom = math.factorial(self._c) * (1 - self.ro) ** 2

            # Calculates p0 and lq if there is a single server
        else:
            self._p0 = 1 - self.ro

            lq_num = wlamda ** 2
            lq_denom = self._mu * (self._mu - wlamda)

        self._lq = lq_num / lq_denom

    def is_valid(self):
        """
        Boolean function determining if the given queue is valid
        :return: True if the queue is valid, false otherwise
        """

        lamda = self._simplify_lamda(self._lamda)

        # Checks if lamda or mu or c is invalid
        if math.isnan(lamda) or math.isnan(self._mu) or math.isnan(self._c):
            return False

        # If they are valid return true
        return True

    def is_feasible(self):
        """
        Boolean function determining if the given queue is feasible
        :return: True if the queue is feasible, false otherwise
        """

        # Checks if queue is infeasible
        if not self.is_valid() or not self.ro < 1:
            return False

        # If queue passes all tests, it is feasible
        return True

    def __str__(self):
        """
        Function returns all the relevant queue metrics
        :return: f string with all the metrics
        """
        a = super().__str__()
        a = f"c: {self._c}\n" + a
        return a
