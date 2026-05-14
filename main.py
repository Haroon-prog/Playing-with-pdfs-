from PyPDF2 import PdfWriter, PdfReader

print("PDF Tool - Choose an option:")
print("1. Merge multiple PDFs")
print("2. Split a PDF into multiple parts")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    # Merge PDFs
    merger = PdfWriter()
    pdfs = []
    n = int(input("Enter the number of PDFs to be merged: "))

    for i in range(0, n):
        name = input(f"Enter the name of PDF {i+1}: ")
        pdfs.append(name)

    for pdf in pdfs:
        merger.append(pdf)

    merger.write("merged-pdf.pdf")
    merger.close()
    print("PDFs merged successfully!")

elif choice == 2:
    # Split PDF into parts
    filename = input("Enter the name of the PDF file to split: ")
    num_parts = int(input("Enter the number of parts to split into: "))
    
    reader = PdfReader(filename)
    total_pages = len(reader.pages)
    
    # Calculate pages per part
    pages_per_part = total_pages // num_parts
    extra_pages = total_pages % num_parts
    
    start_page = 0
    for part in range(1, num_parts + 1):
        # Calculate end page for this part
        if part <= extra_pages:
            end_page = start_page + pages_per_part + 1
        else:
            end_page = start_page + pages_per_part
        
        # Create new PDF for this part
        merger = PdfWriter()
        for page_num in range(start_page, end_page):
            merger.add_page(reader.pages[page_num])
        
        output_filename = f"part{part}.pdf"
        merger.write(output_filename)
        merger.close()
        
        print(f"Created {output_filename} (pages {start_page + 1} to {end_page})")
        start_page = end_page
    
    print(f"Split into {num_parts} parts successfully!")