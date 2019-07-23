1) заходим на сайт
![Alt_text](https://github.com/x1Dman/CTF_STUFF/blob/master/ROSTELECOM_CTF/Bookkepr(WEB)/photos/Screenshot%202019-07-23%20at%2006.12.56.png)
2) пытаемся потыкаться во все, что можно
3) смотрим исходник и видимо, что встроен пост прям в HTML
![Alt_text](https://github.com/x1Dman/CTF_STUFF/blob/master/ROSTELECOM_CTF/Bookkepr(WEB)/photos/Screenshot%202019-07-23%20at%2006.23.02.png)
4) немного поигравшись - видимо, что он изменяем (например email можно заменить на login)
5) при логине появляется payment, однако другие оплаты закрыты, значит нам как раз туда и нужно!)
![Alt_text](https://github.com/x1Dman/CTF_STUFF/blob/master/ROSTELECOM_CTF/Bookkepr(WEB)/photos/Screenshot%202019-07-23%20at%2006.24.42.png)
6) понятно, что это может сделать только админ
7) запускаем BurpSuite Community Edition(в моем случае я подключил его как прокси к Firefox) и перед отправлением ПОСТ запроса добавляем параметр admin
![Alt_text](https://github.com/x1Dman/CTF_STUFF/blob/master/ROSTELECOM_CTF/Bookkepr(WEB)/photos/Screenshot%202019-07-23%20at%2006.16.29.png)
![Alt_text](https://github.com/x1Dman/CTF_STUFF/blob/master/ROSTELECOM_CTF/Bookkepr(WEB)/photos/Screenshot%202019-07-23%20at%2006.10.07.png)
8) переходим на payment 1 - кайфуем слоупоком и забираем флаг
![Alt_text](https://github.com/x1Dman/CTF_STUFF/blob/master/ROSTELECOM_CTF/Bookkepr(WEB)/photos/Screenshot%202019-07-23%20at%2006.09.55.png)
![Alt_text](https://github.com/x1Dman/CTF_STUFF/blob/master/ROSTELECOM_CTF/Bookkepr(WEB)/photos/Screenshot%202019-07-23%20at%2006.12.45.png)

![#f03c15](https://placehold.it/15/f03c15/000000?text=12341234) ASDAJSDASJOD
