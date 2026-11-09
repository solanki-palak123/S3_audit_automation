# S3 Audit Automation using Boto3

## Overview
A Python-based automation project that audits an AWS S3 bucket using Boto3.

## Features
- Checks S3 bucket accessibility.
- Lists objects from the `logs/` prefix.
- Skips empty folder marker objects.
- Displays log file name, size, and last modified date.
- Uses S3 paginator to handle multiple pages of objects.
- Handles AWS ClientError exceptions.
- Generates an audit report in a text file.

## Technologies
- Python 3
- AWS S3
- Boto3
- Git and GitHub

## Prerequisites
- Python 3 installed
- Boto3 installed
- AWS CLI configured
- Appropriate IAM permissions

## Installation

```bash
pip install boto3
```

## Configuration

Configure AWS credentials securely using AWS CLI:

```bash
aws configure
```

## Run the Project

```bash
python3 s3_audit.py
```

## Output

The script generates `s3_audit_report.txt`, containing:

- Bucket name
- Bucket access status
- HTTP status code
- Log file names
- File sizes
- Last modified timestamps
- Total number of log files

## Security
- AWS credentials are not stored in the source code.
- Generated reports and virtual environments are excluded using `.gitignore`.
- The project does not change or delete S3 objects.
