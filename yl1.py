import flask
from flask import request, url_for

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


@app.route('//promotion_image')
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


@app.route('/contest', methods=['POST', 'GET'])
def contest():
    if request.method == 'GET':
        return'''<!DOCTYPE html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                            integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1 align="center">Форма для регистрации</h1>
                            <p align="center">в суперсекретной миссии</p>
                            <div class='container' style='margin:center; background-color:#FFCC00; padding: 20px'>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <input type="text" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Образование</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Среднее неполное</option>
                                          <option>Среднее профессиональное</option>
                                          <option>Высшее образование</option>
                                          <option>Магистратура</option>
                                        </select>
                                     </div>
                                    <div class="form-group">
                                        <label for="about">Мотивация для участия в миссии:</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Основные профессии</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="engineer" value="engineer" checked>
                                          <label class="form-check-label" for="engineer">
                                            Инженер-исследователь
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="pilot" value="pilot">
                                          <label class="form-check-label" for="pilot">
                                            Пилот
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="builder" value="builder">
                                          <label class="form-check-label" for="builder">
                                            Строитель
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="exobiologist" value="exobiologist">
                                          <label class="form-check-label" for="exobiologist">
                                            Экзобиолог
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="doctor" value="doctor">
                                          <label class="form-check-label" for="doctor">
                                            Врач
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="terraforming-engineer" value="terraforming-engineer">
                                          <label class="form-check-label" for="terraforming-engineer">
                                            Инженер по терраформированию
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="climatologist" value="climatologist">
                                          <label class="form-check-label" for="climatologist">
                                            Климатолог
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="radio-def-specialist" value="radio-def-specialist">
                                          <label class="form-check-label" for="radio-def-specialist">
                                            Специалист по радиационной защите
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="astrologer" value="astrologer">
                                          <label class="form-check-label" for="astrologer">
                                            Астролог
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="cyberengineer" value="cyberengineer">
                                          <label class="form-check-label" for="cyberengineer">
                                            Киберинженер
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="drone-pilot" value="drone-pilot">
                                          <label class="form-check-label" for="drone-pilot">
                                            Пилот дронов
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['name'])
        print(request.form['surname'])
        print(request.form['email'])
        print(request.form['job'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['sex'])
        print(request.form['accept'])
        return "Форма отправлена"


@app.route('/choice/<planet>')
def choice(planet):
    return '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Выбор планеты</title>
  <link rel="stylesheet"
  href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
  integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
  crossorigin="anonymous">
</head>
<body>
  <h1>Мое предложение: {}</h1>
  <div class="alert alert-primary" role="alert">
      Она большая и цветастая.
    </div>
    <div class="alert alert-success" role="alert">
      На ней все необходимые ресурсы и больше!
    </div>
    <div class="alert alert-warning" role="alert">
      На ней есть магнитное поле!
    </div>
    <div class="alert alert-dark" role="alert">
        На ней есть своя уютная атмосфера.
    </div>
    <div class="alert alert-info" role="alert">
        Наконец, она просто красива!
    </div>
</body>
</html>'''.format(planet)


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return '''<!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>Выбор планеты</title>
      <link rel="stylesheet"
      href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
      integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
      crossorigin="anonymous">
    </head>
    <body>
      <h1>Результаты отбора</h1>
      <h5>претендента на участия в миссии {}</h5>
        <div class="alert alert-success" role="alert">
          Поздравляем! После {} этапа отбора ваш рейтинг 
        </div>
        <div class="alert alert-dark" role="alert">
            составляет {}
        </div>
        <div class="alert alert-info" role="alert">
            Желаем удачи!
        </div>
    </body>
    </html>'''.format(nickname, level, rating)


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    if request.method == 'GET':
        return '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <link rel="stylesheet"
  href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
  integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
  crossorigin="anonymous">
  <link rel="stylesheet" type="text/css" href="/static/css/style.css">
  <title>Document</title>
</head>
<body>
  <div class='container' align='center'>
    <h1 align="center">Загрузка фотографии</h1>
    <p align="center">в суперсекретной миссии</p>
  </div>
  <div class='container' style='margin:center; background-color:#FFCC00; padding: 20px'>
  <form method="post" enctype="multipart/form-data">
    <div class="form-group">
    <label for="photo">Выберите файл</label>
    <input type="file" class="form-control-file" id="photo" name="file">
    </div>
    <img src="{file}" alt="Не существует">
    <button type="submit" class="btn btn-primary">Отправить</button>
    </form>
    </div>
</body>
</html>'''
    elif request.method == 'POST':
        file = request.files['file']
        file.save('static/img/get.jpg')
        return '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <link rel="stylesheet"
  href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
  integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
  crossorigin="anonymous">
  <link rel="stylesheet" type="text/css" href="/static/css/style.css">
  <title>Фото</title>
</head>
<body>
  <div class='container' align='center'>
    <h1 align="center">Загрузка фотографии</h1>
    <p align="center">в суперсекретной миссии</p>
  </div>
  <div class='container' style='margin:center; background-color:#FFCC00; padding: 20px'>
  <form method="post" enctype="multipart/form-data">
    <div class="form-group">
    <label for="photo">Выберите файл</label>
    <input type="file" class="form-control-file" id="photo" name="file">
    </div>
    <img src="{file}" alt="Не существует">
    <button type="submit" class="btn btn-primary">Отправить</button>
    </form>
    </div>
</body>
</html>'''.format(file='static/img/get.jpg')


@app.route('/landscape')
def landscape():
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <link rel="stylesheet"
  href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
  integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
  crossorigin="anonymous">
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
  <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
  <title>Document</title>
</head>
<body>
  <div class='container' align='center'>
    <h1>Пейзажи Марса</h1>
  </div>
 <div class='container' style='padding: 50px;'>
  <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img class="d-block w-100" src="{url_for('static', filename='img/1.jpg')}" alt="First slide">
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="{url_for('static', filename='img/2.jpg')}" alt="Second slide">
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="{url_for('static', filename='img/3.jpg')}" alt="Third slide">
    </div>
  </div>
  <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>
</div>
</body>
</html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')