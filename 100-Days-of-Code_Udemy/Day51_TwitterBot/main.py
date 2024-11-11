from twitter_bot import InternetSpeedTwitterBot

bot = InternetSpeedTwitterBot()
bot.up = 100  # Change accordingly
bot.down = 150  # Change accordingly
tested_down, tested_up = bot.get_internet_speed()
if bot.up > float(tested_up) or bot.down > float(tested_down):
    print("Speeds not OK. Sending message to provider...")
    message = (f"Hey Internet Provider, why is my internet speed {tested_down}down/{tested_up}up "
               f"when I pay for {bot.down}down/{bot.up}up?")
    bot.tweet_at_provider(message)
    bot.driver.quit()
else:
    print("Speeds OK!")
    bot.driver.quit()

