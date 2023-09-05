def print_sorted_transactions(transactions):
    # Sort the transactions in ascending order
    sorted_transactions = sorted(transactions)
    
    # Iterate through the sorted transactions and display them
    for transaction in sorted_transactions:
        if transaction < 0:
            print(f'You spent', transaction  , 'euros')
        else:
            print(f'You received {transaction} euros')

# Example usage:
transactions = [512, 34, -123, 0, 42.08, -12]
print_sorted_transactions(transactions)