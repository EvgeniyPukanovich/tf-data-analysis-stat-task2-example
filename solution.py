import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 123456 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    n = len(x)
    # оцениваем параметры распределения ошибок измерения
    mu = np.mean(x)
    s = np.std(x, ddof=1)
    # вычисляем стандартную ошибку среднего
    se = s / np.sqrt(n)
    # вычисляем критическое значение
    z = norm.ppf(1 - alpha/2)
    # вычисляем интервал
    interval = z * se
    lower = mu - interval
    upper = mu + interval
    return (lower, upper)
