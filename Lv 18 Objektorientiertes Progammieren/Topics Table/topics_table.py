from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Number",["1","1","1","1","1","2","2","2","3","3","3","4","4","4","5","5","5","5"])
table.add_column("Topic",["UML","UML","UML","UML","UML","Grundlagen Programmieren","Grundlagen Programmieren","Grundlagen Programmieren","Grundlagen Netzwerke","Grundlagen Netzwerke","Grundlagen Netzwerke","SQL","SQL","SQL","Pattern","Pattern","Pattern","Pattern"])
table.add_column("Content",["Klassendiagramme","Anwendungsfalldiagramme (Use Case)","Zustandsdiagramme","Aktivitätsdiagramme","Sequenzdiagramme","PAP","Pseudocode","Struktorgramm","IPv4", "IPv6", "OSI","ERD", "RDBM","Normalisierung","Observer","Singleton","Factory","MVC"])
table.align ="l"

print(table)