# integrate.py

A "smart" symbolic multivariable integrator built on top of `SymPy`.

## Features

- **Signal Processing Functions**: Native support for `rect(t)`, `tri(t)`, `sinc(t)`, `sgn(t)`, and `step(t)`.
- **Automatic Support Detection**: Automatically calculates the non-zero intervals of your expressions to prevent "verbose" piecewise outputs and handle infinite bounds `(-oo, oo)` cleanly.
- **Parity Exploitation**: Detects even and odd functions relative to the integration variable to simplify results and speed up computation
- **Indefinite & Definite**: Supports both symbolic primitives and evaluated definite integrals.

## Example usage

Just run `integrate.py` and follow the prompts. Definite integral example:

```
    expr: rect(t)

    vars: t

    t: -oo,oo

    Result: 1 (Smart support detection truncates -oo,oo to -0.5,0.5)
```

## Notes

- Integration order matters, i.e. variables are applied in the order you enter them.
- Bounds follow the format: `lower,upper` (empty for indefinite integral)
- Expressions are parsed using SymPy, so standard mathematical syntax applies.

This script is mainly intended as a **learning tool** and a foundation for building more advanced utils (e.g. plotting regions, numeric approximations, etc.).
