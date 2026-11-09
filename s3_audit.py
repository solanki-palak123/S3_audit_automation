import boto3
from botocore.exceptions import ClientError

# s3 client generation

s3=boto3.client("s3", region_name="ap-southeast-2")
bucket_name="palak-boto3-practice-2026"


try:
   # Bucket access

   response=s3.head_bucket(Bucket=bucket_name)

   paginator=s3.get_paginator("list_objects_v2")

   count=0

   # Report file generation

   with open("s3_audit_report.txt", "w") as file:

      file.write("s3 audit Report\n")
      file.write(f"Bucket Name:{bucket_name}\n")
      file.write(f"Bucket Access Status: Accessible\n") 
      file.write(f"HTTP Status Code: {response['ResponseMetadata']['HTTPStatusCode']}\n\n")

   # Access logs files over 1000+ by using paginator

      for page in paginator.paginate(Bucket=bucket_name, Prefix="logs/"):
        for obj in page.get("Contents", []):

           if obj["Key"].endswith ("/"):
             pass

           else:
               count += 1

               file.write(f"File Name:{obj["Key"]}\n")
               file.write(f"File Size:{obj["Size"]}\n")
               file.write(f"last modified:{obj["LastModified"]}\n\n")

      file.write(f"total log files :{count}\n")

   # if log files are not present

      if count==0:
          file.write("No logs file found\n")

   print("Audit report generated successfilly")

  # Handle AWS errors

except ClientError as e:
   Error_code=e.response["Error"]["Code"]
   if Error_code=="403":
      print("Access denied")
   elif Error_code=="404":
      print("NoSuchBucket")
   else:
      print("Unkown error")
