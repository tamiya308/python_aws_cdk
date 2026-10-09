#!/usr/bin/env python3

import aws_cdk as cdk

from python_aws_cdk.python_aws_cdk_stack import PythonAwsCdkStack


app = cdk.App()
PythonAwsCdkStack(app, "PythonAwsCdkStack")

app.synth()
