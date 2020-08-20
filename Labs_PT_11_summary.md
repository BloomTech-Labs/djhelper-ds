# End of Labs DS PT 11 Documentation

## Summary

Created API call for the back-end team to use aa a start point in search function, https://sp-search.herokuapp.com/track_search_ready/{text}.
Created API call to find similar songs from an Id of the desired one, https://sp-search.herokuapp.com/predict/{id}. It uses NearestNeighbour to find similar songs depending on the features such as: acousticness, danceability, energy, etc.

## Future plans

Created API call for search function that provides the results with the audio features. https://sp-search.herokuapp.com/audio_features/{text}. It can be used to create visualizations to improve application. Also you’ll have the API call to get all the features from the search function. In case you’ll decide to add any extra features to the search result. https://sp-search.herokuapp.com/prepare_search_track/{text}.
