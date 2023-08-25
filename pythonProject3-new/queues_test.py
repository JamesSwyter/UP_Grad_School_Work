from queues import is_valid
from queues import is_feasible
from queues import calc_p0
from queues import calc_lq_mmc

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
