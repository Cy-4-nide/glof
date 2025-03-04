import ee

# Initialize Google Earth Engine with your project ID
ee.Initialize(project='ee-hhsunahd')  # Replace with your actual Project ID

# Define a smaller region to reduce file size
roi = ee.Geometry.Rectangle([90.2, 27.8, 90.8, 28.2])  # Smaller area in Bhutan

# Load Sentinel-2 Harmonized Image Collection (Updated dataset)
sentinel = ee.ImageCollection('COPERNICUS/S2_HARMONIZED') \
    .filterBounds(roi) \
    .filterDate('2023-01-01', '2023-12-31') \
    .sort('CLOUDY_PIXEL_PERCENTAGE') \
    .first()

# Get Image Download Link with reduced scale (lower resolution)
url = sentinel.getDownloadURL({'scale': 100, 'region': roi.getInfo()})  

print("Download Sentinel-2 Image: ", url)
