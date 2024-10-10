def split_corpus(file_path, split_size=32000):
    """
    Split the corpus file into two parts: 
    The first `split_size` lines go into part1, 
    and the next `split_size` lines go into part2.
    
    Args:
    - file_path: Path to the corpus file.
    - split_size: Number of lines per part. Default is 32000.
    """
    part1_lines = []
    part2_lines = []
    
    with open(file_path, 'r', encoding='utf-8') as file:
        # Read and store lines
        all_lines = file.readlines()
        
        # Part 1: First `split_size` lines
        part1_lines = all_lines[:split_size]
        
        # Part 2: Next `split_size` lines
        part2_lines = all_lines[split_size:split_size * 2]
    
    # Save part 1 to a new file
    with open('corpus_part1.txt', 'w', encoding='utf-8') as part1_file:
        part1_file.writelines(part1_lines)
    
    # Save part 2 to another new file
    with open('corpus_part2.txt', 'w', encoding='utf-8') as part2_file:
        part2_file.writelines(part2_lines)
    
    print(f"Corpus split into two parts: 'corpus_part1.txt' and 'corpus_part2.txt'")
    print(f"Each part contains {split_size} lines.")

# Usage example:
corpus_file_path = 'urdu-plain-text-corpus'  # Path to your corpus file
split_corpus(corpus_file_path, split_size=32000)
