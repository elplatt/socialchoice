import itertools
def score(profile):
    alternatives = set(sum([list(pref) for pref in profile.keys()], []))
    pairs = set(itertools.product(alternatives, alternatives))
    for alt in alternatives:
        pairs.remove((alt, alt))
    margins = dict((contest, 0) for contest in pairs)
    for pref, count in profile.items():
        for win in range(len(pref)):
            for lose in range(win + 1, len(pref)):
                margins[(pref[win], pref[lose])] += count
    return margins
        

import networkx as nx
def tideman_graph(profile):
    margins = score(profile)
    ordered_margins = sorted(margins.items(), key=lambda x: x[1], reverse=True)
    G = nx.DiGraph()
    counted = 0
    skipped = 0
    for contest, margin in ordered_margins:
        s, t = contest
        try:
            if nx.has_path(G, t, s):
                # Skip contest, would create cycle
                skipped += margin
                continue
        except nx.NodeNotFound:
            pass
        # Add node to graph
        G.add_edge(s, t)
        counted += margin
    return G, counted, skipped

def social_preference(profile):
    G, counted, skipped = tideman_graph(profile)
    root = next(nx.topological_sort(G))
    social_preference = []
    done = set()
    shell = set([root])
    while len(shell) > 0:
        next_shell = set()
        # Remove alternatives ranked lower than others in shell
        for s in list(shell):
            for t in list(shell):
                if G.has_edge(s, t):
                    shell.remove(t)
        # Update list of completed alternatives
        done = done | shell
        # Build next shell
        for s in shell:
            next_shell = (next_shell | set(G.successors(s))) - done
        # Add current shell to preference
        social_preference.append(shell)
        shell = next_shell
    return social_preference

def social_choice(profile):
    return social_preference(profile)[0]