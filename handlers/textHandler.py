import re

def process_metadata(file_contents, search_string):
    text_length = len(file_contents)
    alphanumeric_count = len(re.findall(r'\w', file_contents))
    occurrences = file_contents.lower().count(search_string.lower())

    metadata = {
        "text_length": text_length,
        "alphanumeric_count": alphanumeric_count,
        "occurrences_of_string": occurrences
    }

    return metadata
