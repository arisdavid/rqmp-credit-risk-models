import argparse
import logging

from worker.task_executor import task_executor

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":

    parser = argparse.ArgumentParser("Credit Risk Models")
    parser.add_argument("input_bucket", help="S3 Input Bucket Name", type=str)
    parser.add_argument("output_bucket", help="S3 Output Bucket Name", type=str)
    parser.add_argument("key", help="S3 Key", type=str)

    args = parser.parse_args()

    input_bucket = args.input_bucket
    output_bucket = args.output_bucket
    key = args.key

    task_executor(input_bucket, output_bucket, key)
