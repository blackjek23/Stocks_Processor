import boto3
from secret import Access_key, Secret_access_key, region_name

def delete_stocks_data():
    # Create a single boto3 session with the credentials
    session = boto3.Session(
        aws_access_key_id=Access_key,
        aws_secret_access_key=Secret_access_key,
        region_name=region_name
    )
    
    # Create a single S3 client from this session
    s3_client = session.client('s3')
    
    bucket_name = 'blackjek-bucket-unique'
    
    with open('stocks.txt', 'r') as f:
        for ticker in f:
            Symbol = ticker.strip()
            s3_object_name = f'{Symbol}.csv'
            
            try:
                s3_client.delete_object(Bucket=bucket_name, Key=s3_object_name)
                print(f"Deleted file from S3://{bucket_name}/{s3_object_name}")
            except Exception as e:
                print(f"Error deleting {Symbol}: {str(e)}")

if __name__ == "__main__":
    delete_stocks_data()
