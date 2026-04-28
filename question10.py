def main() -> None:
    count: int = 1

    while count <= 4:
        curr_sales: float = float(input(f"\nEnter sale {count} amount: "))

        if curr_sales >= 5_000:
            print(f"Commision: {curr_sales * 10 / 100}")
        else:
            print("No commissions for the sale.")


if __name__ == "__main__":
    main()
