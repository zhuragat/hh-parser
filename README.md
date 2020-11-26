# Parsing vacancies
It's a python program that helps you to parse data from hh.kz

## Prerequisites

Your computer must have:
* Python (latest version)

## Installation

These instructions allow you to run a copy of the project on your local machine for development and testing purposes.

1. Download the entire repository.
2. Place the hh-parser directory in your Python environment.
3. Go to the hh-parser directory and do the following:
```console
pip install -r requirements.txt
```

If this is the first time, select the suggested configuration.
At any time in the future, you can easily run the configuration to apply the changes.

## To run the file

For Windows - `python endpoint.py`

For Ubuntu / Linux - `python3 endpoint.py`

It will run on http://localhost:5000

## How it works?

Firstly you need to make an HTTP GET request to parse vacancies. It creates several CSV files ('all_vacancies.csv', 'no_experience_vacancies.csv', 'experience_1_and_3_vacancies.csv', 'experience_3_and_6_vacancies.csv', 'experience_more_than_6_vacancies.csv')
<br/>
<br/>
```console
curl localhost:5000/parse | json_pp
```
<br/>

<br/>

Then you can use these data
* to get all vacancies with title, salary, company, location, date
* to calculate average salary depending on years of experience
* to determine the most popular vacancies on the website
* to figure out the number of vacancies appearing on the website

For each of them except the first, there are exists endpoints that create PNG files with graphs:
```console
curl localhost:5000/vacancies | json_pp
```
```json
{
    "data": [
        [
            "Системный администратор",
            "250 000-300 000 KZT",
            "ТОО Qazaq National Product",
            "Нур-Султан",
            "26 ноября"
        ],
        [
            "ИТ-менеджер",
            "400 000-550 000 KZT",
            "",
            "Нур-Султан",
            "20 ноября"
        ],
        .........
            [
            "Монтажник слаботочных систем",
            "от 100 000 KZT",
            "ТОО Легион-М",
            "Алматы",
            "12 ноября"
        ],
        [
            "Инженер-электронщик (Алматы)",
            "от 150 000 KZT",
            "ТОО Компания Холодом",
            "Алматы",
            "16 ноября"
        ]
    ]
}
```

<br/>

```console
curl localhost:5000/experience | json_pp
```

![alt text](files/experience.png)

<br/>

```console
curl localhost:5000/trend | json_pp
```

![alt text](files/trends.png)

<br/>

```console
curl localhost:5000/appearance | json_pp
```

![alt text](files/appearance.png)
