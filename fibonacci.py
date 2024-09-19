# [[file:Rekursion_og_fraktaler.org::*Fibonacci-serien][Fibonacci-serien:1]]
# Dette er definitionen på en funktion, som hedder fibonacci.

def fibonacci(n):
    if n < 0: # Her tjekkes det, at brugeren ikke indsætter negative tal.
        return "n skal være større end eller lig med nul."
    if n == 0: # Her sørges der får, at man får 0 ud, hvis man vælger n=0
        return 0
    elif n == 1 or n == 2: # Her sikres det, at man får 1 ud for n=1 og n=2
        return 1
    else: 
        # Her kan man se, at funktionen fibonacci kalder sig selv.
        # Denne konstruktion inden for programmering kaldes rekursion.
        return fibonacci(n-2) + fibonacci(n-1) 

# Prøv at ændre n til et andet tal
n = 3
print(fibonacci(n))
# Fibonacci-serien:1 ends here
