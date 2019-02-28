def preferences_to_profile(preferences):
    '''Convert a preference dict to a dict mapping preferences to counts.'''
    profile = {}
    for voter, preference in preferences.items():
        try:
            profile[preference] += 1
        except KeyError:
            profile[preference] = 1
    return profile

def print_preference(preference):
    current_place = 1
    print("Place\tAlternative")
    for i, v in enumerate(preference):
        count = len(v)
        if count == 1:
            place = str(current_place)
        else:
            place = '{}—{}'.format(current_place, current_place + len(v) - 1)
        for alternative in v:
            print('{}\t{}'.format(place, alternative))
        current_place += len(v)

