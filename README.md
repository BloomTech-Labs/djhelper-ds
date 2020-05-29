# 1️⃣ DJ Helper

You can find the project at [https://www.dj-helper.com/](https://www.dj-helper.com/).

## 2️⃣ Contributors

|                                       [Evgenii Dudeiko](https://github.com/Edudeiko)                                        |                                       [Maxwell Kwarteng](https://github.com/maxim371)                                        |
| :-----------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------: |  
|                      [<img src="https://i.ibb.co/MsbFVHQ/linkedin-pic.jpg" width = "200" />](https://github.com/Edudeiko)                       |                      [<img src="https://i.ibb.co/2kYGL7W/max.jpg" width = "200" />](https://github.com/maxim371)                       |                      [<img src="https://www.dalesjewelers.com/wp-content/uploads/2018/10/placeholder-silhouette-male.png" width = "200" />](https://github.com/)                       |
|                 [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/Edudeiko)                 |            [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/maxim371)             |
| [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/ed-dudeiko-06384a195/) | [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/maxwell-kwarteng-b08459b7/) |


🚫 5️⃣ Optional examples of using images with links for your tech stack, make sure to change these to fit your project

![MIT](https://img.shields.io/packagist/l/doctrine/orm.svg)
![Typescript](https://img.shields.io/npm/types/typescript.svg?style=flat)
[![Netlify Status](https://api.netlify.com/api/v1/badges/b5c4db1c-b10d-42c3-b157-3746edd9e81d/deploy-status)](netlify link goes in these parenthesis)
[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)

🚫 more info on using badges [here](https://github.com/badges/shields)

## Project Overview


1️⃣ [Trello Board](https://trello.com/b/udZnuhhk/dj-helper)

1️⃣ [Product Canvas](https://www.notion.so/594af78f1b344d38976c00f9e71cf048?v=d50f07ef5cdc4e61aaadd9b6208e437a)

DJ-helper is a web and IOS application designed to help a DJ get suggestions based on the songs requested by the event audience, so that he can create a playlist that the audience is very likely to like. Before and during the event guests will submit music requests. With the help of machine learning the application will take those requests and create a unique playlist. The DJ can select songs and add them to their set. The application will also function in real time during the event and adjust to any changes in music trend that occur.

### Tech Stack

Python, Dash, Spotipy, Spotify API, Heroku, Plotly

### 2️⃣ Predictions

DJ helper uses an unsupervised k-neighbors model to predict similar songs. The model uses spotify's api to obtain a list of similar artists and then uses the audio features spotify provides to find the closest sounding track.

### 2️⃣ Explanatory Variables

- acousticness
- danceability
- energy
- instrumentalness
- liveness
- loudness
- speechiness
- tempo

### Data Sources
🚫  Add to or delete souce links as needed for your project


-   [Spotify_API](https://developer.spotify.com/documentation/web-api/)
-   [Spotipy](https://spotipy.readthedocs.io/en/2.12.0/#getting-started)
-   [Source 3] (🚫add link to python notebook here)
-   [Source 4] (🚫add link to python notebook here)
-   [Source 5] (🚫add link to python notebook here)

### Python Notebooks

[Create_Dataset](https://github.com/Lambda-School-Labs/djhelper-ds/blob/master/update_dataset.ipynb)

[Python Notebook 2](🚫add link to python notebook here)

[Python Notebook 3](🚫add link to python notebook here)

### 3️⃣ How to connect to the data API

- create .env file with the keys values in your working folder.
  
  SPOTIPY_CLIENT_ID="your_client_ID"

  SPOTIPY_CLIENT_SECRET="your_client_secret_key"
  
  from dotenv import load_dotenv

  import os
  
- you can check your keys variables before running API client credentials.
  
  print("CLIENT ID:", os.environ.get("SPOTIPY_CLIENT_ID"))

  print("CLIENT SECRET:", os.environ.get("SPOTIPY_CLIENT_SECRET"))
  
  import spotipy

  from spotipy.oauth2 import SpotifyClientCredentials
  
  client_credentials_manager = SpotifyClientCredentials()

  sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

## Contributing

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.

Please note we have a [code of conduct](./code_of_conduct.md.md). Please follow it in all your interactions with the project.

### Issue/Bug Request

 **If you are having an issue with the existing project code, please submit a bug report under the following guidelines:**
 - Check first to see if your issue has already been reported.
 - Check to see if the issue has recently been fixed by attempting to reproduce the issue using the latest master branch in the repository.
 - Create a live example of the problem.
 - Submit a detailed bug report including your environment & browser, steps to reproduce the issue, actual and expected outcomes,  where you believe the issue is originating from, and any potential solutions you have considered.

### Feature Requests

We would love to hear from you about new features which would improve this app and further the aims of our project. Please provide as much detail and information as possible to show us why you think your new feature should be implemented.

### Pull Requests

If you have developed a patch, bug fix, or new feature that would improve this app, please submit a pull request. It is best to communicate your ideas with the developers first before investing a great deal of time into a pull request to ensure that it will mesh smoothly with the project.

Remember that this project is licensed under the MIT license, and by submitting a pull request, you agree that your work will be, too.

#### Pull Request Guidelines

- Ensure any install or build dependencies are removed before the end of the layer when doing a build.
- Update the README.md with details of changes to the interface, including new plist variables, exposed ports, useful file locations and container parameters.
- Ensure that your code conforms to our existing code conventions and test coverage.
- Include the relevant issue number, if applicable.
- You may merge the Pull Request in once you have the sign-off of two other developers, or if you do not have permission to do that, you may request the second reviewer to merge it for you.

### Attribution

These contribution guidelines have been adapted from [this good-Contributing.md-template](https://gist.github.com/PurpleBooth/b24679402957c63ec426).

## Documentation

See [Backend Documentation](_link to your backend readme here_) for details on the backend of our project.

See [Front End Documentation](_link to your front end readme here_) for details on the front end of our project.

