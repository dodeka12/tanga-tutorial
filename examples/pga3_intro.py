#!/usr/bin/env python3
"""PGA3 example: creating and transforming 3D points in projective geometric algebra."""

from pytanga import Algebra


def main() -> None:
    # Create a PGA3 algebra
    alg = Algebra.from_name("PGA3")

    # Named basis blades
    blades = alg.blades()
    e1, e2, e3 = blades["e1"], blades["e2"], blades["e3"]
    e0 = blades["e0"]

    print(f"e0   = {e0}")
    print(f"e0² = {e0 * e0}")            # nilpotent (0)

    # Create a point: p = eo + x*e1 + y*e2 + z*e3
    p = alg.multivector("e0 + 1 e1 + 2 e2 + 3 e3")
    print(f"\nPoint at (1, 2, 3): {p}")

    # Translation with dual e1  (translator = 1 - t/2 * e1^e0)
    translator = alg.multivector({0: 1}) - 0.5 * (e1 ^ e0)
    translated = translator * p * translator.rev()
    print(f"Translated by 1 along e1: {translated}")


if __name__ == "__main__":
    main()