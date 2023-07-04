# Creating an AWS EC2 Instance Tutorial

In this tutorial, we will walk through the steps to create an Amazon EC2 instance.

## Prerequisites

Before we begin, make sure you have the following:

- An AWS account
- AWS CLI installed and configured on your local machine (optional)

## Step 1: Sign in to the AWS Management Console

1. Open your web browser and go to the [AWS Management Console](https://console.aws.amazon.com/).
2. Sign in to your AWS account using your credentials.

## Step 2: Navigate to EC2

1. Once you're signed in, you'll be on the AWS Management Console dashboard. Use the search bar at the top to find **EC2**.
2. Click on **EC2** to open the EC2 dashboard.

## Step 3: Launch an Instance

1. On the EC2 dashboard, click on **Launch Instance** to start the instance creation wizard.
2. Select an Amazon Machine Image (AMI) for your instance. You can choose from various pre-configured AMIs based on different operating systems and applications.
3. Choose an instance type based on your requirements. Each instance type has different specifications in terms of CPU, memory, storage, and networking capabilities.
4. Configure the instance details, such as the number of instances, network settings, security groups, and storage options. Make sure to provide necessary details like the VPC, subnet, and security group settings.
5. Review your configuration and click on **Launch**.

## Step 4: Create a Key Pair (Optional)

1. If you don't have an existing key pair, you will be prompted to create a new one. Key pairs are used for secure SSH access to your EC2 instance.
2. Choose **Create a new key pair** and provide a name for the key pair.
3. Download the key pair file (*.pem) and keep it in a secure location. This file is required to connect to your EC2 instance.

## Step 5: Access your EC2 Instance

1. Once your instance is launched, you can see its status on the EC2 dashboard.
2. Select the instance and click on **Connect**.
3. Follow the instructions to connect to your instance using SSH. If you're using the AWS CLI, you can run the following command:

```bash
ssh -i /path/to/your/keypair.pem ec2-user@<instance-public-ip>
