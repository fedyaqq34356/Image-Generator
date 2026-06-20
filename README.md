# G4F Image Generator

A Python-based image generation tool using the g4f library to create AI-generated images from text prompts.

![Example Generation](example.png)
*Example: Image generated with prompt "apple"*

## Features

- 🎨 High-quality image generation using flux-pro model
- 💾 Automatic saving to local directory
- ⚡ Simple command-line interface
- 🔧 Modular code structure
- 🌐 Uses any available g4f provider

## Requirements

- Python 3.10+
- Internet connection

## Installation

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/g4f-image-generator.git
cd g4f-image-generator
```

2. Create virtual environment:

```bash
python -m venv venv
```

3. Activate virtual environment:

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the generator:

```bash
python main.py
```

Enter your prompt when asked:

```
Enter prompt: a beautiful sunset over the ocean
```

Generated images will be saved in the `generated_images/` directory with timestamps.

## Configuration

Edit `config.py` to customize settings:

```python
OUTPUT_DIR = "generated_images"      # Output directory
DEFAULT_MODEL = "flux-pro"           # AI model to use
TIMESTAMP_FORMAT = "%Y%m%d_%H%M%S"   # Filename timestamp format
```

## Project Structure

```
g4f-image-generator/
├── main.py              # Entry point and user interface
├── generator.py         # Image generation logic
├── file_handler.py      # File saving functionality
├── config.py            # Configuration settings
├── requirements.txt     # Python dependencies
├── generated_images/    # Output directory (created automatically)
└── README.md           # This file
```

## How It Works

1. **Input**: User enters a text prompt
2. **Generation**: g4f client generates image using flux-pro model
3. **Download**: Image URL is fetched and downloaded
4. **Save**: Image is saved with timestamp in `generated_images/` directory

## Dependencies

- `g4f` - Free GPT-4 API client with image generation support
- `requests` - HTTP library for downloading images

## Troubleshooting

### Generation fails

- Check your internet connection
- Try again (g4f automatically selects available providers)
- Wait a few seconds and retry

### Import errors

- Reinstall dependencies: `pip install -r requirements.txt --upgrade`
- Check Python version: `python --version` (3.10+ required)

### Permission errors

- Ensure write permissions for the project directory
- Run with appropriate user permissions

## Examples

### Basic usage:
```bash
python main.py
Enter prompt: red apple with water drops
```

### Output:
```
Generating: 'red apple with water drops'...
✓ Saved: generated_images/image_20260109_143052.png

✓ Done!
```

## License

GNU General Public License v3.0 - see LICENSE file for details.

## Acknowledgments

- [g4f](https://github.com/xtekky/gpt4free) - GPT4Free library
- flux-pro model for high-quality image generation

Built with Python and g4f.