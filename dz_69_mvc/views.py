def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f" {title} ".center(50, "="))
            output = func(*args, **kwargs)
            print("=" * 50)
            return output

        return wrap

    return wrapper


class UserInterface:
    @add_title("Редактирование данных каталога фильмов")
    def wait_user_answer(self):
        print("Действия с фильмами:")
        print("1 - Добавление фильма"
              "\n2 - Каталог фильмов"
              "\n3 - Просмотр определенного фильма"
              "\n4 - Удаление фильма"
              "\nq - выход из программы")
        user_answer = input("Выбирите вариант действия: ")
        return user_answer

    @add_title("Добавление фильма")
    def add_user_movie(self):
        dict_movie = {
            "название": None,
            "жанр": None,
            "режиссера": None,
            "год выхода": None,
            "длительность": None,
            "студию": None,
            "актеров": None
        }
        for key in dict_movie:
            dict_movie[key] = input(f"Введите {key} фильма: ")
        return dict_movie

    @add_title("Каталог фильмов")
    def show_all_movies(self, movies):
        for ind, movie in enumerate(movies, 1):
            print(f"{ind}. {movie}")

    @add_title("Ввод названия фильма")
    def get_user_movie(self):
        user_movie = input("Введите название фильма: ")
        return user_movie

    @add_title("Сообщение об ошибке")
    def show_incorrect_title_error(self, user_title):
        print(f"Фильм с названием {user_title} не существует")

    @add_title("Просмотр фильма")
    def show_single_movie(self, movie):
        for key in movie:
            print(f"{key} фильма - {movie[key]}")

    @add_title("Сообщение об ошибке")
    def show_incorrect_answer_error(self, answer):
        print(f"Варианта {answer} не существует")

    @add_title("Удаление фильма")
    def remove_single_movie(self, article):
        print(f"Фильм {article} - был удален")