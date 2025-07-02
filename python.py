import numpy as np
from tqdm import tqdm
import time

total = 100
iter_tqdm = tqdm(range(total))

for i in iter_tqdm:
    print(f"x = {i/100}, sin = {np.sin(i/100.4):.4f}")
    iter_tqdm.set_description(f"x = {i/100}, sin = {np.sin(i/100.4):.4f}")
    time.sleep(1)