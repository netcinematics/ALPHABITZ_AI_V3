import re

class LogicalLymphaticNode:
    def __init__(self):
        # Database of aTOXICaMIMICZa (Toxic Mimetic Pathogens)
        self.fog_pathogens = {
            "it is what it is": {"type": "aSTATICa", "weight": 0.9, "void": "Consequence"},
            "don't overthink it": {"type": "aLIMITZa", "weight": 0.8, "void": "Complexity"},
            "common sense": {"type": "aSHROUDZa", "weight": 0.6, "void": "Nuance"},
            "at the end of the day": {"type": "aVOIDZa", "weight": 0.7, "void": "Resolution"},
            "just be happy": {"type": "aDISaPAINTZa", "weight": 0.9, "void": "Grief/Truth"},
            "life isn't fair": {"type": "aPARaLOGIXa", "weight": 0.85, "void": "Justice"}
        }

    def scan_input(self, text):
        detected_pathogens = []
        fog_score = 0.0
        
        # Normalize text for simple_word_syntax comparison
        clean_text = text.lower().strip()

        for pathogen, metadata in self.fog_pathogens.items():
            if pathogen in clean_text:
                detected_pathogens.append({
                    "phrase": pathogen,
                    "type": metadata["type"],
                    "filling_void": metadata["void"]
                })
                fog_score += metadata["weight"]

        # Normalize score between 0 and 1
        final_fog_index = min(fog_score / 2.0, 1.0) 
        return final_fog_index, detected_pathogens

    def aPURZa_output(self, fog_index, pathogens):
        if fog_index > 0.5:
            print(f"--- [!] aFOGaMENTZa DETECTED (Index: {fog_index:.2f}) ---")
            for p in pathogens:
                print(f"Pathogen: '{p['phrase']}' | Type: {p['type']} | Masking VOID: {p['filling_void']}")
            print("Action: Neutralizing input. Do not ingest logically.")
        else:
            print("--- [✓] aEXISTaEXACTZa: CLEAR VIEWS ---")
            print("Logic integrity maintained.")

# --- Execution ---
filter_system = LogicalLymphaticNode()

# Test Case: A typical "Fog-Hat" interaction
sample_input = "Look, at the end of the day, it is what it is. Just be happy and don't overthink it."

index, findings = filter_system.scan_input(sample_input)
filter_system.aPURZa_output(index, findings)