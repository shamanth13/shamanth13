import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "8BDhaiu1duetQ2J74D6MTbsB0",
    "consumer_secret"     : "Ihl4BRDKOyAFtSBXYjd5BQmE5JZ3CMJ7K3ZpVxFjmi8TUnZRcD",
    "access_token"        : "968052525311160320-WHxBTjlgnC44YaqeXTPuUHTs31cODqU",
    "access_token_secret" : "eBbm2WrBlofTsd3n6QPui93vblJuj6yc0CT0fbGEwADoD" 
    }

  api = get_api(cfg)
  tweet = "Hello, world!......"
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()
