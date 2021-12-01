import logging
import tempfile
import subprocess
from pathlib import Path

#This script takes a directory of PDFs as input. It iterates through the PDFs, converts them to TIFF, and then generates OCR from the TIFF. 

logging.basicConfig(filename='pdf_to_ocr.log', level=logging.DEBUG)
indir = Path(input("Input directory containing PDFs: "))
outdir = Path(input("Output directory for OCR: "))
outdir.mkdir(exist_ok=True)

with tempfile.TemporaryDirectory() as tmp_dir_name:
    for pdf_file in indir.iterdir():
        base = (Path(pdf_file).stem)[:-4]
        pdf_to_tiff = f"convert -density 300 {pdf_file} -depth 8 -strip -background white -alpha off {tmp_dir_name}/{base}.tiff > /dev/null 2>&1"
        pdf_to_tiff_return = subprocess.call(pdf_to_tiff, shell=True)
        if pdf_to_tiff_return != 0:
            logging.error(f"Failed to convert PDF for {pdf_file}")
        else:
            tiff_to_ocr = f"tesseract {tmp_dir_name}/{base}.tiff {outdir}/{base}_OCR > /dev/null 2>&1"
            tiff_to_ocr_return = subprocess.call(tiff_to_ocr, shell=True)
            remove_tiff = f"rm {tmp_dir_name}/{base}.tiff"
            subprocess.call(remove_tiff, shell=True)


# jpg_filename = f"{tmp_dir_name}/{sequence_number:06}-{page_pid}.jpg"

