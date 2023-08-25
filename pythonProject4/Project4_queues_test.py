from Project4_queues import calc_bk_mmc
from Project4_queues import calc_wqk_mmc
from Project4_queues import calc_lqk_mmc
from Project4_queues import use_littles_law
from Project4_queues import is_valid
from Project4_queues import is_feasible
from Project4_queues import calc_p0
from Project4_queues import calc_lq_mmc

# is_valid tests

# is_valid tests with wrong data type
print("Should be false:", is_valid(('five', 1, 5), 1, 1))
print("Should be false:", is_valid(1, 'five', 1))
print("Should be false:", is_valid(1, 1, 'five'))

# is_valid test with invalid queue
print("Should be false:", is_valid(-1, 1, 1))

# is_valid test with valid queue
print("Should be true:", is_valid((1, 5, 6.0), 1, 1))

# is_feasible tests

# Checks that is_feasible is calling is_valid correctly
print("Should be false:", is_feasible(('five', 1, 5), 1, 1))

# is_feasible with infeasible queue
print("Should be false:", is_feasible((1, 1, 5), 1, 1))

# is_feasible with feasible queue
print("Should be true:", is_feasible((1, 1, 5), 5, 5))

# calc_p0 tests

# Checks that calc_p0 is calling is_valid correctly
print("Should be math.nan:", calc_p0(('five', 1, 5), 1, 1))

# Checks that calc_p0 is calling is_feasible correctly
print("Should be math.inf:", calc_p0((1, 1, 5), 1, 1))

# Calculate p0 for valid, feasible queue with multiple servers
print("Should be .176:", calc_p0((1, 1, 5), 5, 2))

# Calculate p0 for valid, feasible queue with single servers
print("Should be .3:", calc_p0((1, 1, 5), 10, 1))

# calc_lq_mmc test

# Checks that calc_lq_mmc is calling calc_p0 correctly
print("Should be math.inf:", calc_lq_mmc((1, 1, 5), 1, 1))

# Calculate lq for valid, feasible queue and multiple servers
print("Should be 1.35:", calc_lq_mmc((1, 1, 5), 5, 2))

# Calculate lq for valid, feasible queue and single servers
print("Should be 1.63:", calc_lq_mmc((1, 1, 5), 10, 1))

# Test if is_valid is being called correctly
print("Should be nan:", calc_bk_mmc(1, -1, 2, 1))
# Test if is_feasible is being called correctly
print("Should be inf:", calc_bk_mmc(1, 1, 1, 1))
# Test if K is being checked correctly
print("Should be nan:", calc_bk_mmc(-1, 1, 2, 1))
print("Should be nan:", calc_bk_mmc("five", 1, 2, 1))

# Test lamda as a scalar
print("Should be .5:", calc_bk_mmc(1, 1, 2, 1))
# Test lamda as a tuple
print("Should be .33:", calc_bk_mmc(2, (1, 1), 3, 1))
# Test if k is zero
print("Should be 1:", calc_bk_mmc(0, 1, 2, 1))

# Tests if calc_lq_mmc is handling errors
print("Should be nan:", calc_wqk_mmc(1, -1, 2, 1))
print("Should be inf:", calc_wqk_mmc(1, 1, 1, 1))
print("Should be nan:", calc_wqk_mmc(-1, 1, 2, 1))
print("Should be nan:", calc_wqk_mmc("five", 1, 2, 1))

# Test lamda as a scalar
print("Should be .5:", calc_wqk_mmc(1, 1, 2, 1))
# Test lamda as a tuple
print("Should be .99:", calc_wqk_mmc(2, (1, 1), 3, 1))

# Test if K is being checked correctly
print("Should be nan:", calc_lqk_mmc(-1, 1, 2))
print("Should be nan:", calc_lqk_mmc("five", 1, 2))

# Test lamda as a scalar
print("Should be 2:", calc_lqk_mmc(1, 1, 2))
# Test lamda as a tuple
print("Should be 4:", calc_lqk_mmc(2, (1, 2), 2))

# Tests if k is being checked
print("Should be nan:", use_littles_law(2, 2, 2))

# Tests lamda as a scalar
print(" Should return {lq: .33, l: 1.33, wq: .165, w: .665, r: 1, p: .5}")
print(use_littles_law(2, 2, 2, lq=.33))
print(use_littles_law(2, 2, 2, l=1.33))
print(use_littles_law(2, 2, 2, wq=.165))
print(use_littles_law(2, 2, 2, w=.665))

# Tests lamda as a tuple
print(" Should return {lq: .33, l: 1.33, wq: .165, w: .665, r: 1, p: .5, wqk: (.11, .22), lqk: (.11, .22)}")
print(use_littles_law((1, 1), 2, 2, lq=.33))
print(use_littles_law((1, 1), 2, 2, l=1.33))
print(use_littles_law((1, 1), 2, 2, wq=.165))
print(use_littles_law((1, 1), 2, 2, w=.665))
