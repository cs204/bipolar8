def main():
    a = input( "Какой ответ на главный вопрос жизни, вселенной и всего такого? ")
    a = a.lower()
    match a:
        case "42" | "сорок два":
            print("Да")
        case _:
            print ( "Heт")

main()