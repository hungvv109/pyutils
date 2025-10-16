import argparse
from pyutils.rename_tool import rename_files
from pyutils.compress_tool import compress_folder
from pyutils.todo_tool import handle_todo
from pyutils.utils import setup_logger

def main():
    parser = argparse.ArgumentParser(
        prog='pyutils',
        description='Python Utilities Pack - small command line tools'
    )
    parser.add_argument('--verbose', action='store_true', help='Show detailed logs')

    subparsers = parser.add_subparsers(dest='command')

    # Subcommands
    rename_parser = subparsers.add_parser('rename', help='Batch rename files in a folder')
    rename_parser.add_argument('--folder', required=True)
    rename_parser.add_argument('--prefix', required=True)

    compress_parser = subparsers.add_parser('compress', help='Compress folder to ZIP')
    compress_parser.add_argument('--input', required=True)
    compress_parser.add_argument('--zip', required=True)

    todo_parser = subparsers.add_parser('todo', help='Simple To-do manager')
    todo_parser.add_argument('action', choices=['add', 'list', 'remove'])
    todo_parser.add_argument('item', nargs='?')

    args = parser.parse_args()
    logger = setup_logger(args.verbose)

    if args.command == 'rename':
        rename_files(args.folder, args.prefix, logger)
    elif args.command == 'compress':
        compress_folder(args.input, args.zip, logger)
    elif args.command == 'todo':
        handle_todo(args.action, args.item, logger)
    else:
        parser.print_help()
