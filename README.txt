DESCRIPTION
    - The software consists of the scraped restaurant data from Yelp 
        packaged as "Data.pickle." The code that scraped the data is found in 
        "Extract Business Data from Yelp.ipynb"
    - The pre-trained model is stored as "model.pkl." The "Train Model.ipynb"
        file contains the code to further train the model if needed.
    - The application (in /src/main/app) runs from "app.py" which is built using Flask.

INSTALLATION
    1. Open anaconda prompt and navigate to desired directory
    2. Copy HTTPS url from github repository
    3. Enter following in terminal to clone files from Github:

        "git clone {HTTPS url}"

    4. Enter following in terminal to create a conda environment from "environment_droplet.yml" file:

        "conda env create -f environment_droplet.yml"

    4. Run the flask server within terminal: 

        "python src/main/app/app.py"

    5. Enter the localhost address flask is running on into a web browser to use the app
        (i.e. "* Running on http://111.111.1.111:80/")

EXECUTION
    1a. Input restaurant parameters
    1b. Click submit to reveal success rate of restaurant
    2. Explore the map to find information of restaurants in NY vicinity
