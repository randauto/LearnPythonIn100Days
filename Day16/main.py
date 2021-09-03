from prettytable import PrettyTable

prettytable = PrettyTable()
prettytable.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
prettytable.add_column("Type", ["Electric", "Water", "Fire"])
prettytable.align = 'l'
print(prettytable)
