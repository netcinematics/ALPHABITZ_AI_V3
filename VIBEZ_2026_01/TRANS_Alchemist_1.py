import json
import random

# CONFIGURATION
input_file = "AXI_VOCABZ_001.jsonl"
# input_file = "miner_output.jsonl"
output_file = "AXI_VOCABZ_001_ready_for_gemma.jsonl"

def create_training_entries(data):
    entries = []
    
    token = data.get("token", "")
    definition = data.get("definition", "")
    spark = data.get("spark", "")
    synonyms = data.get("synonyms", [])
    
    if not token or not definition:
        return []

    # VARIATION 1: Direct Definition (The "What is" logic)
    entries.append({
        "instruction": "Define this ALPHABITZ concept.",
        "input": f"Define: {token}",
        "output": f"{definition} :: [TYPE:DEFINITION]"
    })

    # VARIATION 2: The Spark/Essence (The "Why" logic)
    if spark:
        entries.append({
            "instruction": "Identify the underlying spark or essence of this concept.",
            "input": f"What is the spark of {token}?",
            "output": f"{spark} :: [TYPE:SPARK]"
        })

    # VARIATION 3: Reverse Logic (The "WORDMATHZ" logic)
    # We give the model the definition and ask it to derive the token.
    # This teaches the model to "think" in your language.
    entries.append({
        "instruction": "Derive the ALPHABITZ token that matches this description.",
        "input": f"Concept definition: {definition[:150]}...", # Truncated for a clue
        "output": f"Token: {token} :: [DERIVATION:MATCH]"
    })

    return entries

def main():
    print(f"--- THE ALCHEMIST IS STARTING ---")
    print(f"Transmuting raw ore from {input_file}...")
    
    processed_count = 0
    generated_count = 0
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        with open(input_file, 'r', encoding='utf-8') as infile:
            for line in infile:
                if not line.strip(): continue
                try:
                    data = json.loads(line)
                    training_pairs = create_training_entries(data)
                    
                    for pair in training_pairs:
                        json.dump(pair, outfile)
                        outfile.write('\n')
                        generated_count += 1
                    
                    processed_count += 1
                except json.JSONDecodeError:
                    print(f"Skipping invalid JSON line.")

    print(f"--- TRANSMUTATION COMPLETE ---")
    print(f"Processed {processed_count} raw entries.")
    print(f"Generated {generated_count} training pairs.")
    print(f"Output saved to: {output_file}")
    print(f"You are now ready to run 'train_alphabitz.py'")

if __name__ == "__main__":
    main()