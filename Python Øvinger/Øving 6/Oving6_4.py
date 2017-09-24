import random # Importerer modulen random (generere tilfeldige tall)
import time

def thinking():
    while True:
        time.sleep(random.random()*1)
        print (".",end='',flush=True)
        if (random.random()*1 > 0.7002):
            print("\n")
            break


# Funksjon:     pick_sentence
# Beskrivelse:  Plukker ut en tilfeldig tekststreng fra en liste av tekstsetninger
# Input:        En liste av tekststrenger
# Ouput:        En tekststreng
def pick_sentence(sentences):
    return sentences[random.randint(0, len(sentences)-1)]
# Funksjon:     print_sentence
# Beskrivelse:  Skriver ut tre tekststrenger på ei linje til konsoll.
#               Det skal være mellomrom (space) mellom tekststreng en og to.
#               Det skal ikke være mellomrom (space) mellom tekststreng to og tre.
# Input:        Tre tekststrenger
# Output:       Ingen
# Kommentar:    MANGER KODE HER!!!!

def print_sentence(str1,str2,str3):
    print(str1, str2+str3)


# Funksjon:     intro_text
# Beskrivelse:  Skriver en velkomsttekst til konsoll som skal inneholde:
#               20 linjeskift
#               Setningen: "Hei, jeg heter Eliza og vil gjerne snakke med deg."
#               Setningen: "Ikke start svar med stor bokstav og bruk hele setninger."
#               Setningen: "Skriv 'hade' hvis du vil avslutte samtalen"
#               Setningen: "**************************************************"
#               1 linjeskift
# Input:        Ingen
# Output:       Ingen
# Kommentar:    MANGLER KODE HER!!!

def intro_text():
    print("\n" * 20)
    print("Hei, jeg heter Eliza og vil gjerne snakke med deg.")
    print("Ikke start svar med stor bokstav og bruk hele setninger.")
    print("Skriv 'hade' hvis du vil avslutte samtalen")
    print("************************************************** \n")
# Funksjon:     main
# Beskrivelse:  Hovedfunksjonen i programmet
# Input:        Ingen
# Output:       Ingen
def main():
# Initialisering av variabler
    answer = "ikke hade" # Sørger for at while-løkka kjører første gang
# En liste av spørsmål
    questions = ['Hva gjør du', 'Hvordan går det', 'Hvorfor heter du',
                 'Liker du å hete', 'Føler du deg bra', 'Hva har du gjort idag','Hva tenker du om framtida',
                 'Hva gjør deg glad', 'Hva gjør deg trist']
# En liste av oppfølgningsspørsmål
    follow_ups = ['Hvorfor sier du', 'Hva mener du med', 'Hvor lenge har du sagt', 'Hvilke tanker har du om', 'Kan du si litt mer om','Hvorfor sier du']
# En liste av responser
    responses = ['Fint du sier det', 'Det skjønner jeg godt', 'Så dumt da', 'Føler meg også sånn','Blir trist av det du sier', 'Så bra', 'Du er jammen frekk']
# Skriv velkomsttekst til konsoll vha funksjonen intro_text
# MANGLER KODE HER!!!
    intro_text()
# Spør brukeren om navnet og lagre svaret i en variabel
# MANGLER KODE HER!!!
    navn = input("Hva er navnet ditt?")
    thinking()
# Programmet kjører i løkke helt til brukeren svarer "hade"
    while answer != "hade":
        pass
# NB: All kode her må skrives med to innrykk!!!
# Plukk ut et tilfeldig spørsmål fra lista questions
# ved hjelp av funksjonen pick_sentence
# MANGLER KODE HER!!!
        spm = pick_sentence(questions)

# Skriv spørsmålet etterfulgt av navnet til brukeren
# og et spørsmålstegn ved hjelp av funksjonen print_sentence
# MANGLER KODE HER!!!
        print_sentence(spm,navn,"?")


# Spør brukeren om et svar med teksten "Svar: " og lagre
# resultatet i en variabel
# MANGLER KODE HER!!!
        answer = input("Svar: ")
        thinking()

# Plukk ut et tilfeldig oppfølgingsspørsmål fra lista follow_ups
# ved hjelp av funksjonen pick_sentence
# MANGLER KODE HER!!!
        flg = pick_sentence(follow_ups)

# Skriv oppfølgningsspørsmålet sammen med svaret fra brukeren
# og et spørsmålstegn ved hjelp av funksjonen print_sentence
# MANGLER KODE HER!!!
        print_sentence(flg,answer,"?")


# Spør brukeren om et svar med teksten "Svar: " uten å lagre
# resultatet til variabel
# MANGLER KODE HER!!!
        input("Svar: ")
        thinking()


# Plukk ut en tilfeldig respons fra lista responses
# ved hjelp av funksjonen pick_sentence
# MANGLER KODE HER!!!
        rsp = pick_sentence(responses)

# Skriv reponsen sammen med navnet til brukeren
# og et punktum (".") ved hjelp av funksjonen print_sentence
# MANGLER KODE HER!!!
        print_sentence(rsp,navn,(". \n"))
main()