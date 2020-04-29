import logging

from aws.aws_s3 import AwsS3
from credit_models.kmv import kmv

logging.basicConfig(level=logging.INFO)


def task_executor(input_bucket, output_bucket, key):
    # TODO: remove hardcoded output

    aws_s3 = AwsS3(input_bucket, key)
    df = aws_s3.df

    logging.info("Applying kmv calculation on the data.")
    df["default_probability"] = df.apply(
        lambda col: kmv(
            col["enterprise_value"],
            col["short_term_debt"],
            col["long_term_debt"],
            col["mu"],
            col["sigma"],
        ),
        axis=1,
    )
    logging.info("Finished performing calculations.")

    # Write output to output_bucket
    file_name = "output.csv"
    aws_s3.write_pd_csv_to_s3(df, output_bucket, file_name)
