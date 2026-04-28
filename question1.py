def main() -> None:
    count: int = 1
    total: float = 0
    avarage: float = 0

    while count <= 5:
        curr_marks: float = float(input(f"Enter mark {count}: "))
        total += curr_marks

        count += 1

    avarage = total / 5

    print(f"{total = }")
    print(f"{'Pass' if avarage >= 50 else 'Fail'}")


if __name__ == "__main__":
    main()
