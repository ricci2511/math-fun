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

This script is mainly intended as a **learning tool** and a foundation for building more advanced utils (e.g. plotting regions, numeric approximations, etc.).
