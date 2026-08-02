#!/usr/bin/env python3
"""Basic example: creating an algebra and performing geometric product operations."""

from pytanga import Algebra, MV


def main() -> None:
    # Create a 3D Euclidean algebra (3 basis vectors) with named blades
    alg = Algebra.from_name("E3")

    # Access the basis vectors and bivectors
    e1, e2, e3 = alg.e1, alg.e2, alg.e3
    print(f"Basis vectors: e1={e1}, e2={e2}, e3={e3}")

    # Geometric product of two vectors
    print(f"\ne1 * e2 = {e1 * e2}")   # Should yield e12 (bivector)
    print(f"e1 * e1 = {e1 * e1}")     # Should yield 1 (scalar)

    # Inner product
    print(f"e1 | e2 = {e1 | e2}")     # Should yield 0 (vectors are orthogonal)

    # Outer product: creates the bivector e12
    bv = e1 ^ e2
    print(f"\nBivector: e1 ^ e2 = {bv}")

    # Create a rotor for rotation: R = cos(θ/2) + sin(θ/2) * e12
    from math import pi

    angle = pi / 2  # 90°
    rotor = alg.rotor(angle, e3)  # rotation in e12 plane (axis = e3)
    print(f"\nRotor (90° rotation in e12 plane): {rotor}")

    # Apply rotor to a vector via versor product
    v = e1
    rotated = rotor * v * ~rotor
    print(f"Rotate e1 by 90° in e12 plane: {rotated}")

    # Create a multivector from a dict (blade bitmask → coefficient)
    mv = alg.multivector({0: 3, 1: 2, 2: -1})
    print(f"\nMultivector from dict: {mv}")

    # Create a vector from coordinates
    vec = alg.vector(1, 2, 3)
    print(f"\nVector (1, 2, 3): {vec}")

    # Duality: cross product via dual of outer product
    cross = (e1 ^ e2).dual()
    print(f"(e1 ^ e2)★ = {cross}")   # Should yield e3

    # Grade extraction
    mv2 = e1 * e2 + 3  # scalar + bivector
    print(f"\nmv = {mv2}")
    print(f"Grade 0 (scalar part): {mv2.grade(0)}")
    print(f"Grade 2 (bivector part): {mv2.grade(2)}")


if __name__ == "__main__":
    main()