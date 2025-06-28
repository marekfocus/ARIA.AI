import os
import json
import datetime
from aria_controller import analyze_file

DOCUMENTS_DIR = "./documents"
RESULTS_FILE = "analysis_results.json"
MEMORY_FILE = "logs/memory.json"

results = {}

for filename in os.listdir(DOCUMENTS_DIR):
    if filename.endswith(".txt"):
        file_path = os.path.join(DOCUMENTS_DIR, filename)
        print(f"🔍 Analyzing {filename}...")
        try:
            result = analyze_file(file_path)
            results[filename] = result
        except Exception as e:
            results[filename] = {"error": str(e)}
            print(f"⚠️ Error analyzing {filename}: {e}")

# Zapis wyników analizy
with open(RESULTS_FILE, "w", encoding="utf-8") as out_file:
    json.dump(results, out_file, indent=2, ensure_ascii=False)

# Zapis do lokalnej pamięci
memory_entry = {
    "timestamp": datetime.datetime.now().isoformat(),
    "analyzed_files": list(results.keys()),
    "results": results
}
os.makedirs("logs", exist_ok=True)
with open(MEMORY_FILE, "w", encoding="utf-8") as mem_file:
    json.dump(memory_entry, mem_file, indent=2, ensure_ascii=False)

print("✅ All documents analyzed and saved to memory.")
