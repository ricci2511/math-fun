import sympy as sp

def rect(t):
    return sp.Piecewise(
        (1, sp.Abs(t) <= sp.Rational(.5)),
        (0, True)
    )
    # TODO: Does not fair well with parity check :(
    # return sp.Heaviside(t + sp.Rational(.5)) - sp.Heaviside(t - sp.Rational(.5))

def tri(t):
    return sp.Piecewise(
        (1 - sp.Abs(t), sp.Abs(t) <= 1),
        (0, True)
    )

# Holds any symbols defined in the given expression
# Initialized with some helpful functions used in signal processing
symbol_dict = {
    "u": sp.Heaviside,
    "Heavside": sp.Heaviside,
    "step": sp.Heaviside,
    "sgn": sp.sign,
    "sign": sp.sign,
    "sinc": sp.sinc,
    "rect": rect,
    "tri": tri,
}

def get_symbol(symb):
    if symb not in symbol_dict:
        symbol_dict[symb] = sp.Symbol(symb)
    return symbol_dict[symb]

def parse_symbols(symbs: list):
    for s in symbs:
        get_symbol(s)

def parse_expr(expr_str: str):
    return sp.parse_expr(expr_str, local_dict=symbol_dict)

def get_parity(expr, var):
    if sp.simplify(expr - expr.subs(var, -var)) == 0:
        return 1 # f(t) = f(-t)
    if sp.simplify(expr + expr.subs(var, -var)) == 0:
        return -1 # f(t) = -f(-t)
    return 0

def main():
    print("expr: ", end="")
    raw_expr = input()
    expr = parse_expr(raw_expr)

    print("vars (comma separated): ", end="")
    vars = input().split(',')
    if vars[0] == "":
        print("Please specify the integration variables...")
        return 1

    parse_symbols(vars) # Vars must be pre-parsed

    factor = 1
    bounds = []
    print("bounds (empty for primitive):")
    for v in vars:
        symb = get_symbol(v)

        print(f'  {v}: ', end="")
        bound = input()
        if bound == "":
            bounds.append(symb) # Handle indefinite integrals
            continue

        l, u = bound.split(',');
        lower = parse_expr(l)
        upper = parse_expr(u)

        if lower != -upper:
            bounds.append((symb, lower, upper))
            continue

        # Handle symmetric interval
        parity = get_parity(expr, symb)
        if parity == -1:
            bounds.append((symb, 0, 0)) # Yield zero
            continue
        if parity == 1:
            bounds.append((symb, 0, upper)) # [-a,a] -> [0,a]
            factor *= 2
            continue

    integral = factor * sp.Integral(expr, *bounds)

    print("\n")
    sp.pprint(integral)

    print("\nResult:")
    sp.pprint(integral.doit())

if __name__ == "__main__":
    main()