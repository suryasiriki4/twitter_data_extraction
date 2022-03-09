# import os
# import tweepy as tw
# import pandas as pd
t
# consumer_key = 'hhMhCyOIgKMPQlSqhIeUxx1U0'
# consumer_secret = 'AbOJIrjAvVBX4z1AB7o30Yj20At5iweT5Y6f7oRq5bBhF1dZVX'
# access_token = '1494236675958251525-znFIYtRt49Qk9hk9feCX7j4WT0DFPV'
# access_token_secret = 'XfMPgqM2gpLYWwL3VRghMdjOOmfsgBNAVgs7b901ND7NV'

# auth = tw.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tw.API(auth, wait_on_rate_limit=True)
from Scweet.Scweet.scweet import scrape
import pandas as pd
# ['$AAPL', '$BA', '$CAT', '$CSCO', '$CVX', '$DD', '$DIS', '$GS', '$HD', '$IBM', '$INTC', '$JPM', '$KO', 
#          '$MCD', '$MMM', '$MRK', '$MSFT', '$NKE', 'PFE', '$PG', '$RTX', '$TRV', '$UNH', '$V', '$VZ', '$WBA', '$WMT', '$XOM']
stocks = ['$MCD']
years = [2017, 2018, 2019, 2020]
for i in range(len(stocks)):
    for year in years:
        since_date = "{}-01-01".format(year)
        until_date = "{}-12-31".format(year)
        data_2017_to_2021 = scrape(words=[stocks[i]], since=since_date, until=until_date, from_account=None, interval=1,
                                headless=True, display_type="Top", show_images=False, save_images=False, lang="en",
                                resume=False, filter_replies=False, proximity=False, minlikes=None, minretweets=None)
        df = pd.DataFrame(data_2017_to_2021)
        df.to_csv(stocks[i] + '_{}_nlpData.csv'.format(year))