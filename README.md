
# WordCloud Generator
A Django based open source webapp to generate simple Wordcloud .

## Screenshots

![App Screenshot](https://i.ibb.co/7bZ6fbn/wordcloud-gen.png)


## Demo 
![MIT License](https://i.ibb.co/qm6KK3x/c79fce36504b.jpg)

## Live Url 
https://wordcloudimage.herokuapp.com/
## Acknowledgements

 - [DJANGO](https://www.djangoproject.com/)
 - [tailwindcss](https://tailwindcss.com/)
 - [python-wordcloud](http://amueller.github.io/word_cloud/)
 


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file
- SECRET_KEY= Secret key of your django project
- imgbb_api = imgbb API key 
- DEBUG = "False"
- ALLOWED_HOSTS = ""



## Installation

Install wordcloud library in windows 

```bash
  python -m pip install wordcloud-1.3.2-cp36-cp36m-win_amd64.whl
```
in the project folder
    
## Run Locally

Clone the project

```bash
  git clone https://github.com/ankushbisht01/wordcloud-generator
```

Go to the project directory

```bash
  cd wordcloud-generator
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python manage.py runserver
```


## Uses

This project can be  used as following :

- Visual representation of keywords .
- Can be used to generate Cover wordcloud images .


