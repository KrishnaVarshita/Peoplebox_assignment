def process(status):
    status_actions = {
        'active': 'Active',
        'inactive': 'Inactive'
    }
    print(status_actions.get(status, 'Unknown'))

data = {'status': 'active'}
process(data['status'])