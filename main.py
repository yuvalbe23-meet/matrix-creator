from PIL import Image

# Original matrix dimensions
matrix_size = 100
scaling_factor = 5  # Scale up by a factor of 5

# Define shades of blue
blue_shades = [
    (211, 211, 211),  # Light grey
    (169, 169, 169),  # Dark grey
    (128, 128, 128),  # Grey
    (105, 105, 105),  # Dim grey
    (47, 79, 79)      # Dark slate grey
]

# Define save paths
save_paths = [
    r'C:\\Users\\yuval\Desktop\\img_train\\201-1000%\\200%change.png',
    r'C:\\Users\\yuval\Desktop\\img_train\\201-1000%\\100.0-6.png',
    r'C:\\Users\\yuval\Desktop\\img_train\\201-1000%\\0.75-6.png',
    r'C:\\Users\\yuval\Desktop\\img_train\\201-1000%\\0.5-6.png',
    r'C:\\Users\\yuval\Desktop\\img_train\\201-1000%\\0.25-6.png'
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
