pipenv run behave -f allure_behave.formatter:AllureFormatter -o allure_result_folder ./features

allure serve allure_result_folder

allure generate allure_result_folder/ -o allure_reports
