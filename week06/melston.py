# Milestone 6: Life Expectancy Data Analysis
# Author: Delcio Moniz Eduardo
# This program reports the overall and year-specific life expectancy statistics.
# It also compares the gap between the highest and lowest values for extra insight.

import csv
from pathlib import Path


DATA_FILE = Path(__file__).with_name("life-expectancy.csv")


def main():
    year_data = {}
    overall_min = None
    overall_max = None
    min_country = ""
    min_year = ""
    max_country = ""
    max_year = ""

    try:
        with DATA_FILE.open("r", encoding="utf-8-sig", newline="") as data_file:
            reader = csv.DictReader(data_file)
            if reader.fieldnames is None:
                raise ValueError("The CSV file is empty or does not have a header.")

            required_columns = {"Entity", "Year"}
            missing_columns = required_columns.difference(reader.fieldnames)
            if missing_columns:
                missing = ", ".join(sorted(missing_columns))
                raise ValueError(f"The CSV file is missing required columns: {missing}")

            life_expectancy_key = next(
                (name for name in reader.fieldnames if name.lower() == "life expectancy" or name.lower() == "life expectancy (years)"),
                None,
            )
            if life_expectancy_key is None:
                raise ValueError("The CSV file is missing the life expectancy column.")

            for row in reader:
                country = row["Entity"]
                year = row["Year"]
                life_expectancy_text = row[life_expectancy_key]

                if not country or not year or not life_expectancy_text:
                    continue

                country = country.strip()
                year = year.strip()
                life_expectancy = float(life_expectancy_text)

                if overall_min is None or life_expectancy < overall_min:
                    overall_min = life_expectancy
                    min_country = country
                    min_year = year
                if overall_max is None or life_expectancy > overall_max:
                    overall_max = life_expectancy
                    max_country = country
                    max_year = year

                year_data.setdefault(year, []).append((country, life_expectancy))
    except FileNotFoundError:
        print(f"Dataset not found: {DATA_FILE}")
        print("Place the CSV file in the same folder as this program.")
        return

    if overall_min is None or overall_max is None:
        print("The dataset contains no valid life expectancy values.")
        return

    print(f"The overall max life expectancy is: {overall_max:.3f} "
          f"from {max_country} in {max_year}")
    print(f"The overall min life expectancy is: {overall_min:.3f} "
          f"from {min_country} in {min_year}")
    print(f"The overall difference is: {overall_max - overall_min:.3f} years")

    year_input = input("\nEnter the year of interest: ").strip()
    if year_input not in year_data:
        print(f"\nNo data found for year {year_input}.")
        return

    data_for_year = year_data[year_input]
    average = sum(value for _, value in data_for_year) / len(data_for_year)
    min_country_year, min_value_year = min(data_for_year, key=lambda item: item[1])
    max_country_year, max_value_year = max(data_for_year, key=lambda item: item[1])

    print(f"\nFor the year {year_input}:")
    print(f"The average life expectancy across all countries was {average:.2f}")
    print(f"The max life expectancy was in {max_country_year} "
          f"with {max_value_year:.3f}")
    print(f"The min life expectancy was in {min_country_year} "
          f"with {min_value_year:.3f}")
    print(f"The difference between the max and min was "
          f"{max_value_year - min_value_year:.3f} years")


if __name__ == "__main__":
    main()
