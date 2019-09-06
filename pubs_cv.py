# Create a list of publications based on the entries in my CV
import bibtexparser

with open('/Users/momchilminkov/Drive/Postdoc/Cv/Master/my_bib.bib') as bibtex_file:
# with open('test.bib') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

print(bib_database.entries)