from decouple import config
import logic


def main():


    min_number = config('min_number', cast=int)
    max_number = config('max_number', cast=int)
    attempts = config('attempts', cast=int)
    initial_capital = config('initial_capital', cast=int)


    logic.play_game(min_number, max_number, attempts, initial_capital)


if __name__ == "__main__":
    main()
