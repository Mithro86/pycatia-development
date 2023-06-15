#! /usr/bin/python3.9

"""

    Example - Document - 003:

    Open a catia file.

    Export catia file to STP.

    Close a catia file.

"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath("..\\pycatia"))
##########################################################

import os
from pathlib import Path

from pycatia import catia
from pycatia.in_interfaces.document import Document

# path to file to open.
file_name = r"tests\cat_files\part_measurable.CATPart"

caa = catia()
# open document
documents = caa.documents
documents.open(file_name)

document = caa.active_document
assert isinstance(document, Document)

# _Full_ path of new file. This uses current working directory.
new_file_name = Path(os.getcwd(), "new_part.CATPart")
# save document as new name.
document.save_as(new_file_name, overwrite=True)

# to export to another support file_format (license permitting).
new_export_file_name = Path("c:\\temp\\new_export_part.stp")
document.export_data(new_export_file_name, "stp", overwrite=True)

# close document
document.close()
