# Blog_app

#### It is blog app which contain some article.
#### Article have some attribute
+ Title
+ content
+ Author name
+ Feature Image
+ Date


#### It contains Four Functionalites:
+ Login and registration.
+ create an article (with rich text editor).
+ See all list of article order by the date.
+ See each article.


# Run Local
Make sure the python3 and Django 1.10 have installed.

Clone the repository, migrate the database and Run the server
```
$ git clone https://github.com/vermanil/Blog_app.git
$ cd Blog_app
$ python3 manage.py makemigrations blog
$ python3 manage.py migrate
$ python3 manage.py runserver

```
