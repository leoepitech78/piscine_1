def print_transactions(transactions):
    for amount in transactions:
        if amount > 0:
            print(f'You received {amount} euros')
        elif amount < 0:
            print(f'You spent {abs(amount)} euros')
        else:
            print(f'No transaction for {amount} euros')