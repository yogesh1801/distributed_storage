from minio import Minio
from config import *
from util.create_bucket import create_bucket
from util.upload import upload
from util.download import download
from util.summarizer import summarize
import os


client = Minio(
    f"{HOST}:9000",
    access_key=ACCESS_KEY,
    secret_key=SECRET_KEY,
    secure=False    
)


create_bucket(client=client, bucket_name="content")
create_bucket(client=client, bucket_name="results")

upload(client=client, bucket_name="content", file_name="article.txt", file_path="./article.txt")
print(f"file saved")

download(client=client, bucket_name="content", file_name="article.txt", file_path="./download.txt")
print(f"file downloaded")

summarize("./download.txt", "./output.txt")
upload(client=client, bucket_name="results", file_name="output.txt", file_path="./output.txt")
download(client=client, bucket_name="results", file_name="output.txt", file_path="downloaded_summary.txt")




