from collections import defaultdict

def normalize_system_output(system_output):
    # Split the system output by space and then separate tokens from their tags
    normalized = []
    for token_tag in system_output.split():
        if '/' in token_tag:
            token, tag = token_tag.rsplit('/', 1)  # Split only from the right once
            normalized.append(f"{token}\t{tag}")
    return '\n'.join(normalized)


def evaluate_ner(system_output, gold_standard):
    # Initialize counters for each entity type
    entity_types = defaultdict(lambda: {'tp': 0, 'fp': 0, 'fn': 0})
    
    system_entities = system_output.strip().splitlines()
    gold_entities = gold_standard.strip().splitlines()

    for sys_line, gold_line in zip(system_entities, gold_entities):
        sys_tokens = sys_line.split()
        gold_tokens = gold_line.split()
        
        if len(sys_tokens) == len(gold_tokens) and len(sys_tokens) > 1:
            system_tag = sys_tokens[-1]
            gold_tag = gold_tokens[-1]

            if system_tag == gold_tag and system_tag != "O":
                # True positive: correct entity prediction
                entity_type = system_tag.split('-')[-1]
                entity_types[entity_type]['tp'] += 1
            elif system_tag != "O" and system_tag != gold_tag:
                # False positive: system predicts an entity, but it's wrong
                system_entity_type = system_tag.split('-')[-1]
                entity_types[system_entity_type]['fp'] += 1
                if gold_tag != "O":
                    gold_entity_type = gold_tag.split('-')[-1]
                    entity_types[gold_entity_type]['fn'] += 1
            elif system_tag == "O" and gold_tag != "O":
                # False negative: system misses an entity in gold standard
                gold_entity_type = gold_tag.split('-')[-1]
                entity_types[gold_entity_type]['fn'] += 1

    return entity_types


def calculate_metrics(entity_counts):
    results = []
    total_tp, total_fp, total_fn = 0, 0, 0
    
    for entity_type, counts in entity_counts.items():
        tp, fp, fn = counts['tp'], counts['fp'], counts['fn']
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
        results.append([entity_type, precision, recall, f1, tp, fp, fn])
        total_tp += tp
        total_fp += fp
        total_fn += fn
    
    # Calculate total metrics
    total_precision = total_tp / (total_tp + total_fp) if (total_tp + total_fp) > 0 else 0
    total_recall = total_tp / (total_tp + total_fn) if (total_tp + total_fn) > 0 else 0
    total_f1 = 2 * total_precision * total_recall / (total_precision + total_recall) if (total_precision + total_recall) > 0 else 0
    results.append(["Totals", total_precision, total_recall, total_f1, total_tp, total_fp, total_fn])
    
    return results


def print_and_save_results(results, output_file):
    with open(output_file, 'w') as file:
        file.write(f"{'Entity':<15} {'P':<10} {'R':<10} {'F1':<10} {'TP':<5} {'FP':<5} {'FN':<5} \n")
        print(f"{'Entity':<15} {'P':<10} {'R':<10} {'F1':<10} {'TP':<5} {'FP':<5} {'FN':<5}")
        for result in results:
            file.write(f"{result[0]:<15} {result[1]:<10.4f} {result[2]:<10.4f} {result[3]:<10.4f} {result[4]:<5} {result[5]:<5} {result[6]:<5} \n")
            print(f"{result[0]:<15} {result[1]:<10.4f} {result[2]:<10.4f} {result[3]:<10.4f} {result[4]:<5} {result[5]:<5} {result[6]:<5}")
    


# Load the system output and gold standard
with open('stanford-wikipedia-fix.txt', 'r') as wikipedia:
    wikipedia = wikipedia.read()

with open('wikipedia-gold.txt', 'r') as wiki_gold:
    wiki_gold = wiki_gold.read()


with open('stanford-famwiki-fix.txt', 'r') as famwiki:
    famwiki = famwiki.read()

with open('famwiki-gold.txt', 'r') as fam_gold:
    fam_gold = fam_gold.read()

# Normalize system output format
wiki_output_normalized = normalize_system_output(wikipedia)
fam_output_normalized = normalize_system_output(famwiki)

# Perform evaluation
wiki_evaluation = evaluate_ner(wiki_output_normalized, wiki_gold)
fam_evaluation = evaluate_ner(fam_output_normalized, fam_gold)

# Calculate precision, recall, F1, and other metrics
wiki_results = calculate_metrics(wiki_evaluation)
fam_results = calculate_metrics(fam_evaluation)

# Print the results in the desired format along with token and tag counts
print_and_save_results(wiki_results, 'wikipedia-fix-eval.txt')
print_and_save_results(fam_results, 'famwiki-fix-eval.txt')


# Function to count tokens
# def count_tokens(text):
#     tokens = text.split()
#     return len(tokens)

# # Load the gold text file and system text file
# with open('fanwiki-gold.txt', 'r') as gold_file:
#     gold_text = gold_file.read()

# with open('stanford-famwiki.txt', 'r') as system_file:
#     system_text = system_file.read()

# # Count tokens in both files
# gold_token_count = count_tokens(gold_text)
# system_token_count = count_tokens(system_text)

# # Print the results
# print(f"Gold token count: {gold_token_count}")
# print(f"System token count: {system_token_count}")

# # Check if they match
# if gold_token_count == system_token_count:
#     print("Both files have the same number of tokens.")
# else:
#     print("The token counts do not match!")
