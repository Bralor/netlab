# Just temporary file

def func(a: int, b: int, **args) -> int:
    if args.get("rezim") == "soucet":
        return a + b


func(1, 14, rezim="soucet")

