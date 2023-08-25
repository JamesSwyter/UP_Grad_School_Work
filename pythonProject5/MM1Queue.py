from BaseQueue import BaseQueue


class MM1Queue(BaseQueue):

    def __init__(self, lamda, mu):
        """
        MM1 constructor, calls BaseQueue constructor to test and assign lamda and mu
        :param lamda: arrival rate
        :param mu: service rate
        """

        super().__init__(lamda, mu)

    def _calc_metrics(self):
        """
        Function calculates the values of lq, the average number of customers waiting, and p0, the probability
        of an empty queue.
        """
        lq_num = self._lamda ** 2
        lq_denom = self._mu * (self._mu - self._lamda)

        self._lq = lq_num / lq_denom

        self._p0 = 1 - self.ro

        self._recalc_needed = False
