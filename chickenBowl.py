import pandas as pd

# 파일 가져오기
file_path = './chipotle.tsv'

# csv 파일 읽어오기
chipo = pd.read_csv(file_path, sep = '\t')

# order_id는 수치로 볼 수 없고 범주형으로 볼 수 있으므로 Dtype str로 변경하기 -> 이후 분석할때 불편할 수 있기 때문에!
chipo['order_id'] = chipo['order_id'].astype(str)
# 람다식 써서 $ 표시 제거
chipo['item_price'] = chipo['item_price'].apply(lambda x: float(x[1:]))

# Chicken Bowl
# 일단 치킨볼만 뽑아서 chipo_chicken 에 담아준다.  -> 1. 데이터 프레임에서 item_name으로 Chicken Bowl을 필터링
chipo_chicken = chipo[chipo['item_name'] == "Chicken Bowl"]

# 주문 번호를 기준으로 (grouby 사용할 것) 선정 -> 2. 주문 번호를 기준으로 그룹을 선정 -> 3. 그 후 , item_price로 합계를 구함
chipo_chicken_order_sum = chipo_chicken.groupby('order_id').sum()['item_price']

# 가장 많이 지불한 주문 번호 5개만 출력해야 하므로 마지막에 [:5] 해준다.
print(chipo_chicken_order_sum.sort_values(ascending=False)[:5])
