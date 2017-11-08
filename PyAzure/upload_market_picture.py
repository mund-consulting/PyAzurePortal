from azure.storage.blob import BlockBlobService

account_name = 'marketpicture'
account_key = 'MklBCTnVC0h097QAtgfdOzQ6Cnu5xcROIpRwyT7NHFDjJm/rRi2/TIF4xTKv9B2NaXJJDs3PHPaaurbw0tc6+w=='
block_blob_service = BlockBlobService(account_name = account_name, account_key = account_key)

# create container
container_name = 'mpcontainer'
block_blob_service.create_container(container_name)

# upload files
blob_name = 'Unconfirmed 690928.crdownload'
file_path = 'C:/Users/USER/Downloads/Unconfirmed 690928.crdownload'
block_blob_service.create_blob_from_path(container_name, blob_name, file_path)

# List the blobs in a container
generator = block_blob_service.list_blobs(container_name)
for blob in generator:
    print(blob.name)