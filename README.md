# NLTK Text classifier

The purpose of this project is to create a text classifier using NLTK and deploy 
as an API endpoint. For simplicity, I followed the [gender classification](http://www.nltk.org/book/ch06.html)
example from the NLTK cookbook.
#### Exploring the UI  
First steps were to familiarize myself with the tool and learn the UI. I created 
a Jupyter session to load the NLTK names data and play around with different features. 
After getting a decent accuracy, I pickled the model for deployment.
#### Using the CLI  
I also spent some time using the CLI to walk through the same steps. For this, I 
downloaded the data into the project directory to avoid having to use the jupyter 
notebook for training the model every time.
## Deploying the model  
After pickling the model, I created a deploy script for loading the model and exposing it via
a function. Ran into a few issues with the version of NLTK installed, so I upgraded this 
to `3.2.2` After testing the endpoint, I upgraded it to be able to accept multiple names 
and also return the original query with the response.
## Thoughts  
Overall, the UI was fairly easy to get hang of. There were a few frustrating points, 
such as `CMD+S` not working and inconsistent behavior from the `Run` button.

The CLI was very intuitive and made transferring local development to Domino a seamless experience.

For reference, here is the code for testing the API:

```
curl -v -X POST \
https://trial.dominodatalab.com/v1/josibake/nltk-classifier/endpoint \
-H 'Content-Type: application/json' \
-H 'X-Domino-Api-Key: ${DOMINO_API_KEY}' \
-d '{"parameters": [ "samuel", "sarah", "emily"]}'
```
## More thoughts on API publishing
Doesn't look like you can fully set up an API endpoint from the CLI: no place to specify what function to use. 
Also, can't deploy scripts that depend on parameters. Script will run successfully, but not deploy.
