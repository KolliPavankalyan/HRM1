behave features
behave -f allure_behave.formatter:AllureFormatter -o Reports/features
allure serve Reports/features
