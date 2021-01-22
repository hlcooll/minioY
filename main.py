from minio import Minio
from minio.error import S3Error
from progress.prog import Progress

minioClient = Minio('127.0.0.1:9000',
                  access_key='usename',
                  secret_key='password',secure=False
                  )

# Create bucket.
class minioCreateBucket(object):
    #init
    def __init__(self,newPersonName):
        self.name=newPersonName
        try:
            minioClient.make_bucket(self.name, location="us-east-1")
        except S3Error as err:
            print(err)

    # Upload data.
    def upload(self,object,filename):
        try:
            minioClient.fput_object(self.name, object,
                                    filename)
        except FileNotFoundError as err:
            print(err)
        except S3Error as err:
            print(err)

    # Upload data with progress bar.
    def uploadResult(self,object,filename):
        result = minioClient.fput_object(
            self.name, object, filename,
            progress=Progress(),
        )
        print(
            "created {0} object; etag: {1}, version-id: {2}".format(
                result.object_name, result.etag, result.version_id,
            ),
        )

if __name__ == '__main__':
    object_name='sw.md'
    filename_url="/Users/hualei/hugo/hlcooll.github.io/content/kubernetes/ceph/ceph.md"
    miniB = minioCreateBucket("maylogs")
    miniB.uploadResult(object_name,filename_url)

