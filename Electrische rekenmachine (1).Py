## Statements

## Selection Menu
print('')
print('')
print('Welkom in de Elektrische Rekenmachine')
print('Gemaakt Door Casper 17/01/2023')
print('')
print('')
print('1 = Voorschakel weerstand berekenen met u en i waardes')
print('2 = Weerstand berekenen met u en i waardes')
print('3 = Wattage berekenen met i en r waardes')
print('4 = Ampere berekenen met U en R Waardes')
print('')
print('')
## Input = Welke je wilt gebruiken 
A = float(input('Welke rekenmachine wil je gebruiken?:'))
## Choice
if A == 1:
    print('')
    print('Voorschakel weerstand bereken met U en I waardes wordt geladen! ')
    print('')
    ## Hieronder de formule voor het bereken van de voorschakelweerstand
    ## Rt = (1/R1)+(1/R2)+(1/R3)+(1/R4)
    U1 = float(input('wat is de U waarde in Volt   van 1: '))
    I1 = float(input('wat is de I waarde in Ampere van 1: '))
    
    R1 = (U1/I1)
    print('Jouw 1e Weerstandswaarde is')
    print(R1)
    
    U2 = float(input('wat is de U waarde in Volt   van 2: '))
    I2 = float(input('wat is de I waarde in Ampere van 2: '))
    
    R2 = (U2/I2)
    print('Jouw 2e Weerstandswaarde is')
    print(R2)
    
    U3 = float(input('wat is de U waarde in Volt   van 3: '))
    I3 = float(input('wat is de I waarde in Ampere van 3: '))
    
    R3 = (U3/I3)
    print('Jouw 3e Weerstandswaarde is')
    print(R3)
    
    U4 = float(input('wat is de U waarde in Volt   van 4: '))
    I4 = float(input('wat is de I waarde in Ampere van 4: '))
    
    R4 = (U4/I4)
    print('Jouw 4e Weerstandswaarde is')
    print(R4)
    
    Rt = ((1/R1) + (1/R2) + (1/R3) + (1/R4))
    Ru1 = (1/Rt) 
    print('')
    print(Ru1)                                                         ## Made by Casper 17/01/2023
if A == 2:
    print('')
    print('Weerstand berekenen met U en I Waardes wordt geladen! ')
    print('')
    ## Hieronder de formule voor het bereken van de Weerstand
    ## R = U/I
    U = float(input('wat is de U waarde in Volt  : '))
    I = float(input('wat is de I waarde in Ampere: '))
    
    R = (U/I)
    print(R)                                                         ## Made by Casper 17/01/2023
if A == 3: 
    print('')
    print('U Wattage Berekenen wordt geladen! ')
    print('')
    ## Hieronder de formule voor het bereken van de Wattage
    ## U = I*R
    I = float(input('wat is de I waarde in Ampere: '))
    R = float(input('wat is de R waarde in Ohm   : '))
    
    U = I*R
    print(U)                                                         ## Made by Casper 17/01/2023
if A == 4: 
    print('')
    print('U Wattage Berekenen wordt geladen! ')
    print('')
    ## Hieronder de formule voor het bereken van de Ampere
    ## I = U/R
    U = float(input('wat is de U waarde in Volt  : '))
    R = float(input('wat is de R waarde in Ohm   : '))
    
    I = U/R
    print(I)                                                           ## Made by Casper 17/01/2023