
class Narzedzia:
    SAMOGLOSKI = set("aąeęiouóyAĄEĘIOUÓY")

    def policz_samogloski(tekst: str) -> int:
        if tekst:
            return sum(1 for znak in tekst if znak in Narzedzia.SAMOGLOSKI)
        return 0
    def usun_powtorzenia(lancuch: str)-> str:
        if lancuch:
            wynik = [lancuch[0]]
            for znak in lancuch[1:]:
                if znak != wynik[-1]:
                    wynik.append(znak)
            return "".join(wynik)
        return ""
        
def main() -> None: 
    tekst = input("TEkst do zliczbenia samogłosek: ")
    print("Samogłoski: ", Narzedzia.policz_samogloski(tekst))
    
    lancuch = input("Łancuch do usuniecia powtorzen: ")
    print("Po usunięciu: ", Narzedzia.usun_powtorzenia(lancuch))

if __name__ == "__main__": main()