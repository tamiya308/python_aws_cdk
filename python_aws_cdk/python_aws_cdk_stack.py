from aws_cdk import (
    RemovalPolicy,
    Stack,
)
from aws_cdk import (
    aws_dynamodb as dynamodb,
)
from constructs import Construct


class StudentApiCdkStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Minimal-cost table: on-demand billing (no charge when idle), AWS-owned
        # encryption (free). DESTROY removes the table and its data on `cdk destroy`.
        dynamodb.Table(
            self,
            "StudentsEnrolmentsTable",
            table_name="StudentsEnrolments",
            partition_key=dynamodb.Attribute(
                name="Id", type=dynamodb.AttributeType.NUMBER
            ),
            sort_key=dynamodb.Attribute(
                name="Name", type=dynamodb.AttributeType.STRING
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=RemovalPolicy.DESTROY,
        )
