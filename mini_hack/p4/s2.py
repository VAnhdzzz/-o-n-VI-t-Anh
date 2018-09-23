
ten_dang_nhap = (input("nhap ten dang nhap "))
mk = input("nhap may khau")
nhap_lai =(input("nhap lai mat khau"))
if mk != nhap_lai:
    print("loi")
    nhap_lai =(input("nhap lai mat khau"))
email = (input("email: "))
while "@" not in email and "." not in email:
    email = (input("email: "))

while  mk.isalpha() and  mk.isdigit():
    mk = (input("nhap may khau"))
