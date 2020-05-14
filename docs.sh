# Create documentation in docs folder

# Create HTML
pdoc --force --html --output-dir docs rf

# Create Markdown
pdoc --pdf rf > docs/pdf.md

# Create PDF
# Tested with miktex on windows 10
pandoc --metadata=title:"T-Mobile HPE Redfish Documentation" --toc --toc-depth=4 --from=markdown+abbreviations  --variable=mainfont:"DejaVu Sans" --output="docs/T-Mobile HPE Redfish Documentation.pdf" docs/pdf.md


