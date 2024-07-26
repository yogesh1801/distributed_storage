def upload(client, bucket_name, file_name, file_path):
    try:
        result = client.fput_object(bucket_name, file_name, file_path)
        return
    except Exception as e:
        print(f"Error uploading file: {str(e)}")
        return None