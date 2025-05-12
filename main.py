def calculate_tm(seq):
    seq = seq.upper()
    a = seq.count("A")
    t = seq.count("T")
    g = seq.count("G")
    c = seq.count("C")
    tm = 2 * (a + t) + 4 * (g + c)
    return tm

# Example
dna = "ATGCATGC"
print("Melting Temperature (Tm):", calculate_tm(dna), "°C")
