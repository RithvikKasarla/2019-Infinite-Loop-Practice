def donor_sort(last_year: str, this_year: str):
    last_year_donors = last_year.split(',')
    this_year_donors = this_year.split(',')

    both_years = sorted(list(set(last_year_donors).intersection(this_year_donors)))

    last_year_donors = sorted([person for person in last_year_donors if person not in both_years])
    this_year_donors = sorted([person for person in this_year_donors if person not in both_years])

    return [','.join(last_year_donors), ','.join(both_years), ','.join(this_year_donors)]
    



with open("Prob05.in.txt") as input_file:
    lines = input_file.readlines()[1:]

    for i in range(0, len(lines), 2):
        print(*donor_sort(lines[i].strip(), lines[i + 1].strip()), sep='\n')
