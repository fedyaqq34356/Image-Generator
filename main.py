from generator import generate_image
from file_handler import save_image
from config import DEFAULT_MODEL

def main():
    print("=" * 60)
    print("G4F Image Generator")
    print("=" * 60)
    
    prompt = input("\nEnter prompt: ").strip()
    
    if not prompt:
        print("Error: Empty prompt")
        return
    
    image_url = generate_image(prompt, DEFAULT_MODEL)
    
    if image_url:
        saved = save_image(image_url)
        if saved:
            print("\n✓ Done!")
        else:
            print("\n✗ Could not save image")
    else:
        print("\n✗ Generation failed")

if __name__ == "__main__":
    main()