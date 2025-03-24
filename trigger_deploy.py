import boto3
import os

# Load environment variables
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
CODEDEPLOY_APP = os.getenv("CODEDEPLOY_APP")
CODEDEPLOY_GROUP = os.getenv("CODEDEPLOY_GROUP")
TASK_DEFINITION_ARN = os.getenv("TASK_DEFINITION_ARN")

# Initialize Boto3 client
client = boto3.client("codedeploy", region_name=AWS_REGION)

# Define AppSpec content dynamically
appspec_content = f"""version: 0.0
Resources:
  - TargetService:
      Type: AWS::ECS::Service
      Properties:
        TaskDefinition: "{TASK_DEFINITION_ARN}"
        LoadBalancerInfo:
          ContainerName: "pharmacy-container"
          ContainerPort: 80
"""

try:
    response = client.create_deployment(
        applicationName=CODEDEPLOY_APP,
        deploymentGroupName=CODEDEPLOY_GROUP,
        revision={
            "revisionType": "AppSpecContent",
            "appSpecContent": {"content": appspec_content}
        }
    )
    print(f"✅ Deployment triggered successfully: {response['deploymentId']}")
except Exception as e:
    print(f"❌ Deployment failed: {str(e)}")
