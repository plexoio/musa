# Library Imports
from cloudinary_storage.storage import StaticHashedCloudinaryStorage
from cloudinary.api import resources_by_tag


class CustomCloudinaryStorage(StaticHashedCloudinaryStorage):

    def _exists_with_etag(self, name, content):
        """
        Override this method to implement custom logic.
        """
        # Use Cloudinary's API to check if a file with the given name exists.
        # This example uses the resources_by_tag method, assuming that
        # 'name' can be used as a tag.
        # Modify the logic based on your needs and Cloudinary's available APIs.
        try:
            resources = resources_by_tag(name)
            if resources and resources['resources']:
                return True
        except Exception as e:
            # Handle any exceptions that arise from the API call
            print(f"Error checking existence of file {name}: {e}")

        # If no resources are found with the given name, return False.
        return False
