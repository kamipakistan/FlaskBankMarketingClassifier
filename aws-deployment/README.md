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

On the EC2 dashboard, click on **Launch Instance** to start the instance creation wizard.

### A. Name and tags
* **Name**: Assign a descriptive name to the EC2 instance for easy identification and management.
* **Tags**: Additional metadata in the form of key-value pairs that can be assigned to EC2 instances. Tags are useful for organizing resources, tracking costs, and implementing management policies. Common tags include "Environment," "Project," and "Owner."

### B. Application and OS Images (Amazon Machine Image)
Select an Amazon Machine Image (AMI) for your instance. You can choose from various pre-configured AMIs based on different operating systems and applications.
    
```text
 Free tier eligible
 Ubuntu Server 22.04 LTS (HVM), SSD Volume Type 
 ami-0989fb15ce71ba39e (64-bit (x86)) / ami-0ebb6753c095cb52a (64-bit (Arm))
 Virtualization: hvm
 ENA enabled: true
 Root device type: ebs
 
 Description
 Canonical, Ubuntu, 22.04 LTS, amd64 jammy image build on 2023-05-16
 Architecture
 
 64-bit (x86)
 AMI ID
 ami-0989fb15ce71ba39e
 ```

### C. Instance type
Choose an instance type based on your requirements. Each instance type has different specifications in terms of CPU, memory, storage, and networking capabilities.
 ```text
 Free tier eligible
 
 t3.micro    Family: t3  2 vCPU  1 GiB Memory    Current generation: true
 
 On-Demand RHEL pricing: 0.0708 USD per Hour
 On-Demand SUSE pricing: 0.0108 USD per Hour
 On-Demand Linux pricing: 0.0108 USD per Hour
 On-Demand Windows pricing: 0.02 USD per Hour
 ```

### D. Create a Key Pair

1. If you don't have an existing key pair, you will be prompted to create a new one. Key pairs are used for secure SSH access to your EC2 instance.
2. Choose **Create a new key pair** and provide a name for the key pair.
3. Download the key pair file (*.pem) and keep it in a secure location. This file is required to connect to your EC2 instance.

### E. Network Settings 
AWS EC2 provides default network settings, including a default VPC, subnets, and security groups. These settings are suitable for most projects. However, if your project has specific networking requirements, you can customize the settings. Options include creating additional subnets, modifying security group rules, allocating Elastic IP addresses, and configuring load balancers for improved scalability. Assess your project's needs to determine if default settings suffice or if modifications are necessary.

### F. Configure Storage

In this section, you have the option to keep the default storage settings, which are suitable for most projects. However, if your project has specific storage requirements, you can make changes accordingly. You can customize the storage options by selecting the appropriate instance store volumes, configuring the size and type of Amazon EBS volumes, enabling encryption for enhanced security, and utilizing features like snapshots and Elastic File System (EFS). Assess your project's storage needs and decide whether to keep the default settings or make modifications to optimize storage performance and data management.

### G. Advanced Details
The "Advanced Details" section in AWS EC2 allows you to provide additional configuration details for your instances. It offers advanced options for fine-tuning and customizing your EC2 deployment according to your project's requirements. You have the flexibility to keep the default settings or make changes to suit your specific needs.

#### i. User Data

- **Default**: If you prefer, you can leave the User Data field empty to use the default settings.
- **Customization**: If desired, you can provide custom scripts or initialization commands in the User Data field to automate instance configuration, software installation, or any other tasks during instance startup.

#### ii. IAM Role

- **Default**: By default, instances are launched without an IAM role assigned.
- **Customization**: If needed, you can assign an IAM role to instances in the "Advanced Details" section. IAM roles provide temporary security credentials and permissions for accessing AWS services and resources without explicit credentials.

#### iii. Network Interfaces

- **Default**: Instances are launched with a default network interface attached.
- **Customization**: In the "Advanced Details" section, you can configure additional network interfaces as per your requirements. This can be helpful when multiple interfaces or specialized network configurations are needed.

#### iv. Shutdown Behavior

- **Default**: Instances are set to stop when shut down using the default setting.
- **Customization**: In the "Advanced Details" section, you can choose different shutdown behaviors such as stopping the instance, terminating the instance, or hibernating the instance (if supported by the instance type).

#### v.Placement Groups

- **Default**: Instances are launched without any specific placement group.
- **Customization**: If desired, you can configure placement groups to influence the placement of instances in relation to each other for achieving low-latency and high-bandwidth network connectivity.

When using the "Advanced Details" section in AWS EC2, you have the choice to keep the default settings or make changes based on your project's requirements. Customizing these advanced settings allows you to fine-tune your instances and optimize their performance, security, and connectivity.

**Note:** The exact options and configurations available may vary based on the AWS EC2 console version and region.

### Review
Review your configuration and click on **Launch**.


## Step 4: Access your EC2 Instance

1. Once your instance is launched, you can see its status on the EC2 dashboard.
2. Select the instance and click on **Connect**.
3. Follow the instructions to connect to your instance using SSH. If you're using the AWS CLI, you can run the following command:

```bash
ssh -i /path/to/your/keypair.pem ec2-user@<instance-public-ip>
