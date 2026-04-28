def main() -> None:
    attempts_left: int = 3
    correct_password: str = "admin"

    while attempts_left >= 1:
        input_password: str = input("Enter password: ")

        if input_password == correct_password:
            print("Access Granted!")
        else:
            print("Incorrect password.")

            attempts_left -= 1

            if attempts_left == 0:
                print("No more attempts left! You're locked out!\n")
                break
            else:
                print(f"Only {attempts_left} attempts left!\n")


if __name__ == "__main__":
    main()
