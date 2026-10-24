# Models evaluation results


## 1.Baseline Models  results

### Logistic Regression - Baseline Results
Accuracy:  0.9459
Precision: 0.9419
Recall:    0.9410
F1-score:  0.9415
ROC-AUC:   0.9904

### Random Forest - Baseline Results
Accuracy: 0.9421
Precision: 0.9389
Recall: 0.9355
F1-score: 0.9372
ROC-AUC: 0.988
---


## 2.Models tuning results

### Hyperparameter toning - Logistic Regression 
Best Parameters: {'model__C': 0.01, 'model__solver': 'lbfgs'}
Best CV F1-score: 0.9395


### Hyperparameter toning - Random forest 
Best Parameters: {'model__max_depth': None, 'model__min_samples_split': 2, 'model__n_estimators': 200}
Best CV F1-score: 0.9347

---

## 3.Tuned Models metrics results

### Logistic Regression - Tuned Results
Accuracy:  0.9455
Precision: 0.9418
Recall:    0.9401
F1-score:  0.9409
ROC-AUC:   0.9904


### Random Forest - Tuned Results
Accuracy: 0.9424
Precision: 0.9387
Recall: 0.9365
F1-score: 0.9376
ROC-AUC: 0.9882

---


## Confusion Matrix - Tuned Models

### Logistic Regression
True Negatives (TN): 10218
False Positives (FP): 537
False Negatives (FN): 554
True Positives (TP): 8691
Total Errors: 1091

### Random Forest
True Negatives (TN): 10190
False Positives (FP): 565
False Negatives (FN): 587
True Positives (TP): 8658
Total Errors: 1152