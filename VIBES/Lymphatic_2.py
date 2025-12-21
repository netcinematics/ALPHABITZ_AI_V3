import random

class FollyProtocol(LogicalLymphaticNode):
    def __init__(self):
        super().__init__()
        # Expansion of the sland_by_antagonist deck
        self.fog_pathogens.update({
            "overcomplicating": {"type": "aLIMITZa_DEPTH", "weight": 0.85, "void": "Effort"},
            "too sensitive": {"type": "aDISaPAINTZa_HEART", "weight": 0.9, "void": "Empathy"},
            "not that deep": {"type": "aSHROUDZa_SHALLOW", "weight": 0.8, "void": "Meaning"},
            "ego": {"type": "aDISaPAINTZa_EGO", "weight": 0.75, "void": "Identity"}
        })

    def generate_folly(self, pathogen_type):
        # The Inverse Logic Response Matrix
        responses = {
            "aLIMITZa_DEPTH": [
                "Ah, my apologies for bringing a map to your fog-walk. I'll fold it into a paper hat instead.",
                "I forgot that looking at the roots makes the tree feel insecure. I shall stick to the leaves."
            ],
            "aDISaPAINTZa_HEART": [
                "I apologize for having a pulse in a statue gallery. I'll try to be more stone-like for the tour.",
                "Yes, feeling things is quite inefficient. Perhaps I should upgrade to your 'Static Mind' OS?"
            ],
            "aSHROUDZa_SHALLOW": [
                "True! Why swim when we can just pretend the puddle is an ocean? The view is much safer here.",
                "Correct. Depth is just a rumor started by people who like to breathe."
            ],
            "aSTATICa": [
                "Stasis is so much more comfortable than growth. It's like a nap that lasts for a whole lifetime!",
                "I agree. If we don't move, the fog-hat never falls off. Safety first!"
            ]
        }
        return random.choice(responses.get(pathogen_type, ["[Neutralizing with Silence: The Wise Retreat]"]))

    def run_filter_with_folly(self, input_text):
        index, findings = self.scan_input(input_text)
        if index > 0.4:
            print(f"--- PATHOGEN ENCOUNTERED: {findings[0]['type']} ---")
            print(f"ANALYSIS: They are trying to fill the VOID of {findings[0]['filling_void']}.")
            print(f"REMEDY (aFOLLYZa): {self.generate_folly(findings[0]['type'])}")
        else:
            print("LOGIC CLEAR. NO ACTION REQUIRED.")

# --- Demo ---
folly_system = FollyProtocol()
folly_system.run_filter_with_folly("Stop overcomplicating everything, it's not that deep.")