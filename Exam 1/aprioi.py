from efficient_apriori import apriori

itemsets = [("p", "q"), ("p", 'r'), ('p', 's'), ('p', 't'), ('q', 'r'), ('q', 't'), ('r', 's'), ('s', 't')]

itemsets, rules = apriori(itemsets, min_support=0.5, min_confidence=1)

print(rules)