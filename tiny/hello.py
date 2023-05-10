import argparse


def get_args():
    parser = argparse.ArgumentParser(description='Say Hello')
    # 명령행 인수: -n(축약형), --name
    parser.add_argument('-n',
                        '--name',
                        metavar='name',
                        default='World',
                        help="name to greet")
    return parser.parse_args()


def main():
    args = get_args()
    print('Hello, ' + args.name + "!")


if __name__ == "__main__":
    main()
