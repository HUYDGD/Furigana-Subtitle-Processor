import MeCab
import re
import sys
import os

def add_furigana_to_line(text):
    # Ensure MeCab uses the correct dictionary path for IPAdic
    ipadic_path = r"C:\\Users\\%user%\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\ipadic\\dicdir"
    
    # Set the environment variable for MeCab (this tells MeCab where the dictionary is located)
    os.environ['MECAB_PATH'] = r'C:\\Program Files (x86)\\MeCab\\bin\\mecab.exe'  # Adjust this path if needed
    os.environ['MECAB_DICDIR'] = ipadic_path

    # Initialize MeCab Tagger with -Ochasen output format and the IPAdic dictionary
    tagger = MeCab.Tagger(f"-Ochasen -d {ipadic_path}")
    
    # Remove EOS from the subtitle
    text = text.replace("EOS", "").strip()

    result = []
    words = tagger.parse(text).splitlines()

    for word in words:
        word_info = word.split("\t")
        if len(word_info) >= 2:
            kanji = word_info[0]
            reading = word_info[1]

            # Only add furigana to kanji characters
            if re.search(r'[\u4e00-\u9fff]', kanji):  # Check if the word contains kanji
                # Check if the reading is different from the kanji itself and add furigana only once
                if reading != "*" and reading != kanji and reading not in ''.join(result):
                    # Format the furigana using parentheses
                    result.append(f"{kanji}({reading})")
                else:
                    result.append(kanji)  # If no reading or the reading is the same as the kanji, just append the kanji
            else:
                result.append(kanji)  # For hiragana/katakana, no furigana added

    # Join the processed words back into a string
    return ''.join(result)

def process_ass_file(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        processed_lines = []

        for line in lines:
            if line.startswith("Dialogue"):
                parts = line.split(",", 9)
                if len(parts) > 9:
                    original_text = parts[9]
                    # Process only the dialogue text (the 10th part)
                    processed_text = add_furigana_to_line(original_text)
                    # Rebuild the line with the furigana text
                    parts[9] = processed_text
                    processed_line = ",".join(parts)
                    processed_lines.append(processed_line + "\n")
                else:
                    processed_lines.append(line)
            else:
                processed_lines.append(line)

        with open(output_file, 'w', encoding='utf-8') as file:
            file.writelines(processed_lines)

        print(f"Processing complete. Output file: {output_file}")

    except Exception as e:
        print(f"Error processing file: {e}")

def process_srt_file(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        processed_lines = []
        subtitle_text = ""

        for line in lines:
            if line.strip().isdigit() or "-->" in line:
                # Copy subtitle numbers and timestamps without modification
                processed_lines.append(line)
            else:
                # Process the subtitle text and add furigana
                subtitle_text = line.strip()
                processed_text = add_furigana_to_line(subtitle_text)
                processed_lines.append(processed_text + "\n")

        # Write the processed lines to the new SRT file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.writelines(processed_lines)

        print(f"Processing complete. Output file: {output_file}")

    except Exception as e:
        print(f"Error processing file: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python furigana.py <input_file>.ass or <input_file>.srt")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = input_file.replace(".", "_with_furigana.")

    if input_file.endswith(".ass"):
        print(f"Processing ASS file: {input_file}")
        output_file = output_file.replace(".ass", ".ass")
        process_ass_file(input_file, output_file)
    elif input_file.endswith(".srt"):
        print(f"Processing SRT file: {input_file}")
        output_file = output_file.replace(".srt", ".srt")
        process_srt_file(input_file, output_file)
    else:
        print("Invalid file format. Please provide a valid .ass or .srt file.")
        sys.exit(1)

if __name__ == "__main__":
    main()
