def main() -> None:
    count: int = 1
    total: float = 0

    while count <= 3:
        curr_units: float = float(input(f"Enter month {count}'s units: "))
        total += curr_units

        count += 1

    print(f"\n{'High Usage' if total >= 300 else 'Normal Usage'} of {total} units")


if __name__ == "__main__":
    main()
