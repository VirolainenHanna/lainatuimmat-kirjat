import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

kirjat = pd.read_csv("Helmet_lainatuimmat_kirjat.csv", sep=";")
# print(kirjat.info())

aikuistenkirjat = kirjat[kirjat.Kirja == "aikuistenkirjat"]
# print(aikuistenkirjat.info())

aikuistenkirjat["Teos"] = aikuistenkirjat["Tekijä"] + aikuistenkirjat["Nimeke"]
# print(aikuistenkirjat.head())

lainatuimmat_vuosittain = aikuistenkirjat.groupby(["Vuosi", "Teos"], as_index=False)[
    "Lainauskerrat"
].sum()
# print(lainatuimmat_vuosittain.head())


# Lainatuimmat kirjat 2014
lainatuimmat_2014 = lainatuimmat_vuosittain[lainatuimmat_vuosittain.Vuosi == 2014]
lainatuimmat_2014_sort = (
    lainatuimmat_2014.sort_values(by=["Lainauskerrat"], ascending=False)
    .reset_index(drop=True)
    .iloc[0:9]
)

sns.barplot(x="Lainauskerrat", y="Teos", data=lainatuimmat_2014_sort)
plt.title("Lainatuimmat kirjat 2014")
sns.set_style("whitegrid")
sns.set_palette("Paired")
ax = plt.subplot()
for i in ax.patches:
    plt.text(
        i.get_width(), i.get_y() + 0.65, str(round(i.get_width())),
    )
plt.ylabel("")
plt.axis([6000, 15000, 9, -1])
plt.show()

# Lainatuimmat kirjat 2015
lainatuimmat_2015 = lainatuimmat_vuosittain[lainatuimmat_vuosittain.Vuosi == 2015]
lainatuimmat_2015_sort = (
    lainatuimmat_2015.sort_values(by=["Lainauskerrat"], ascending=False)
    .reset_index(drop=True)
    .iloc[0:9]
)

plt.clf()
sns.barplot(x="Lainauskerrat", y="Teos", data=lainatuimmat_2015_sort)
plt.title("Lainatuimmat kirjat 2015")
sns.set_style("whitegrid")
sns.set_palette("Paired")
ax = plt.subplot()
for i in ax.patches:
    plt.text(
        i.get_width(), i.get_y() + 0.65, str(round(i.get_width())),
    )
plt.ylabel("")
plt.axis([4000, 12000, 9, -1])
plt.show()

# Lainatuimmat kirjat 2016
lainatuimmat_2016 = lainatuimmat_vuosittain[lainatuimmat_vuosittain.Vuosi == 2016]
lainatuimmat_2016_sort = (
    lainatuimmat_2016.sort_values(by=["Lainauskerrat"], ascending=False)
    .reset_index(drop=True)
    .iloc[0:9]
)

plt.clf()
sns.barplot(x="Lainauskerrat", y="Teos", data=lainatuimmat_2016_sort)
plt.title("Lainatuimmat kirjat 2016")
sns.set_style("whitegrid")
sns.set_palette("Paired")
ax = plt.subplot()
for i in ax.patches:
    plt.text(
        i.get_width(), i.get_y() + 0.65, str(round(i.get_width())),
    )
plt.ylabel("")
plt.axis([8000, 15000, 9, -1])
plt.show()

# Lainatuimmat kirjat 2017
lainatuimmat_2017 = lainatuimmat_vuosittain[lainatuimmat_vuosittain.Vuosi == 2017]
lainatuimmat_2017_sort = (
    lainatuimmat_2017.sort_values(by=["Lainauskerrat"], ascending=False)
    .reset_index(drop=True)
    .iloc[0:9]
)

plt.clf()
sns.barplot(x="Lainauskerrat", y="Teos", data=lainatuimmat_2017_sort)
plt.title("Lainatuimmat kirjat 2017")
sns.set_style("whitegrid")
sns.set_palette("Paired")
ax = plt.subplot()
for i in ax.patches:
    plt.text(
        i.get_width(), i.get_y() + 0.65, str(round(i.get_width())),
    )
plt.ylabel("")
plt.axis([4000, 8000, 9, -1])
plt.show()

