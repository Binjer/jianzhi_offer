import time
import sys
from sklearn.model_selection import KFold
import numpy as np

# for i in range(5):
#     print(i)
#     sys.stdout.flush()
#     time.sleep(1)

k_fold = KFold(n_splits=10, shuffle=False)
for idx, (train, test) in enumerate(k_fold.split(np.arange(6000))):
    pass