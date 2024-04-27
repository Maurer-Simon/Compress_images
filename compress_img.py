from PIL import Image
import os

IMAGE_WIDTH = 1000 #If the image is wider than it is tall, it will be set to this width.
IMAGE_HEIGHT = 600 #If the image is taller than it is wide, it will be set to this height.


def compress_image(image_path, output_path, quality_threshold):
    # Open the image
    with Image.open(image_path) as img:
        # Check if image is wider than tall
        if img.width >= img.height:
            # Resize to width 1000px
            img = img.resize((IMAGE_WIDTH, int(img.height * (IMAGE_WIDTH / img.width))))
        else:
            # Resize to height 600px
            img = img.resize((int(img.width * (IMAGE_HEIGHT / img.height)), IMAGE_HEIGHT))

        # Get the original image size
        original_size = os.path.getsize(image_path)

        # Compress the image with quality steps until the threshold is met
        for quality in range(100, 0, -1):
            img.save(output_path, quality=quality, optimize=True)
            compressed_size = os.path.getsize(output_path)
            compression_ratio = compressed_size / original_size

            # Check if compression ratio meets the threshold
            if compression_ratio <= (1 - quality_threshold):
                break


if __name__ == "__main__":
    # Set the folder path
    folder_path = os.getcwd()

    # Set the quality threshold (20% reduction)
    quality_threshold = 0.2

    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        # Check if the file is a JPEG image
        if filename.endswith(".jpg") or filename.endswith(".jpeg"):
            # Get the input image path
            image_path = os.path.join(folder_path, filename)

            # Set the output file path
            output_path = os.path.join(folder_path, filename)

            # Compress the image
            compress_image(image_path, output_path, quality_threshold)
            print(f"Image '{filename}' compressed successfully to '{output_path}'")
