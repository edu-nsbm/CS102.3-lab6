def main() -> None:
    count: int = 1
    total: float = 0
    discount_p: float = 0

    while count <= 5:
        curr_bill: float = float(input(f"Enter item {count}'s price: "))
        total += curr_bill

        count += 1

    if total >= 5_000:
        discount_p = 20

    print("===== Bill =====")
    print(f"{total = }")
    print(f"{discount_p = }")
    print(f"Discount applied total: {total * (100 - discount_p) / 100}")


if __name__ == "__main__":
    main()
