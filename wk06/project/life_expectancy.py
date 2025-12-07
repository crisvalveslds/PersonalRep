# Life Expectancy Analyses
# It was really interesting to learn how to import files, use lists and manipulate its contents
# I learned a lot also about using next() and seek() to move between lines in the open file
# Also the importance of using the with: statement

with open("wk06/project/life-expectancy.csv") as life_expt:
    min_life_expt = 200
    max_life_expt = 0
    country_min = ""
    country_max = ""
    country_list = []
    country = []
    year_max = 0
    year_min = 2100
    age_average = 0
    age_count = 0
    age_max_country = []
    age_min_country = []
    age_max_interest = ['','','',0.0]
    age_year_interest = 0.0
    age_interest = 0.0
    age_count_interest = 0
    age_avr_interest = 0.0

    next(life_expt)
    for line in life_expt:
        country = line.strip().lower().split(",")
        if country[0] not in country_list:
            country_list.append(country[0])
        if int(country[2]) < year_min:
            year_min = int(country[2])
        if int(country[2]) > year_max:
            year_max = int(country[2])

    print("\nWelcome to Life Expectancy Analyses!\n")        
    year_of_interest = input(f"Choose a year between {year_min} and {year_max} to analyze: ")

    print(f"\nHere is a list of countries:\n\n {', '.join(country_list).title()}.\n")
    country_interest = input("Choose a country you have interest: ").lower()

    while country_interest not in country_list:
        print("Country not found. Please try again.")
        country_interest = input("Choose a country you have interest: ").lower()

    age_max = 0.0
    age_min = 200.0
    
    life_expt.seek(0)
    next(life_expt)
    
    for line in life_expt:
        country = line.strip().split(",")
        if float(country[3]) < min_life_expt:
            min_life_expt = float(country[3])
            country_min = country
        if float(country[3]) > max_life_expt:
            max_life_expt = float(country[3])
            country_max = country
        if country[2] == year_of_interest:
            age_average += float(country[3])
            age_count += 1
            if float(country[3]) > age_max:
                age_max = float(country[3])
                age_max_country = country
            if float(country[3]) < age_min:
                age_min = float(country[3])
                age_min_country = country
        if country[0].lower() == country_interest:
            if float(country[3]) > float(age_max_interest[3]):
                age_max_interest = country
            if country[2] == year_of_interest:
                age_year_interest = float(country[3])
            age_interest += float(country[3])
            age_count_interest += 1

    age_average = age_average / age_count
    age_avr_interest = age_interest / age_count_interest
    
    print("\nLet's start with the basics...\n")
    print(f"The country with the lowest life expectancy is {country_min[0]} in {country_min[2]} with {min_life_expt:.3f} years.")
    print(f"The country with the highest life expectancy is {country_max[0]} in {country_max[2]}  with {max_life_expt:.3f} years.")
    print(f"\nThe average life expectancy in {year_of_interest} was {age_average:.3f} years.")
    print(f"\nThe country with the highest life expectancy in {year_of_interest} was {age_max_country[0]} with {age_max:.3f} years.")
    print(f"The country with the lowest life expectancy in {year_of_interest} was {age_min_country[0]} with {age_min:.3f} years.")
    print(f"\nIn {country_interest.title()} I found the following interesting facts:\n")
    print(f"The average life expectancy in {year_of_interest} was {age_year_interest:.3f} years.")
    print(f"The largest life expectancy was {age_max_interest[3]} years in {age_max_interest[2]}")
    print(f"The total average life expectancy was {age_avr_interest:.3f} years.")
    print("\nThank you for using Life Expectancy Analyses!\n")