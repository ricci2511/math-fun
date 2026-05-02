import sympy as sp
from signals import rect, tri, lower_signals
from support import get_support

# Holds any symbols defined in the given expression
# Initialized with some helpful functions used in signal processing
symbol_dict = {
    "u": sp.Heaviside,
    "Heaviside": sp.Heaviside,
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
        support = get_support(expr, symb)
        merged_support = sp.Intersection(support, sp.Interval(lower, upper))
        if merged_support.is_empty:
            bounds = []
            factor = 0 # Over empty set -> 0
            break
        lower = merged_support.inf
        upper = merged_support.sup

        # Exploit symmetries
        if sp.simplify(lower + upper) == 0:
            parity = get_parity(expr, symb)
            if parity == -1:
                bounds = []
                factor = 0 # Odd over symmetric interval -> 0
                break
            if parity == 1:
                bounds.append((symb, 0, upper)) # [-a,a] -> [0,a]
                factor *= 2
                continue

        bounds.append((symb, lower, upper))

    expr = lower_signals(expr)
    integral = factor * sp.Integral(expr, *bounds)

    print("\n")
    sp.pprint(integral)

    print("\nResult:")
    res = integral.doit()
    sp.pprint(res)

    print("\nSimplified:")
    sp.pprint(sp.simplify(res))

if __name__ == "__main__":
    main()
