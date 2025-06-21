# HTML CSS Class Extractor 🎨

This Python script is designed to extract all CSS class names from HTML files. It's ideal for analyzing and listing CSS classes used in large HTML projects.

## 📋 Features

- ✅ Extracts all CSS class names from HTML files
- ✅ Removes duplicate classes
- ✅ Alphabetical sorting
- ✅ Provides detailed statistics
- ✅ Outputs results to both console and file
- ✅ UTF-8 encoding support
- ✅ CSS class prefix analysis
- ✅ Error handling included

## 🛠️ Requirements

- Python 3.6+
- BeautifulSoup4 library

## 📦 Installation

### 1. Install Python Package

```bash
pip install beautifulsoup4
```

### 2. Download the Script

Add `extract_classes.py` file to your project.

## 🚀 Usage

### Basic Usage

```bash
python extract_classes.py
```

The script searches for and analyzes `index.html` file by default.

### For Different HTML File

Change the `html_file` variable in the `main()` function:

```python
html_file = "your-file.html"  # Change the filename
```

## 📊 Output Format

The script produces two types of output:

### 1. Console Output
```
Extracting CSS class names from HTML file...
File: index.html
--------------------------------------------------

Found CSS Class Names (223 total):
--------------------------------------------------
  1. active
  2. colorred
  3. deleteIcon_container
  ...

📊 Statistics:
   • Total unique classes: 223
   • Longest class name: product_slider__content_list_item_details_price_detail_price_inbasket_text
   • Shortest class name: fab

🏷️  Most common class prefixes:
   • footer_*: 48 items
   • navbar_*: 43 items
   • product_*: 24 items
```

### 2. File Output (`css_classes.txt`)
```
All CSS Class Names from HTML File
==================================================

  1. active
  2. colorred
  3. deleteIcon_container
  ...

Total: 223 unique classes found.
```

## 🔧 Functions

### `extract_classes_from_html(file_path)`
- **Parameter**: Path to HTML file
- **Returns**: Sorted CSS class list
- **Description**: Parses HTML file and extracts all CSS classes

### `save_classes_to_file(classes, output_file)`
- **Parameters**: 
  - `classes`: CSS class list
  - `output_file`: Output file name
- **Description**: Saves class list to file in formatted way

### `main()`
- **Description**: Manages main program flow and displays statistics

## 🎯 Use Cases

### 1. CSS Cleanup
To find unused CSS classes:
```python
# Compare extracted classes from HTML with your CSS file
html_classes = extract_classes_from_html("index.html")
```

### 2. Component Analysis
To analyze which components use the most classes:
```python
# Use prefix analysis results
# Example: footer_* → 48 items (Footer component might be too complex)
```

### 3. Code Review
To check CSS class naming conventions in large projects.

## ⚙️ Customization

### Different Output Formats

To change the output format, modify the `save_classes_to_file()` function:

```python
# To save in JSON format:
import json

def save_classes_to_json(classes, output_file):
    data = {
        "total_classes": len(classes),
        "classes": classes,
        "timestamp": datetime.now().isoformat()
    }
    
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
```

### CSS File Comparison

```python
def compare_with_css(html_classes, css_file):
    """Compare HTML classes with CSS file classes"""
    with open(css_file, 'r', encoding='utf-8') as file:
        css_content = file.read()
    
    unused_classes = []
    for cls in html_classes:
        if f".{cls}" not in css_content:
            unused_classes.append(cls)
    
    return unused_classes
```

## 🐛 Troubleshooting

### Common Errors

1. **`ModuleNotFoundError: No module named 'bs4'`**
   ```bash
   pip install beautifulsoup4
   ```

2. **`FileNotFoundError: [Errno 2] No such file or directory: 'index.html'`**
   - Make sure the HTML file is in the correct location
   - Check the filename

3. **`UnicodeDecodeError`**
   - Check the encoding of your HTML file
   - The script uses UTF-8 encoding

### Debug Mode

To add logging for debug information:

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Usage in functions:
logger.debug(f"Processing element: {element.name}")
```

## 📁 File Structure

```
project/
├── extract_classes.py    # Main script
├── index.html           # HTML file to analyze
├── css_classes.txt      # Output file (auto-generated)
└── README.md           # This file
```

## 🤝 Contributing

1. Fork the project
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is distributed under the MIT License.

## 🔗 Related Projects

- [CSS Unused](https://github.com/uncss/uncss) - Removes unused CSS
- [PurifyCSS](https://github.com/purifycss/purifycss) - CSS optimization
- [Critical](https://github.com/addyosmani/critical) - Critical CSS extraction

## 📞 Contact

You can open an issue or send a pull request for any questions.
