import yfinance as yf
import pandas as pd
from datetime import date, timedelta
from io import BytesIO
import boto3

def download_stocks_data():
    end_date= date.today()
    start_date= end_date- timedelta(days=365)
    with open('stocks.txt', 'r') as f:
        for ticker in f:
            Symbol= ticker.strip()
            df= yf.download(Symbol, start=start_date, end= end_date, interval="1d")
            csv_buffer = BytesIO()
            df.to_csv(csv_buffer, index=False)
            csv_buffer.seek(0)
            # Create an S3 client
            s3_client = boto3.client('s3')

            # Upload to S3
            bucket_name = 'blackjek-bucket-unique'
            s3_object_name = (f'{Symbol}.csv')

            s3_client.upload_fileobj(csv_buffer, bucket_name, s3_object_name)

            print(f"DataFrame uploaded to S3://{bucket_name}/{s3_object_name}")

download_stocks_data()