import pdfplumber
import csv

def extract_tables_auto(pdf_path, output_csv):
    with pdfplumber.open(pdf_path) as pdf, open(output_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        for page_num, page in enumerate(pdf.pages, start=1):
            # Get all words on the page
            words = page.extract_words()
            if not words:
                print(f"No text on page {page_num}")
                continue

            # Find bounding box of all detected words
            x0 = min(float(w["x0"]) for w in words)
            y0 = min(float(w["top"]) for w in words)
            x1 = max(float(w["x1"]) for w in words)
            y1 = max(float(w["bottom"]) for w in words)

            # Crop to just the detected text area
            cropped = page.crop((x0, y0, x1, y1))
            table = cropped.extract_table()

            if table:
                print(f"Extracted table from page {page_num}")
                for row in table:
                    writer.writerow(row)
            else:
                print(f"No table detected on page {page_num}")

# Usage
extract_tables_auto("input.pdf", "output.csv")
print("✅ Done! Tables saved to output.csv")
