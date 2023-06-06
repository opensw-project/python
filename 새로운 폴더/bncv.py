from scipy.optimize import minimize_scalar

# 사용 예시
def f(x):
    return x**2 - 4*x + 3

# minimize_scalar 함수를 사용하여 최솟값 계산
result = minimize_scalar(f)
min_value = result.fun

print(min_value)  # 출력: -1.0
