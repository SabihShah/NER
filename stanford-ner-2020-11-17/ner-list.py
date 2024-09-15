def entities(text_file):
    entities = []
    current_entity = []
    current_tag = None

    for word_tag in text_file.split():
        if '/' not in word_tag:
            continue

        word, tag = word_tag.rsplit('/', 1)

        if tag != 'O':
            if current_tag == tag:
                current_entity.append(word)

            else:
                if current_entity:
                    entities.append(" ".join(current_entity))
                
                current_entity = [word]
                current_tag = tag

        else:
            if current_entity:
                entities.append(" ".join(current_entity))
                current_entity = []
                current_tag = None
    
    if current_entity:
        entities.append(" ".join(current_entity))

    return entities


def ner_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    extracted_entities = entities(text)

    with open(output_file, 'w', encoding='utf-8') as f:
        for entity in extracted_entities:
            f.write(entity + '\n')


ner_file('stanford-wikipedia.txt', 'ner-list-wikipedia.txt')
ner_file('stanford-famwiki.txt', 'ner-list-famwiki.txt')