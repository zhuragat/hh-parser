import numpy
import re
from parser import read_csv
import matplotlib.pyplot as plt

def convertSalaries(salary_list):
    res_salaries = []
    for salary in salary_list:
        if not isinstance(salary, str):
            continue
        if "KZT" not in salary:
            continue
        res = re.sub(r'^.*?-', '', salary)
        res = re.sub('[^0-9]', '', res)
        res_salaries.append(res)
    return list(map(int, res_salaries))

def average(lst):
    return sum(lst) / len(lst)

def visualize_average_salary():
    no_experience = numpy.transpose(read_csv('no_experience_vacancies.csv')).tolist()
    between1and3 = numpy.transpose(read_csv('experience_1_and_3_vacancies.csv')).tolist()
    between3and6 = numpy.transpose(read_csv('experience_3_and_6_vacancies.csv')).tolist()
    more_than6 = numpy.transpose(read_csv('experience_more_than_6_vacancies.csv')).tolist()
    list1 = convertSalaries(no_experience[1]) if len(no_experience) > 2 else []
    list2 = convertSalaries(between1and3[1]) if len(between1and3) > 2 else []
    list3 = convertSalaries(between3and6[1]) if len(between3and6) > 2 else []
    list4 = convertSalaries(more_than6[1]) if len(more_than6) > 2 else []
    average_salary_1 = round(average(list1)) if len(list1) > 2 else 0
    average_salary_2 = round(average(list2)) if len(list2) > 2 else 0
    average_salary_3 = round(average(list3)) if len(list3) > 2 else 0
    average_salary_4 = round(average(list4)) if len(list4) > 2 else 0
    
    directions = ['0', '1-3', '3-6', '6+']
    salaries = [average_salary_1, average_salary_2, average_salary_3, average_salary_4]
    plt.bar(directions, salaries)
    plt.xticks(directions)
    plt.yticks(salaries)
    plt.title('Average salary depending on years of experience in tenge') 
    plt.savefig('experience.png')

def visualize_trending_jobs():
    all_vacancies = numpy.transpose(read_csv('all_vacancies.csv')).tolist()
    titles = all_vacancies[0] if len(all_vacancies) > 2 else []
    
    java = sum('java' in s.lower() for s in titles)
    php = sum('php' in s.lower() for s in titles)
    python = sum('python' in s.lower() for s in titles)
    sql = sum('sql' in s.lower() for s in titles)
    c1 = sum('1c' in s.lower() for s in titles)
    js = sum('js' in s.lower() for s in titles)
    ios = sum('ios' in s.lower() for s in titles)
    android = sum('android' in s.lower() for s in titles)
    devops = sum('devops' in s.lower() for s in titles)

    languages = ['java', 'php', 'python', 'sql', 'android', 'js', 'ios', '1c', 'devops']
    number = [java, php, python, sql, android, js, ios, c1, devops]
    plt.bar(languages, number)
    plt.xticks(languages)
    plt.yticks(number)
    plt.title('The most popular programming languages over the last month') 
    plt.savefig('trends.png')
    
def visualize_job_appearances(): 
    all_vacancies = numpy.transpose(read_csv('all_vacancies.csv')).tolist()
    dates = all_vacancies[4] if len(all_vacancies) > 2 else []
    dates = [re.sub('[^\d.]', '', x) for x in dates if 'ноября' in x]
    dates = sorted(dates, key= lambda x: int(x))
    frequency = {}
    for date in dates:
        frequency[date] = dates.count(date)

    date = [*frequency]
    number = list(frequency.values())

    plt.bar(date, number)
    plt.xticks(date,fontsize=10, rotation=90)
    plt.yticks()
    plt.title('Job appearences over the last month (November)') 
    plt.savefig('appearence.png')