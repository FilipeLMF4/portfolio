from bs4 import BeautifulSoup
from datetime import datetime
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "ID"
CLIENT_SECRET = "Secret"


def travel_to():
    input_date = input("Which year do you want to travel to? Type the date in YYYY-MM-DD. "
                       "Leave empty for today's date or type exit to end.\n")
    print("")
    if input_date == "":
        return ""
    elif input_date == "exit":
        return None
    else:
        try:
            date_object = datetime.strptime(input_date, "%Y-%m-%d")
            if date_object.year > datetime.today().year:
                print("Requested date is in the future. ", end="")
                raise ValueError
        except ValueError:
            print("Please enter a valid date in the requested format.")
            url = travel_to()
            return url
        else:
            return date_object.date()


def create_spotify(song_list, artist_list, songs_date):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                   client_secret=CLIENT_SECRET,
                                                   redirect_uri="http://example.com",
                                                   scope="playlist-modify-private",
                                                   show_dialog=True,
                                                   cache_path="token.txt",
                                                   username="User"
                                                   ))

    current_user = sp.me()['id']
    spotify_uris = []
    for j in range(len(song_list)):
        spotify_song = sp.search(q=f"track:{song_list[j]} artist:{artist_list[j]}", limit=1, type='track')
        try:
            spotify_uris.append(spotify_song['tracks']['items'][0]['uri'])
            print(f"{song_list[j]} by {artist_list[j]} added to list.")
        except IndexError:

            print(f"Could not find '{song_list[j]}' by {artist_list[j]} in Spotify. Skipped.")

    playlist_id = sp.user_playlist_create(user=current_user,
                                          name=f"{songs_date} Billboard 100",
                                          public="False",
                                          description=f"Billboard 100 songs for the week of {songs_date}"
                                          )

    sp.playlist_add_items(playlist_id=playlist_id["id"], items=spotify_uris)


# travel_date = travel_to()
billboard_url = "https://www.billboard.com/charts/hot-100/"
travel_date = travel_to()
if travel_date is not None:
    travel_url = billboard_url + str(travel_date)
    response = requests.get(travel_url)
    soup = BeautifulSoup(response.text, "html.parser")
    songs = soup.select(selector=".o-chart-results-list-row-container .lrv-u-width-100p .o-chart-results-list__item h3")
    artist = soup.select(selector=".o-chart-results-list-row-container .lrv-u-width-100p "
                                  ".o-chart-results-list__item .c-label.a-no-trucate")
    top100 = []
    top100_artists = []
    for i in range(len(songs)):
        top100.append(songs[i].getText().strip())
        top100_artists.append(artist[i].getText().strip())

    create_spotify(top100, top100_artists, str(travel_date))
