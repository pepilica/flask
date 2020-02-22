import flask

app = flask.Flask(__name__)


@app.route('/')
def colon():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    return'''<p>Человечество вырастает из детства.</p>
            <p>Человечеству мала одна планета.</p>
            <p>Мы сделаем обитаемыми безжизненные пока планеты.</p>
            <p>И начнем с Марса!</p>
            <p>Присоединяйся!</p>'''


@app.route('/image_mars')
def pic():
    return'''<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8">
		<link rel="stylesheet" type='text/css' href="/static/css/style.css">
		<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
		integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
		<title>Привет, Марс!</title>
	</head>
	<body>
		<h1>Жди нас, Марс!</h1>
		<img src="/static/img/mars.jpg" alt="Картинки нет">
		<p>(эта красивая планета)</p>
		<div class="alert alert-primary" role="alert">
			Человечество вырастает из детства.
		</div>
		<div class="alert alert-success" role="alert">
            Человечеству мала одна планета.
		</div>
		<div class="alert alert-warning" role="alert">
 			Мы сделаем обитаемыми безжизненные пока планеты.
		</div>
		<div class="alert alert-dark" role="alert">
  			И начнем с Марса!
		</div>
		<div class="alert alert-info" role="alert">
  			Присоединяйся!
		</div>
	</body>
</html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')