from aws_cdk import core
import aws_cdk.aws_iam as iam

class MyStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Define IAM user
        my_user = iam.User(
            self, "MyUser",
            user_name="my-iam-user"
        )

        # Create a login profile for the user with a password
        my_user.add_login_profile(
            password="my-password",
            password_reset_required=True
        )

app = core.App()
MyStack(app, "MyStack")
app.synth()
