def main() -> None:
    correct_pin: int = 1234

    while True:
        input_pin: int = int(input("Enter PIN: "))

        if input_pin == correct_pin:
            print("Correct PIN!\n")
            break
        else:
            print("Incorrect PIN!\n")


if __name__ == "__main__":
    main()
