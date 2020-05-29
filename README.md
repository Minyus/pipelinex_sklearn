# PipelineX Scikit-learn

A Simple example project using [PipelineX](https://github.com/Minyus/pipelinex), Kedro, and Scikit-learn

<p align="center">
<img src="img/kedro_pipeline.png">
Pipeline visualized by Kedro-viz
</p>



## 0: Download `train.csv` and `test.csv` from [Kaggle Titanic](https://www.kaggle.com/c/titanic/data) to `data/input` directory

## 1. Install dependencies

```bash
$ pip install pipelinex scikit-learn pandas kedro mlflow plotly kedro-viz
```

Note: `plotly` and `kedro-viz` are for visualization.

## 2. Clone this repository and run `main.py`

```bash
$ git clone https://github.com/Minyus/pipelinex_sklearn.git
$ cd pipelinex_sklearn
$ python main.py
```

## 3. [Optional] View the experiment logs in MLflow's UI 

```bash
$ mlflow server --host 0.0.0.0 --backend-store-uri sqlite:///mlruns/sqlite.db --default-artifact-root ./mlruns/experiment_001
```

<p align="center">
<img src="img/mlflow_ui.png">
Experiment logs in MLflow's UI
</p>


## Tested environment

- Python 3.6.8
