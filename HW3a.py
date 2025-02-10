from numericalMethods import GPDF, Probability, Secant


def probability_difference(c, target_P, mean, stDev, GT, OneSided):
    """
    Function to compute the difference between computed probability and target probability.
    Used for the Secant method root finding.
    """
    if OneSided:
        prob = Probability(GPDF, (mean, stDev), c, GT=GT)
    else:
        prob = Probability(GPDF, (mean, stDev), c, GT=True)
        prob = 1 - 2 * prob
        if GT:
            prob = 1 - prob
    return prob - target_P


def main():
    Again = True
    while Again:
        mean = float(input("Population mean? ").strip())
        stDev = float(input("Standard deviation? ").strip())
        find_c = input(
            "Are you specifying c and solving for P, or specifying P and solving for c? (c/p) ").strip().lower() == "p"

        if find_c:
            target_P = float(input("Enter the desired probability P: ").strip())
            GT = input("Probability greater than c? (y/n) ").strip().lower() == "y"
            OneSided = input("One sided? (y/n) ").strip().lower() == "y"

            # Use Secant method to find c
            x0, x1 = mean, mean + stDev  # Initial guesses
            c, iterations = Secant(lambda c_val: probability_difference(c_val, target_P, mean, stDev, GT, OneSided), x0,
                                   x1)

            print(f"Computed c value: {c:0.3f} after {iterations} iterations")
        else:
            c = float(input("c value? ").strip())
            GT = input("Probability greater than c? (y/n) ").strip().lower() == "y"
            OneSided = input("One sided? (y/n) ").strip().lower() == "y"

            if OneSided:
                prob = Probability(GPDF, (mean, stDev), c, GT=GT)
                print(f"P(x {'>' if GT else '<'} {c:0.2f} | {mean:0.2f}, {stDev:0.2f}) = {prob:0.3f}")
            else:
                prob = Probability(GPDF, (mean, stDev), c, GT=True)
                prob = 1 - 2 * prob
                if GT:
                    print(f"P({mean - (c - mean)}>x>{mean + (c - mean)} | {mean:0.2f}, {stDev:0.2f}) = {1 - prob:0.3f}")
                else:
                    print(f"P({mean - (c - mean)}<x<{mean + (c - mean)} | {mean:0.2f}, {stDev:0.2f}) = {prob:0.3f}")

        Again = input("Go again? (y/n) ").strip().lower() == "y"


if __name__ == "__main__":
    main()
