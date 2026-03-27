Following https://codelabs.developers.google.com/deploy-google-adk-agent-to-cloud-run?hl=en#0 

### what are we doing here
1) Set upp a Google Cloud Project for Cloud Run,  build a simple AI agent using Google ADK and vertex AI, define and use local tools within the agent, package the agent using Docker and FASTAPI server and deploy on Google Cloud Run and interact with the deployed agent through a web UI and via curl as client.


(hello_agent) jindal_vivek10@cloudshell:~/projects$ **git clone https://github.com/abhishekr700/Cloud-Run-Day-Workshop-2025.git simple_agent_deploy_cloudrun/**

From directory  jindal_vivek10@cloudshell:~/projects/simple_agent_deploy_cloudrun/workshop1

**gcloud run deploy news-assistant-agent \
  --source . \
  --region us-central1 \
  --project vjindal-project-ai-basic \
  --allow-unauthenticated \
  --set-env-vars="GOOGLE_GENAI_USE_VERTEXAI=TRUE,GOOGLE_API_KEY="**

### The following APIs are not enabled on project [vjindal-project-ai-basic]:
        artifactregistry.googleapis.com
        cloudbuild.googleapis.com
        run.googleapis.com
### Do you want enable these APIs to continue (this will take
(hello_agent) jindal_vivek10@cloudshell:~/projects/simple_agent_deploy_cloudrun/workshop1$ gcloud run deploy news-assistant-agent \

Do you want enable these APIs to continue (this will take a few minutes)? (Y/n)?  Y
Do you want to create the artifact registry named "cloud-run-source-deploy" - Y

   |  Building and deploying new service... Building Container.      
OK Building and deploying new service... Done.
                                                                                                                 Done.       
Service [news-assistant-agent] revision [news-assistant-agent-00001-srs] has been deployed and is serving 100 percent of traffic.

Service URL: https://news-assistant-agent-658050955671.us-central1.run.app


## Running the agent locally by running the FastAPI main.py
### Initialize the folder as a uv project
**uv init**

### Import all libraries from requirements.txt into the project configuration
**uv add -r requirements.txt**

### Modify agent.py code to include following environment variables
**os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "TRUE"**
**os.environ["GOOGLE_CLOUD_PROJECT"] = os.environ.get("GOOGLE_CLOUD_PROJECT", "vjindal-project-ai-basic")**


### This command automatically syncs the environment and starts your FastAPI server
**uv run python main.py**

INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)

## Invoking the Cloud RUN agent using Curl command to send the payload (create new session first and then use that username and session to sent prompt)

(example of how some client can call your deployed agent in Cloud RUN cos so far you were manually going to the cloud run URL and typing the prompt in the chat interface)

## CREATE user ID and session ID first in this way as agent does not provide APIs for the 
## jindal_vivek10@cloudshell:~/projects/simple_agent_deploy_cloudrun/workshop1$ curl -X POST https://news-assistant-agent-658050955671.us-central1.run.app/apps/news_assistant_agent/users/vjindal_user/sessions/session_vj_001 -H "Content-Type: application/json" -d '{"state": {}}'                                                               
{"id":"session_vj_001","appName":"news_assistant_agent","userId":"vjindal_user","state":{"state":{}},"events":[],

## Then invoke the agent running on cloud run using CURL 

## jindal_vivek10@cloudshell:~/projects/simple_agent_deploy_cloudrun/workshop1$ curl -X POST https://news-assistant-agent-658050955671.us-central1.run.app/run -H "Content-Type: application/json" -d '{"appName": "news_assistant_agent", "userId": "vjindal_user", "sessionId": "session_vj_001", "newMessage": {"role": "user", "parts": [{"text":
"What is the news in Bengaluru?"}]}}'             

## Create repository and upload code to github
create repository in github
## In cloud shell do following
**git init**

Create .gitignore file (to remove env files, sessions.db and pycache files from uploading to git) and you need to upload pyproject.toml and uv.lock files as well including .gitignore to GitHub repo 

IF you get below error when clicking on Commit in editor then do following
"Make sure you configure your "user.name" and "user.email" in git."

 **git config --global user.name "Vivek Jindal"**
**git config --global user.email "jindal.vivek10@gmail.com"**

 # Press the "sync changes" button now and authorize cloud shell and give permission to github

 ## To delete Cloud run deployed instance
 **gcloud config set project vjindal-project-ai-basic**


 jindal_vivek10@cloudshell:~/projects/simple_agent_deploy_cloudrun/workshop1 (vjindal-project-ai-basic)$ **gcloud run services delete news-assistant-agent --region us-central1 --quiet**

