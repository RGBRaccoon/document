discriminant_analysis = "판별분석은 두 개 이상의 범주로 분류되는 데이터를 분류하는 모형.\
        두 개 또는 그 이상의 그룹(또는 군집 또는 모집단)이 사전에 알려져 있을 때,\
        새로운 관측값을 특성에 기초하여 이미 알려진 모집단 가운데 하나로 분류하는 기법\
        예측변수가 연속형 변수인 경우 사용됨"
# 반응 변수, 예측변수들의 결합분포를 기반으로 분류
# 범주가 잘 정리되어있을 때, 로지스틱 보다 더 나은 성능
# n이 작고 X의 분표가 정규분포에 가까울수록 좋음.
# 다중 변수의 경우 로지스틱보다 간단

# 이차원 평면에 두 그룹의 데이터가 있고 이를 타원으로 각각 표현한다.
# 이 둘을 가장 잘 나누는 선을 찾는것이 목적적
# 타원의 의미:
# 각 그룹(노랑, 파랑)의 데이터가 95% 확률로 존재하는 영역을 나타냅니다
# 이 타원들은 서로 겹칠 수 있고, 겹치는 부분이 초록색으로 표시됩니다
# 최적의 구분선 찾기:
# 두 타원이 겹치는 초록색 영역을 지나는 직선을 찾습니다
# 이 직선은 겹치는 영역의 길이가 가장 짧아야 합니다
# 즉, 두 그룹을 가장 효율적으로 구분하는 선을 찾는 것입니다


class DiscriminantAnalysis:
    pass
