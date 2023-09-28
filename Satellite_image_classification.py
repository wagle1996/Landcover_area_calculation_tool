import rasterio
import numpy as np

# Define the path to the satellite image file (e.g., a GeoTIFF file)
satellite_image_path = 'C:/Land_cover/landcover.tif'

# Open the satellite image using rasterio
with rasterio.open(satellite_image_path) as src:
    # Read the image as a numpy array
    image_data = src.read()

    # Extract the spatial information (e.g., land cover types)
    # You may need to adjust the bands and thresholds based on your specific data
    # In this example, we assume a simplified classification where:
    # - 1 represents urban areas
    # - 2 represents vegetation
    # - 3 represents water bodies
    # You should adapt these values to match your actual data
    urban_areas = np.where(image_data == 1, 1, 0)
    vegetation = np.where(image_data == 2, 1, 0)
    water_bodies = np.where(image_data == 3, 1, 0)

# Calculate statistics or perform further analysis as needed
urban_area_percentage = np.sum(urban_areas) / np.sum(image_data)
vegetation_percentage = np.sum(vegetation) / np.sum(image_data)
water_bodies_percentage = np.sum(water_bodies) / np.sum(image_data)

# Print the results
print(f"Urban Area Percentage: {urban_area_percentage * 100}%")
print(f"Vegetation Percentage: {vegetation_percentage * 100}%")
print(f"Water Bodies Percentage: {water_bodies_percentage * 100}%")
