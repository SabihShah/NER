import re

def fix_ner(input_text):
    # Split the input text by spaces to process each token
    tokens = input_text.split()

    fixed_tokens = []
    
    for token in tokens:
        # Check if the token contains a NER tag
        if '/' in token:
            word, tag = token.rsplit('/', 1)  # Split the word from its tag
            
            # Check if the word is punctuation using regex
            if re.match(r'^[^\w\s]', word):  # This matches any punctuation character
                tag = 'O'  # Change the tag to 'O' for any punctuation
                
            # Append the fixed token back
            fixed_tokens.append(f"{word}/{tag}")
        else:
            fixed_tokens.append(token)  # In case no tag is present, append as is
    
    # Return the fixed text
    return ' '.join(fixed_tokens)


def process_file(input_file, output_file):
    # Read the input file
    with open(input_file, 'r') as f:
        input_text = f.read()

    # Apply the NER fix
    fixed_text = fix_ner(input_text)

    # Write the fixed text to the output file
    with open(output_file, 'w') as f:
        f.write(fixed_text)


# File paths
wikipedia_input_file = 'stanford-wikipedia.txt'  # Change this to the actual input file name
wikipedia_output_file = 'stanford-wikipedia-fix.txt'  # Change this to the desired output file name

famwiki_input_file = 'stanford-famwiki.txt'
famwiki_output_file = 'stanford-famwiki-fix.txt'

# Apply the fix and process the file
process_file(wikipedia_input_file, wikipedia_output_file)
process_file(famwiki_input_file, famwiki_output_file)

print(f"Fixed NER tags and saved to {wikipedia_output_file} and {famwiki_output_file}")