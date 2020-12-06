from stars import Sky


def main():
    sky = Sky.from_file('data/data.txt')
    sky.find_message()


if __name__ == '__main__':
    main()
