import math
from MMcQueue import MMcQueue
from numbers import Number


class MMcPriorityQueue(MMcQueue):

    def __init__(self, lamda, mu, c):
        """
        MMcPriorityQueue constructor tests lamda, mu and c for validity and assigns the variables
        :param lamda: arrival rate
        :param mu: service rate
        :param c: amount of servers
        """

        # Call MMc Constructor to assign variables and test lamda, mu and c
        super().__init__(lamda, mu, c)

        self._lamda_k = lamda

        # Checks if lamda is a tuple or scalar
        if isinstance(lamda, tuple):
            # Lamda is a tuple, so each value of lamda is tested for validity
            for i in lamda:
                if not isinstance(i, Number) or i <= 0:
                    self._lamda_k = math.nan

        else:
            # Lamda is a scalar, test for validity
            if not isinstance(lamda, Number) or lamda <= 0:
                self._lamda_k = math.nan

        # Lamda has to be in the form of a tuple for the length calculation later on
        if not isinstance(self._lamda_k, tuple):
            a = [self._lamda_k]
            self._lamda_k = tuple(a)

    @property
    def lamda_k(self):
        """
        Getter function returns lamda_k when called
        :return: self._lamda_k, which is arrival rate
        """
        return self._lamda_k

    @lamda_k.setter
    def lamda_k(self, lamda):
        """
        Setter function sets the value of self._lamda_k, checks for validity and feasibility
        :param lamda: arrival rate(s)
        """

        self.lamda(lamda)

        self._lamda_k = lamda

        # Checks if lamda is a tuple or scalar
        if isinstance(lamda, tuple):
            # Lamda is a tuple, so each value of lamda is tested for validity
            for i in lamda:
                if not isinstance(i, Number) or i <= 0:
                    self._lamda_k = math.nan

        else:
            # Lamda is a scalar, test for validity
            if not isinstance(lamda, Number) or lamda <= 0:
                self._lamda_k = math.nan

        # Lamda has to be in the form of a tuple for the length calculation later on
        if not isinstance(self._lamda_k, tuple):
            a = [self._lamda_k]
            self._lamda_k = tuple(a)

    def get_b_k(self, k):
        """
        Getter function calculates and returns b_k
        :return: bk, which is capacity remaining for classes that are lower priority than k
        """

        if self.is_valid() is False:
            return math.nan
        if self.is_feasible() is False:
            return math.inf

        # Check that k is a valid input
        if not isinstance(k, int) or k < 0 or k > len(self._lamda_k):
            return math.nan

        # Bk = 1 if k = 0
        if k == 0:
            return 1

        # Calculate Bk
        p = [a / (self._c * self._mu) for a in self._lamda_k[0:k]]

        b_k = 1 - sum(p)

        return b_k

    def get_l_k(self, k):
        """
        Getter function calculates and returns l_k when called
        :return: l_k, which is average number of customers of class k in the system
        """

        if self.is_valid() is False:
            return math.nan
        if self.is_feasible() is False:
            return math.inf

        # Check that k is a valid input
        if not isinstance(k, int) or k <= 0 or k > len(self._lamda_k):
            return math.nan

        l_k = self.get_lq_k(k) + self.get_lamda_k(k) / self._mu

        return l_k

    def get_lamda_k(self, k):
        """
        Getter function returns lamda_k when called
        :return: lamda_k, arrival rate for k class
        """

        # If k exists, return lamda_k
        if k:

            # Check that k is a valid input
            if not isinstance(k, int) or k <= 0 or k > len(self._lamda_k):
                return math.nan

            lamda_k = self._lamda_k[k-1]

        # If k doesn't exist, return all lamda values
        else:
            lamda_k = self._lamda_k

        return lamda_k

    def get_lq_k(self, k):
        """
        Calculates Lq,k for a customer of priority class k
        :return: Lq,k is average number of customers of priority class k that are waiting
        """

        if self.is_valid() is False:
            return math.nan
        if self.is_feasible() is False:
            return math.inf

        # Checks that k is a valid priority class
        if not isinstance(k, int) or k <= 0 or k > len(self._lamda_k):
            return math.nan

        # Calculate and return lqk
        lamdak = self.lamda_k[k-1]

        lqk = lamdak * self.get_wq_k(k)

        return lqk

    def get_ro_k(self, k):
        """
        Calculates ro_k for a customer of priority class k
        :return: ro_k is the system utilization of priority class k
        """

        if self.is_valid() is False:
            return math.nan
        if self.is_feasible() is False:
            return math.inf

        # Checks that k is a valid priority class
        if not isinstance(k, int) or k <= 0 or k > len(self._lamda_k):
            return math.nan

        r = self.get_lamda_k(k) / self._mu

        ro = r / self._c

        return ro

    def get_w_k(self, k):
        """
        Calculates w_k for a customer of priority class k
        :return: w_k is the average time spent in the system for a customer of priority class k
        """

        if self.is_valid() is False:
            return math.nan
        if self.is_feasible() is False:
            return math.inf

        # Check that k is a valid input
        if not isinstance(k, int) or k <= 0 or k > len(self._lamda_k):
            return math.nan

        w = self.get_l_k(k) / self.get_lamda_k(k)

        return w

    def get_wq_k(self, k):
        """
        Calculates wq,k for a customer of priority class k
        :return: wq,k is the average waiting time for a customer of priority class k
        """

        if self.is_valid() is False:
            return math.nan
        if self.is_feasible() is False:
            return math.inf

        # Check that k is a valid input
        if not isinstance(k, int) or k <= 0 or k > len(self._lamda_k):
            return math.nan

        # bk calculation
        bk = self.get_b_k(k - 1)

        # Second bk calculation
        bk_2 = self.get_b_k(k)

        # wqk calculation
        wqk = ((1 - self.ro) * self.lq) / (self._lamda * bk * bk_2)

        return wqk

    def __str__(self):

        a = super().__str__()

        for k in range(1, len(self._lamda_k)):
            a = a + f"lamda_k: {self.get_lamda_k(k)}"\
                    f"b_k: {self.get_b_k(k)}"\
                    f"wqk: {self.get_wq_k(k)}"\
                    f"wk: {self.get_w_k(k)}"\
                    f"lq: {self.get_lq_k(k)}"\
                    f"l: {self.get_l_k(k)}\n"

        return a
