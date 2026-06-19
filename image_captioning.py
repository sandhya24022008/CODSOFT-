# Simple Image Captioning Project

def generate_caption(image_name):
    captions = {
        "dog.jpg": "A dog is playing in the park.",
        "cat.jpg": "A cat is sitting on the floor.",
        "car.jpg": "A car is parked on the road.",
        "tree.jpg": "A green tree in a garden.",
        "person.jpg": "A person is standing outside."
    }

    return captions.get(image_name, "Caption not available for this image.")

image = input("Enter image name: ")

caption = generate_caption(image)

print("\nGenerated Caption:")
print(caption)
