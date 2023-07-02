# Test assignment for Middle QA Automation Engineer

## Task:
```
Develop several (at least 3) UI autotests for
https://hb-eta.stage.sirenltd.dev/siding

Use scenario:
-- zip code 09090
-- answer the questions on the form
-- enter the first and last name
-- enter an email
-- enter the phone number
-- (if necessary) confirm the phone number
-- get a "thank you" page.

Feel free to choose the checks yourself.
Use "py test" + "selenium"
```

## Used tools

+ [Python 3.7](https://www.python.org/downloads/)
+ [Selenium](https://selenium-python.readthedocs.io/) - API for SeleniumWebDriver
+ [pytest](https://docs.pytest.org) - test runner
+ [webdriver_manager](https://github.com/SergeyPirogov/webdriver_manager) - for webdrivers (no more driver installations
  needed)
+ [Allure](https://github.com/allure-framework/allure2) - for test run reports

**Project setup**

- Install <b><a href="https://www.python.org/downloads/">Python</a></b> (v3.7+) and <b><a href="https://pip.pypa.io/en/stable/installation/">PIP</a></b> and add to your System PATH
- Install requirements
```
pip install -r requirements.txt
```

**Start auto tests (from IDE)**

```
pytest
```

**Start auto tests with allure report (from IDE)**
```
pytest --alluredir=./allure-results
allure serve
```