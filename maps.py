from data_structures import CountryElement


class Ukraine:
    def __init__(self):
        self.Cherkasy = CountryElement("Cherkasy")
        self.Chernihiv = CountryElement("Chernihiv")
        self.Chernivtsi = CountryElement("Chernivtsi")
        self.Crimea = CountryElement("Crimea")
        self.Dnipropetrovsk = CountryElement("Dnipropetrovsk")
        self.Donetsk = CountryElement("Donetsk")
        self.IvanoFrankivsk = CountryElement("Ivano-Frankivsk")
        self.Kharkiv = CountryElement("Kharkiv")
        self.Kherson = CountryElement("Kherson")
        self.Khmelnytskyi = CountryElement("Khmelnytskyi")
        self.Kiev = CountryElement("Kiev")
        self.Kirovohrad = CountryElement("Kirovohrad")
        self.Luhansk = CountryElement("Luhansk")
        self.Lviv = CountryElement("Lviv")
        self.Mykolaiv = CountryElement("Mykolaiv")
        self.Odessa = CountryElement("Odessa")
        self.Poltava = CountryElement("Poltava")
        self.Rivne = CountryElement("Rivne")
        self.Sumy = CountryElement("Sumy")
        self.Ternopil = CountryElement("Ternopil")
        self.Vinnytsia = CountryElement("Vinnytsia")
        self.Volyn = CountryElement("Volyn")
        self.Zakarpattia = CountryElement("Zakarpattia")
        self.Zaporizhia = CountryElement("Zaporizhia")
        self.Zhytomyr = CountryElement("Zhytomyr")

        self.Cherkasy.neighbours.append(self.Kiev)
        self.Cherkasy.neighbours.append(self.Poltava)
        self.Cherkasy.neighbours.append(self.Kirovohrad)
        self.Cherkasy.neighbours.append(self.Vinnytsia)

        self.Chernihiv.neighbours.append(self.Kiev)
        self.Chernihiv.neighbours.append(self.Sumy)
        self.Chernihiv.neighbours.append(self.Poltava)

        self.Chernivtsi.neighbours.append(self.IvanoFrankivsk)
        self.Chernivtsi.neighbours.append(self.Ternopil)
        self.Chernivtsi.neighbours.append(self.Khmelnytskyi)
        self.Chernivtsi.neighbours.append(self.Vinnytsia)

        self.Crimea.neighbours.append(self.Kherson)

        self.Dnipropetrovsk.neighbours.append(self.Poltava)
        self.Dnipropetrovsk.neighbours.append(self.Kharkiv)
        self.Dnipropetrovsk.neighbours.append(self.Donetsk)
        self.Dnipropetrovsk.neighbours.append(self.Zaporizhia)
        self.Dnipropetrovsk.neighbours.append(self.Kherson)
        self.Dnipropetrovsk.neighbours.append(self.Mykolaiv)
        self.Dnipropetrovsk.neighbours.append(self.Kirovohrad)

        self.Donetsk.neighbours.append(self.Luhansk)
        self.Donetsk.neighbours.append(self.Kharkiv)
        self.Donetsk.neighbours.append(self.Dnipropetrovsk)
        self.Donetsk.neighbours.append(self.Zaporizhia)

        self.IvanoFrankivsk.neighbours.append(self.Zakarpattia)
        self.IvanoFrankivsk.neighbours.append(self.Lviv)
        self.IvanoFrankivsk.neighbours.append(self.Ternopil)
        self.IvanoFrankivsk.neighbours.append(self.Chernivtsi)

        self.Kharkiv.neighbours.append(self.Sumy)
        self.Kharkiv.neighbours.append(self.Poltava)
        self.Kharkiv.neighbours.append(self.Dnipropetrovsk)
        self.Kharkiv.neighbours.append(self.Donetsk)
        self.Kharkiv.neighbours.append(self.Luhansk)

        self.Kherson.neighbours.append(self.Crimea)
        self.Kherson.neighbours.append(self.Zaporizhia)
        self.Kherson.neighbours.append(self.Dnipropetrovsk)
        self.Kherson.neighbours.append(self.Mykolaiv)

        self.Khmelnytskyi.neighbours.append(self.Vinnytsia)
        self.Khmelnytskyi.neighbours.append(self.Zhytomyr)
        self.Khmelnytskyi.neighbours.append(self.Rivne)
        self.Khmelnytskyi.neighbours.append(self.Ternopil)
        self.Khmelnytskyi.neighbours.append(self.Chernivtsi)

        self.Kiev.neighbours.append(self.Cherkasy)
        self.Kiev.neighbours.append(self.Chernihiv)
        self.Kiev.neighbours.append(self.Zhytomyr)
        self.Kiev.neighbours.append(self.Vinnytsia)

        self.Kirovohrad.neighbours.append(self.Mykolaiv)
        self.Kirovohrad.neighbours.append(self.Dnipropetrovsk)
        self.Kirovohrad.neighbours.append(self.Poltava)
        self.Kirovohrad.neighbours.append(self.Cherkasy)
        self.Kirovohrad.neighbours.append(self.Vinnytsia)
        self.Kirovohrad.neighbours.append(self.Odessa)

        self.Lviv.neighbours.append(self.Zakarpattia)
        self.Lviv.neighbours.append(self.IvanoFrankivsk)
        self.Lviv.neighbours.append(self.Ternopil)
        self.Lviv.neighbours.append(self.Rivne)
        self.Lviv.neighbours.append(self.Volyn)

        self.Luhansk.neighbours.append(self.Kharkiv)
        self.Luhansk.neighbours.append(self.Donetsk)

        self.Mykolaiv.neighbours.append(self.Odessa)
        self.Mykolaiv.neighbours.append(self.Kirovohrad)
        self.Mykolaiv.neighbours.append(self.Dnipropetrovsk)
        self.Mykolaiv.neighbours.append(self.Kherson)

        self.Odessa.neighbours.append(self.Vinnytsia)
        self.Odessa.neighbours.append(self.Kirovohrad)
        self.Odessa.neighbours.append(self.Mykolaiv)

        self.Poltava.neighbours.append(self.Dnipropetrovsk)
        self.Poltava.neighbours.append(self.Kharkiv)
        self.Poltava.neighbours.append(self.Sumy)
        self.Poltava.neighbours.append(self.Chernihiv)
        self.Poltava.neighbours.append(self.Cherkasy)
        self.Poltava.neighbours.append(self.Kirovohrad)

        self.Rivne.neighbours.append(self.Volyn)
        self.Rivne.neighbours.append(self.Lviv)
        self.Rivne.neighbours.append(self.Ternopil)
        self.Rivne.neighbours.append(self.Khmelnytskyi)
        self.Rivne.neighbours.append(self.Zhytomyr)

        self.Sumy.neighbours.append(self.Chernihiv)
        self.Sumy.neighbours.append(self.Poltava)
        self.Sumy.neighbours.append(self.Kharkiv)

        self.Ternopil.neighbours.append(self.Chernivtsi)
        self.Ternopil.neighbours.append(self.Khmelnytskyi)
        self.Ternopil.neighbours.append(self.Rivne)
        self.Ternopil.neighbours.append(self.Lviv)
        self.Ternopil.neighbours.append(self.IvanoFrankivsk)

        self.Vinnytsia.neighbours.append(self.Chernivtsi)
        self.Vinnytsia.neighbours.append(self.Khmelnytskyi)
        self.Vinnytsia.neighbours.append(self.Zhytomyr)
        self.Vinnytsia.neighbours.append(self.Kiev)
        self.Vinnytsia.neighbours.append(self.Cherkasy)
        self.Vinnytsia.neighbours.append(self.Kirovohrad)
        self.Vinnytsia.neighbours.append(self.Odessa)

        self.Volyn.neighbours.append(self.Lviv)
        self.Volyn.neighbours.append(self.Rivne)

        self.Zakarpattia.neighbours.append(self.Lviv)
        self.Zakarpattia.neighbours.append(self.IvanoFrankivsk)

        self.Zaporizhia.neighbours.append(self.Kherson)
        self.Zaporizhia.neighbours.append(self.Dnipropetrovsk)
        self.Zaporizhia.neighbours.append(self.Donetsk)

        self.Zhytomyr.neighbours.append(self.Rivne)
        self.Zhytomyr.neighbours.append(self.Khmelnytskyi)
        self.Zhytomyr.neighbours.append(self.Vinnytsia)
        self.Zhytomyr.neighbours.append(self.Kiev)

    def as_list(self):
        return [a for a in [getattr(self, attr) for attr in dir(self)] if isinstance(a, CountryElement)]
