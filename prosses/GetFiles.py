from secret import Access_key, Secret_access_key
import boto3
import pandas as pd
from io import StringIO
from TryAlert import detect_ema_cross

region_name= 'us-west-1'

def read_s3_csv_files(bucket_name):
    session = boto3.Session(
        aws_access_key_id=Access_key,
        aws_secret_access_key=Secret_access_key,
        region_name=region_name
    )
    # Initialize a session using Amazon S3
    s3 = boto3.client('s3')
    
    try:
        # List the objects in the bucket
        response = s3.list_objects_v2(Bucket=bucket_name)
        
        if 'Contents' in response:
            for obj in response['Contents']:
                file_key = obj['Key']
                
                # Assuming all files are CSV
                if file_key.endswith('.csv'):
                    # Fetch the file from S3
                    file_obj = s3.get_object(Bucket=bucket_name, Key=file_key)
                    file_content = file_obj['Body'].read().decode('utf-8')
                    
                    # Read the CSV file into a pandas DataFrame
                    stock_data = pd.read_csv(StringIO(file_content), parse_dates=['Date'], index_col='Date')
                    print(file_key)
                    detect_ema_cross(stock_data)
        else:
            print(f"No contents found in the bucket {bucket_name}.")
    except Exception as e:
        print(f"Error fetching the bucket contents: {e}")

if __name__ == "__main__":
    read_s3_csv_files('blackjek-bucket-unique')