def main() -> None:

    n_temps_high: float = 0

    while True:
        curr_temperature: float = float(input("Enter current temperature: "))

        if curr_temperature == -1:
            break
        elif curr_temperature > 30:
            n_temps_high += 1

    print(f"\nThere are {n_temps_high} high temp reads.")


if __name__ == "__main__":
    main()
