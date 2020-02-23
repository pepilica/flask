import flask
from flask import request, render_template

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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')