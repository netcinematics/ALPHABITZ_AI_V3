import re
import json
import sys

def parse_markdown_to_jsonl(input_file, output_file):
    """
    Parses the ALPHABITZ vocab markdown and outputs a JSONL file.
    """
    
    # 1. Initialize storage for our entries
    entries = []
    current_entry = {}
    capture_mode = None  # Tracks if we are capturing text for a specific section

    # Regex patterns based on your specific syntax
    # Finds headers like "### aWORD | Synonym | Synonym :"
    header_pattern = re.compile(r"^###\s+(.*)") 
    
    # Finds blockquotes like "> The energy source of life..."
    spark_pattern = re.compile(r"^>\s+(.*)")
    
    # Finds pronunciation like "- Pronounce:[...]"
    pronounce_pattern = re.compile(r"^-\s*Pronounce:\[(.*)\]")

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()

        # Skip empty lines if we aren't inside a definition
        if not line:
            continue

        # --- DETECT NEW ENTRY (###) ---
        if header_pattern.match(line):
            # If we were building an entry, save it before starting a new one
            if current_entry:
                entries.append(current_entry)
            
            # Reset for new entry
            raw_header = header_pattern.match(line).group(1)
            # Remove trailing colons or whitespace
            raw_header = raw_header.rstrip(' :')
            
            # Split by pipe '|' to get term and synonyms
            parts = [p.strip() for p in raw_header.split('|')]
            
            # The first part is usually the Primary Token, the rest are synonyms
            primary_token = parts[0]
            synonyms = parts[1:] if len(parts) > 1 else []

            current_entry = {
                "token": primary_token,
                "synonyms": synonyms,
                "pronunciation": "",
                "spark": "",     # The > Blockquote
                "definition": "" # The main text
            }
            continue

        # --- DETECT SPARK (>) ---
        spark_match = spark_pattern.match(line)
        if spark_match and current_entry:
            # Append to spark if multiple lines, or set it
            if current_entry["spark"]:
                current_entry["spark"] += " " + spark_match.group(1)
            else:
                current_entry["spark"] = spark_match.group(1)
            continue

        # --- DETECT PRONUNCIATION ---
        pronounce_match = pronounce_pattern.match(line)
        if pronounce_match and current_entry:
            current_entry["pronunciation"] = pronounce_match.group(1)
            continue

        # --- CAPTURE STANDARD TEXT ---
        # If it's not a header, spark, or separator, it's body text.
        # We exclude the separator lines like "___"
        if "___" in line:
            continue
            
        if current_entry:
            # Append text to the definition body
            current_entry["definition"] += line + " "

    # Don't forget to append the very last entry found in the file
    if current_entry:
        entries.append(current_entry)

    # --- WRITE TO JSONL ---
    with open(output_file, 'w', encoding='utf-8') as f:
        for entry in entries:
            # Clean up whitespace
            entry["definition"] = entry["definition"].strip()
            f.write(json.dumps(entry, ensure_ascii=False) + '\n')

    print(f"✅ Success! Parsed {len(entries)} vocab terms.")
    print(f"📂 Output saved to: {output_file}")

# --- EXECUTION ---
# You can run this by passing your filename
if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_filename = sys.argv[1]
        # Generate output name if not provided
        if len(sys.argv) > 2:
            output_filename = sys.argv[2]
        else:
            output_filename = input_filename.rsplit('.', 1)[0] + '.jsonl'
    else:
        # Defaults
        input_filename = 'AI_aVOCABZa_003.md'
        output_filename = 'vocab_base_mech_1.jsonl'
    
    try:
        parse_markdown_to_jsonl(input_filename, output_filename)
    except FileNotFoundError:
        print(f"❌ Error: Could not find file '{input_filename}'. Please check the path.")


#{"token": "aENa", "synonyms": ["Encouragement", "NET_Positive_Force"], "spark": "aEN is a CLASS_DEFINITOR...", "definition": "A linguistic root used..."} 