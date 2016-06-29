import numpy as np
from pkg import test

tests = [
            (np.int32, test.process_int32),
            (np.uint32, test.process_uint32),
            (np.int64, test.process_int64),
            (np.uint64, test.process_uint64),
         ]
            
for t in tests:
    try:
        t[1](np.array([1,2], dtype=t[0]))
        print('%s succeeded!' % t[0])
    except Exception as e:
        print('%s:%s failed : %s' % (t[0], t[1], e))
