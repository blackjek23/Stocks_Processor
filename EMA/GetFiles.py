from secret import Access_key, Secret_access_key
import boto3
import pandas as pd
from io import StringIO
from EMAclac import detect_ema_cross

region_name= 'us-west-1'

def read_s3_csv_files():
    session = boto3.Session(
        aws_access_key_id=Access_key,
        aws_secret_access_key=Secret_access_key,
        region_name=region_name
    )
    # Initialize a session using Amazon S3
    s3 = session.client('s3')

    bucket_name = 'blackjek-bucket-unique'
    
    try:
        # List the objects in the bucket
        response = s3.list_objects_v2(Bucket=bucket_name)
        
        if 'Contents' in response:
            # open the output file
            with open('./output/ema.txt', 'w') as output_file:
                for obj in response['Contents']:
                    file_key = obj['Key']
                    
                    # Assuming all files are CSV
                    if file_key.endswith('.csv'):
                        # Fetch the file from S3
                        file_obj = s3.get_object(Bucket=bucket_name, Key=file_key)
                        file_content = file_obj['Body'].read().decode('utf-8')
                        
                            # Read the CSV file into a pandas DataFrame
                        stock_data = pd.read_csv(StringIO(file_content), parse_dates=['Date'], index_col='Date')
                            
                        last_cross_row = detect_ema_cross(stock_data, output_file)
            
                        if last_cross_row is not None:
                            # Write the ticker name and the last row to the alerts file
                            output_file.write(f"Ticker: {file_key}\n")
                            output_file.write(f"Date: {last_cross_row.name}\n")
                            output_file.write(f"{last_cross_row.to_string()}\n")
                            output_file.write("\n")  # Add a newline for separation between entries
        else:
            print(f"No contents found in the bucket {bucket_name}.")
    except Exception as e:
        print(f"Error fetching the bucket contents: {e}")

if __name__ == "__main__":
    read_s3_csv_files()