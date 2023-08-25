import math
from numbers import Number


def is_valid(lamda: float, mu: float, c: int = 1) -> bool:
    """
    Boolean function determining if the given queue is valid
    :param lamda: arrival rate
    :param mu: service rate
    :param c: amount of servers
    :return: True if the queue is valid, false otherwise
    """

    # Checks if lamda is a tuple or scalar
    if isinstance(lamda, tuple):
        # Lamda is a tuple, so each value of lamda is tested for validity
        for i in lamda:
            if not isinstance(i, Number) or i <= 0:
                return False

    else:
        # Lamda is a scalar, test for validity
        if not isinstance(lamda, Number) or lamda <= 0:
            return False

    # Tests mu for validity
    if not isinstance(mu, Number) or mu <= 0:
        return False

    # Tests c for validity
    if not isinstance(c, Number) or c <= 0:
        return False

    # If the inputs have passed all tests, the queue is valid
    return True


def is_feasible(lamda: float, mu: float, c: int = 1) -> bool:
    """
    Boolean function determining if the given queue is feasible
    :param lamda: arrival rate
    :param mu: service rate
    :param c: amount of servers
    :return: True if the queue is feasible, false otherwise
    """

    # First tests to make sure queue is valid
    if not is_valid(lamda, mu, c):
        return False

    # Checks if lamda is a tuple or scalar
    if isinstance(lamda, tuple):
        # Lamda is a tuple, so we use lamda aggregate in our feasibility equation
        wlamda = sum(lamda)

    else:
        wlamda = lamda

    # Calculates p
    p = wlamda / (c * mu)

    # Test feasibility
    if not p < 1:
        return False

    # If queue passes all tests, it is feasible
    return True


def calc_p0(lamda: float, mu: float, c: int = 1) -> float:
    """
     Calculates p0, the probability of an empty queue for single and multiple
     server queues
     :param lamda: arrival rate
     :param mu: service rate
     :param c: amount of servers
     :return: p0, probability of an empty queue
     """

    # Runs through basic checks for validity and feasibility
    if is_valid(lamda, mu, c) is False:
        return math.nan

    if is_feasible(lamda, mu, c) is False:
        return math.inf

    # If lamda is a tuple, we must use lamda aggregate for our p0 calculation
    if isinstance(lamda, tuple):
        wlamda = sum(lamda)

    else:
        wlamda = lamda

    # Prepare r and p for p0 calculation later on
    r = wlamda / mu
    p = r / c

    # Calculate p0 if there are multiple servers
    if c > 1:

        list_for_p0 = []

        for n in range(0, c):
            term1 = (r ** n) / math.factorial(n)
            list_for_p0.append(term1)

        term2 = (r ** c) / (math.factorial(c) * (1 - p))

        p0 = 1 / (sum(list_for_p0) + term2)

    # Calculates p0 if there is a single server
    else:
        p0 = 1 - p

    return p0


def calc_lq_mmc(lamda: float, mu: float, c: int = 1) -> float:
    """
     Calculates lq, the average number of customers waiting for an m/m/c queue
     :param lamda: arrival rate
     :param mu: service rate
     :param c: amount of servers
     :return: lq, the average number of customers waiting for an m/m/c queue
     """

    # Calculates p0
    p0 = calc_p0(lamda, mu, c)

    # If the queue did not pass validity or feasibilty test, return the error value
    if math.isinf(p0) or math.isnan(p0):
        return p0

    # If lamda is a tuple, we must use lamda aggregate for our lq calculation
    if isinstance(lamda, tuple):
        wlamda = sum(lamda)

    else:
        wlamda = lamda

    # Calculate r and p values for later lq calculation
    r = wlamda / mu
    p = r / c

    # Calculate the two terms in lq equation for multiple server queues
    if c > 1:
        lq_num = r ** c * p * p0
        lq_denom = math.factorial(c) * (1 - p) ** 2

    # Calculate the two terms in lq equation for single server queues
    else:
        lq_num = wlamda ** 2
        lq_denom = mu * (mu - wlamda)

    # Calculate lq
    lq = lq_num / lq_denom

    return lq

print(calc_lq_mmc(2, 2, 2))
print(calc_lq_mmc((1,1), 2, 2))