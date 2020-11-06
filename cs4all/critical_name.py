from flask import Flask, request
import time


def naughty_or_nice(x):
    naughty = "https://media.giphy.com/media/Pc7cdzjs5KooM/giphy.gif"
    nice = "https://media.giphy.com/media/NBcNQdJqr9Qdy/giphy.gif"
    very_naughty = "https://media.giphy.com/media/ZPpox9nLNojx6/giphy.gif"

    name_len = len(x)
    if name_len % 2 == 0 :
        return ("NICE : )", nice)
    elif name_len >= 10 && name_len % 2 == 0:
        return (" Very Naughty T.T ", very_naughty)
    else:
        return ("Naughty >.< ", naughty)

app = Flask(__name__)
app.config["DEBUG"] = True
@app.route('/', methods=["GET", "POST"])
def adder_page():
    errors = ""
    if request.method == "POST":
        first_name = None
        try:
            first_name = str(request.form["first_name"])
        except:
            errors += "<p>{!r} is not a name.</p>\n".format(request.form["first_name"])
        if first_name is not None:
            result = naughty_or_nice(first_name)
            time.sleep(5)
            return '''
                <html>
                    <body>
                        <p><font size="+5">{first_name} is {result[0]}</font></p>
                        <p><a href="/">Click here to calculate again</a></p>
                        <img src={result[1]} alt="this slowpoke moves"  width=500/>
                    </body>
                </html>
            '''.format(result=result, first_name=first_name)

    return '''
        <html>
            <body>
                {errors}
                <p><font size="+5">Enter your First Name:</font></p>
                <form method="post" action=".">
                    <p><input name="first_name" /></p>
                    <p><input type="submit" value="Naughty or Nice" /></p>
                </form>
            </body>
        </html>
    '''.format(errors=errors)