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
git clone https://github.com/pritesh2000/Wine_Quality_Prediction
```

### step 1: Create a virtual environment after opening the repository

```bash
cd Wine_Quality_Prediction
```

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
open up your localhost and train model using by extending url with '/train' or run command python main.py
Now app can run using trained data and predict the result
```
