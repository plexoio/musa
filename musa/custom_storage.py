from cloudinary_storage.storage import StaticHashedCloudinaryStorage


class CustomCloudinaryStorage(StaticHashedCloudinaryStorage):

    def _exists_with_etag(self, name, content):
        """
        Override this method to implement custom logic
        or simply return False to bypass the check.
        """
        # For demonstration purposes, we're simply bypassing the check.
        # You can implement custom logic here if needed.
        return False
