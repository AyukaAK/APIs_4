#!/usr/bin/env python
# coding: utf-8

# # WeatherAPI (Weather)
# 
# Answer the following questions using [WeatherAPI](http://www.weatherapi.com/). I've added three cells for most questions but you're free to use more or less! Hold `Shift` and hit `Enter` to run a cell, and use the `+` on the top left to add a new cell to a notebook.
# 
# Be sure to take advantage of both the documentation and the API Explorer!
# 
# ## 0) Import any libraries you might need
# 
# - *Tip: We're going to be downloading things from the internet, so we probably need `requests`.*
# - *Tip: Remember you only need to import requests once!*

# [Interactive API Explorer](https://www.weatherapi.com/api-explorer.aspx#forecast)
# 
# [Documentation](https://www.weatherapi.com/docs/)
# 

# In[4]:


import requests


# ## 1) Make a request to the Weather API for where you were born (or lived, or want to visit!).
# 
# - *Tip: The URL we used in class was for a place near San Francisco. What was the format of the endpoint that made this happen?*
# - *Tip: Save the URL as a separate variable, and be sure to not have `[` and `]` inside.*
# - *Tip: How is north vs. south and east vs. west latitude/longitude represented? Is it the normal North/South/East/West?*
# - *Tip: You know it's JSON, but Python doesn't! Make sure you aren't trying to deal with plain text.* 
# - *Tip: Once you've imported the JSON into a variable, check the timezone's name to make sure it seems like it got the right part of the world!*

# In[41]:


url_live = "http://api.weatherapi.com/v1/current.json?key=976685a7f4594f9c90b191549221406&q=Reykjavik&aqi=no"


# In[42]:


response = requests.get (url_live)
data = response.json()


# This is a request to the weather API for Reykjavik, Iceland

# ## 2) What's the current wind speed? How much warmer does it feel than it actually is?
# 
# - *Tip: You can do this by browsing through the dictionaries, but it might be easier to read the documentation*
# - *Tip: For the second half: it **is** one temperature, and it **feels** a different temperature. Calculate the difference.*

# In[43]:


print(data)


# In[44]:


print(data['current']['wind_kph'])


# In[45]:


print(data['current'].keys())


# In[46]:


print(data['current']['temp_c'])


# In[47]:


print(data['current']['feelslike_c'])


# In[48]:


print("It feels like", round(data['current']['temp_c']-data['current']['feelslike_c']), "C degree warmer than it actually is")


# ## 3) What is the API endpoint for moon-related information? For the place you decided on above, how much of the moon will be visible tomorrow?
# 
# - *Tip: Check the documentation!*
# - *Tip: If you aren't sure what something means, ask in Slack*

# In[49]:


url_moon = "http://api.weatherapi.com/v1/astronomy.json?key=976685a7f4594f9c90b191549221406&q=Reykjavik&dt=2022-06-16"
response_moon = requests.get(url_moon)
data_moon = response_moon.json()


# In[50]:


print(data_moon)


# In[51]:


print(data_moon['astronomy']['astro']['moon_phase'])


# ## 4) What's the difference between the high and low temperatures for today?
# 
# - *Tip: When you requested moon data, you probably overwrote your variables! If so, you'll need to make a new request.*

# In[55]:


url_today = "http://api.weatherapi.com/v1/forecast.json?key=976685a7f4594f9c90b191549221406&q=Reykjavik&days=1&aqi=no&alerts=no"
response = requests.get(url_today)
data = response.json()
print(data)


# For the max and min temp for today, you need to have the forecast API (one day)

# In[82]:


print(data['forecast']['forecastday'][0]['day'].keys())


# In[89]:


temp_dif = data['forecast']['forecastday'][0]['day']['maxtemp_c']-data['forecast']['forecastday'][0]['day']['mintemp_c']
print("Temperatures difference between the high and the low is", round(temp_dif),"C degrees")


# ## 4.5) How can you avoid the "oh no I don't have the data any more because I made another request" problem in the future?
# 
# What variable(s) do you have to rename, and what would you rename them?

# ### You name the url variable with different names

# In[ ]:





# ## 5) Go through the daily forecasts, printing out the next three days' worth of predictions.
# 
# I'd like to know the **high temperature** for each day, and whether it's **hot, warm, or cold** (based on what temperatures you think are hot, warm or cold).
# 
# - *Tip: You'll need to use an `if` statement to say whether it is hot, warm or cold.*

# In[90]:


url_3days = 'http://api.weatherapi.com/v1/forecast.json?key=976685a7f4594f9c90b191549221406&q=Reykjavik&days=3&aqi=no&alerts=no'
response_3days = requests.get(url_3days)
data_3days = response_3days.json()
print(data_3days)


# In[100]:


print(data_3days['forecast']['forecastday'][0]['day'])


# In[101]:


print(data_3days['forecast']['forecastday'][0]['day']['maxtemp_c'])


# In[102]:


print(data_3days['forecast']['forecastday'][0]['date'])


# In[118]:


for max_temp in data_3days['forecast']['forecastday']:
    if max_temp['day']['maxtemp_c'] < 15:
        print("On", max_temp['date'], "The highest temperature is", max_temp['day']['maxtemp_c'], "C degrees and it's cold")

