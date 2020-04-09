import argparse
import logging

from credit_models import kmv

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":

    # TODO: Give the user the option to select a model

    parser = argparse.ArgumentParser("Credit Risk Models")
    parser.add_argument("enterprise_value", help="Enterprise value", type=float)
    parser.add_argument("short_term_debt", help="Short term debt", type=float)
    parser.add_argument("long_term_debt", help="Long term debt", type=float)
    parser.add_argument("mu", help="Expected annual growth rate", type=float)
    parser.add_argument("sigma", help="Expected annual volatility", type=float)

    args = parser.parse_args()

    edf = kmv.kmv(
        args.enterprise_value,
        args.short_term_debt,
        args.long_term_debt,
        args.mu,
        args.sigma,
    )

    logging.info(f"Expected default frequency = {edf}")
