# Crowd Server API

This is a brief documentation for Crowd Server API.The API is organized around [REST](https://en.wikipedia.org/wiki/Representational_state_transfer). The API has predictable resource-oriented URLs, accepts [form-encoded](https://en.wikipedia.org/wiki/POST_(HTTP)#Use_for_submitting_web_forms) request bodies, returns [JSON](https://www.json.org/json-en.html)-encoded responses, and uses standard HTTP response codes and authentication.     

---         
## Apps
- **Food Compare**      
    This app compares two food images about a specific feature(e.g which one is more filling, healthier ...)        
    see [Google Crowd Source](https://crowdsource.google.com/csf/?hl=en#/contribute/food_compare) for more examples         
- **Food Fact**         
    This app asks if a fact is true for the shown image     
    see [Google Crowd Source](https://crowdsource.google.com/csf/?hl=en#/contribute/food_facts) for more examples           
- **Food Labeler**          
    This app asks if a given label is true for the shown image       
    see [Google Crowd Source](https://crowdsource.google.com/csf/?hl=en#/contribute/food_labeler) for more examples      
- **Image Caption**             
    This app asks if a given caption is appropriate for the shown image             
    see [Google Crowd Source](https://crowdsource.google.com/cs/contribute/image-caption/en) for more examples 
- **Sentiment**         
    This app asks about the kind of emotion expressed in a sentence          
    see [Google Crowd Source](https://crowdsource.google.com/) for more examples  
- **Translation Validator**             
    This app asks if the given translation of a sentence/phrase/word is true            
    see [Google Crowd Source](https://crowdsource.google.com/) for more examples

---             
## Access the API                        
You can Access the API on both Github and Dockerhub. Although **it is highly recommended that you use the docker image to work with the API.**                  

### Docker
Access the Dockerhub repository from here:               
- [Dockerhub repository](https://hub.docker.com/r/tahoora/crowd-server-api)     
     
You can easily work with the API with the following commands:
- `docker pull tahoora/crowd-server-api:version2`
- `docker run -p 8000:8000 tahoora/crowd-server-api:version2`

### Github
Access the Github repository from here:(Until further notice, **use the version1 branch** of this repository)
- [Github repository](https://github.com/Zarebin/nextgen-py-4/tree/main/crowd-server)

## For More Info 
for more detailed information about the API, after running the API, visit [localhost:8000/api/docs](localhost:8000/api/docs)

---
## Contact The Developer
- Tahoora Majlesi
    - tahooramajlesi@yahoo.com
    - [Github](https://github.com/Tahoora78)
    - [Linkedin](https://www.linkedin.com/in/tahoora-majlesi/)
---
## Issues
Feel free to report the bugs in the [issue section](https://github.com/Zarebin/nextgen-py-4/issues)
