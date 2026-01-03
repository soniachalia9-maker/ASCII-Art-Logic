import PIL.Image
from PIL import Image, ImageDraw
import base64
import io

def create_test_image():
    """Create a simple test image if no image file exists"""
    # Create a smiley face image
    img = Image.new('RGB', (100, 100), color='white')
    draw = ImageDraw.Draw(img)
    
    # Yellow face
    draw.ellipse((10, 10, 90, 90), fill='yellow', outline='black', width=2)
    
    # Eyes
    draw.ellipse((30, 30, 40, 40), fill='black')
    draw.ellipse((60, 30, 70, 40), fill='black')
    
    # Smile
    draw.arc((30, 50, 70, 80), 0, 180, fill='black', width=3)
    
    # Save it
    img.save('test_smiley.png')
    print("Created test image: test_smiley.png")
    return 'test_smiley.png'

def image_to_ascii(image_path, output_width=100):
    # 1. Define the ASCII characters from darkest to lightest
    ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

    try:
        # 2. Open the image
        img = PIL.Image.open(image_path)
        print(f"Successfully loaded image: {image_path}")
        print(f"Original size: {img.size}")
    except:
        print(f"Unable to find image at path: {image_path}")
        print("Creating a test image instead...")
        image_path = create_test_image()
        img = PIL.Image.open(image_path)

    # 3. Resize the image
    # ASCII characters are taller than they are wide, so we adjust height by 0.55
    width, height = img.size
    aspect_ratio = height / width
    new_height = int(output_width * aspect_ratio * 0.55)
    print(f"Resizing to: {output_width} x {new_height}")
    img = img.resize((output_width, new_height))

    # 4. Convert image to Grayscale
    img = img.convert("L")

    # 5. Map pixels to ASCII characters
    pixels = img.getdata()
    new_pixels = [ASCII_CHARS[pixel // 25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)

    # 6. Format the string into the correct width
    ascii_image = [new_pixels[index:index + output_width] 
                   for index in range(0, len(new_pixels), output_width)]
    
    ascii_image = "\n".join(ascii_image)

    # 7. Print and Save the result
    print("\n" + "="*50)
    print("ASCII ART OUTPUT:")
    print("="*50 + "\n")
    print(ascii_image)
    
    # Save to a text file
    with open("ascii_art.txt", "w") as f:
        f.write(ascii_image)
    print("\n" + "="*50)
    print("[✓] ASCII art saved to 'ascii_art.txt'")
    print(f"[✓] Output width: {output_width} characters")
    print(f"[✓] Total characters: {len(new_pixels)}")
    print("="*50)

# --- RUN THE CODE ---
print("ASCII Art Converter")
print("="*50)

# Try to use 'your_photo.jpg', if not found, create a test image
image_to_ascii('your_photo.jpg', output_width=60)

# Optional: Uncomment below to see different sizes
# print("\n\n=== Trying different width ===")
# image_to_ascii('test_smiley.png', output_width=80) for linkedin post
