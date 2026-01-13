class Calculator:
    def toplama(self, a, b):
        return a + b

    def cikarma(self, a, b):
        return a - b

    def carpma(self, a, b):
        return a * b

    def bolme(self, a, b):
        if b == 0:
            return "Hata: Bir sayı 0'a bölünemez."
        return a / b


class CalculatorApp:
    def __init__(self):
        self.calculator = Calculator()

    def menu_goster(self):
        print("\n--- OOP PYTHON HESAP MAKİNESİ ---")
        print("1 - Toplama")
        print("2 - Çıkarma")
        print("3 - Çarpma")
        print("4 - Bölme")
        print("5 - Çıkış")

    def sayi_al(self, mesaj):
        while True:
            try:
                return float(input(mesaj))
            except ValueError:
                print("Lütfen geçerli bir sayı giriniz.")

    def calistir(self):
        while True:
            self.menu_goster()
            secim = input("Seçiminizi girin (1-5): ")

            if secim == "5":
                print("Programdan çıkılıyor...")
                break

            if secim not in ["1", "2", "3", "4"]:
                print("Geçersiz seçim!")
                continue

            sayi1 = self.sayi_al("Birinci sayı: ")
            sayi2 = self.sayi_al("İkinci sayı: ")

            if secim == "1":
                sonuc = self.calculator.toplama(sayi1, sayi2)
            elif secim == "2":
                sonuc = self.calculator.cikarma(sayi1, sayi2)
            elif secim == "3":
                sonuc = self.calculator.carpma(sayi1, sayi2)
            elif secim == "4":
                sonuc = self.calculator.bolme(sayi1, sayi2)

            print("Sonuç:", sonuc)


if __name__ == "__main__":
    app = CalculatorApp()
    app.calistir()
