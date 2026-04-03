import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from a dictionary
df = pd.DataFrame(
    {
        "Name": [
            "Suresh",
            "Sithum",
            "Amanda"
        ],
        "Age": [26, 25, 25],
        "Sex": ["Male", "Male", "Female"]
    }
)
print(f"The DataFrame:\n {df}")

# Accessing a column
print(f"Age column:\n {df['Age']}")

# Creating a Series
ages = pd.Series([26, 25, 25], name="Age")
print(f"Age Series:\n {ages}")

# Maximum age use Table method
max_age = df["Age"].max()
print(f"Maximum age: {max_age}")

# Maximum age use Series method
max_age = ages.max()
print(f"Maximum age: {max_age}")

# Describe the DataFrame
df.describe()
print(f"DataFrame description:\n {df.describe()}")

# read and write tabular data
titanic = pd.read_csv("data/titanic.csv")
print("--------Titanic DataFrame--------")
print(titanic)

print("-------- Describe Titanic DataFrame --------")
print(titanic.describe())

print("-------- First 8 rows of the Titanic DataFrame --------")
print(titanic.head(8))

print("-------- Last 5 rows of the Titanic DataFrame --------")
print(titanic.tail())

print("-------- Data types of the Titanic DataFrame --------")
print(titanic.dtypes)

# --------create xlsx file from the Titanic DataFrame-------- #
titanic.to_excel("data/titanic.xlsx", sheet_name="passengers", index=False)

# --------read xlsx file-------- #
titanic = pd.read_excel("data/titanic.xlsx", sheet_name="passengers")
print("--------Titanic DataFrame from Excel file--------")
print(titanic.head())

print("-------- Info of the Titanic DataFrame --------")
print(titanic.info())

ages = titanic["Age"]
print("-------- Ages of the passengers --------")
print(ages.head())

print("-------- Type of the Age column --------")
print(type(titanic["Age"]))

print("-------- Shape of the Age column --------")
print(titanic["Age"].shape)

# --------head of Age and Sex columns-------- #
age_sex = titanic[["Age", "Sex"]]
print("-------- head of Age and Sex columns --------")
print(age_sex.head())

# --------Type of the Age and Sex columns-------- #
print("-------- Type of the Age and Sex columns --------")
print(type(titanic[["Age", "Sex"]]))

# --------Shape of the Age and Sex columns-------- #
print("-------- Shape of the Age and Sex columns --------")
print(titanic[["Age", "Sex"]].shape)

# -------- filter specific rows -------- #
above_35 = titanic[titanic["Age"] > 35]
print("-------- Passengers above 35 years old --------")
print(above_35.head())

print("-------- Boolean mask for passengers above 35 years old --------")
print(titanic["Age"] > 35)

print(above_35.shape)

# -------- filter specific rows using isin -------- #
class_23 = titanic[titanic["Pclass"].isin([2, 3])]
print("-------- Passengers in class 2 and 3 --------")
print(class_23.head())

# -------- filter specific rows using logical operators -------- #
class_23 = titanic[(titanic["Pclass"] == 2) | (titanic["Pclass"] == 3)]
print("-------- Passengers in class 2 and 3 --------")
print(class_23.head())

# -------- filter specific rows using notna -------- #
age_no_na = titanic[titanic["Age"].notna()]
print("-------- Passengers with non-missing age --------")
print(age_no_na.head())

print(age_no_na.shape)

# ---------- select specific rows and columns use loc --------- #
adult_names = titanic.loc[titanic["Age"] > 35, "Name"]
print("-------- Names of passengers above 35 years old --------")
print(adult_names.head())

# -------- select specific rows and columns use iloc --------- #
print(titanic.iloc[9:25, 2:5])

titanic.iloc[0:3, 3] = "anonymous"
print("-------- Updated Titanic DataFrame --------")
print(titanic.iloc[:5, 3])

# -------- create plots in pandas -------- #
air_quality = pd.read_csv("data/air_quality_no2.csv", index_col = 0, parse_dates = True)
print("-------- Air Quality DataFrame --------")
print(air_quality.head())

air_quality.plot()
plt.show()

air_quality["station_paris"].plot()
plt.show()

# -------- compare 𝑁⁢𝑂2 values measured in London versus Paris. -------- #
air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)
plt.show()

# -------- find the available plot methods -------- #
print([
    method_name
    for method_name in dir(air_quality.plot)
    if not method_name.startswith("_")
])

# -------- create a box plot -------- #
air_quality.plot.box()
plt.show()

# -------- create an area plot with separate subplots -------- #
axs = air_quality.plot.area(figsize=(12, 4), subplots=True)
plt.show()

# -------- create an area plot with one subplot -------- #
fig, axs = plt.subplots(figsize=(12, 4))
air_quality.plot.area(ax=axs)

axs.set_ylabel("NO$_2$ concentration")

fig.savefig("no2_concentration.png")

plt.show()

# -------- create a new column with the NO2 concentration in London in mg per cubic meter -------- #

air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882
print("-------- Air Quality DataFrame with new column --------")
print(air_quality.head())

# -------- create a new column with the ratio between the NO2 concentration in Paris and Antwerp -------- #
air_quality["ratio_paris_antwerp"] = (
    air_quality["station_paris"] / air_quality["station_antwerp"]
)
print(air_quality.head())

# -------- rename the columns -------- #
air_quality_renamed = air_quality.rename(
    columns={
        "station_antwerp" : "BETR801",
        "station_paris" : "FR04014",
        "station_london" : "London Westminister"
    }
)

#-------- convert the column names to lowercase -------- #
print(air_quality_renamed.head())

air_quality_renamed = air_quality_renamed.rename(columns=str.lower)
print(air_quality_renamed.head())

# calculate summary of statistics
titanic = pd.read_csv("data/titanic.csv")
print(titanic.head())

# -------- calculate the mean age of the passengers -------- #
print("-------- Mean age of the passengers --------")
print(titanic["Age"].mean())

# -------- calculate the median age and ticket fare of the passengers -------- #
print("-------- Median age and ticket fare of the passengers --------")
print(titanic[["Age", "Fare"]].median())

print("-------- Summary statistics of age and ticket fare of the passengers --------")
print(titanic[["Age", "Fare"]].describe())

print("-------- aggregate statistics of age and ticket fare of the passengers --------")
print(titanic.agg(
    {
        "Age": ["min", "max", "median", "skew"],
        "Fare": ["min", "max", "median", "mean"]
    }
))

print("-------- average age for male versus female Titanic passengers --------")
# methode 01
print(titanic[["Sex", "Age"]].groupby("Sex").mean())


print(titanic.groupby("Sex").mean(numeric_only=True))

print(titanic.groupby("Sex")["Age"].mean())

print("-------- number of passengers in each Pclass --------")
print(titanic["Pclass"].value_counts())

print("-------- number of passengers in each Pclass use groupby --------")
print(titanic.groupby("Pclass")["Pclass"].count())