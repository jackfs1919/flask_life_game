from rich.console import Console
s = "func(a, b func2(c, func3(d)))"
console = Console()
print(s)
console.log(s)
