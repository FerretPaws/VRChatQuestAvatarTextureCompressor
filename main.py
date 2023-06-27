import os
from PIL import Image

def resize_images(parent_folder, new_size):
    # Iterate through all subdirectories and files within the parent folder
    for root, dirs, files in os.walk(parent_folder):
        for file in files:
            # Check if the file is an image
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                file_path = os.path.join(root, file)
                
                # Open the image file
                image = Image.open(file_path)
                
                # Resize the image
                resized_image = image.resize((new_size, new_size), Image.ANTIALIAS)
                
                # Save the resized image, overwriting the original file
                resized_image.save(file_path)
                
                print(f"Resized {file} to {new_size}x{new_size}")
    
    print("Image resizing complete.")

# Example usage: Resize all images to 512x512 within the "parent_folder"
resize_images("Your Unity Project's Asset Folder goes here. Leave it at the parent folder.", 512)
