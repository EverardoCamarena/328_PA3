# Everardo Camarena
def max_gold(weights, capacity):
    # Initialize a 2D list (DP table) with 0s, having rows equal to number of items + 1
    # and columns equal to capacity + 1.
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Build the table dp[][] in bottom-up manner.
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                # If including the current item yields a better value, include it
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + weights[i-1])
            else:
                # Else, exclude the current item
                dp[i][w] = dp[i-1][w]

    # The last cell of the table will have the maximum value of gold that can be carried.
    return dp[n][capacity]
