def select_dates(potential_dates):
    names = []
    for date in potential_dates:
        if date["age"] > 30 and 'art' in date["hobbies"] and date["city"] == 'Berlin':
            names.append(date["name"])
    return ', '.join(names)

