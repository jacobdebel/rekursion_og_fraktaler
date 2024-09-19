# [[file:Rekursion_og_fraktaler.org::*Programmering af fakultet i =python=][Programmering af fakultet i =python=:1]]
# Her defineres funktionen fakultet
def fakultet(tal):
    if tal < 0: #Her tjekkes det om tallet er positivt.
        return "Tallet skal være positivt."
    elif tal == 0: #Her sørges der for at 0! = 1
        return 1
    else:
        if isinstance(tal, int): #Her tjekkes det at tallet er et heltal
            return tal*fakultet(tal-1) #Læg mærke til at funktionen kalder sig selv. Det kaldes rekursion.
        else:
            return "Tallet skal være et heltal."
# Prøv at ændre værdien af n og se, hvad der sker.
n=5
print(fakultet(n))
# Programmering af fakultet i =python=:1 ends here
