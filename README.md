# MLOPS_project_1

## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the app.py


# How to run ?

## Steps:

Clone the repository

```bash
https://github.com/pritesh2000/MLOPS_project_1
```

### step 1: Create a virtual environment after opening the repository

```bash
virtualenv myenv
```

```bash
source myenv/scripts/activate
```

### step 2: install the requirements
```bash
pip install -r requirements.txt
```

```bash
# Finally run the following command
python app.py
```

```bash
open up your local host and port
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)

##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/priteshptadvi29/MLOPS_project_1.mlflow \
MLFLOW_TRACKING_USERNAME=priteshptadvi29 \
MLFLOW_TRACKING_PASSWORD=(your_token) \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/priteshptadvi29/MLOPS_project_1.mlflow

export MLFLOW_TRACKING_USERNAME=priteshptadvi29

export MLFLOW_TRACKING_PASSWORD=(your_token)
```


ECR repo to save docker image
saved URI : 905418078680.dkr.ecr.ap-south-1.amazonaws.com/mlproj