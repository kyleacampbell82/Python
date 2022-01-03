n = 1

def newton(n, estimate=n):
    n = float(n)
    estimate = float(estimate)

    if abs(n - estimate ** 2) <= 0.000001:
        return estimate
    else:
        estimate = newton(n, (estimate + n / estimate) / 2)
    return estimate
