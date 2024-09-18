from PIL import Image

# Original matrix dimensions
matrix_size = 100
scaling_factor = 5  # Scale up by a factor of 5

# Define shades of blue
blue_shades = [
    (255, 255, 224),  # Light yellow
    (255, 255, 102),  # Pale yellow
    (255, 255, 0),    # Yellow
    (204, 204, 0),    # Dark yellow
    (153, 153, 0)     # Mustard yellow
]

# Define save paths
save_paths = [
    r'C:\\Users\\yuval\Desktop\\img_train\\11-30%\\200%change.png',
    r'C:\\Users\\yuval\Desktop\\img_train\\11-30%\\100.0-2.png',
    r'C:\\Users\\yuval\Desktop\\img_train\\11-30%\\0.75-2.png',
    r'C:\\Users\\yuval\Desktop\\img_train\\11-30%\\0.5-2.png',
    r'C:\\Users\\yuval\Desktop\\img_train\\11-30%\\0.25-2.png'
]

# Generate and save each matrix
for shade, save_path in zip(blue_shades, save_paths):
    # Create a new image with the scaled dimensions
    new_width = matrix_size * scaling_factor
    new_height = matrix_size * scaling_factor
    image = Image.new('RGB', (new_width, new_height), 'white')

    # Fill the image with the specified shade of blue
    pixels = image.load()
    for x in range(matrix_size):
        for y in range(matrix_size):
            # Scale up the matrix value to the larger image
            for i in range(scaling_factor):
                for j in range(scaling_factor):
                    pixels[x * scaling_factor + i, y * scaling_factor + j] = shade

    # Save the image
    image.save(save_path)

print("Matrices have been created and saved.")
