from collections import deque

ramen = [int(el) for el in input().split(", ")]
customers = deque([int(el) for el in input().split(", ")])

while ramen and customers:
    current_ramen_bowl = ramen.pop()
    current_customer = customers.popleft()
    if current_ramen_bowl == current_customer:
        continue
    elif current_customer > current_ramen_bowl:
        current_customer -= current_ramen_bowl
        customers.appendleft(current_customer)
    elif current_ramen_bowl > current_customer:
        current_ramen_bowl -= current_customer
        ramen.append(current_ramen_bowl)


if not customers:
    print(f"Great job! You served all the customers.")
    if ramen:
        print(f'Bowls of ramen left: {", ".join(str(el) for el in ramen)}')


if not ramen and customers:
    print(f"Out of ramen! You didn't manage to serve all customers.")
    print(f'Customers left: {", ".join(str(el) for el in customers)}')
