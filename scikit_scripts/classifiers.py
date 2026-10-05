from sklearn.base import ClassifierMixin
from typing import Any

def run_classifier(clf_class: ClassifierMixin, X_train: Any, y_train: Any, X_test: Any, y_test: Any, **kwargs) -> float:
    clf = clf_class(**kwargs)
    clf.fit(X_train, y_train)
    acc = accuracy_score(y_test, clf.predict(X_test))
    return acc

