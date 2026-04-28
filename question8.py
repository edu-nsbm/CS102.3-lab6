def main() -> None:
    count: int = 1
    n_products_low: int = 0

    while count <= 5:
        curr_stock: int = int(input(""))

        if curr_stock < 10:
            n_products_low += 1

        count += 1

    print(f"{n_products_low} of products are low in stock!")


if __name__ == "__main__":
    main()
