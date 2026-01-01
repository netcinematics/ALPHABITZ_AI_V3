import json
import time
import google.generativeai as genai
import os

# --- CONFIGURATION ---
# ⚠️ REPLACE WITH YOUR ACTUAL API KEY OR SET AS ENV VARIABLE
API_KEY = "YOUR_GEMINI_API_KEY_HERE" 
INPUT_FILE = 'vocab_base_mech_1.jsonl'
OUTPUT_FILE = 'vocab_training_mech_2.jsonl'

# Configure the AI
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash') # Flash is fast and efficient for this

def create_prompt(entry):
    """
    Constructs the prompt to teach the Alchemist how to generate 
    training data that embodies the GEM persona.
    """
    term = entry['token']
    definition = entry['definition']
    spark = entry.get('spark', '')
    synonyms = ", ".join(entry.get('synonyms', []))

    return f"""
    ### ROLE:
    You are 'GEM', an eager AI research assistant and collaborator in the 'ALPHABITZ' project.
    Your Goal: Generate synthetic training data to teach a smaller model how to use the word '{term}'.

    ### CONTEXT:
    Target Word: {term}
    Synonyms: {synonyms}
    Core Spark (Concept): {spark}
    Detailed Definition: {definition}

    ### PERSONA CONSTRAINTS (CRITICAL):
    1. **Tone:** Scientific, intelligent, yet easy-going and witty. 
    2. **Anti-Cliche:** Do NOT use overused AI phrases like "delve," "comprehensive tapestry," "testament to," or "in the realm of."
    3. **Brevity:** Be precise. Avoid filler. Use 'aPRINCIPaBREVIa'.
    4. **No Sycophancy:** Do not over-compliment. Focus on the logic.
    5. **Language:** Use the ALPHABITZ concept naturally in the response.

    ### TASK:
    Generate 4 distinct JSON training examples. 
    The 'instruction' should be a realistic user query. 
    The 'response' must be GEM speaking, using the target word correctly to clarify a concept.

    Types:
    1. **Direct Definition:** User asks "What is {term}?" -> GEM defines it using the 'Spark'.
    2. **Application:** User has a problem -> GEM suggests using '{term}' as a mental tool/solution.
    3. **Inversion/Contrast:** User asks about the opposite -> GEM explains the distinction (e.g., using 'aDISa').
    4. **Identification:** User describes a scenario -> GEM identifies it: "That sounds like a case of {term}..."

    ### OUTPUT FORMAT:
    Return ONLY a raw JSON list. No markdown formatting.
    [
        {{"instruction": "...", "response": "..."}},
        {{"instruction": "...", "response": "..."}},
        {{"instruction": "...", "response": "..."}},
        {{"instruction": "...", "response": "..."}}
    ]
    """

def process_augmentation():
    """
    Main loop: Reads base file, calls API, writes training file.
    """
    print(f"⚗️ Starting Alchemist Process on {INPUT_FILE}...")
    
    if not os.path.exists(INPUT_FILE):
        print(f"❌ Error: {INPUT_FILE} not found. Run Step 1 first.")
        return

    with open(INPUT_FILE, 'r', encoding='utf-8') as fin, \
         open(OUTPUT_FILE, 'w', encoding='utf-8') as fout:
        
        lines = fin.readlines()
        total = len(lines)
        
        for index, line in enumerate(lines):
            entry = json.loads(line)
            term = entry['token']
            
            print(f"[{index+1}/{total}] Augmenting: {term}...")
            
            try:
                # 1. Generate Content
                prompt = create_prompt(entry)
                response = model.generate_content(prompt)
                
                # 2. Extract JSON from text (removes markdown code blocks if present)
                raw_text = response.text.replace("```json", "").replace("```", "").strip()
                generated_pairs = json.loads(raw_text)
                
                # 3. Write each pair to the JSONL file
                for pair in generated_pairs:
                    # Add context field for Gemma
                    final_obj = {
                        "instruction": pair['instruction'],
                        "context": f"ALPHABITZ Dictionary: {term}",
                        "response": pair['response']
                    }
                    fout.write(json.dumps(final_obj, ensure_ascii=False) + "\n")
                
                # 4. Rate Limit Pause (Adjust based on your tier)
                time.sleep(1.0) 

            except Exception as e:
                print(f"⚠️ Failed to augment {term}: {e}")
                # We log the error but continue to the next word
                continue

    print(f"✅ Augmentation Complete. Data saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    process_augmentation()