# Furigana Subtitle Processor

This Python script adds furigana (pronunciation guides) to kanji characters in subtitle files. It supports both `.ass` and `.srt` subtitle formats and uses the MeCab morphological analyzer to generate the readings for kanji characters.

## Features

- **Adds furigana**: Automatically adds furigana readings to kanji characters in subtitle files.
- **Supports both `.ass` and `.srt` formats**: Process both types of subtitle files.
- **Formatting**: Furigana is added in the format `(reading)` above the kanji.

## Requirements

- Python 3.x
- MeCab and IPAdic dictionary
- `MeCab` Python bindings

### Installation

1. **Install MeCab**:
   - **Windows**: You can download and install MeCab from the official website: [https://taku910.github.io/mecab/](https://taku910.github.io/mecab/).
     - Make sure to download the version with the IPAdic dictionary included.
   - **Linux/macOS**: Install MeCab using your package manager:
     - For **Ubuntu**: 
       ```bash
       sudo apt-get install mecab libmecab-dev mecab-ipadic
       ```
     - For **macOS** (using Homebrew):
       ```bash
       brew install mecab mecab-ipadic
       ```

2. **Install Python dependencies**:
   Install the required Python libraries:
   ```bash
   pip install mecab-python3
3. **Configure MeCab:**
On Windows, you may need to adjust the path to the mecab.exe and the dictionary directory (ipadic) in the script. Modify the following paths in the code to match your installation:
MECAB_PATH (path to mecab.exe)
MECAB_DICDIR (path to IPAdic dictionary)
On Linux/macOS, the script should automatically detect the correct paths.

## Usage
### Running the Script
To run the script, execute the following command in your terminal or command prompt:
```
python furigana.py <input_file>.ass  # for .ass files
python furigana.py <input_file>.srt  # for .srt files
```
The script will process the input subtitle file, add furigana readings to the kanji characters, and generate a new subtitle file with _with_furigana added to the filename.
### Example
If you have a subtitle file example.srt, run:
```
python furigana.py example.srt
```
This will generate a new file called example_with_furigana.srt with furigana readings added to any kanji characters.
### Input Example for .srt
Input:
```
1
00:00:01,000 --> 00:00:05,000
そんなの俺耐えられない

2
00:00:06,000 --> 00:00:10,000
これが僕の戦いだ
```
Output:
```
1
00:00:01,000 --> 00:00:05,000
そんなの俺(オレ)耐えられない

2
00:00:06,000 --> 00:00:10,000
これが僕(ボク)の戦いだ
```
Input Example for .ass
Input:
```
[Events]
Dialogue: 0,0:00:01.00,0:00:05.00,Default,,0,0,0,,そんなの俺耐えられない
Dialogue: 0,0:00:06.00,0:00:10.00,Default,,0,0,0,,これが僕の戦いだ
```
Output:
```
[Events]
Dialogue: 0,0:00:01.00,0:00:05.00,Default,,0,0,0,,そんなの俺(オレ)耐えられない
Dialogue: 0,0:00:06.00,0:00:10.00,Default,,0,0,0,,これが僕(ボク)の戦いだ
```

## Notes
The script will process both the .ass and .srt formats automatically, and you can run it on either format by providing the correct file extension as an argument.
Furigana is added in the format (reading) for kanji characters.
If you have a lot of subtitle lines to process, the script might take a little time to complete, as it processes each line individually.

## Acknowledgements
MeCab: Used for Japanese morphological analysis and generating furigana readings for kanji characters.
IPAdic: The default dictionary used for generating the readings.

## Troubleshooting
MeCab not found: Ensure that mecab.exe is correctly installed and the MECAB_PATH environment variable is set correctly in the script.
Encoding issues: If you face any encoding issues, try saving the subtitle files with UTF-8 encoding and ensure that your terminal or editor supports UTF-8.

Feel free to contribute or open issues if you encounter any bugs!
