from aws_cdk import (
    aws_s3 as _s3,  #_s3 is being used to avoid collitions with other packages   
    core
)

class MyFirstCdkProjectStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        _s3.Bucket(
            self, 
            "myBucketId",
            bucket_name="jv-myfirstcdkproject-456-dev",
            versioned=True,
            encryption=_s3.BucketEncryption.KMS_MANAGED
        )
