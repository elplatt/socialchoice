def score(profile):
    votes = {}
    for pref, count in profile.items():
        try:
            top = pref[0]
        except IndexError:
            continue
        try:
            votes[top] += count
        except KeyError:
            votes[top] = count
    return votes

def social_preference(profile):
    profile_score = score(profile)
    ordered_scores = sorted(profile_score.items(), reverse=True, key=lambda x: x[1])
    social_preference = []
    last_score = ordered_scores[0][1]
    current_set = set()
    for alternative, alt_score in ordered_scores:
        # If the score has changed, create a new set of alternatives
        if alt_score == last_score:
            current_set.add(alternative)
        else:
            social_preference.append(current_set)
            current_set = set([alternative])
        last_score = alt_score
    social_preference.append(current_set)
    return social_preference

def social_choice(profile):
    social_preference = social_preference(profile)
    return social_preference[0]