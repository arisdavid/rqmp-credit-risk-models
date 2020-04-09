import pytest
from credit_models.kmv import kmv


@pytest.mark.parametrize(
    "enterprise_value, short_term_debt, long_term_debt, mu, sigma, expected",
    [(1_000_000, 900_000, 500_000, 0.18, 0.12, 0.39153629601210416)],
)
def test_kmv_model(
    enterprise_value, short_term_debt, long_term_debt, mu, sigma, expected
):
    """ Test KMV model """
    assert kmv(enterprise_value, short_term_debt, long_term_debt, mu, sigma) == expected
