from pars import Parser


def main():
    pars = Parser("https://aif.ru/", "news.csv")
    pars.run()


if __name__ == '__main__':
    main()
