import os
import requests
from datetime import datetime
from config import OUTPUT_DIR, TIMESTAMP_FORMAT

def save_image(image_url: str):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    timestamp = datetime.now().strftime(TIMESTAMP_FORMAT)
    filename = f"{OUTPUT_DIR}/image_{timestamp}.png"
    
    try:
        response = requests.get(image_url)
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"✓ Saved: {filename}")
        return filename
        
    except Exception as e:
        print(f"✗ Save error: {e}")
        return None