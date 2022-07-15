def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    """move the disc from from_rod to to_rod using aux_rod as auxiliary

    Args:
        n (integer): number of discs
        from_rod (string): starting rod
        to_rod (string): destination rod
        aux_rod (string): auxiliary rod(the rod that not either from_rod nor to_rod)
    """
    if n == 0:
        return
    # when it reach the line below, it will loop the function itself till the n value is 0
    TowerOfHanoi(n - 1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n - 1, aux_rod, to_rod, from_rod)


# Driver code
n = 4
TowerOfHanoi(n, "A", "C", "B")
