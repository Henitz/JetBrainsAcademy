units = int(input())
if units < 1:
    print('no army')
elif units in range(1, 10):
    print('few')
elif units in range(10, 50):
    print('pack')
elif units in range(50, 500):
    print('horde')
elif units in range(500, 1000):
    print('swarm')
elif units >= 1000:
    print('legion')