class Utilizator():
    def __init__(self, nume, varsta, sex):
        self.nume = nume
        self.varsta = varsta
        self.sex = sex

    def informatii_client(self):
        print("Detalii client:")
        print("")
        print("Nume", self.nume)
        print("Varsta", self.varsta)
        print("Sex", self.sex)

class Banca(Utilizator):
    def __init__(self, nume, varsta, sex):
        super().__init__(nume, varsta, sex)
        self.sold_bancar = 0

    def economie(self, suma):
        self.suma = suma
        self.sold_bancar = self.sold_bancar + self.suma
        print("Soldul bancar a fost actualizat: LEI", self.sold_bancar)

    def retrageri(self, suma):
        self.suma = suma
        if(self.suma > self.sold_bancar):
            print("Fond insuficient | Sold disponibil: LEI", self.sold_bancar)
        else:
            print("Soldul bancar a fost actualizat: LEI", self.sold_bancar)
    def afisare_sold(self):
        self.afiseaza_detalii()
        print("Sold: LEI", self.sold_bancar)
            
