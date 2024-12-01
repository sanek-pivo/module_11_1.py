# Цель: познакомиться с использованием сторонних библиотек в Python и применить их в различных задачах
# установлены через терминал командой pip install requests (pandas, numpy, matplotlib, pillow)
# отчет об установленных библиотеках командой в консоли:
# aiofiles==24.1.0
# aiogram==3.13.1
# aiohappyeyeballs==2.4.3
# aiohttp==3.10.10
# aiosignal==1.3.1
# annotated-types==0.7.0
# anyio==4.6.2.post1
# attrs==24.2.0
# boto3==1.35.50
# botocore==1.35.50
# category-encoders==2.6.4
# certifi==2024.8.30
# charset-normalizer==3.4.0
# click==8.1.7
# colorama==0.4.6
# configparser==7.1.0
# contourpy==1.3.0
# cycler==0.12.1
# datacleanerpandas==0.1.1
# fonttools==4.54.1
# frozenlist==1.5.0
# h11==0.14.0
# httpcore==1.0.6
# httpx==0.27.2
# idna==3.10
# jmespath==1.0.1
# joblib==1.4.2
# kiwisolver==1.4.7
# magic-filter==1.0.12
# matplotlib==3.9.2
# multidict==6.1.0
# nltk==3.9.1
# numpy==2.1.2
# packaging==24.1
# pandas==2.2.3
# Pandas3==0.0.1
# patsy==0.5.6
# pillow==11.0.0
# propcache==0.2.0
# pydantic==2.9.2
# pydantic_core==2.23.4
# pydatacleaner==0.1.2.9
# pyparsing==3.2.0
# pyTelegramBotAPI==4.23.0
# python-dateutil==2.9.0.post0
# python-telegram-bot==21.6
# pytz==2024.2
# regex==2024.9.11
# requests==2.32.3
# s3transfer==0.10.3
# scikit-learn==1.5.2
# scipy==1.14.1
# six==1.16.0
# sniffio==1.3.1
# statsmodels==0.14.4
# tabulate==0.9.0
# telegram==0.0.1
# telegramApi==1.5
# telegramPublishBot==0.1.6
# threadpoolctl==3.5.0
# tk==0.1.0
# tqdm==4.66.6
# typing_extensions==4.12.2
# tzdata==2024.2
# urllib3==2.2.3
# yarl==1.17.0


import requests
import pandas
import matplotlib.pyplot as plt
from pprint import pprint

# Matplotlib - это комплексная библиотека для создания статических, анимированных и интерактивных визуализаций
# pandas - отличный инструмент для обработки данных, в том числе чтения данных из файлов
# в целом изучение самой библиотеки pandas не уйдет много времени
# pillow обеспечивает широкую поддержку форматов файлов
# DataFrame: двумерная структура данных, которая хранит данные в виде двумерного массива или таблицы.Работает совместно с numpy, matplotlib а самое главное работает с
#  электронными таблицами CSV
df = pd.DataFrame(np.random.randint(0, 5, (10, 5)))
df.to_csv("foo.csv")
pprint(pd.read_csv("foo.csv"))

if __name__ == "__main__":
# создадим массив с элементами типа float
arr_f = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], float)

print(arr_f)
# тип данных можно посмотреть через атрибут dtype
print(arr_f.dtype)

# Matplotlib Для начал построим простую линейную зависимость,
# дадим нашему графику название, подпишем оси и отобразим сетку. Код программы:
# Независимая (x) и зависимая (y) переменные
x = np.linspace(0, 10, 50)
y = x
# Построение графика
plt.title("Линейная зависимость y = x") # заголовок
plt.xlabel("x") # ось абсцисс
plt.ylabel("y") # ось ординат
plt.grid()      # включение отображение сетки
plt.plot(x, y)  # построение графика