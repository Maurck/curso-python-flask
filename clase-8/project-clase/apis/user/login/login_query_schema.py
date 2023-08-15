
login_query_schema = {
    'email': {
        'nullable': False,
        'required': True,
        'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    },
    'password': {
        'nullable': False,
        'required': True
    }
}