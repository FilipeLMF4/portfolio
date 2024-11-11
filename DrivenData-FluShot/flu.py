import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def vaccination_rate_plot(col, target, data, ax=None):
    """Stacked bar chart of vaccination rate for `target` against
    `col`.

    Args:
        col (string): column name of feature variable
        target (string): column name of target variable
        data (pandas DataFrame): dataframe that contains columns
            `col` and `target`
        ax (matplotlib axes object, optional): matplotlib axes
            object to attach plot to
    """
    counts = (joined_df[[target, col]]
                  .groupby([target, col])
                  .size()
                  .unstack(target)
             )
    group_counts = counts.sum(axis='columns')
    props = counts.div(group_counts, axis='index')

    props.plot(kind="barh", stacked=True, ax=ax)
    ax.invert_yaxis()
    ax.legend().remove()

def plot_roc(y_true, y_score, label_name, ax):
    fpr, tpr, thresholds = roc_curve(y_true, y_score)
    ax.plot(fpr, tpr)
    ax.plot([0, 1], [0, 1], color='grey', linestyle='--')
    ax.set_ylabel('TPR')
    ax.set_xlabel('FPR')
    ax.set_title(f"{label_name}: AUC = {roc_auc_score(y_true, y_score):.4f}")

#Import data sets
pd.set_option('display.max_columns',100)

features_df=pd.read_csv('training_set_features.csv',index_col='respondent_id')
labels_df=pd.read_csv('training_set_labels.csv',index_col='respondent_id')
test_features_df=pd.read_csv('test_set_features.csv',index_col='respondent_id')
submission_df=pd.read_csv('submission_format.csv',index_col='respondent_id')

print('Features_df Shape:', features_df.shape)
print('labels_df Shape:',labels_df.shape)

try:
    np.testing.assert_array_equal(features_df.index.values, labels_df.index.values)
except AssertionError:
    print('DataFrames\' indices do not match up. Verify DataFrames')
    quit()

joined_df = features_df.join(labels_df)


#Import Training models
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer

from sklearn.linear_model import LogisticRegression
from sklearn.multioutput import MultiOutputClassifier

from sklearn.pipeline import Pipeline

from sklearn.model_selection import train_test_split

from sklearn.metrics import roc_curve, roc_auc_score

RANDOM_SEED = 6

#Feature Preprocessing
numeric_cols=features_df.columns[features_df.dtypes!='object'].values

# chain preprocessing into a Pipeline object
# each step is a tuple of (name you chose, sklearn transformer)
numeric_preprocessing_steps=Pipeline([
    ('standard_scaler',StandardScaler()),
    ('simple_imputer',SimpleImputer(strategy='median'))
])

# create the preprocessor stage of final pipeline
# each entry in the transformer list is a tuple of
# (name you choose, sklearn transformer, list of columns)
preprocessor=ColumnTransformer(
    transformers = [
        ('numeric',numeric_preprocessing_steps,numeric_cols)
    ],
    remainder='drop'
)

estimators=MultiOutputClassifier(estimator=LogisticRegression(penalty='l2',C=1))

full_pipeline=Pipeline([
    ('preprocessor',preprocessor),
    ('estimators',estimators)
])

#Training and Evaluating
X_train, X_test, y_train, y_test = train_test_split(
    features_df,
    labels_df,
    test_size=0.33,
    shuffle=True,
    stratify=labels_df,
    random_state=RANDOM_SEED
)

full_pipeline.fit(X_train,y_train)
preds=full_pipeline.predict_proba(X_test)
print(preds)

y_preds=pd.DataFrame(
    {
        'h1n1_vaccine':preds[0][:,1],
        'seasonal_vaccine':preds[1][:,1]
    },
    index=y_test.index
)

print(y_preds.head())

#Make ROC curve plots
fig, ax = plt.subplots(1, 2, figsize=(7, 3.5))

plot_roc(
    y_test['h1n1_vaccine'],
    y_preds['h1n1_vaccine'],
    'h1n1_vaccine',
    ax=ax[0]
)
plot_roc(
    y_test['seasonal_vaccine'],
    y_preds['seasonal_vaccine'],
    'seasonal_vaccine',
    ax=ax[1]
)
fig.tight_layout()
plt.show()

print('Roc_auc_score:',roc_auc_score(y_test,y_preds))

#Train whole dataset
full_pipeline.fit(features_df, labels_df)
test_probas=full_pipeline.predict_proba(test_features_df)

#Compile submission form
try:
    np.testing.assert_array_equal(test_features_df.index.values,submission_df.index.values)
except AssertionError:
    print('DataFrames\' indices do not match')
    quit()

submission_df['h1n1_vaccine']=test_probas[0][:,1]
submission_df['seasonal_vaccine']=test_probas[1][:,1]

submission_df.to_csv('my_submission.csv',index=True)
