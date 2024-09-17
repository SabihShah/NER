## Stanford NER 

This repository contains the Stanford NER implementation

In this Named Entity Recognition (NER) tasks, three key metrics are used to evaluate the system's performance:

**Precision:** Precision measures how many of the entities identified by the system are correct, essentially focusing on the accuracy of the identified entities. \
Mathematically:
<p align="center"> precision = True positives / (True positives + False positives) </p>

**Recall:** Recall measures how many of the actual entities present in the text were correctly identified by the system. \
Mathematically:
<p align="center"> recall = True Positives / (True Positives + False negatives) </p>

**F1 score:** The F1 score is the harmonic mean of precision and recall, providing a balanced measure that accounts for both false positives (incorrect entities) and false negatives (missed entities). \
Mathematically:
<p align="center"> F-score = 2 [(precision × recall) / (precision + recall)] </p>

From the evalaution results for both wikipedia-eval.txt and famwiki-eval.txt, we can see varying performance across different entity types.

**Wikipedia-eval.txt**
| Entity        |     P    |     R    |    F1    |  TP |  FP |  FN |  
|---------------|----------|----------|----------|-----|-----|-----|  
| PERSON        | 0.8237   | 0.9211   | 0.8697   | 257 |  55 |  22 |  
| ORGANIZATION  | 0.8505   | 0.5170   | 0.6431   |  91 |  16 |  85 |  
| LOCATION      | 0.8072   | 0.9306   | 0.8645   |  67 |  16 |   5 |  
| Totals        | 0.8267   | 0.7875   | 0.8066   | 415 |  87 | 112 |

The system performs better overall, especially for `PERSON` entities, achieving a precision of 0.8237 and a recall of 0.9211, leading to a 
strong F1 score of 0.8697. This indicates a balanced performance, with most entities being correctly identified, and few entities being 
missed or incorrectly tagged. However, the `ORGANIZATION` category sees a significant drop in recall (0.5170), meaning nearly half of the 
actual entities are missed, while precision remains fairly high at 0.8505, indicating that most identified entities are correct. `LOCATION` 
entities show a solid balance with high precision and recall, reflected in an F1 score of 0.8645.

**Famwiki-eval.txt**
| Entity        |     P    |     R    |    F1    |  TP |  FP |  FN |  
|---------------|----------|----------|----------|-----|-----|-----|  
| PERSON        | 1.0000   | 0.5361   | 0.6980   |  52 |   0 |  45 |  
| ORGANIZATION  | 0.6111   | 1.0000   | 0.7586   |  11 |   7 |   0 |  
| LOCATION      | 1.0000   | 1.0000   | 1.0000   |   2 |   0 |   0 |  
| Totals        | 0.9028   | 0.5909   | 0.7143   |  65 |   7 |  45 |

For the famwiki-eval results, the PERSON entity has a perfect precision of 1.0, indicating that all the identified PERSON entities are correct. 
However, the recall is 0.5361, meaning that almost half of the actual person entities were missed. This suggests that the system is very cautious 
and doesn't over-predict, but it fails to capture many of the entities present. The F1 score of 0.6980 reflects this imbalance. In contrast, for 
ORGANIZATION, recall is perfect at 1.0, meaning all organization entities were identified, but precision is lower at 0.6111, indicating some incorrect 
identifications (false positives). The F1 score here is moderate at 0.7586. Finally, the LOCATION entity achieves perfect precision, recall, and F1 score, 
meaning both the accuracy and completeness of entity recognition are excellent in this category.

Overall, the system performs better on the wikipedia data compared to the famwiki data, particularly in the recall of PERSON entities. The lower recall 
values in famwiki-eval suggest that the system misses a significant portion of entities in this dataset, while on wikipedia-eval, the system shows a more 
balanced ability to detect and accurately identify entities across categories. The F1 scores provide a clear picture of the system's performance, showing 
that while precision is strong in most cases, recall can vary, especially for more complex entities like ORGANIZATION.

**FIX-NER:**
In NER systems, it's common for punctuation marks to be incorrectly tagged as part of an entity (e.g., parentheses being tagged as `PERSON`). This can lead to incorrect evaluations of precision and recall. 
The goal of this project is to fix such errors by changing the NER tags for punctuation to `O`, which signifies that the token is not part of any entity.

By applying fix-ner on stanford-wikipedia.txt and stanford-famwiki.txt, we noted some changes in the evaluation results of both files. In stanford-wikipedia 
Total precision increased to 0.8449 from 0.8267 and F1 score increased from 0.8066 to 0.8142 which shows some fixes from the previous text. In stanford-famwiki 
no changes were observed which shows that there was no incorrect tagging of punctuation in the original file.


### Use of AI generators in this assessed task
- Extracting data from wikipedia was easy but got help from ChatGPT for extracting from famwiki but had to modify the code to my requirements.
- For ner-list and eval taks, got help from ChatGPT for manipulating text in the required format.
