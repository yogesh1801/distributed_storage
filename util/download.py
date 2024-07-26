def download(client, bucket_name, file_name, file_path):
    try:
        result = client.fget_object(bucket_name, file_name, file_path)
        return
    except Exception as e:
        print(f"Error downloading file: {str(e)}")
        return None