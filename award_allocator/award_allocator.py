import random


def award_allocator(budget, applications):
    """ Prints randomly selected applications until budget is exceeded.

    Args:
        budget(int): Total award  budget.
        applications(dict): Application ID: Grant amount sought.

    """
    # Convert to a list
    application_list = list(applications.items())

    # Shuffle the list
    random.shuffle(application_list)

    # Loop through the list and deduct amounts from the budget
    for ref, amount in application_list:
        budget -= amount
        print(f'Reference: {ref}, Value: {amount}, Remaining Budget: {budget}')

        if budget < 0:
            print('Budget is now negative')
            break

    print(f'Final budget: {budget}')


if __name__ == '__main__':
    # Sample data
    award_budget = 1000
    application_budgets = {
        'A': 200, 'B': 300, 'C': 500, 'D': 150, 'E': 450, 'F': 300
    }

    award_allocator(award_budget, application_budgets)
