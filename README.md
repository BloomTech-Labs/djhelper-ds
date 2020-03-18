


# DJ Helper

You can find the project at [www.dj-helper.com](https://www.dj-helper.com).

## Contributors


|                                       [Jordan Heuer](https://github.com/j-m-d-h)                                        |                                       [Mariana Dominguez](https://github.com/madinanachan)                                        |                                       [Isaac Lopez](https://github.com/lopez-isaac)                                        |                                     |                                                                               |
| :-----------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------: |
|                      [<img src="https://ca.slack-edge.com/T4JUEB3ME-UJQR645R8-ea8dc0f12cf6-512" width = "200" />](https://github.com/j-m-d-h)                       |                      [<img src="https://ca.slack-edge.com/T4JUEB3ME-UL44ALSSK-3e3a00d49ce2-512" width = "200" />](https://github.com/madinanachan)                       |                      [<img src="https://ca.slack-edge.com/T4JUEB3ME-UNK2RKG2H-26c2bec454b7-512" width = "200" />](https://github.com/lopez-isaac)    |
|                 [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/)                 |            [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/honda0306)             |           [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/Mister-Corn)            |      |
| [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](http://linkedin.com/in/jmdh) | [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/) | [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/isaac-lopez-ds/) |




![MIT](https://img.shields.io/packagist/l/doctrine/orm.svg)
![Typescript](https://img.shields.io/npm/types/typescript.svg?style=flat)


## Project Overview


[Trello Board](https://trello.com/b/8PQ8BRod/labs-21-dj-helper)

[Product Canvas](https://www.notion.so/594af78f1b344d38976c00f9e71cf048?v=d50f07ef5cdc4e61aaadd9b6208e437a)

DJ-helper is a web application designed to help DJ's discover and create a more flavorful playlists for the event they
are performing at. Before an event starts guests will submit music requests. With the help of machine learning the
application will take those requests and create a unique playlist. The DJ can select songs and add them to their set.
The application will also function in real time during the event and adjust to any changes in music trend that occur. 

[Deployed Front End](https://www.dj-helper.com)

### Tech Stack

Python, Dash, spotipy, spotify api

### Predictions

DJ helper uses an unsupervised k-neighbors model to predict audibly similar songs. The model uses spotify's api to
obtain a list of similar artists and then uses the musical features spotify provides to find the closest sounding track. 


### Data Sources


-   [Spotipy](https://spotipy.readthedocs.io/en/2.9.0/)
-   [Spotify API](https://developer.spotify.com/documentation/web-api/)


### Python Notebooks


[Python Model Notebook](https://github.com/Lambda-School-Labs/djhelper-ds/blob/feature/Recommendation_Machine_V3.ipynb)

[Python Visual Notebook](https://github.com/Lambda-School-Labs/djhelper-ds/blob/visuals_canvas/radar%20function.ipynb)

[Python Dash App Notebook](🚫add link to python notebook here)


### How to connect to the data API

1. First you will need to Apply for spotify developer account to obtain API keys
2. replicate this code and your set to go 
    
    client_id = "Your token key" \
    client_secret = "Your token key"
    
    credentials = oauth2.SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret)

    token = credentials.get_access_token()
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    
    




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

See [Backend Documentation](https://github.com/Lambda-School-Labs/djhelper-be/blob/master/README.md) for details on the backend of our project.

See [Front End Documentation](https://github.com/Lambda-School-Labs/djhelper-fe/blob/master/README.md) for details on the front end of our project.

