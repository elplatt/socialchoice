def count(profile):
    borda = {}
    alternatives = set(sum(map(list, profile.keys()), []))
    for pref, count in profile.items():
        remaining = set(alternatives)
        for i, alternative in enumerate(pref):
            remaining.remove(alternative)
            try:
                borda[alternative] += len(remaining) * count
            except KeyError:
                borda[alternative] = len(remaining) * count
        average = sum(range(len(remaining))) / len(remaining)
        for alternative in remaining:
            try:
                borda[alternative] += average
            except KeyError:
                borda[alternative] = average
    return borda

def social_preference(profile):
    borda = count(profile)
    ordered_scores = sorted(borda.items(), key=lambda x: x[1], reverse=True)
    social_preference = []
    last_score = ordered_scores[0][1]
    current_set = set()
    for alternative, score in ordered_scores:
        # If the score has changed, create a new set of alternatives
        if score == last_score:
            current_set.add(alternative)
        else:
            social_preference.append(current_set)
            current_set = set([alternative])
        last_score = score
    social_preference.append(current_set)
    return social_preference

def social_choice(profile):
    return social_preference(profile)[0]
