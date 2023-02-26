def calculate_transaction_fifo(list_transaction: list[dict]) -> float:
    """
    for each transaction
        if type == B
            append to wallet
        elif type == S
            for each coin in wallet
                calculate profit
    ถ้าเหรียญที่เคยซื้อมาไม่พอขายให้แสดงข้อความ error และหยุดการทำงาน
    :param list_transaction:
    :return: profit
    """
    profit = 0
    wallet = []
    '''
    wallet = [
                {
                    name: str,
                    amount: int,
                    price: int
                }
            ]
    '''
    for transaction in list_transaction:
        print(f'transaction: {transaction}')
        print(f"present_wallet: {wallet}")
        coin_name = transaction['name']
        type_transaction = transaction['type']
        if type_transaction == 'B':
            print(f'Buying {coin_name}')
            wallet.append(
                {
                    'name': coin_name,
                    'amount': transaction['amount'],
                    'price': transaction['price']
                }
            )
        elif type_transaction == 'S':
            amount_to_sell = transaction['amount']
            for coin in wallet:
                if amount_to_sell == 0:
                    break
                if coin['amount'] == 0:
                    continue
                if coin['name'] != transaction['name']:
                    continue
                print(f'Selling {coin_name}')

                print(f'to sell: {amount_to_sell}')
                amount_selling = min(amount_to_sell, coin['amount'])
                print(f"selling {amount_selling}")

                cost = amount_selling * coin['price']
                sale = amount_selling * transaction['price']

                profit += sale - cost
                print(f'profit: {sale - cost}')

                amount_to_sell -= amount_selling
                coin['amount'] -= amount_selling
                print(f'left to sell  {amount_to_sell}')

            # after loop in wallet
            # if coin sell transaction left, meaning coin in wallet is insufficient
            if amount_to_sell > 0:
                raise Exception('insufficient_coin')

    return profit


def create_crypto_obj(type_transaction, name, price, amount) -> dict:
    return {
        'type': type_transaction,
        'name': name,
        'amount': amount,
        'price': price
    }


def read_txt_file(file_name):
    """
    ex: B ETH 43000.0 12.0
    field 1: B หรือ S คือ ซื้อ (buy) หรือ ขาย (sell)
    field 2: ชื่อเหรียญ
    field 3: ราคาของเหรียญ ที่ซื้อหรือขาย ต่อ 1 เหรียญ
    field 4: จำนวนเหรียญที่ซื้อ
    """
    list_transaction = []
    with open(file_name) as f:
        for line in f:
            line = line.split(' ')
            type_transaction = line[0]
            name = line[1]
            unit_price = float(line[2])
            amount = float(line[3])
            list_transaction.append(
                create_crypto_obj(type_transaction=type_transaction,
                                  name=name, price=unit_price, amount=amount)
            )

    return list_transaction


def main() -> float:
    """
    อ่านข้อมูลไฟล์
    คำนวณกำไร/ขาดทุนรวม ของการซื้อขายเหรียญคริปโตหลาย ๆ เหรียญรวมกัน แบบ FIFO
    result: 96000.00
    """
    file_name = 'crypto_tax.txt'
    list_transaction = read_txt_file(file_name)
    return calculate_transaction_fifo(list_transaction)


if __name__ == '__main__':
    try:
        result = main()
        print(f'total profit: {result}')
    except Exception as e:
        print(f'error: {e}')
