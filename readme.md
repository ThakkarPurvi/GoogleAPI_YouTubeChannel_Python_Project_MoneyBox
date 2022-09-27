## **YouTube API Project**

[Project_Description](https://github.com/ThakkarPurvi/GoogleAPI_YouTubeChannel_Python_Project_MoneyBox/blob/master/readme.md#project_description)

[Installation](https://github.com/ThakkarPurvi/GoogleAPI_YouTubeChannel_Python_Project_MoneyBox/blob/master/readme.md#Installation)

[Tech Stack](https://github.com/ThakkarPurvi/GoogleAPI_YouTubeChannel_Python_Project_MoneyBox/blob/master/readme.md#Tech-Stack)

[Run](https://github.com/ThakkarPurvi/GoogleAPI_YouTubeChannel_Python_Project_MoneyBox/blob/master/readme.md#Run)

[Thank you](https://github.com/ThakkarPurvi/GoogleAPI_YouTubeChannel_Python_Project_MoneyBox/blob/master/readme.md#Thank-you)

[Profile](https://github.com/ThakkarPurvi/GoogleAPI_YouTubeChannel_Python_Project_MoneyBox/blob/master/readme.md#Profile)


## **Project_Description**

This is a simple Youtube API search project craeted by CFG students as a project. This programs uses your youtube channel name and displays their viewcount, vide count and subscribers on that channel. 

**Minimum Viable Product**
 - The MVP of this project is to extract channel live data from the requested channel. 
 - This programs uses your youtube channel name and displays their viewcount, vide count and subscribers on that channel. 

**Extended Product** 
- Once you retrieve the data from that channel this program will automatically save the output in a new file.

**Project Parts explained**

- A. [Create new project on Google Console](https://console.cloud.google.com/)

        Create new Project 
        Enable API 
        Create Credentials 
        Copy and securely save API Key

- B. [Install VM](https://github.com/googleapis/google-api-python-client)

        Install VM 
        Docs folder - Building and calling a service
        to use build() function
        youtube is the service name v3 and developerskey

    get channel information
    channels (instance method) - you will get the list

- C. [API Keys]()

        When calling APIs that do not access private user data, you can use simple API keys. These keys are used to authenticate your application for accounting purposes. The Google Developers Console documentation also describes API keys.
        Note: If you do need to access private user data, you can create one throught yoru google console. 

        Using API Keys:
        To use API keys, pass them to the build() function when creating service objects. For example:

    youtube = build("youtube", "v3", developerKey=api_key)
    All calls made using the youtube object will include your API key. 

- D. [Create Virtual Environment]()

        - Install this library in a virtualenv using pip. 
        - virtualenv is a tool to create isolated Python environments. 
        - The basic problem it addresses is one of dependencies and versions, and indirectly permissions.
    
    With virtualenv, it's possible to install this library without needing system install permissions, and without clashing with the installed system dependencies.

- E. [Create request](https://developers.google.com/youtube/v3/docs/channels/list)
        
        create request 
        request =youtube.channels().list(
            part=""
            forUSername=""

## **Installation**

Install this library in a virtualenv using pip. virtualenv is a tool to create isolated Python environments. The basic problem it addresses is one of dependencies and versions, and indirectly permissions.

With virtualenv, it's possible to install this library without needing system install permissions, and without clashing with the installed system dependencies.

**Mac/Linux**

    pip3 install virtualenv
    virtualenv <your-env>
    source <your-env>/bin/activate
    <your-env>/bin/pip install google-api-python-client

**Windows**

    pip install virtualenv
    virtualenv <your-env>
    <your-env>\Scripts\activate
    <your-env>\Scripts\pip.exe install google-api-python-client

**Python Console**

    pip install virtualenv
    virtualenv <your-env>
    <your-env>\Scripts\activate
    <your-env>\Scripts\pip.exe install google-api-python-client

## **Tech Stack**

**API Link**

- [Google Developers Console](https://console.developers.google.com/)
- [Google API Python Client](https://github.com/googleapis/google-...)
- [YouTube API](https://developers.google.com/youtube/v3)

**Back-end**

- Python - version 3.10
    - [PyCharm](https://www.jetbrains.com/pycharm/) — to run the application 

**Logo**

[YOUTUBEAPI](art.py) - Saved in the art file

**Color Reference**

| Color             | Hex                   |
| ----------------- | --------------------- |
| Logo Color        | ![#f03c15](https://via.placeholder.com/15/f03c15/f03c15.png)|

## **Program**

Below are the 5 steps we followed to create and run this project successfully. 

**Step 1: get_youtube_data**

        - This function gets the information of the Youtube Channel requested
            Args:
                channel_name (str): string with the channel name
            Returns:
                statistics (dict): dictionary containing the metrics from the channel

**Step 2: format_results**

        - Returns a formatted string with the specified metrics
            Args:
                channel_name (str): string with the channel name
                results (dict): dictionary containing the metrics from the channel
                metric_name (str): string that specified the requested metric. Defaults to 'all'
            Returns:
                formatted_text (str): formatted string with the specified metrics

**Step 3: print_result**

        - It will automatically print the output in a .txt file within the main folder. 


**Step 4: save_result**

        - It will then save the same output in a .txt file within the main folder. 


**Step 5: run_the_program**
        
        - Using input function user is asked - which channel data is the user willing to view.
        - Once answered, user is promted - which metrics does the user is interested to retrieve.


## **Team Members**

This project is created by CFG Python Students in Sep 2022 by the following members:

- [Purvi Thakkar](https://www.linkedin.com/in/thakkarpurvilondon)
- [Brunella Adrianzen](https://github.com/brunella-adrianzen)

## 🔗 **Profile**

 - [![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://github.com/ThakkarPurvi)
 - [![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/thakkarpurvilondon/)
 - [![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/purvi41)

