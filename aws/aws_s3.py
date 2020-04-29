import tempfile

import boto3
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

s3 = boto3.client("s3")


class AwsS3:
    def __init__(self, bucket, key):
        self.bucket = bucket
        self.key = key

    def get_etag(self):
        resp = s3.head_object(Bucket=self.bucket, Key=self.key)
        return resp.get("ETag")

    def get_file_path(self):

        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            s3.download_fileobj(self.bucket, self.key, temp_file)
            temp_file.seek(0)

            return temp_file.name

    @property
    def df(self):
        file_path = self.get_file_path()
        return pd.read_csv(file_path, encoding="utf-8")

    @staticmethod
    def write_pd_parquet_to_s3(df, bucket, key, file_path):

        table = pa.Table.from_pandas(df)
        pq.write_table(table, file_path)

        # upload to s3
        bucket = bucket
        with open(file_path) as f:
            object_data = f.read()
            s3.put_object(Body=object_data, Bucket=bucket, Key=key)
