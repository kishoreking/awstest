Install aws cli - pip3 install awscli --upgrade

zappa deploy --debug

AmazonAPIGatewayAdministrator	AWS managed	Directly
AmazonAPIGatewayInvokeFullAccess	AWS managed	Directly
AmazonS3FullAccess	AWS managed	Directly
AWSCloudFormationFullAccess	AWS managed	Directly
AWSCloudFormationReadOnlyAccess	AWS managed	Directly
AWSConfigRulesExecutionRole	AWS managed	Directly
AWSLambda_FullAccess	AWS managed	Directly
CloudWatchEventsFullAccess	AWS managed	Directly
IAMFullAccess	AWS managed	Directly

User
what is s3_key?

ChatGPT
The s3_key refers to the key or path of the object within the S3 bucket where you want to upload the file. In Amazon S3, objects are stored in buckets, and each object has a unique key that serves as its identifier within the bucket.

For example, if you want to upload the file tmpfile.txt to a bucket named my-bucket and store it in a folder named folder, the s3_key would be 'folder/tmpfile.txt'.

Here's how you can use the s3_key parameter in the upload_to_s3 function:

python
Copy code
def upload_to_s3(local_file_path, bucket_name, s3_key):
    s3 = boto3.client('s3')
    s3.upload_file(local_file_path, bucket_name, s3_key)
When you call this function, you pass the local file path (local_file_path), the name of the S3 bucket (bucket_name), and the desired key (s3_key) where you want to store the file in the bucket.