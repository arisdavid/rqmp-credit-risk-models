from aws.aws_s3 import AwsS3
from credit_models.kmv import kmv


def task_executor(bucket, key):

    aws_s3 = AwsS3(bucket, key)
    df = aws_s3.df

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

    aws_s3.write_pd_parquet_to_s3(df, bucket, key, ".temp/output.parquet")
