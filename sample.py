from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf(filename):
    # Create a PDF document with letter-size pages
    pdf = canvas.Canvas(filename, pagesize=letter)
    width, height = letter  # Get width and height of the page

    # Set title and add text
    pdf.setTitle("Sample PDF Report")
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(100, height - 100, "Hello, this is a sample PDF!")

    # Add a subtitle
    pdf.setFont("Helvetica", 12)
    pdf.drawString(100, height - 130, "Generated using the ReportLab library.")

    # Add a simple line
    pdf.line(100, height - 140, 400, height - 140)

    # Add a paragraph (multi-line text)
    sample_text = (
        "ReportLab is a powerful library for creating PDFs in Python. "
        "You can use it to generate invoices, reports, and more. "
        "This is just a simple example of what you can do."
    )
    pdf.drawString(100, height - 170, sample_text[:50])  # First part of text
    pdf.drawString(100, height - 190, sample_text[50:])  # Second part of text

    # Save the PDF
    pdf.save()
    print(f"PDF '{filename}' created successfully!")

# Generate the PDF
create_pdf("sample_report.pdf")