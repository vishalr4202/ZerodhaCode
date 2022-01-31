import kitesettings
from kiteconnect import KiteConnect
import logging


def order_place():
    kite = KiteConnect(kitesettings.API_KEY)
    kite.set_access_token(kitesettings.access_token)
    try:
        order_id = kite.place_order(tradingsymbol="INFY",
                                    exchange=kite.EXCHANGE_NSE,
                                    transaction_type=kite.TRANSACTION_TYPE_BUY,
                                    quantity=1,
                                    price=1300.0,
                                    variety=kite.VARIETY_REGULAR,
                                    order_type=kite.ORDER_TYPE_MARKET,
                                    product=kite.PRODUCT_NRML)
        logging.info("Order placed. ID is: {}".format(order_id))
    except Exception as e:
        logging.info("Order placement failed: {}".format(e.message))

    return order_id

# ---testing--------------------


result = order_place()

print("------------------")
print(result)
