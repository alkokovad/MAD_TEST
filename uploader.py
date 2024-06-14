from minio import Minio
from minio.error import S3Error


def main(method="get", file=None, meme_id=None):
    client = Minio(
        "127.0.0.1:9000",
        access_key="b03l0mCVxeXdQMit2SIX",
        secret_key="zrQXFyAVEOkQoYI2L3qpvGnf1k9ymLL4ldbyp1CT",
        secure=False,
    )

    if method == "post" and file:
        client.put_object(
            "memes",
            file.filename,
            data=file.file,
            content_type=file.content_type,
            length=file.size,
        )

    get_files = []
    objects = list(client.list_objects("memes"))
    obj_list = [{"name": i.object_name, "last_modified": i.last_modified, "id": meme_id} for meme_id, i in
                enumerate(objects)]
    for i in obj_list:
        get_files.append(
            {"meme": client.get_presigned_url(bucket_name="memes", object_name=i["name"], method="GET"), "id": i["id"]})

    if method == "put" and meme_id is not None:
        pass
        # result = client.put_object(
        #     "memes",
        #     file.filename,
        #     data=file.file,
        #     content_type=file.content_type,
        #     length=file.size,
        # )

    if method == "delete" and meme_id is not None:
        pass
        # client.remove_object("my-bucket", "my-object")

    return get_files


if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error occurred.", exc)
