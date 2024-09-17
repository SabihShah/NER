import re

def fix_ner(input_text):
    tokens = input_text.split()

    fixed_tokens = []
    
    for token in tokens:
        if '/' in token:
            word, tag = token.rsplit('/', 1)  
            
            if re.match(r'^[^\w\s]', word):  
                tag = 'O' 
                
            fixed_tokens.append(f"{word}/{tag}")
        else:
            fixed_tokens.append(token)
    
    return ' '.join(fixed_tokens)


def process_file(input_file, output_file):
    
    with open(input_file, 'r') as f:
        input_text = f.read()

    
    fixed_text = fix_ner(input_text)

    with open(output_file, 'w') as f:
        f.write(fixed_text)


wikipedia_input_file = 'stanford-wikipedia.txt'  
wikipedia_output_file = 'stanford-wikipedia-fix.txt'  

famwiki_input_file = 'stanford-famwiki.txt'
famwiki_output_file = 'stanford-famwiki-fix.txt'

process_file(wikipedia_input_file, wikipedia_output_file)
process_file(famwiki_input_file, famwiki_output_file)

print(f"Fixed NER tags and saved to {wikipedia_output_file} and {famwiki_output_file}")
