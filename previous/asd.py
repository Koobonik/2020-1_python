import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



file_path = 'chipotle.tsv'
chipo = pd.read_csv(file_path, sep = '\t')

print(chipo.shape)
print("--------------------")
print(chipo.info())

print("----------------")
print(chipo.columns)
print(chipo.index)

chipo['order_id'] = chipo['order_id'].astype(str)
print(chipo.describe())

item_count = chipo['item_name'].value_counts()[:10]
for idx, (val, cnt) in enumerate(item_count.iteritems(), 1):
    print("Top", idx, ":", val, cnt)


# 주문 개수
order_count = chipo.groupby('item_name')['order_id'].count()
print(order_count[:10])

# 주문 총량
item_quantity = chipo.groupby('item_name')['quantity'].sum()
item_quantity[:10]


item_name_list = item_quantity.index.tolist()
x_pos = np.arange(len(item_name_list))
order_cnt = item_quantity.values.tolist()

# plt.bar(x_pos, order_cnt, align='center')
# plt.ylabel('ordered_item_count')
# plt.title("Distribution of all orderd item")
#
# plt.show()

chipo['item_price'] = chipo['item_price'].apply(lambda x: float(x[1:]))
print(chipo.describe())


# 주문당 평균 계산 금액 출력

print(chipo.groupby('order_id')['item_price'].sum().mean())


# 한 주문에 10달러 이상 사용한 id를 출력
chipo_orderid_group = chipo.groupby('order_id').sum()
result = chipo_orderid_group[chipo_orderid_group.item_price >=10]

print(result[:10])
print(result.index.values)


# 각 아이템의 가격을 계산
chipo_one_item = chipo[chipo.quantity == 1]
price_per_item = chipo_one_item.groupby('item_name').min()
print(price_per_item.sort_values(by = "item_price", ascending= False)[:10])


# Veggie Salad Bowl 필터링
chipo_salad = chipo[chipo['item_name'] == "Veggie Salad Bowl"]
chipo_salad = chipo_salad.drop_duplicates(['item_name', 'order_id'])
print(len(chipo_salad))
chipo_salad.head(5)


# Chicken Bowl
# 일단 치킨볼만 뽑아서 chipo_chicken 에 담아준다.  -> 1. 데이터 프레임에서 item_name으로 Chicken Bowl을 필터링
chipo_chicken = chipo[chipo['item_name'] == "Chicken Bowl"]

# 주문 번호를 기준으로 (grouby 사용할 것) 선정 -> 2. 주문 번호를 기준으로 그룹을 선정 -> 3. 그 후 , item_price로 합계를 구함
chipo_chicken_ordersum = chipo_chicken.groupby('order_id').sum()['item_price']

# 가장 많이 지불한 주문 번호 5개만 출력해야 하므로 마지막에 [:5] 해준다.
print(chipo_chicken_ordersum.sort_values(ascending= False)[:5])
