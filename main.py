from sys import argv
from os.path import exists


def get_dir_to_listen_from_argv() -> str:
    if len(argv) < 2:
        return ''

    dir_to_listen_index = 1
    return argv[dir_to_listen_index]


def get_dir_to_listen_from_user() -> str:
    print('Type a dir to listen')

    while True:
        dir_to_listen = input()

        if exists(dir_to_listen):
            break

        print('Directory does not exist')

    return dir_to_listen


def get_dir_to_listen() -> str:
    dir_to_listen = get_dir_to_listen_from_argv()

    if not dir_to_listen:
        dir_to_listen = get_dir_to_listen_from_user()

    return dir_to_listen


def main():
    dir_to_listen = get_dir_to_listen()


if __name__ == '__main__':
    main()
