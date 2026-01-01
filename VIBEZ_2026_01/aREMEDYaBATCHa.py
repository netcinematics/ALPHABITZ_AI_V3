import os
import re

class aREMEDYaBATCHa:
    def __init__(self, memz_path="MEMZ/"):
        self.memz_path = memz_path
        self.void_registry = []
        self.processed_memz = 0

    def compile_memz(self):
        print(f"--- INITIALIZING aREMEDYaBATCHa: SCANNING FOR aGAPZa ---")
        
        # Ensure the directory exists
        if not os.path.exists(self.memz_path):
            print(f"[!] Path {self.memz_path} not found. Awaiting user input...")
            return

        for filename in os.listdir(self.memz_path):
            if filename.endswith(".md"):
                self.processed_memz += 1
                with open(os.path.join(self.memz_path, filename), 'r') as f:
                    content = f.read()
                    self._extract_metadata(content, filename)

        self._generate_report()

    def _extract_metadata(self, content, filename):
        # Extract Status and Voids using Regex
        status_match = re.search(r"\*\*Status:\*\* \[(.*?)\]", content)
        void_match = re.search(r"\*\*aVOIDZa Identified:\*\* \[(.*?)\]", content)
        
        status = status_match.group(1) if status_match else "UNKNOWN"
        void = void_match.group(1) if void_match else "NONE"

        if status == "aMULLa" or void != "NONE":
            self.void_registry.append({
                "file": filename,
                "void": void,
                "status": status
            })

    def _generate_report(self):
        print(f"\n--- SCAN COMPLETE: {self.processed_memz} TXTZ PROCESSED ---")
        if not self.void_registry:
            print("[✓] aFOGaFREEa: No conceptual gaps detected in processed MEMZ.")
        else:
            print(f"[!] {len(self.void_registry)} aGAPZa IDENTIFIED. Wordcraft required:")
            print("-" * 50)
            for entry in self.void_registry:
                print(f"FILE: {entry['file']} | VOID: {entry['void']} | ACTION: aDECIPHERZa")

# --- EXECUTION ---
# This will run once your folder 'MEMZ' is populated with the TXTZ templates.
processor = aREMEDYaBATCHa()
processor.compile_memz()