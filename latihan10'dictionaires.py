,# membuat dictionary

user = {
    "Name": "Khifransyah",
    "Age": 19,
    "Country": "Indonesia",
    "Married": False,
    "Hobby": ["Coding", "Fishing", "Futsal"],
    "Socmed": {
        "Instagram": "@keeprunn",
        "Whatsapp": "08986930758"
    }
}
print("Nama user adalah :", user["Name"])
print("Social media-nya :", user["Socmed"])
print("="*20)

# atau bisa pake dict

warnaBaju = dict(jamal="Orange", pukis="biru", keep="hijau")

print("warna baju jamal :", warnaBaju['jamal'])
print("="*20)

# mengubah nilai dictionary

warnaBaju ['jamal'] = "Biru"
print("warna baju jamal skrg :" , warnaBaju['jamal'])
print("="*20)

# menghapus nilai dictionary

del warnaBaju['keep']
print(warnaBaju)
print("="*20)

# menambah item ke dictionary

warnaBaju.update({"keep":"ungu"})

print(warnaBaju)
print("="*20)

# mengambil panjang dictionary

print("total dictionary warnaBaju adalah : ", len(warnaBaju))
print("="*20)

# mengambil nilai dictionary dengan .get

print("saya mengambila warna baju pukis : ", warnaBaju.get("pukis"))
print("=" * 20)
# mengambil nilai dictionary pake perulangan/looping

for key, val in user.items():
    print("%s : %s" % (key, val))