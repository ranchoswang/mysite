from tweepy import OAuthHandler
from tweepy import API

access_token = "762889126840377344-QokfOoxEdg30hhdhDrpTXSPZ1Xn3wlO"
access_token_secret = "Et0fFXrxcj3trVvvXKGbxDsqc9Ex6Wib6isIjJkgb61os"
consumer_key = "Gv4501GM9zTfFOmGxGB5lxUTU"
consumer_secret = "goZ5uM8yjZ9fki7iooh3lQj2HdBbrmzNKePCCmJfLPSmgxctBZ"

if __name__ == "__main__":

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    search_api = API(auth_handler=auth)

    trump_id = "25073877"##ID here
    cnn_id = "759251"
    melania_id = "818876014390603776"
    query = "Donald Trump"
    count = 100

    result = search_api.show_friendship(source_id=trump_id, target_id=melania_id)
    print(result)
