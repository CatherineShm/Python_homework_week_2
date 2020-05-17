### Zadanie 3.2 | Miesiące

# import mock   ##powinne być przydatne dla test_function()
# import module


def days_of_month(month=input("Podaj miesiąc: ").lower(), year=2020):
# def days_of_month(month: str, year=2020): ### wersja dla testow, jak sprawdzaam, dodawałam również lower wszędzie przy
#                                                "month", ale i tak testy z dużymi literami nie przechodzą
#Wersja bez testów działa sprawnie :)
    """
    This function return the number of days for the asked month.
    :param month: provide a month
    :param year: if your month is "luty", provide the year
    :return: number of days
    """

    if month == "luty":
        year = int(input("Podaj rok: "))
        if year % 4 != 0:
            return f"Luty w {year} roku ma 28 dni."
        else:
            return f"Luty w {year} roku ma 29 dni."

    months = {"styczen": 31, "marzec": 31, "maj": 31, "lipiec": 31,
                 "sierpien": 31, "pazdziernik": 31, "grudzien": 31,
                 "kwiecien": 30, "czerwiec": 30, "wrzesien": 30, "listopad": 30}
    if month in months:
        return f"{month.title()} ma {months[month]} dni/dzień."

print(days_of_month())

def test_days():
    assert days_of_month(month="marzec") == "Marzec ma 31 dni/dzień."
    assert days_of_month(month="sierpien") == "Sierpien ma 31 dni/dzień."
def test_upper():
    assert days_of_month(month="Maj") == "Maj ma 31 dni/dzień."
    assert days_of_month(month="ListoPad") == "Listopad ma 30 dni/dzień."
# def test_function():
#     with mock.patch.days_of_month(__builtins__, "Podaj rok: ", lambda: "2020"):
#         assert module.days_of_month("luty") == "Luty w 2020 roku ma 28 dni."
