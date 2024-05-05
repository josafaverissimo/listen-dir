from sys import argv
from os.path import exists


def get_dir_to_listen_from_argv() -> str:
    if len(argv) < 2:
        return ''

    dir_to_listen_index = 1
    return argv[dir_to_listen_index]


def get_target_dirs_from_argv() -> list[str]:
    target_dirs_index = 2

    return [target_dir for target_dir in argv[target_dirs_index:] if exists(target_dir)]


def get_dir_to_listen_from_user() -> str:
    print('Dir to listen path')

    while True:
        dir_to_listen = input()

        if exists(dir_to_listen):
            break

        print('Directory does not exist')

    return dir_to_listen


def get_target_dirs_from_user() -> list[str]:
    target_dirs = []
    flags = ['q']

    while True:
        target_dir = input('Target dir path [q to quit]: ')

        if target_dir in flags:
            if not target_dirs:
                print('Target dir is required. Type at least one target dir')
                continue
            break

        if not exists(target_dir):
            print('Directory does not exist')
            continue

        if target_dir not in target_dirs:
            target_dirs.append(target_dir)

    return target_dirs


def get_dir_to_listen() -> str:
    dir_to_listen = get_dir_to_listen_from_argv()

    if not dir_to_listen:
        dir_to_listen = get_dir_to_listen_from_user()

    return dir_to_listen


def get_target_dirs() -> list[str]:
    target_dirs = get_target_dirs_from_argv()

    if not target_dirs:
        target_dirs = get_target_dirs_from_user()

    return target_dirs


def main():
    dir_to_listen = get_dir_to_listen()
    target_dirs = get_target_dirs()

    print(dir_to_listen)
    print(target_dirs)
