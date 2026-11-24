# California Housing
import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, mean_squared_error, precision_score, r2_score, recall_score, roc_auc_score
from sklearn.model_selection import KFold, RepeatedKFold, StratifiedKFold, cross_val_score, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier

folder = r"C:\Users\Amlsh\PycharmProjects\AdvancedPython" + "\\"

# Part 1: classification (Adult Income)
print("Part 1: Classification")
df = pd.read_csv(folder + "adult.csv")
for col in df.select_dtypes(exclude="number").columns:
    df[col] = df[col].str.strip()
df = df.replace("?", np.nan)
print("Shape:", df.shape, "| missing:", df.isnull().sum()[df.isnull().sum() > 0].to_dict())

for col in df.columns[df.isnull().any()]:
    df[col] = df[col].fillna(df[col].median() if pd.api.types.is_numeric_dtype(df[col]) else df[col].mode()[0])

y = LabelEncoder().fit_transform(df["income"].astype(str).str.rstrip("."))
X = pd.get_dummies(df.drop(columns="income"), drop_first=True)
print("Class shares:", pd.Series(y).value_counts(normalize=True).round(2).to_dict(), "| features:", X.shape[1])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
class_models = {
    "Logistic Regression": make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)),
    "Decision Tree": DecisionTreeClassifier(max_depth=5, random_state=42),
}

rows = []
for name, model in class_models.items():
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    prob = model.predict_proba(X_test)[:, 1]
    rows.append({"Model": name, "Accuracy": accuracy_score(y_test, pred), "Precision": precision_score(y_test, pred),
                 "Recall": recall_score(y_test, pred), "F1": f1_score(y_test, pred), "ROC_AUC": roc_auc_score(y_test, prob)})
print(pd.DataFrame(rows).set_index("Model").round(4))
print()

# Part 2: regression (California Housing)
print("Part 2: Regression")
data = fetch_california_housing(as_frame=True).frame
print("Shape:", data.shape, "| missing:", data.isnull().sum().sum(), "| duplicates:", data.duplicated().sum())
data = data.drop_duplicates().dropna()

X_h = data.drop(columns="MedHouseVal")
y_h = data["MedHouseVal"]
Xh_train, Xh_test, yh_train, yh_test = train_test_split(X_h, y_h, test_size=0.2, random_state=42)
reg_models = {
    "Linear Regression": LinearRegression(),
    "Random Forest": RandomForestRegressor(n_estimators=50, random_state=42, n_jobs=-1),
}

rows = []
for name, model in reg_models.items():
    pred = model.fit(Xh_train, yh_train).predict(Xh_test)
    mse = mean_squared_error(yh_test, pred)
    rows.append({"Model": name, "MSE": mse, "RMSE": np.sqrt(mse), "R2": r2_score(yh_test, pred)})
print(pd.DataFrame(rows).set_index("Model").round(4))
print()

# Part 3: cross-validation
print("Part 3: Cross-Validation")
kfold = KFold(n_splits=5, shuffle=True, random_state=42)
stratified = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
repeated = RepeatedKFold(n_splits=5, n_repeats=2, random_state=42)

rows = []
for name, model in class_models.items():
    for cv_name, cv in [("K-Fold", kfold), ("Stratified K-Fold", stratified)]:
        scores = cross_val_score(model, X, y, cv=cv, scoring="accuracy")
        rows.append({"Model": name, "CV": cv_name, "Mean": scores.mean(), "Std": scores.std(), "Lowest fold": scores.min()})
print("Classification (accuracy):")
print(pd.DataFrame(rows).round(4).to_string(index=False))

rows = []
for name, model in reg_models.items():
    for cv_name, cv in [("K-Fold", kfold), ("Repeated K-Fold", repeated)]:
        scores = cross_val_score(model, X_h, y_h, cv=cv, scoring="r2")
        rows.append({"Model": name, "CV": cv_name, "Mean": scores.mean(), "Std": scores.std(), "Lowest fold": scores.min()})
print("Regression (R2):")
print(pd.DataFrame(rows).round(4).to_string(index=False))
