import logging

from worker.task_executor import task_executor

logging.basicConfig(level=logging.INFO)

"""if __name__ == "__main__":

    parser = argparse.ArgumentParser("Credit Risk Models")
    parser.add_argument("bucket", help="S3 Bucket Name", type=str)
    parser.add_argument("key", help="S3 Key", type=str)

    args = parser.parse_args()

    bucket = args.bucket
    key = args.key

    task_executor(bucket, key)"""

task_executor("kubeq-ingest-kmv", "sample-data-kmv-model.csv")
