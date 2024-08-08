# Wine_Quality_Prediction

### Docker image of this project: 
```
docker pull priteshtadvi/wine-quality-image:latest
```
### Deployed on huggingface:
[https://huggingface.co/spaces/pritesh29/Wine-Quality-Prediction](https://huggingface.co/spaces/pritesh29/Wine-Quality-Prediction)


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

## How to run ?

### Steps:

Clone the repository

```bash
git clone https://github.com/pritesh2000/Wine_Quality_Prediction
```

### Step 1: Create a virtual environment after opening the repository

```bash
cd Wine_Quality_Prediction
```

```bash
virtualenv env
```

#### Based on CLI run
```bash
# for bash
source env/scripts/activate
```
or
```bash
# for command prompt
env\scripts\activate
```

### Step 2: install the requirements
```bash
pip install -r requirements.txt
```

```bash
python app.py
```

```
Open up your localhost:8080 (make sure the port has not been used before).
Now app can run using trained data and predict the result
```
