def create_bucket(client, bucket_name):
    if not client.bucket_exists(bucket_name):
        client.make_bucket(bucket_name)
        print(f"Bucket '{bucket_name}' created successfully")
    else:
        print(f"Bucket '{bucket_name}' already exists")