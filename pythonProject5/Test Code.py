from BaseQueue import BaseQueue
from MMcQueue import MMcQueue
from MMcPriorityQueue import MMcPriorityQueue
from MM1Queue import MM1Queue
from MD1Queue import MD1Queue
from MG1Queue import MG1Queue

sample = BaseQueue(4, 5)
print(sample.is_valid())
print(sample.is_feasible())
print(sample.__str__())

sample = BaseQueue('four', 'five')
print(sample.is_valid())
print(sample.is_feasible())
print(sample.__str__())

sample = BaseQueue(5, 5)
print(sample.is_valid())
print(sample.is_feasible())
print(sample.__str__())

print("Done with Base Queue testing")

sample = MG1Queue(4, 5)
print(sample.is_valid())
print(sample.is_feasible())
print(sample.__str__())

sample = MG1Queue('four', 'five')
print(sample.is_valid())
print(sample.is_feasible())
print(sample.__str__())

sample = MG1Queue(5, 5)
print(sample.is_valid())
print(sample.is_feasible())
print(sample.__str__())

print("Done with MG1 Queue testing")

sample = MD1Queue(4, 5)
print(sample.is_valid())
print(sample.is_feasible())
print(sample.__str__())

sample = MD1Queue('four', 'five')
print(sample.is_valid())
print(sample.is_feasible())
print(sample.__str__())

sample = MD1Queue(5, 5)
print(sample.is_valid())
print(sample.is_feasible())
print(sample.__str__())

print("Done with MD1 Queue testing")

sample = MM1Queue(4, 5)
print(sample.is_valid())
print(sample.is_feasible())
print(sample.__str__())

sample = MM1Queue('four', 'five')
print(sample.is_valid())
print(sample.is_feasible())
print(sample.__str__())

sample = MM1Queue(5, 5)
print(sample.is_valid())
print(sample.is_feasible())
print(sample.__str__())

print("Done with MM1 Queue testing")

sample = MMcQueue(4, 5, 1)
print(sample.is_valid())
print(sample.is_feasible())
print(sample.__str__())

sample = MMcQueue('four', 'five', 'one')
print(sample.is_valid())
print(sample.is_feasible())
print(sample.__str__())

sample = MMcQueue(5, 5, 1)
print(sample.is_valid())
print(sample.is_feasible())
print(sample.__str__())

print("Done with MMC Queue testing")

sample = MMcPriorityQueue(4, 5, 1)
print(sample.is_valid())
print(sample.is_feasible())
print(sample.__str__())

sample = MMcPriorityQueue('four', 'five', 'one')
print(sample.is_valid())
print(sample.is_feasible())
print(sample.__str__())

sample = MMcPriorityQueue(5, 5, 1)
print(sample.is_valid())
print(sample.is_feasible())
print(sample.__str__())

print("Done with MMC Priority Queue testing")
