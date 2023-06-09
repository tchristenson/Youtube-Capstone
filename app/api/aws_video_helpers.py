import boto3
import botocore
import os
import uuid

BUCKET_NAME = os.environ.get("S3_VIDEO_BUCKET")
S3_LOCATION = f"http://{BUCKET_NAME}.s3.amazonaws.com/"
ALLOWED_VIDEO_EXTENSIONS = {"mp4", "mov", "wmv", "avi", "avchd", "flv", "f4v", "swf",
                      "mkv", "webm", "html5", "mpeg1", "mpeg2", "mpeg4", "3gp",
                      "ogg", "m4v", "mp4v", "webm"}

s3 = boto3.client(
   "s3",
   aws_access_key_id=os.environ.get("S3_KEY"),
   aws_secret_access_key=os.environ.get("S3_SECRET")
)

def get_unique_video_filename(filename):
    ext = filename.rsplit(".", 1)[1].lower()
    unique_filename = uuid.uuid4().hex
    return f"{unique_filename}.{ext}"

def upload_video_file_to_s3(file, acl="public-read"):
    try:
        print('s3 ======>>>>>>>', s3)
        print('S3_KEY ========>>>>>>>>>', os.environ.get("S3_KEY"))
        print('S3_SECRET ========>>>>>>>>>', os.environ.get("S3_SECRET"))
        print('file inside AWS upload function ========>>>>>>>>>', file)
        print('type(file) inside AWS upload function ========>>>>>>>>>', type(file))
        print('BUCKET_NAME inside AWS upload function ========>>>>>>>>>', BUCKET_NAME)
        print('type(BUCKET_NAME) inside AWS upload function ========>>>>>>>>>', type(BUCKET_NAME))
        print('file.filename inside AWS upload function ========>>>>>>>>>', file.filename)
        print('type(file.filename) inside AWS upload function ========>>>>>>>>>', type(file.filename))
        s3.upload_fileobj(
            file,
            BUCKET_NAME,
            file.filename,
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type
            }
        )
    except Exception as e:
        # in case the our s3 upload fails
        print("errors======>>>>>>>>>", str(e))
        return {"errors": str(e)}

    return {"url": f"{S3_LOCATION}{file.filename}"}

def remove_video_file_from_s3(image_url):
    # AWS needs the image file name, not the URL,
    # so we split that out of the URL
    key = image_url.rsplit("/", 1)[1]
    # print(key)
    try:
        s3.delete_object(
        Bucket=BUCKET_NAME,
        Key=key
        )
    except Exception as e:
        return { "errors": str(e) }
    return True
