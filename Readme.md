# Model Server API
## Description
This repo contains the code for a model server api, it is used by kubeflow pipelines to create a container image that is served with Kserve.  
Kubeflow pipelines uses the code source in this repo and a sklearn model that is created during the pipeline workflow, combining both in a docker image. The docker image is then used to create a kserve inference service.
