# Automation-Skill-Set
This python repo shows Ming's automated testing skills, it includes:
1. Assignment-1: handle the json file, output the `test report` 
2. Assignment-2(`Web auto test`): understand HTML and CSS, locate cssSelector and xpath locators, design and build the automation framework using selenium webdriver + pytest, run parallel testing
3. Assignment-3: analyse and compose the `test plan`
4. `Mobile auto test`: design and build the mobile automation framework (appium  + android emulator + selenium webdriver + pytest)
5. Organize and manage the `cross-browser` project (both web app and mobile app)

# Assignment-1: Deal with the json file including the test result to output test report in console  
1. Print test suite name
2. Print out the total number of tests that passed and their test name, time and status
3. Print out the total number of tests that failed and their test name, time and status
4. Print out the total number of tests that are blocked
5. Print out the total number of tests that took more than 10 seconds to execute
6. Provide screenshots of the console output if possible

# Assignment-2: the framework of the web app : selenium webdriver + pytest
1. Browse to http://slashdot.org/
2. Print how many articles (highlighted in green) are on the page
3. Print a list of unique icons (highlighted in red) used on article titles and how many times was
it used
4. Vote for some random option on the daily poll
5. Return the number of people that have voted for that same option

# Assignment-3: the test plan designed for the Roomba 900 Serial
Provide a test plan (testcases grouped by categories) for testing a Roomba 900 robot (google it).
Only show the creativity and insightfulness of my own testing skills

# Mobile auto test: the framework of the web app : selenium webdriver + appium + android emulator + pytest
1. adopt the POM (Page Object Model) design pattern to manage behaviors in each page.
2. understand CSS and HTML, locate the selectors using cssSelector or xpath etc.
3. manage the `cross-browser` tests

# Get Started
We will be using macOS as example, based on the different use cases, choose what to follow:

## Pre-requisites:
  * [PyCharm 2019.3 CE](https://www.jetbrains.com/pycharm/download/#section=mac) installed.
  * [ChromeDriver 80.0.3987.106](https://chromedriver.storage.googleapis.com/index.html?path=80.0.3987.106/) installed
  * please fork this [automation-skill-set](https://github.com/Ming-Free-Lab/automation-skill-set) and download
  * make sure you are in the automation-skill-set project root folder
  * if you get any running issue, please reference to the ``requirements.txt`` to check if those required packages were installed correctly, you can also contact our QA Engineer/Tester via liangyang720@gmail.com.

## Uses Cases

### Use Case #1: I only want to run each test one by one
  * Assignment 1: Check the output report
  run ``<root_folder>automation-skill-set/PYTHONPATH=. pytest -v -s webapp-auto-test/assignment-1/test_output_report_in_console.py``
  * Assignment 2 - 1: Print how many articles (highlighted in green) are on the page
  run ``<root_folder>automation-skill-set/BROWSER_NAME='DESKTOP CHROME' PYTHONPATH=. pytest -v -s webapp-auto-test/assignment-2 -k test_article_number_on_page``
  * Assignment 2 - 2: Print a list of unique icons used on article titles and how many times was
it used
  run ``<root_folder>automation-skill-set/BROWSER_NAME='DESKTOP CHROME' PYTHONPATH=. pytest -v -s webapp-auto-test/assignment-2 -k test_icons_used_status``
  * Assignment 2 - 3: Vote for some random option on the daily poll and return the number of people that have voted for that same option
  run ``<root_folder>automation-skill-set/BROWSER_NAME='DESKTOP CHROME' PYTHONPATH=. pytest -v -s webapp-auto-test/assignment-2 -k test_vote_option``
  
### Use Case #2: I want to run the `parallel testing` for assignment 2 in local
  run ``<root_folder>automation-skill-set/BROWSER_NAME='DESKTOP CHROME' PYTHONPATH=. pytest webapp-auto-test/assignment-2/test_on_dotslash_web.py``

### Use Case #3: I want to run the `parallel testing` for assignment 2 in the selenium-grid
  download the selenium grid jar file [selenium-server-standalone-3.141.59.jar](https://www.selenium.dev/downloads/)
  set the directory of the selenium grid jar file into the PATH variable
  open the terminal on the mac 
  run ``<root_folder>automation-skill-set/java -jar selenium-server-standalone-3.141.59.jar -role hub`` to start selenium grid hub
  run ``<root_folder>automation-skill-set/java -jar selenium-server-standalone-3.141.59.jar -role node -hub http://localhost:4444/grid/register -port 5566`` to register the selenium node
  run ``<root_folder>automation-skill-set/TARGET_ENV='SELENIUM GRID' BROWSER_NAME='DESKTOP CHROME' PYTHONPATH=. pytest webapp-auto-test/assignment-2/test_on_dotslash_web.py``

### Use Case #4: I want to run the `parallel testing` for assignment 2 in the selenium-grid with the jenkins
  open the terminal on the mac 
  run ``<root_folder>automation-skill-set/java -jar selenium-server-standalone-3.141.59.jar -role hub`` to start selenium grid hub
  run ``<root_folder>automation-skill-set/java -jar selenium-server-standalone-3.141.59.jar -role node -hub http://localhost:4444/grid/register -port 5566`` to register the selenium node
  enter ``http://localhost:8080/job/automation-skill-set/ `` to access the Jenkins
  select ``automation-skill-set`` pipeline to build 

### Use Case #5: I want to run the `android mobile` auto testing in local
  run ``<root_folder>automation-skill-set/BROWSER_NAME='MOBILE' PYTHONPATH=. pytest mobileapp-auto-test/test_gmail_android.py``

# Test Result Screenshot for Assignment1 and 2:
  Please refer to the [Assignment Requirements and Result](https://docs.google.com/spreadsheets/d/15EN2fixOko38UAQnboBkzmGMVlRh4ou0SETpyANyyuE/edit?usp=sharing)

# Test Videos of Ming skill set:
  Please refer to the following Ming skill videos:
  1. [Test Report](https://www.screencast.com/t/FtUdb5Zvgx)
  2. [Web App Test](https://www.screencast.com/t/tXtOl8yt5)
  3. [Parallel Testing of the Web App Test](https://www.screencast.com/t/gXcLKlZ3Si)
  4. [Test Plan](https://www.screencast.com/t/lmD4NDYANZg)
  5. [Mobile App Test](https://www.screencast.com/t/8ytoL1NV)
  
  Note:  Enable the flash option in the browser to watch this video. 
  
# Test Plan for Assignment3
  Please refer to the [Test Plan of iRobot Roomba 900 Series](https://docs.google.com/document/d/1FENakT7TpKSQE0_0iioB8V_ChJNE3xTbYDczpYO00nU/edit?usp=sharing)