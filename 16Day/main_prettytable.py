from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Pokemon" , "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirle", "Water"])
table.add_row(["Chamander", "Fire"])

table.align = "l"

print(table)


