from math import gamma, sqrt, pi
import scipy.stats as stats


# Simpson's Rule Implementation
def t_pdf(t, df):
    num = gamma((df + 1) / 2)
    den = sqrt(df * pi) * gamma(df / 2)
    return num / den * (1 + t ** 2 / df) ** (-((df + 1) / 2))


def simpsons_rule(f, a, b, n, df):
    delta_x = (b - a) / n
    result = f(a, df) + f(b, df)
    for i in range(1, n, 2):
        result += 4 * f(a + i * delta_x, df)
    for i in range(2, n - 1, 2):
        result += 2 * f(a + i * delta_x, df)
    result *= delta_x / 3
    return result


# Function to use SciPy to calculate the t-distribution probability
def scipy_t_distribution_probability(df, t_value):
    return stats.t.cdf(t_value, df)


# Test the functions
def compare_methods(df, t_value):
    simpson_probability = simpsons_rule(t_pdf, -100, t_value, 10000, df)
    scipy_probability = scipy_t_distribution_probability(df, t_value)
    print(f"Degrees of freedom: {df}, t-value: {t_value}")
    print(f"Simpson's rule probability: {simpson_probability:.6f}")
    print(f"SciPy probability: {scipy_probability:.6f}")
    print(f"Difference: {abs(simpson_probability - scipy_probability):.6f}\n")


# Main function to run the comparison
def main():
    test_values = [(7, 0.5), (7, 1.0), (7, 1.5),
                   (11, 0.5), (11, 1.0), (11, 1.5),
                   (15, 0.5), (15, 1.0), (15, 1.5)]

    for df, t_value in test_values:
        compare_methods(df, t_value)


if __name__ == "__main__":
    main()
