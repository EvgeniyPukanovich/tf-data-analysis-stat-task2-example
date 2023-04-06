import pandas as pd
import numpy as np

from scipy.stats import gamma


chat_id = 970839957  # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = x.shape[0]
    m = x.mean()
    return m/2 - 0.25 + gamma.ppf((1 - p)/2, n) / (2 * n), m/2 - 0.25 + gamma.ppf((1 + p)/2, n) / (2 * n)
