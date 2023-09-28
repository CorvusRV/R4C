# Тестовое задание

Для работы приложения вам необходимо создать .env файл и внести в него следующие параметры:  
**DEBUG**=True/False  
**SECRET_KEY**='Секретный ключ'  
**EMAIL_HOST_USER**='Адрес вашей электронной почты'  
**EMAIL_HOST_PASSWORD**='Пароль' - создается в аккаунте пользователя для использования SMTP  
Приложение настроено для работы с учетной записью Gmail  
Настройка SMTP для Gmail - https://support.google.com/mail/answer/7126229  


## REST API

### Создание робота
`POST /create/`
    curl -i -H 'Accept: application/json' -d '&model=R2,&version=D2,&created=2023-09-28 22:00:00'

### Создание заказа
`POST /order/`
    curl -i -H 'Accept: application/json' -d '&email=corvusrv@gmail.com,&robot_serial=R2-D2'

### Получение отчета о кол-ве созданных роботов за неделю
`GET /report/`
    curl -i -H 'Accept: application/json'
