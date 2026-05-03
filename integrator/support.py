import sympy as sp
from signals import rect, tri

def get_heaviside_support(f, var):
    try:
        arg = f.args[0]
        return sp.solve_univariate_inequality(arg >= 0, var).as_set()
    except:
        raise NotImplementedError(
            f"Cannot determine support of {f} wrt {var}"
        )

def get_rect_support(f, var):
    try:
        arg = f.args[0]
        return sp.solve_univariate_inequality(sp.Abs(arg) <= sp.Rational(.5), var).as_set()
    except:
        raise NotImplementedError(
            f"Cannot determine support of {f} wrt {var}"
        )

def get_tri_support(f, var):
    try:
        arg = f.args[0]
        return sp.solve_univariate_inequality(sp.Abs(arg) <= 1, var).as_set()
    except:
        raise NotImplementedError(
            f"Cannot determine support of {f} wrt {var}"
        )

support_mappers = {
    sp.Heaviside: get_heaviside_support,
    rect: get_rect_support,
    tri: get_tri_support,
}

def get_support(expr, var):
    """
    Recursively detects the support of an expression with respect to `var`,
    that is the set of points where the expression is non-zero.
    """
    # Base case 1: Expression independent from the current variable => no specific bound
    if var not in expr.free_symbols:
        return sp.S.Reals

    # Base case 2: Handle known signals with constrained supports
    if expr.func in support_mappers:
        return support_mappers[expr.func](expr, var)

    if expr.is_Mul:
        # Filter out terms that do not contain the integration variable
        relevant_args = [arg for arg in expr.args if var in arg.free_symbols]
        if not relevant_args:
            return sp.S.Reals

        sets = []
        for arg in relevant_args:
            sets.append(get_support(arg, var))
        return sp.Intersection(*sets)
    
    if expr.is_Add:
        sets = []
        for arg in expr.args:
            sets.append(get_support(arg, var))
        return sp.Union(*sets)
    
    return sp.S.Reals
