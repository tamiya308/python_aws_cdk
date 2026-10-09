#!/usr/bin/env python3

import aws_cdk as cdk

from python_aws_cdk.python_aws_cdk_stack import StudentApiCdkStack

app = cdk.App()
StudentApiCdkStack(app, "StudentApiCdkStack")

app.synth()
