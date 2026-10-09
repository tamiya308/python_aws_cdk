import aws_cdk as core
from aws_cdk import assertions

from python_aws_cdk.python_aws_cdk_stack import StudentApiCdkStack


def _template():
    app = core.App()
    stack = StudentApiCdkStack(app, "python-aws-cdk")
    return assertions.Template.from_stack(stack)


def test_only_one_resource_created():
    template = _template()

    assert len(template.to_json()["Resources"]) == 1
    template.resource_count_is("AWS::S3::Bucket", 1)


def test_s3_bucket_properties():
    template = _template()

    template.has_resource_properties(
        "AWS::S3::Bucket",
        {
            "BucketName": "python-cdk-s3-mluy",
            "PublicAccessBlockConfiguration": {
                "BlockPublicAcls": True,
                "BlockPublicPolicy": True,
                "IgnorePublicAcls": True,
                "RestrictPublicBuckets": True,
            },
        },
    )
    template.has_resource(
        "AWS::S3::Bucket",
        {"DeletionPolicy": "Delete", "UpdateReplacePolicy": "Delete"},
    )
