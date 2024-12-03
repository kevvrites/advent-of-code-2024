def calculate_similarity_scores(input_file):
    # Read the numbers from the file
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    # Parse the numbers into two separate lists
    left_col = []
    right_col = []
    for line in lines:
        left, right = map(int, line.strip().split())
        left_col.append(left)
        right_col.append(right)
    
    # Sort both columns (though sorting isn't strictly necessary for this calculation)
    sorted_left = sorted(left_col)
    sorted_right = sorted(right_col)
    
    # Count occurrences in right column
    right_counts = {}
    for num in right_col:
        right_counts[num] = right_counts.get(num, 0) + 1
    
    # Calculate similarity scores for matching numbers
    similarity_scores = []
    for num in left_col:
        if num in right_counts:
            # If number from left appears in right, multiply by its frequency in right
            score = num * right_counts[num]
            similarity_scores.append((num, right_counts[num], score))
    
    return similarity_scores

if __name__ == "__main__":
    input_file = "day1input.txt"
    
    scores = calculate_similarity_scores(input_file)
    
    # Print details of each score
    print("\nSimilarity Score Details:")
    print("Left Number | Occurrences in Right | Score")
    print("-" * 45)
    
    total_score = 0
    for num, occurrences, score in scores:
        print(f"{num:11d} | {occurrences:18d} | {score:5d}")
        total_score += score
    
    print("\nTotal Similarity Score:", total_score)
    print("Number of matching values found:", len(scores))
