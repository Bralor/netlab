# Just temporary file

def func(a: int, b: int, **args) -> int:
    if args.get("rezim") == "soucet":
        print(a + b)
        return a + b

    if args.get("rezim") == "rozdil":
        print(a - b)
        return a - b


func(1, 14, rezim="soucet")
func(14, 1, rezim="rozdil")

