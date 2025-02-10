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
    m = int(input("Enter degrees of freedom (m): ").strip())
    z = float(input("Enter a z value: ").strip())

    probability = t_distribution_cdf(z, m)
    print(f"\nF({z}) for m={m} = {probability:.6f}")


if __name__ == "__main__":
    main()
