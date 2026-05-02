import sympy as sp

"""
Adds additional functions common in signal processing.

These signals are defined as classes that make them "human readable"
during the parsing and support-detection phases.
"""

class rect(sp.Function):
    nargs = 1

    @classmethod
    def eval(cls, t):
        return None  # keep symbolic

class tri(sp.Function):
    nargs = 1

    @classmethod
    def eval(cls, t):
        return None # keep symbolic

# Mathematical definitions of the signals
CUSTOM_REWRITE = {
    rect: lambda x: sp.Heaviside(x + sp.Rational(.5)) - sp.Heaviside(x - sp.Rational(.5)),
    tri:  lambda x: sp.Piecewise(
        (1 - sp.Abs(x), sp.Abs(x) <= 1),
        (0, True)
    ),
}

def lower_signals(expr):
    """
    Transforms any custom function definitions (e.g. rect, tri) into functions
    that sympy understands
    """
    if expr.is_Atom:
        return expr

    args = [lower_signals(arg) for arg in expr.args]

    expr = expr.func(*args)

    if type(expr) in CUSTOM_REWRITE:
        return CUSTOM_REWRITE[type(expr)](*expr.args)

    return expr
