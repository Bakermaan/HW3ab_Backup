from math import gamma, sqrt, pi

def t_pdf(t, df):
    # Calculate the t-distribution probability density function
    num = gamma((df + 1) / 2)
    den = sqrt(df * pi) * gamma(df / 2)
    return num / den * (1 + t**2 / df) ** (-((df + 1) / 2))

def simpsons_rule(f, a, b, n, df):
    # Apply Simpson's Rule for numerical integration
    delta_x = (b - a) / n
    summation = f(a, df) + f(b, df)
    for i in range(1, n):
        x = a + i * delta_x
        summation += f(x, df) * (4 if i % 2 != 0 else 2)
    return delta_x / 3 * summation

def main():
    print("T-Distribution Probability Calculator")

    for df in [7, 11, 15]:
        df = int(input(f"Enter degrees of freedom (try {df}): "))
        for _ in range(3):
            z = float(input("Enter z value: "))
            # Assuming -100 is a reasonable approximation of negative infinity for the t-distribution
            probability = simpsons_rule(t_pdf, -100, z, 1000, df)
            print(f"The probability for df={df} and z={z} is: {probability:.4f}")

if __name__ == "__main__":
    main()
