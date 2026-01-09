from g4f.client import Client

def generate_image(prompt: str, model: str = "flux"):
    print(f"Generating: '{prompt}'...")
    
    try:
        client = Client()
        response = client.images.generate(
            model=model,
            prompt=prompt,
            response_format="url"
        )
        
        return response.data[0].url
            
    except Exception as e:
        print(f"Error: {e}")
        return None
    