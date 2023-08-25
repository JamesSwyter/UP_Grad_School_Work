from numbers import Number
import math


class BaseQueue:

    def __init__(self, lamda, mu):
        """
        BaseQueue constructor tests lamda, mu for validity and assigns the variables
        :param lamda: arrival rate
        :param mu: service rate
        """

        # Assign the variables for testing
        self._lamda = lamda
        self._mu = mu

        # Tests for validity
        if not isinstance(mu, Number) or mu <= 0:
            self._mu = math.nan

        # Checks if lamda is a tuple or scalar
        if isinstance(lamda, tuple):
            # Lamda is a tuple, so each value of lamda is tested for validity
            for i in lamda:
                if not isinstance(i, Number) or i <= 0:
                    self._lamda = math.nan

        else:
            # Lamda is a scalar, test for validity
            if not isinstance(lamda, Number) or lamda <= 0:
                self._lamda = math.nan

        # If it is valid, lamda is converted to aggregate value
        if self.is_valid():
            self._lamda = self._simplify_lamda(lamda)

        # Recalc is needed since lamda and mu have been changed
        self._recalc_needed = True

    @property
    def lamda(self):
        """
        Getter function returns lamda when called
        :return: self._lamda, which is arrival rate
        """
        return self._lamda

    @lamda.setter
    def lamda(self, lamda):
        """
        Setter function sets the value of self._lamda, checks for validity and feasibility
        :param lamda: arrival rate
        """

        # Assign lamda for testing
        self._lamda = lamda

        if isinstance(lamda, tuple):
            # Lamda is a tuple, so each value of lamda is tested for validity
            for i in lamda:
                if not isinstance(i, Number) or i <= 0:
                    self._lamda = math.nan

        else:
            # Lamda is a scalar, test for validity
            if not isinstance(lamda, Number) or lamda <= 0:
                self._lamda = math.nan

        # Once it has been tested for validity, lamda is converted to aggregate value
        if self.is_valid():
            self._lamda = self._simplify_lamda(lamda)

        self._recalc_needed = True

    @property
    def mu(self):
        """
        Getter function returns mu when called
        :return: self._mu, which is service rate
        """
        return self._mu

    @mu.setter
    def mu(self, mu):
        """
        Setter function sets the value of self._mu, checks for validity and feasibility
        :param mu: service rate
        """

        # Assign mu for testing
        self._mu = mu

        # Tests mu for validity
        if not isinstance(mu, Number) or mu <= 0:
            self._mu = math.nan

        self._recalc_needed = True

    def _simplify_lamda(self, lamda):
        """
        Function takes lamda, returns the sum (aggregate value)
        :param lamda: arrival rate
        :return: lamda, which is the sum of the input
        """

        if isinstance(lamda, tuple):
            return sum(lamda)

        else:
            return lamda

    def _calc_metrics(self):
        """
        Function calculates the values of lq, the average number of customers waiting, and p0, the probability
        of an empty queue. For BaseQueue the variables are both set to nan.
        """

        self._lq = math.nan
        self._p0 = math.nan

        self._recalc_needed = False

    @property
    def lq(self):
        """
        Getter function returns lq when called
        :return: self._lq, the average number of customers waiting
        """

        if self.is_valid() is False:
            return math.nan
        if self.is_feasible() is False:
            return math.inf

        # If lq and p0 haven't been calculated for the new lamda and mu values, calculate them
        if self._recalc_needed:
            self._calc_metrics()

        return self._lq

    @property
    def p0(self):
        """
        Getter function returns p0 when called
        :return: self._p0, the probability of an empty queue
        """

        if self.is_valid() is False:
            return math.nan
        if self.is_feasible() is False:
            return math.inf

        if self._recalc_needed:
            self._calc_metrics()

        return self._p0

    @property
    def l(self):
        """
        Getter function calculates and returns l when called
        :return: l, average number of customers in the system
        """

        if self.is_valid() is False:
            return math.nan
        if self.is_feasible() is False:
            return math.inf

        wlamda = self._simplify_lamda(self._lamda)

        l = self.lq + wlamda / self._mu

        return l

    @property
    def r(self):
        """
        Getter function calculates and returns r when called
        :return: r, average number of servers in use
        """

        wlamda = self._simplify_lamda(self._lamda)

        r = wlamda / self._mu

        return r

    @property
    def w(self):
        """
        Getter function calculates and returns w when called
        :return: w, average time customer spends in system
        """

        if self.is_valid() is False:
            return math.nan
        if self.is_feasible() is False:
            return math.inf

        wlamda = self._simplify_lamda(self._lamda)

        w = self.l / wlamda

        return w

    @property
    def wq(self):
        """
        Getter function calculates and returns wq when called
        :return: wq, average customer waiting time
        """

        if self.is_valid() is False:
            return math.nan
        if self.is_feasible() is False:
            return math.inf

        wlamda = self._simplify_lamda(self._lamda)

        wq = self.lq / wlamda

        return wq

    @property
    def ro(self):
        """
        Getter function calculates and returns ro when called
        :return: ro, which is system utilization
        """

        ro = self.r

        return ro

    @property
    def utilization(self):
        """
        Getter function calculates and returns utilization when called
        :return: utilization, which is ro but as a percentage
        """

        if self.is_valid() is False:
            return math.nan
        if self.is_feasible() is False:
            return math.inf

        utilization = self.ro * 100

        return utilization

    def is_valid(self):
        """
        Boolean function determining if the given queue is valid
        :return: True if the queue is valid, false otherwise
        """

        lamda = self._simplify_lamda(self._lamda)

        # Checks if lamda or mu is invalid
        if math.isnan(lamda) or math.isnan(self._mu):
            return False

        # If they both are valid return true
        return True

    def is_feasible(self):
        """
        Boolean function determining if the given queue is feasible
        :return: True if the queue is feasible, false otherwise
        """

        # Checks if queue is infeasible
        if not self.ro < 1:
            return False

        # If queue passes all tests, it is feasible
        return True

    def __str__(self):
        """
        Function returns all the relevant queue metrics
        :return: f string with all the metrics
        """

        return f"lamda: {self.lamda}\n"\
               f"mu: {self.mu}\n" \
               f"lq: {self.lq}\n" \
               f"p0: {self.p0}\n" \
               f"ro: {self.ro}\n" \
               f"r: {self.r}\n" \
               f"l: {self.l}\n" \
               f"w: {self.w}\n" \
               f"wq: {self.wq}\n" \
               f"utilization: {self.utilization}\n"
