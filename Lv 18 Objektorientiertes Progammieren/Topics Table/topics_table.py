from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Number", ["1"])
table.add_column("Topic", ["Placeholder"])
table.add_column("Content", ["Another one"])
table.align = "l"

print(table)