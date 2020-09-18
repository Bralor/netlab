# Just temporary file

def func(a: int, b: int, **args) -> int:
    if args.get("rezim") == "soucet":
        return a + b

    if args.get("rezim") == "rozdil":
        return a - b


print(func(1, 14, rezim="soucet"))
print(func(14, 1, rezim="rozdil"))

