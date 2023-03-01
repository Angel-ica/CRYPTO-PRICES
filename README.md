# CRYPTO-PRICES

The main task of this project is automation. 
Data which is extracted through scraping the websites is put in CSV format for analysis and the entire process is containerised using Docker.
GitHub Actions is used to create a CI/ CD pipeline to automate and streamline the running of the application. 

--------------------------------------------
CI/CD

---Continuous Integration(CI) involves automatically building and testing code changes each time they are committed to a repository. This helps catch errors and bugs earlier in the development process, before they can cause bigger problems downstream.

---Continuous Deployment(CD) involves automatically deploying tested code changes to a production environment. This allows for quick and reliable push changes to applications, reducing the risk of human error and improving the speed and efficiency of the development process.

--------------------------------------------
This project uses selenium to extract useful data from two competing cryptocurrency websites - Coinmarketcap and Crypto compare and then compares; prices in GBP, market value and percentage change in price within a specified time period. DevOps tools like Docker for building and containerising the application and GitHub Actions is used to create a custom workflow to build, test and deploy the application.

---------------------------------------------
The main functionality of the application is defined in the 'main_script.py'.

'from cryptocompare_scraper import run_scraper'
--- 'run_scraper' as defined in cryptocompare_scraper.py is the function used to automatically run the scraper, extract and store all required data.

'from coinmarketcap_scraper import run'
--- 'run_scraper' as defined in coinmarketcap_scraper.py is the function used to automatically run the scraper, extract and store all required data.


''' 

def script():
    run_scraper()    #runs cryptocompare_scraper
   
   run()     #runs coinmarketcap_scraper

if __name__ == '__main__':

   script()      #runs script 
   
  '''
    
--------------------------------------------

Docker

'FROM python:latest'

--- Pulls python image.

--- An image is a lightweight, standalone, executable package that includes everything needed to run a piece of software, including code, dependencies, libraries, and system tools.

--- In this case, it indicates that the Docker container should be based on the latest version of the official Python image available from the Docker Hub registry.

'CMD ["python","main_script.py"]'

--- CMD specifies the default behavior of a container when it is started based on the image. The command is to execute a Python script called main_script.py.

-------------------------------------------

GitHub Actions 

This is a yaml configuration file for a GitHub Actions workflow. The workflow is called "ci" and is triggered when code is pushed to the main branch or a pull request is opened against the main branch.

The workflow defines a single job called "build" which runs on an Ubuntu environment. The job consists of four steps:

I. Checkout: this step checks out the code from the repository using the "actions/checkout" action.

II. Login to Docker Hub: this step logs in to Docker Hub using the "docker/login-action" action. The Docker Hub credentials are stored as secrets in the repository settings.

III. Set up Docker Buildx: this step sets up Docker Buildx, a tool for building and pushing Docker images, using the "docker/setup-buildx-action" action.

IV. Build and push: this step builds the Docker image using the "docker/build-push-action" action and pushes it to Docker Hub. The image is built from the Dockerfile in the current directory and is tagged with the latest version. The Docker Hub username is used as the image repository name.

-----------------------------------------------
Feel free to clone this repo or pull the image from dockerhub!
NOTE that in the scraper files, the paths to the elements are constantly changing on the website so the ones used used probably won't work anymore. 

E.g: 
-- change_currency=self.driver.find_element(by=By.XPATH, value='//div[@class="sc-8580441d-1 klKJWV"]//button').click()-- 

The XPATH above won't work anymore. 


