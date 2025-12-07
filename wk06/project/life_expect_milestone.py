with open("wk06/project/life-expectancy.csv") as life_expt:
    min_life_expt = 200
    max_life_expt = 0
    country_min = ""
    country_max = ""
    country = []
    
    next(life_expt)
    for line in life_expt:
        country = line.strip().split(",")
        if float(country[3]) < min_life_expt:
            min_life_expt = float(country[3])
        if float(country[3]) > max_life_expt:
            max_life_expt = float(country[3])
    
    print(f"The lowest life expectancy is {min_life_expt:.2f} years.")
    print(f"The highest life expectancy is {max_life_expt:.2f} years.")