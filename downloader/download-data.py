import yfinance as yf
import pandas as pd
from datetime import date, timedelta
from io import BytesIO
import boto3
from secret import Access_key, Secret_access_key

region_name= 'us-west-1'

def download_stocks_data():
    # Create a single boto3 session with the credentials
    session = boto3.Session(
        aws_access_key_id=Access_key,
        aws_secret_access_key=Secret_access_key,
        region_name=region_name
    )

    # Create a single S3 client from this session
    s3_client = session.client('s3')

    end_date = date.today()
    start_date = end_date - timedelta(days=365)
    bucket_name = 'blackjek-bucket-unique'

    with open('stocks.txt', 'r') as f:
        for ticker in f:
            Symbol = ticker.strip()
            df = yf.download(Symbol, start=start_date, end=end_date, interval="1d")
            csv_buffer = BytesIO()
            df.to_csv(csv_buffer, index=False)
            csv_buffer.seek(0)

            # Upload to S3
            s3_object_name = f'{Symbol}.csv'

            try:
                s3_client.upload_fileobj(csv_buffer, bucket_name, s3_object_name)
                print(f"DataFrame uploaded to S3://{bucket_name}/{s3_object_name}")
            except Exception as e:
                print(f"Error uploading {Symbol}: {str(e)}")

if __name__ == "__main__":
    download_stocks_data()
