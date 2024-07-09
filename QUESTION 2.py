def maxScore(cardPoints, k):
    n = len(cardPoints)
    # Initial sum of the first k cards
    current_sum = sum(cardPoints[:k])
    max_points = current_sum
    
    # Sliding window: we slide the window from the end to the beginning
    for i in range(1, k + 1):
        current_sum += cardPoints[-i] - cardPoints[k - i]
        max_points = max(max_points, current_sum)
        
    return max_points

# Taking input from the user
cardPoints = list(map(int, input("Enter the card points separated by spaces: ").split()))
k = int(input("Enter the value of k: "))

# Calculate and print the maximum score
print("The maximum score you can obtain is:", maxScore(cardPoints,k))