# Lainatuimmat kirjat 2018
lainatuimmat_2018 = lainatuimmat_vuosittain[lainatuimmat_vuosittain.Vuosi == 2018]
lainatuimmat_2018_sort = (
    lainatuimmat_2018.sort_values(by=["Lainauskerrat"], ascending=False)
    .reset_index(drop=True)
    .iloc[0:9]
)

plt.clf()
sns.barplot(x="Lainauskerrat", y="Teos", data=lainatuimmat_2018_sort)
plt.title("Lainatuimmat kirjat 2018")
sns.set_style("whitegrid")
sns.set_palette("Paired")
ax = plt.subplot()
for i in ax.patches:
    plt.text(
        i.get_width(), i.get_y() + 0.65, str(round(i.get_width())),
    )
plt.ylabel("")
plt.axis([8000, 16000, 9, -1])
plt.show()

# Lainatuimmat kirjat 2019
lainatuimmat_2019 = lainatuimmat_vuosittain[lainatuimmat_vuosittain.Vuosi == 2019]
lainatuimmat_2019_sort = (
    lainatuimmat_2019.sort_values(by=["Lainauskerrat"], ascending=False)
    .reset_index(drop=True)
    .iloc[0:9]
)

plt.clf()
sns.barplot(x="Lainauskerrat", y="Teos", data=lainatuimmat_2019_sort)
plt.title("Lainatuimmat kirjat 2019")
sns.set_style("whitegrid")
sns.set_palette("Paired")
ax = plt.subplot()
for i in ax.patches:
    plt.text(
        i.get_width(), i.get_y() + 0.65, str(round(i.get_width())),
    )
plt.ylabel("")
plt.axis([6000, 14000, 9, -1])
plt.show()

# Lainatuimmat kirjat 2020
lainatuimmat_2020 = lainatuimmat_vuosittain[lainatuimmat_vuosittain.Vuosi == 2020]
lainatuimmat_2020_sort = (
    lainatuimmat_2020.sort_values(by=["Lainauskerrat"], ascending=False)
    .reset_index(drop=True)
    .iloc[0:9]
)

plt.clf()
sns.barplot(x="Lainauskerrat", y="Teos", data=lainatuimmat_2020_sort)
plt.title("Lainatuimmat kirjat 2020")
sns.set_style("whitegrid")
sns.set_palette("Paired")
ax = plt.subplot()
for i in ax.patches:
    plt.text(
        i.get_width(), i.get_y() + 0.65, str(round(i.get_width())),
    )
plt.ylabel("")
plt.axis([4000, 10000, 9, -1])
plt.show()

# Lainatuimmat kirjat 2014-2020
lainatuimmat_14_20 = aikuistenkirjat.groupby(["Teos"], as_index=False)[
    "Lainauskerrat"
].sum()
lainatuimmat_14_20_sort = (
    lainatuimmat_14_20.sort_values(by=["Lainauskerrat"], ascending=False)
    .reset_index(drop=True)
    .iloc[0:19]
)

sns.barplot(x="Lainauskerrat", y="Teos", data=lainatuimmat_14_20_sort)
sns.set_palette("Paired")
sns.set_style("whitegrid")
ax = plt.subplot()
for i in ax.patches:
    plt.text(i.get_width(), i.get_y() + 0.65, str(round(i.get_width())))
plt.title("Lainatuimmat kirjat 2014-2020")
plt.ylabel("")
plt.axis([14000, 29000, 19, -1])
plt.show()


# Millä kvartaalilla ihmiset lainaavat eniten, tämän datan perusteella...
lainatuimmat_kvartaali = (
    aikuistenkirjat.groupby(["Kvartaali"], as_index=False)["Lainauskerrat"]
    .sum()
    .sort_values(by=["Lainauskerrat"], ascending=False)
)

plt.clf()
sns.set_palette("Paired")
sns.set_style("whitegrid")
sns.barplot(x="Kvartaali", y="Lainauskerrat", data=lainatuimmat_kvartaali)
plt.title("Lainat kvartaalettain")
plt.axis([-1, 4, 950000, 1300000])
plt.ylabel("Miljoonaa")
plt.xlabel("")
ax = plt.subplot()
ax.set_xticks([0, 1, 2, 3])
ax.set_xticklabels(["tammi-maalis", "huhti-kesä", "heinä-syys", "loka-joulu"])
for i in ax.patches:
    plt.text(
        i.get_x() + 0.65, i.get_width(), str(round(i.get_width())),
    )
plt.show()

