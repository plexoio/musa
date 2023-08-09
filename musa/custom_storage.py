# Library Imports
from cloudinary_storage.storage import StaticHashedCloudinaryStorage
from cloudinary.api import resources_by_tag


class CustomCloudinaryStorage(StaticHashedCloudinaryStorage):
    """This class uses the resources_by_tag method,
    assuming that 'name' can be used as a tag.
    We are overriding django default expectation from Cloudinary."""

    def _exists_with_etag(self, name, content):
        try:
            resources = resources_by_tag(name)
            if resources and resources['resources']:
                return True
        except Exception as e:
            print(f"Error checking existence of file {name}: {e}")

        # If no resources are found with the given name, return False.
        return False
