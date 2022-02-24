# Iterando com .iterrows()

# Iterate over pit_df and print each row
for i,row in pit_df.iterrows():
    print(row)


# Print the row and type of each row
for row_tuple in pit_df.iterrows():
    print(row_tuple)
