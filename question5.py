def main() -> None:

    total: float = 0

    while True:
        curr_deposit: float = float(input("Enter deposit: "))

        if curr_deposit == 0:
            print()
            break
        else:
            total += curr_deposit
            print(f"{total = }\n")

    print(f"{'Premium Customer' if total >= 10_000 else 'Regular Customer'}")


if __name__ == "__main__":
    main()
