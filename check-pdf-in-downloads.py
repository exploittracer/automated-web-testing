from pathlib import Path

# Define the Downloads folder and target file
downloads = Path("D:/Downloads")

pdf_file = downloads / "20-python-libraries-you-arent-using-but-should.pdf"

# Check existence
if pdf_file.exists():
    print(f"✅ '{pdf_file.name}' exists in Downloads.")
else:
    print(f"❌ '{pdf_file.name}' not found in Downloads.")
