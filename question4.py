def main() -> None:
    count: int = 1
    n_even: int = 0
    n_odd: int = 0

    while count <= 5:
        curr_num: int = int(input(f"Enter number {count}: "))

        if curr_num % 2 == 0:
            n_even += 1
            print(f"{curr_num} is an even number")
        else:
            n_odd += 1
            print(f"{curr_num} is an odd number")

        count += 1

    print(f"{n_even = } \n{n_odd = }")


if __name__ == "__main__":
    main()
