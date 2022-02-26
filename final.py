### Final Project: Researching Catalogued Work in MoMA

## Introduction: Representation of art is known to be very problematic in terms ...
##   In this study, we look to see if there is any relation between if the artwork is catalogued and 
##   the other attributes which it might have. Cataloguing artworks is extremely important as it 
##   not only showcases the importance which the musuem might place on the artwork, but it also
##   essential for risk management, research and exhibition development. 

  ## https://mgnsw.org.au/sector/resources/online-resources/collection-management/cataloguing/

## Data: ...

## Importing & reading data
import pandas as pd

df = pd.read_csv("./collection/Artworks.csv")

## Cleaning the data
print(df.columns)

# These attributes give the same info: 'Artist' & 'ConstituentID'
#  so I plan on droping 'Artist'.
df.drop("Artist", axis=1, inplace=True)

# These attributes give the same info: "ObjectID" & "Title"
#  so I plan on droping "Title"
df.drop("Title", axis=1, inplace=True)

# Measurement attributes give the same info as "Dimensions"
#  so I plan on droping "Dimensions"
df.drop("Dimensions", axis=1, inplace=True)

# Also droping 'URL' & 'ThumbnailURL' as they don't give any real info.
#  These are only filled out for catalogued artworks.
df.drop('URL', axis=1, inplace=True)
df.drop('ThumbnailURL', axis=1, inplace=True)

# "AccessionNumber" refers to the barely visible coded number attached the artwork in 
#  real life. This is used to link the displayed or archived work with it proper 
#  identification and knowledge for the humans working at the museum.
   # https://www.okmuseums.org/sites/oma2/uploads/documents/Technical_Bulletins/Technical_Bulletin_42_-_Applying_Accession_Numbers_Part_I.pdf

df.drop("AccessionNumber", axis=1, inplace=True)

# Measurement attributes that are NaN will now be zero (ie 'Circumference (cm)', 
#  'Depth (cm)', 'Diameter (cm)', 'Height (cm)', 'Length (cm)', 'Weight (kg)', 'Width (cm)', 
#  'Seat Height (cm)', 'Duration (sec.)' )
df['Circumference (cm)'].replace(pd.NA, 0, inplace=True)
df['Depth (cm)'].replace(pd.NA, 0, inplace=True)
df['Diameter (cm)'].replace(pd.NA, 0, inplace=True)
df['Height (cm)'].replace(pd.NA, 0, inplace=True)
df['Length (cm)'].replace(pd.NA, 0, inplace=True)
df['Weight (kg)'].replace(pd.NA, 0, inplace=True)
df['Width (cm)'].replace(pd.NA, 0, inplace=True)
df['Seat Height (cm)'].replace(pd.NA, 0, inplace=True)
df['Duration (sec.)'].replace(pd.NA, 0, inplace=True)


# This is now a datetime obj
df["DateAcquired"] =  pd.to_datetime(df["DateAcquired"]) 

# Changing string attributes to numbers as well as giving them their own csv
departments = dict()
for idx, x in enumerate(df["Department"].unique()):
	departments[x] = idx
	df["Department"].replace(x, idx, inplace=True)

classifications = dict()
for idx, x in enumerate(df["Classification"].unique()):
	classifications[x] = idx
	df["Classification"].replace(x, idx, inplace=True)

creditlines = dict()
for idx, x in enumerate(df["CreditLine"].unique()):
	creditlines[x] = idx
	df["CreditLine"].replace(x, idx, inplace=True)


#TODO: Decide how I am dealing with these attribues:
  #'ArtistBio', 'Nationality', 'BeginDate', 'EndDate', 'Gender', 'Date', 'Medium',

print(df.head(5))

## Exploration (EDA)


## Classification Analysis