# High-Level Natural Language Processing framework

### Стек технологий:

Изначально я собирался использовать Django, для работы с базами данных и создания веб-приложения, но кажется монолитность Django несёт с собой оверхед, поэтому было решено отдельно использовать ORM PeeWee, для работы с БД. Технологию для веб-интерфейса я ещё не выбрал, но думаю это будет React приложение.

###  Генерация моделей для Peewee с Pwiz

Для того, чтобы пользователю не нужно было описывать таблицы вручную мы используем Pwiz, который самостоятельно генерирует Peewee модели

### Отображения полей в Feature space

Возможность написать конфигурационный файл, описывающий как нужно обрабатывать типы данных и контретные поля. Например какой именно embeding использовать

### Применения обученых моделей к базе данных

И сохранение результата в поле или в новую таблицу.