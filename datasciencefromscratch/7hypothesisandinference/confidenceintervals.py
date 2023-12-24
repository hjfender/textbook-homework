import math
from exampleflipplingcoins import normal_two_sided_bounds

p_hat = 525 / 1000
mu = p_hat
sigma = math.sqrt(p_hat * (1 - p_hat) / 1000)   # 0.0158
normal_two_sided_bounds(0.95, mu, sigma)    # [0.4940, 0.5560]

p_hat = 540 / 1000
mu = p_hat
sigma = math.sqrt(p_hat * (1 - p_hat) / 1000)   # 0.0158
normal_two_sided_bounds(0.95, mu, sigma)    # [0.5091, 0.5709]