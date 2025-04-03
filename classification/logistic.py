logistic_regression = "로지스틱 모형은 Y에 대한 직접적인 모형화가 아닌, Y에 속할 확률을 모형화 반응 변수가 두개로 이루어진 이진분류"
threshold = "임계치. 두 클래스를 구분하는 기준이 되는 확률 값. 보통 0.5가 사용됨. 확률이 0.5를 넘기면 1 아니면 0같은 방식. 예측하고자하는 대상에\
따라 임계치를 조정하기도 함"
import pandas as pd

maximum_likelihood = "최대가능도 추정법. 확률 모형에서 모수를 추정하는 방법. 주어진 데이터가 나올 확률을 최대화하는 모수를 찾는 방법"


class LogisticRegression:
    def __init__(self):
        self.train_path = "train.csv"
        self.test_path = "test.csv"
        self.output_path = "output.csv"
        self.train_data = pd.read_csv(self.train_path)
        self.test_data = pd.read_csv(self.test_path)
        self.threshold = 0.5

    def preprocess_data(self):
        pass

    def train(self):
        pass

    def predict(self):
        pass
