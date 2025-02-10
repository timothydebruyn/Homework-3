import scipy.integrate as spi
import scipy.special as sp
import numpy as np


def gamma_function(alpha):
    """Computes the gamma function using numerical integration."""
    integral, _ = spi.quad(lambda t: np.exp(-t) * t ** (alpha - 1), 0, np.inf)
    return integral


def t_distribution_cdf(z, m):
    """Computes the cumulative probability F(z) for the t-distribution."""
    K_m = sp.gamma(0.5 * (m + 1)) / (np.sqrt(m * np.pi) * sp.gamma(0.5 * m))
    integral, _ = spi.quad(lambda u: (1 + (u ** 2 / m)) ** (-(m + 1) / 2), -np.inf, z)
    return K_m * integral


def main():
    """
    Main function to compute probabilities from the t-distribution.

    Steps:
    1. Display a welcome message.
    2. Enter an interactive loop to prompt the user for degrees of freedom (m) and a z-value.
    3. Compute the cumulative probability F(z) using numerical integration.
    4. Handle potential input errors gracefully.
    5. Ask the user if they want to continue or exit the program.
    """
    """
    Main function to interact with the user, accept inputs, and compute the cumulative
    probability for the t-distribution using numerical integration.

    Steps:
    1. Prompt the user to input three z-values for testing.
    2. Compute and print the cumulative probability for each z-value using degrees
       of freedom 7, 11, and 15.
    3. Display the results in a formatted output to compare with Table A9.
    """
    """
    Main function to interact with the user, accept inputs, and compute the cumulative
    probability for the t-distribution using numerical integration.

    The user is prompted to input degrees of freedom (m) and z-values. The program
    calculates and prints the cumulative probability for each given z-value.
    """
    # Prompt the user to input degrees of freedom
    m = int(input("Enter degrees of freedom (m): ").strip())

    # Prompt the user to input a z value
    z = float(input("Enter a z value: ").strip())

    # Compute the cumulative probability F(z)
    probability = t_distribution_cdf(z, m)

    # Display the computed probability
    print(f"\nF({z}) for m={m} = {probability:.6f}")


if __name__ == "__main__":
    main()
