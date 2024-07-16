import boto3

def delete_data():
    bucket_name = 'blackjek-bucket-unique'
    with open('stocks.txt', 'r') as f:
        for ticker in f:
            Symbol= ticker.strip()
            target_file= (f'{Symbol}.csv')

            s3_client = boto3.client('s3')
            s3_client.delete_object(Bucket=bucket_name, Key=target_file)
            print(f"File {target_file} deleted successfully from {bucket_name}")

delete_data()