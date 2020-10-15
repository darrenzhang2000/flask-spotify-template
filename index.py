from flask import Flask, redirect, request, render_template
import startup
import spotify

app = Flask(__name__)

  

@app.route('/', methods = ['GET', 'POST'])
def index():
    response = startup.getUser()

    if request.method == 'POST':
        # get top songs listened to 
        # call spotify API
        res = spotify.getTopArtists()
        print('top artsts', res)

        return 'posted'

    return redirect(response)

@app.route('/callback/')
def callback():
    startup.getUserToken(request.args['code'])
    return render_template('home.html')



if __name__ == '__main__':
    app.run()

