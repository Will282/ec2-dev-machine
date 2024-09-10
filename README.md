# ec2-dev-machine

## Overview

This Python package provides a L2 CDK Construct for spinning up a EC2 instance from a YAML configuration to quickly create and manage development instances.

The instances created have public IPs (cheaper than NAT Gateway for single instances) but have no open ports. All access to the instance should be done via SSM.

## Usage

1. Create a configuration file based on the example (`config.example.yaml`)
2. Set up CDK. If unfamiliar with CDK see the [Getting Started Guide](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html)
3. [Bootstrap](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html) your account for CDK deployments.
    ```bash
    cdk bootstrap aws://{account_number}/{region}
    ```
4. Deploy the instance with CDK
    ```bash
    cdk deploy
    ```
5. Install the Session Manager plugin for the AWS CLI - [Docs](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-install-plugin.html)
6. Connect to your instance with SSM
    ```bash
    aws ssm start-session --target {instance_id}
    ```
7. (Optional) Port Foward SSH to your local machine with SSH, for example if you want to use VSCode Remote-SSH - [Docs](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-sessions-start.html).

    Windows (Powershell):
    ```powershell
    aws ssm start-session `
        --target {instance_id} `
        --document-name AWS-StartPortForwardingSession `
        --parameters portNumber="22",localPortNumber="40000"
    ```
    Linux/Mac (bash):
    ```bash
    aws ssm start-session \
        --target {instance_id} \
        --document-name AWS-StartPortForwardingSession \
        --parameters "{"portNumber":["22"],"localPortNumber":["40000"]}"
    ```
8. (Optional) SSH into your instance
    ```bash
    ssh -i /path/key-pair-name.pem -p 40000 ec2-user@localhost
    ```
