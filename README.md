# Walking Time Bot

This is just a useless demo bot that I created to familiarize myself with Rasa and its concepts.

## How to run locally

First run the action server:

```
GOOGLE_API_KEY="YOUR_API_KEY" rasa run actions
```

`YOUR_API_KEY` is you Google API key, with [Distance Matrix API](https://developers.google.com/maps/documentation/distance-matrix) enabled.


And in another terminal tab, start the Rasa shell to interact with the bot:

```
rasa shell
```