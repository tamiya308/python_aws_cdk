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
    template.resource_count_is("AWS::DynamoDB::Table", 1)


def test_students_table_properties():
    template = _template()

    template.has_resource_properties(
        "AWS::DynamoDB::Table",
        {
            "TableName": "Students",
            "KeySchema": [
                {"AttributeName": "Id", "KeyType": "HASH"},
                {"AttributeName": "Name", "KeyType": "RANGE"},
            ],
            "AttributeDefinitions": [
                {"AttributeName": "Id", "AttributeType": "N"},
                {"AttributeName": "Name", "AttributeType": "S"},
            ],
            "BillingMode": "PAY_PER_REQUEST",
        },
    )
    template.has_resource(
        "AWS::DynamoDB::Table",
        {"DeletionPolicy": "Delete", "UpdateReplacePolicy": "Delete"},
    )
