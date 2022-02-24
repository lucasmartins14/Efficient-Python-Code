# Comparando com set()

# Convert both lists to sets
ash_set = set(ash_pokedex)
misty_set = set(misty_pokedex)

# Os dados em comum nos dois sets
# Find the Pokémon that exist in both sets
both = ash_set.intersection(misty_set)
print(both)

# Os dados que estão em um set que não estão no outro
# Find the Pokémon that Ash has, and Misty does not have
ash_only = ash_set.difference(misty_set)
print(ash_only)

# Dados exclusivos de cada set, mas nao em ambos
# Find the Pokémon that are in only one set (not both)
unique_to_set = ash_set.symmetric_difference(misty_set)
print(unique_to_set)