print ("It is always below 15C degrees and cold in Reykjavik, Iceland, because it's in the Arctic!!")


# ## 5b) The question above used to be an entire week, but not any more. Try to re-use the code above to print out seven days.
# 
# What happens? Can you figure out why it doesn't work?
# 
# * *Tip: it has to do with the reason you're using an API key - maybe take a look at the "Air Quality Data" introduction for a hint? If you can't figure it out right now, no worries.*

# In[128]:


url_7days = 'http://api.weatherapi.com/v1/forecast.json?key=976685a7f4594f9c90b191549221406&q=Reykjavik&days=7&aqi=no&alerts=no'
response_7days = requests.get(url_7days)
data_7days = response_7days.json()
print(data_7days)


# In[129]:


for max_temp_7days in data_7days['forecast']['forecastday']:
    if max_temp_7days ['day']['maxtemp_c'] < 15:
        print("On", max_temp_7days['date'], "The highest temperature is", max_temp_7days['day']['maxtemp_c'], "C degrees and it's cold")

print ("It is always below 15C degrees and cold in Reykjavik, Iceland, because it's in the Arctic!!")


# I changed the API to the 7 days forecast but it still shows for 3 days...

# ## 6) What will be the hottest day in the next three days? What is the high temperature on that day?

# In[131]:


url_3days = 'http://api.weatherapi.com/v1/forecast.json?key=976685a7f4594f9c90b191549221406&q=Reykjavik&days=3&aqi=no&alerts=no'
response_3days = requests.get(url_3days)
data_3days = response_3days.json()
print(data_3days)


# In[135]:


#Example of the first day
print(data_3days['forecast']['forecastday'][0]['day']['maxtemp_c'])
print(data_3days['forecast']['forecastday'][0]['date'])


# In[145]:


MaxTemp = max(Temp3 ["day"]["maxtemp_c"] for Temp3 in data_3days ["forecast"]["forecastday"])

for Temp3 in data_3days ["forecast"]["forecastday"]:
    if Temp3["day"]["maxtemp_c"] == MaxTemp:
        print (Temp3["date"], "has the highest temperature of", MaxTemp, "C degree,", "but it is still cold")


# ## 7) What's the weather looking like for the next 24+ hours in Miami, Florida?
# 
# I'd like to know the temperature for every hour, and if it's going to have cloud cover of more than 50% say "{temperature} and cloudy" instead of just the temperature. 
# 
# - *Tip: You'll only need one day of forecast*

# In[146]:


url_miami = 'http://api.weatherapi.com/v1/forecast.json?key=976685a7f4594f9c90b191549221406&q=Miami&days=1&aqi=no&alerts=no'
response_miami = requests.get(url_miami)
data_miami = response_miami.json()
print(data_miami)


# In[156]:


print(data_miami['forecast']['forecastday'][0]['hour'][0].keys())


# In[160]:


#Example
print(data_miami['forecast']['forecastday'][0]['hour'][0]['time'])
print(data_miami['forecast']['forecastday'][0]['hour'][0]['temp_c'])
print(data_miami['forecast']['forecastday'][0]['hour'][0]['cloud'])


# In[163]:


#Example: we just loop through the second list because it's just only one day
print(data_miami['forecast']['forecastday'][0]['hour'][1]['time'])


# In[168]:


for weather_miami in data_miami['forecast']['forecastday'][0]['hour']:
    if weather_miami['cloud'] > 50:
        print ("On", weather_miami['time'], "the temperature is", weather_miami['temp_c'], "C degree", "and it's cloudy")
    else:
        print ("On", weather_miami['time'], "the temperature is", weather_miami['temp_c'], "C degree")
               


# ## 8) For the next 24-ish hours in Miami, what percent of the time is the temperature above 85 degrees?
# 
# - *Tip: You might want to read up on [looping patterns](http://jonathansoma.com/lede/foundations-2017/classes/data%20structures/looping-patterns/)*

# In[170]:


#Now I swtiched from C to F
#Example: I need to only loop through the second list (time)
print(data_miami['forecast']['forecastday'][0]['hour'][1]['temp_f'])


# In[212]:


#How many hours it is above 85 degree?
miami = 0
for weather_miami in data_miami['forecast']['forecastday'][0]['hour']:
    if weather_miami['temp_f'] > 85:
         miami =  miami+1
print(miami)

#How many hours in a day?
print(len(weather_miami))

warm = miami/len(weather_miami)*100

#What percent of the time is the temperature above 85 degrees?
print(f"It is {warm:.1f} percentage of the time, the temperature is above 85 degrees")




# In[ ]:





# ## 9) How much will it cost if you need to use 1,500,000 API calls?
# 
# You are only allowed 1,000,000 API calls each month. If you were really bad at this homework or made some awful loops, WeatherAPI might shut down your free access. 
# 
# * *Tip: this involves looking somewhere that isn't the normal documentation.*

# Anything above 1,000,000 calls per month isn't free, so it will be $4/month for the lowest subscription option of 2,000,000 callls per month...

# In[ ]:





# ## 10) You're too poor to spend more money! What else could you do instead of give them money?
# 
# * *Tip: I'm not endorsing being sneaky, but newsrooms and students are both generally poverty-stricken.*

# You just make a new account with a new email address :)

# In[ ]:




