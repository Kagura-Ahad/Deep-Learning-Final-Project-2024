# Simulate load_dictionaries function for testing
def load_dictionaries(part):
    if part == 1:
        word_pos_dict = {
            'میرے': ['DET'],
            'بھائی': ['NOUN'],
            'کا': ['ADP'],
            'میل': ['NOUN'],
            'ہے۔': ['SCONJ', 'NOUN', 'PUNCT', 'AUX'],
        }
        lemma_word_dict = {
            'بھائی': ['بھائی'],
            'کا': ['کا'],
            'میل': ['میل'],
        }
    elif part == 2:
        word_pos_dict = {
            'میرے': ['PRON'],
            'بھائی': ['PRON'],
            'کی': ['ADP', 'VERB'],
            'آیا': ['VERB'],
            'ہے۔': ['VERB'],
        }
        lemma_word_dict = {
            'بھائی': ['بھائی'],
            'آیا': ['آیا'],
            'کی': ['کی'],
        }
    return word_pos_dict, lemma_word_dict

# Simulate save_dictionaries function for testing
def save_dictionaries(merged_word_pos_dict, merged_lemma_word_dict, part):
    print(f"Merged Word to POS Tags Dictionary ({part}):")
    for word, pos_tags in merged_word_pos_dict.items():
        print(f"{word}: {pos_tags}")
    
    print("\nMerged Lemma to Word Dictionary:")
    for lemma, words in merged_lemma_word_dict.items():
        print(f"{lemma}: {words}")

# Your merge_dictionaries function
def merge_dictionaries(dict1, dict2):
    for key, value in dict2.items():
        if key in dict1:
            # Avoid duplicates in lists
            dict1[key] = list(set(dict1[key] + value))
        else:
            dict1[key] = value
    return dict1

# Load both parts
word_pos_dict_part1 = load_dictionaries(part=1)[0]
word_pos_dict_part2 = load_dictionaries(part=2)[0]
merged_word_pos_dict = merge_dictionaries(word_pos_dict_part1, word_pos_dict_part2)

lemma_word_dict_part1 = load_dictionaries(part=1)[1]
lemma_word_dict_part2 = load_dictionaries(part=2)[1]
merged_lemma_word_dict = merge_dictionaries(lemma_word_dict_part1, lemma_word_dict_part2)

# Save the final merged dictionaries
save_dictionaries(merged_word_pos_dict, merged_lemma_word_dict, part='merged')
