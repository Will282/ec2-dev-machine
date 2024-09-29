import pytest
import yaml
from syrupy.extensions.json import JSONSnapshotExtension


@pytest.fixture
def snapshot_json(snapshot):
    return snapshot.use_extension(JSONSnapshotExtension)


@pytest.fixture
def temp_yaml_config(tmp_path):
    # Example configuration dictionary
    config_dict = {
        "stack_id": "my-stack",
        "base_resource_name": "my-resource",
        "ec2": {
            "instance_type": "t4g.nano",
            "key_pair_name": "example-key-pair",
            "ebs_volume_size": 50,
            "vpc_id": "vpc-123",
            "managed_policies": ["AWSCodeCommitPowerUser"],
            "custom_policy": {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Sid": "ListObjectsInBucket",
                        "Effect": "Allow",
                        "Action": ["s3:ListBucket"],
                        "Resource": ["arn:aws:s3:::example-bucket"],
                    },
                    {
                        "Sid": "AllObjectActions",
                        "Effect": "Allow",
                        "Action": "s3:*Object",
                        "Resource": ["arn:aws:s3:::example-bucket/*"],
                    },
                ],
            },
        },
        "user_data": {"python_version": "3.10.14", "git_user_name": "John Smith", "git_user_email": "john@example.com"},
        "environment": {"account": "012345678901", "region": "us-east-1"},
    }

    # Create a temporary YAML file path
    temp_file = tmp_path / "config.yaml"

    # Write the dictionary to the file in YAML format
    with temp_file.open("w") as f:
        yaml.dump(config_dict, f)

    # Return the path to the YAML file
    return temp_file
