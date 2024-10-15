import boto3

# Configuration
s3 = boto3.client('s3')

# Function to upload files to S3

def upload_to_s3(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = file_name
    s3.upload_file(file_name, bucket, object_name)
    print(f'Uploaded {file_name} to s3://{bucket}/{object_name}')

# Upload raw data files

upload_to_s3('<your-local-path>/orders.csv', '<your-bucket>', 'ecommerce_data/raw/orders.csv')
# Repeat for other datasets
