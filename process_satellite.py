import os
import cv2

# Path to the folder where images are extracted
image_folder = r"C:\Users\Dhanush\Desktop\hackathon"  # Change this to your actual folder name

# Check if the folder exists
if not os.path.exists(image_folder):
    print(f"Error: Folder not found at {image_folder}")
    exit()

# Loop through all images in the folder
for filename in os.listdir(image_folder):
    if filename.endswith((".jpg", ".png", ".tif", ".jpeg")):  # Process only image files
        image_path = os.path.join(image_folder, filename)
        image = cv2.imread(image_path)

        if image is None:
            print(f"Error: Unable to load {filename}. Skipping...")
            continue  # Skip corrupted files

        print(f"Processing: {filename}")
        cv2.imshow("Satellite Image", image)
        cv2.waitKey(500)  # Show each image for 0.5 seconds
        cv2.destroyAllWindows()

print("Processing complete!")
