# math-fun

Small collection of personal math utils for experimentation, learning, and quick cli-based computations.

---

## integrate.py

Simple cli multivariable integrator built on top of `SymPy`.

### Notes

- Integration order matters, i.e. variables are applied in the order you enter them.
- Bounds follow the format: `lower,upper`
- Leaving bounds empty computes an **indefinite integral**.
- Expressions are parsed using SymPy, so standard mathematical syntax applies.
- Includes additional signal-processing functions:
  - `rect` (rectangular pulse)
  - `tri` (triangular pulse)
  - `u` / `step` (unit step)

### Caveats

- When using piecewise-defined functions (e.g. `rect`, `tri`), results may become verbose or not fully simplified.
- For cleaner results, prefer **finite bounds** when possible (automatic support detection is not yet implemented and non-trivial).

This script is mainly intended as a **learning tool** and a foundation for building more advanced utils (e.g. plotting regions, numeric approximations, etc.).
