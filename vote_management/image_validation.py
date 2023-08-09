from django.contrib import messages


def validate_image_size(request, event_image):
    ''' Validate images based on the following conditions '''

    max_upload_size = 500000  # 500KB in bytes
    if event_image.size > max_upload_size:
        messages.error(request, "File size must not exceed 500KB.")
        return False
    return True
