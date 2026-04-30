import sympy as sp

symbol_dict = {}

def get_symbol(symb):
    if symb not in symbol_dict:
        symbol_dict[symb] = sp.Symbol(symb)
    return symbol_dict[symb]

def parse_symbols(symbs: list):
    for s in symbs:
        get_symbol(s)

def parse_expr(expr_str: str):
    return sp.parse_expr(expr_str, local_dict=symbol_dict)

def main():
    print("expr: ", end="")
    expr = input()

    print("vars (comma separated): ", end="")
    vars = input().split(',')
    if vars[0] == "":
        print("Please specify the integration variables...")
        return 1

    parse_symbols(vars) # Vars must be pre-parsed

    bounds = []
    print("bounds (empty for primitive):")
    for v in vars:
        print(f'  {v}: ', end="")
        bound = input()
        if bound == "":
            bounds.append(get_symbol(v)) # Handle indefinite integrals
            continue
        b1, b2 = bound.split(',');
        bounds.append((get_symbol(v), parse_expr(b1), parse_expr(b2)))

    integral = sp.Integral(parse_expr(expr), *bounds)

    print("\n")
    sp.pprint(integral)

    print("\nResult:")
    sp.pprint(integral.doit())

if __name__ == "__main__":
    main()