from aws_cdk import (
    RemovalPolicy,
    Stack,
)
from aws_cdk import (
    aws_s3 as s3,
)
from constructs import Construct


class StudentApiCdkStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Minimal-cost bucket: SSE-S3 (free), no versioning, private.
        # DESTROY removes the bucket on `cdk destroy` (bucket must be empty).
        s3.Bucket(
            self,
            "PythonCdkS3Bucket",
            bucket_name="python-cdk-s3-mluy",
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            encryption=s3.BucketEncryption.S3_MANAGED,
            versioned=False,
            removal_policy=RemovalPolicy.DESTROY,
        )
