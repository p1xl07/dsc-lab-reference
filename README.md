# Data Science Lab Reference — v2.0.0

A practical collection of short Jupyter notebooks for university data science practicals.

## Included notebooks

1. `01_Regression.ipynb` — simple/multiple linear regression (manual NumPy) and single-/multiple-feature logistic regression (scikit-learn).
2. `02_Data_Preprocessing.ipynb` — CSV loading, inspection, missing values, encoding, scaling, train/test split.
3. `03_NumPy_Pandas.ipynb` — arrays, indexing, numerical operations, DataFrames, filtering, sorting, CSV export.
4. `04_Model_Evaluation.ipynb` — MAE, MSE, RMSE, R², confusion matrix, accuracy, precision, recall, F1.
5. `05_Visualization.ipynb` — line, scatter, bar, histogram, box plot, correlation heatmap.

## Install from GitHub

Upload the contents of this folder to a GitHub repository. On a lab computer, run:

```bash
pip install git+https://github.com/p1xl07/dsc-lab-reference.git
```

Copy all notebooks into the current directory:

```bash
dsc-lab-notebooks
```

This creates a `dsc-lab-notebooks` folder containing all five notebooks.

Open Jupyter:

```bash
jupyter notebook
```

If Jupyter is not installed:

```bash
pip install notebook
```

## Test locally

From this project folder:

```bash
pip install .
dsc-lab-notebooks
```

## Notes

- Replace sample datasets and column names with those in your practical question.
- In a proper ML workflow, split the data first, fit preprocessing/scaling steps on training data, then transform test data.
- The notebooks are reference material, not a substitute for checking your lab's required method and permitted resources.
