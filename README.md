# Sprint_7
# Sprint_7
Тестирование API учебного сервиса Яндекс Самокат

1.	Тестирование создания курьера
1.1	для создания курьера переданы все обязательные поля;
       запрос возвращает правильный код ответа;
       успешный запрос возвращает {"ok":true};
1.2 ошибка при попытке создания двух одинаковых курьеров;
1.3 ошибка, если одного из полей нет;
1.4 ошибка при создании курьера с уже существующим логином.

2.	Тестирование авторизации курьера
2.1	курьер может авторизоваться;
для авторизации нужно передать все обязательные поля;
успешный запрос возвращает id.
2.2 ошибка при некорректном указании логина или пароля;
2.3 ошибка, если одного из полей нет;
2.4 ошибка, если авторизоваться под несуществующим пользователем, 
       
3.	Тестирование создания заказа
3.1 можно указать один из цветов — BLACK или GREY;
3.2 можно указать оба цвета;
3.3 можно совсем не указывать цвет;
3.4 тело ответа содержит track.

4.	Тестирование получения списка заказов
4.1 возвращается список заказов.
