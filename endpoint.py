from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from parser import create
from parser import read_csv
from visualization import visualize_average_salary
from visualization import visualize_trending_jobs
from visualization import visualize_job_appearances
import pandas as pd
import csv
import json
app = Flask(__name__)
api = Api(app)


class Vacancy(Resource):

    @app.route('/parse', methods=['GET'])
    def create_csv():
	# depending on an area value, it generates vacancies from there 
        area = request.args.get('area')
        if area is None:
            area = 'kz'
        if area.lower() == 'kz':
            area = '40'
        if area.lower() == 'alm':
            area = '160'
        if area.lower() == 'ast':
            area = '159'
        if area.lower() == 'kgd':
            area = '177'

        basic_url = 'https://hh.kz/search/vacancy?st=searchVacancy&text=&specialization=1&salary=&currency_code=KZT&order_by=relevance&search_period=0&items_on_page=100&no_magic=true&L_save_area=true&area=' + area
        create(basic_url, 'all_vacancies.csv')
        print('Created csv file all_vacancies.csv')
        create(basic_url + '&experience=noExperience',
               'no_experience_vacancies.csv')
        print('Created csv file no_experience_vacancies.csv')
        create(basic_url + '&experience=between1And3',
               'experience_1_and_3_vacancies.csv')
        print('Created csv file experience_1_and_3_vacancies.csv')
        create(basic_url + '&experience=between3And6',
               'experience_3_and_6_vacancies.csv')
        print('Created csv file experience_3_and_6_vacancies.csv')
        create(basic_url + '&experience=moreThan6',
               'experience_more_than_6_vacancies.csv')
        print('Created csv file experience_more_than_6_vacancies.csv')
        return {'status': 'success'}, 200

    @app.route('/vacancies', methods=['GET'])
    def get_all_vacancies():
        data = read_csv('files/all_vacancies.csv')
        return json.dumps({"data": data}, ensure_ascii=False), 200, {'Content-Type': 'application/json'}

    @app.route('/experience', methods=['GET'])
    def get_average_salary():
        visualize_average_salary()
        return {'status': 'success'}, 200

    @app.route('/trend', methods=['GET'])
    def get_trending_jobs():
        visualize_trending_jobs()
        return {'status': 'success'}, 200

    @app.route('/appearance', methods=['GET'])
    def get_job_appearance():
        visualize_job_appearances()
        return {'status': 'success'}, 200


if __name__ == '__main__':
    app.run()
