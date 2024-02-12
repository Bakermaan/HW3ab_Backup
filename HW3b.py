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

    while True:  # Main loop to allow restarting the calculations
        df_input = input("Enter degrees of freedom (or type 'exit' to quit): ")
        if df_input.lower() == 'exit':
            break  # Exit the loop, ending the program
        df = int(df_input)

        for _ in range(3):  # Loop for entering up to 3 z values
            z_input = input("Enter z value (or type 'exit' to quit): ")
            if z_input.lower() == 'exit':
                return  # Immediately exits the main function, and thus the program
            z = float(z_input)
            probability = simpsons_rule(t_pdf, -100, z, 1000, df)
            print(f"The probability for df={df} and z={z} is: {probability:.4f}")

        restart_input = input("Do you want to restart with new degrees of freedom? (yes/no): ")
        if restart_input.lower() != 'yes':
            print("Exiting program. Thank you for using the calculator.")
            break  # Exit the loop, ending the program

if __name__ == "__main__":
    main()
