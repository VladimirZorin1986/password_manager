if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Command line interface for password manager')

    group1 = parser.add_mutually_exclusive_group()
    group1.add_argument('-n', '--new_user', help='create new user info',
                        action='store_true')
    group1.add_argument('-c', '--current_user', help='access to current_user info',
                        action='store_true')

    args = parser.parse_args()

    if args.new_user:
        print('Creating new user')
        login = input('Login: ')
        password = input('Password: ')
        password_for_check = input('Please write your password once more: ')
        if hash(password) == hash(password_for_check):
            print(f'User {login} registered successfully!')
    if args.current_user:
        print('Here will be check password from db')