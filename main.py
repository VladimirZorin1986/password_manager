if __name__ == '__main__':
    import argparse
    from utils import create_password, pretty_display
    import config
    from models import User, UserPasswordManager

    parser = argparse.ArgumentParser()

    # создаем группу субпарсеров для отделения создания нового юзера от существующего
    subparsers = parser.add_subparsers(dest='sub_parser')

    parser_new_user = subparsers.add_parser('new_user')
    parser_new_user.add_argument('name')
    parser_new_user.add_argument('-p', '--password', default=create_password())

    parser_current_user = subparsers.add_parser('current_user')
    parser_current_user.add_argument('name')
    parser_current_user.add_argument('password')
    parser_current_user.add_argument('-del', '--delete',
                                     dest='delete_user', action='store_true')

    # создаем группу субпарсеров для эмуляции выбора меню
    parser_choices = parser_current_user.add_subparsers(dest='choice')

    add_choice = parser_choices.add_parser('add')
    add_choice.add_argument('resource')
    add_choice.add_argument('resource_password')
    add_choice.add_argument('-c', '--comments')

    update_choice = parser_choices.add_parser('update')
    update_choice.add_argument('resource')
    update_choice.add_argument('new_password')

    extract_choice = parser_choices.add_parser('extract')
    extract_choice.add_argument('resource')

    delete_choice = parser_choices.add_parser('delete')
    delete_choice.add_argument('resource')

    list_choice = parser_choices.add_parser('list')

    args = parser.parse_args()

    if args.sub_parser == 'new_user':
        User(args.name, args.password).add_to_db()
    elif args.sub_parser == 'current_user':
        if not args.delete_user:
            manager = UserPasswordManager(args.name, args.password)
            if args.choice == 'add':
                manager.add_resource(args.resource, args.resource_password, args.comments)
            elif args.choice == 'update':
                manager.update_resource(args.resource, args.new_password)
            elif args.choice == 'extract':
                manager.extract_resource(args.resource)
            elif args.choice == 'delete':
                manager.delete_resource(args.resource)
            else:
                print(pretty_display(manager.all_resources_info))
        else:
            User(args.name, args.password).delete_from_db()

    config.DB.close_db()