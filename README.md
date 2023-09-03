# ------------- Epítome (Summary) -------------------------

# -------- Gattering the Data
The idea that motivated this project was to use selenium to search on Google for the prices of every
website that was advertising that specific product and retrieve the price and the name of the site into
a CSV and/or xlsx file and then do some analysis comparing the prices from Google and our fictitious 
prices and data.

At first, we tried to use the product's description and factory ID to find it on Google, but the
search didn't give back a precise and trustful result. So, we tried to use the product's code bars to
search for it on Google, which had a much more satisfactory result.


# --------- Data Cleaning
# Price:
The price's data always came with the dollar sign and had a varying type sometimes, it came as a string,
sometimes came as a float. So we created a Python file called "Functions" and created in it a function 
called "clean_float," that would treat all the price's data.

# Market Competitor:
The market competitor's data almost always came with the ".com" or ".com.br" with it and sometimes in caps,
sometimes in lower, we needed to standardize it, so we created the function "clean_competition" to treat
this data.

# Dealing with the nan's
When we put all the data together the first time we saw that we had 15% of all the data as null values.
We needed to fill that data to get a better analysis. So, we saw that some products where almost the same,
only different by color, and in almost all the cases we had the price of one but didn't find the price
of the other. What helped us was that these products had almost the same factory id, only the last number
was different. So, if the code found a null value, but we had the price from the similar product the code 
would replace the null value for the price of the similar product.

- What about the products that had a null value but didn't have a similiar product's price found?
In this case we considered that the product has not yet arrived on the internet. So, we replaced the
null values for our fictitious prices.


# ---------- "I'm not a robot" problem


# A work in progesss
# a list of improvements that we think the code needs to peform perfectly:
- An "if" filter to see if the product that we wanted is really the one that we found. Maybe we can only 
get the product's price if the description of the product says it is the kind of product that we are 
expecting it to be;
- Think of a way of dealing with the "I'm not a robot" problem without closing the browser and re-opening
it;
