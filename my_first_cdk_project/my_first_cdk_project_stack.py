from aws_cdk import (
    aws_s3 as _s3,  #_s3 is being used to avoid collitions with other packages
    aws_iam as _iam,   
    core
)

class MyFirstCdkProjectStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        _s3.Bucket(
            self, 
            "myBucketId",
            bucket_name="jv-myfirstcdkproject-456-dev-1",
            versioned=True,
            encryption=_s3.BucketEncryption.S3_MANAGED,
            block_public_access=_s3.BlockPublicAccess.BLOCK_ALL
        )

        mybucket = _s3.Bucket(
            self,
            "myBucketId1"
        )

        #print(mybucket.bucket_name)

        _iam.Group(
            self,
            "gid"
        )

        output_1 = core.CfnOutput(
            self,
            "myBucketOutput1",
            value=mybucket.bucket_name,
            description=f"My first CDK bucket",
            export_name="myBucketOutput1"
        )