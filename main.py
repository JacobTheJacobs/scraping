
# call requests to get the data
response = requests.get(cap_url)
json_data = response.json()


candles = []


# iterate over json and isert the data into candles
for article in json_data["data"]:
    title = ''
    subtitle = ''
    sourceUrl = ''
    releasedAt = ''
    for key, value in article['meta'].items():

        if key == "title":
            title = value
        if key == "subtitle":
            subtitle = value
        if key == "sourceUrl":
            sourceUrl = value
        if key == "releasedAt":
            releasedAt = value

    candles.append({'title': title,
                    'subtitle': subtitle,
                    'sourceUrl': sourceUrl,
                    'releasedAt': releasedAt})


df_marketcap = pd.DataFrame(candles, columns=[
    'title', 'subtitle', 'sourceUrl', 'releasedAt'])
df_marketcap.to_html('temp.html')
