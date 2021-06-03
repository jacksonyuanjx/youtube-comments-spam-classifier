# YouTube Comments Spam Classifier

### YouTube Walkthrough
* [Training the model](https://youtu.be/FmmlHbHqgGY)
* [Deploying Flask API](https://youtu.be/Q_Z5kzKpofk)

### Running locally to generate predictions
#### Run the Flask API
* install `pipenv`
* run `python server.py`
* send requests to `POST localhost:5000/predict` or use the Swagger UI to generate predictions

#### OR, run the Jupyter notebook

### Limitations
* dataset only comes from comments on music videos of five artists so the model may not perform as expected in other contexts (e.g. a tech video)
* what is considered spam in one context may just as well be considered non-spam in a different context
