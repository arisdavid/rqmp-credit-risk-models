import math

from scipy.stats import norm


def kmv(enterprise_value, short_term_debt, long_term_debt, mu, sigma, period=1):

    """
    KMV Model - https://www.math.ust.hk/~maykwok/Web_ppt/KMV/KMV.pdf
    :param enterprise_value: Enterprise Value of the Firm (can market capitalisation)
    :param short_term_debt: Firm's short term debt
    :param long_term_debt: Firm's long term debt
    :param mu: Expected Return after 1 year
    :param sigma: Expected Annualized Volatility
    :param period: period in years
    :return: EDF (Expected Default Frequency or Probability of Default)
    """

    # Calculate default point
    default_point = short_term_debt + (0.5 * long_term_debt)

    # Numerator
    x = (
        math.log(enterprise_value / default_point)
        + (mu - math.pow(sigma, 2) / 2) * period
    )

    # Denominator
    y = sigma * period

    # Distance to Default
    distance_to_default = x / y
    expected_default_frequency = norm.cdf(-distance_to_default)

    return expected_default_frequency
