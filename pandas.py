#-----------------------------------------------------------------------------#
#          For this tutorial we need the following packages                   #
#                   pandas, matplotlib, openpyxl                              #
#      The link to this code + data are in the video description              #
#-----------------------------------------------------------------------------#
import pandas as pd
import matplotlib.pyplot as plt

# Read data from .csv file
df = pd.read_csv("C:/examples/titanic.csv", sep=",", header=0)

# Explore the data
df.index                        # Show row index
df.columns                      # Show column names
df.shape                        # Show shape
df.loc[:, ["Age", "Fare"]]      # Acess all valus in certain columns
df.loc[1, "Age"]                # Get value of a specific cell
df.rename(columns={"Ticket": "ticket", "Cabin": "cabin"}, inplace=True)

# Subset of data frame
df[["Age", "Fare"]]
df[df["Age"] > 50]
df[df["Pclass"].isin([1,2])]
df[(df["Age"] > 50) | (df["Pclass"] > 2)]

# Statistics
df.loc[:, ["Age", "Fare"]].max(axis=0)
df.loc[:, ["Age", "Fare"]].std(axis=0)

# Create a new column from existing columns
df["Survived_Age"] = df["Survived"] * df["Age"]

# Visualize
df.plot(y="Age", kind="hist")
plt.show()

df.plot(x="Age", y="Fare", kind="scatter", alpha=0.5)
plt.show()

df.plot(y=["Age", "Fare"], kind="box", subplots=True)
plt.show()

# Save data
df.to_csv("C:/examples/new_titanic.csv", index=False)
df.to_pickle("C:/examples/new_titanic.pkl")
df.to_excel("C:/examples/new_titanic.xlsx", engine="openpyxl")
df.to_parquet("C:/examples/new_titanic.parquet.gzip", compression="gzip")
df.to_hdf("C:/examples/new_titanic.h5", key="s")

ndf = pd.read_pickle("C:/examples/new_titanic.pkl")
ndf = pd.read_excel("C:/examples/new_titanic.xlsx", sheet_name="Sheet1")
ndf = pd.read_parquet("C:/examples/new_titanic.parquet.gzip")
ndf = pd.read_hdf("C:/examples/new_titanic.h5", key="s")












