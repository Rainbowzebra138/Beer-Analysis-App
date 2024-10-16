# Beer-Analysis-App
This project aims to see what attributes makes a highly rated beer. This project was done as part of a collage assingment for data sciance, but also offers a unique look on beer data from as resent as 2021

The spicifics of the data used were all downloaded from Kaggle. As of 10/16/2024 the app only analysis 2 diffrent data sets that were merged into one data set called beer_df.csv. 
The two data sets used were a list of beers and beer rankings from 2021 scraped from the website Beer Advicate, and beer recipes scraped from the website brewers friend from 2016. 
The back bone of the project data comes from the beer advicate data set. All of the beers shown, there rankings, and atributes all originate from this dataset. 
The brewers freind datas contains less data on beer flavor profiles but contains a much larger list of beer and beer messurment information. 
The beer recipe data information was avraged into beer styles and merged with the beer advicate data according to beer style. 
When merging the data, the style names from both data sets were not 1:1 with each other so I had to align the beers together using string matching scores and manuily correcting incorect matches with the closest avalible style on the list. 
The final product was beer_df.csv which uses the beer avicate data as an achor and the beer style means and variance from the beer recipe data to fill in some of the missing information from the former data set.

I also had to impute some of the missing values from the beer advicate data to create beer_df.csv but most of the data from beer advicate was present so little of the data is synthetic.

One last importent note; When using the beer app and it asks you to enter in a name of something, the name has to be the exact name as it appers in the table. 
If you have a beer in mind and are unsure of the beers exact name I sugest you enter the name into the surch bar on the data table and copy the exact name of the beer from the table, or you can google the beer name and copy the exact name from the beer advicate website.

Overall this is my first coding project and I expect some bugs or unoptimal code in the sorce so keep this in mind. As of 10/16/2024 I might revist this project to add more data but dont get your hopes up if you plan on following this project. 
