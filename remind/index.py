import sys
import dayRemind
import beforeRemind
import setSchodule


# print(sys.argv)

# ['index.py', 'setSch', '1', '2']
if sys.argv[1] == 'setSchedule':
    setSchodule.index()
elif sys.argv[1] == 'dayRemind':
    dayRemind.index()
elif sys.argv[1] == 'beforeRemind':
    beforeRemind.index(sys.argv[2])
