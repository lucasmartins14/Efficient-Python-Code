# Iterando com .itertuples()

# Loop over the DataFrame and print each row
for row in rangers_df.itertuples():
  print(row)

  # Loop over the DataFrame and print each row's Index, Year and Wins (W)
for row in rangers_df.itertuples():
  i = row[0]
  year = row[3]
  wins = row[6]
  print(i, year, wins)