#installing barcode using CMD
from barcode import EAN13
from barcode.writer import ImageWriter
num_of_barcodes = int(input("how mnay bacodes are required ?"))
numbers = range(num_of_barcodes)
for i in numbers:
    id = input("Give 12-Digit number for your barcode id:")
    my_code = EAN13(id, writer= ImageWriter)
    name = input("give the name to save barcodes:")
    my_code.save(name)


