tables = {
    "orders" : {
        "columns" : {
            "order_id"          : { "name": "id", "type": "text" },
            "customer"          : { "name": "customerName", "type": "text" },
            "email"             : { "name": "email", "type": "text" },
            "order_status"      : { "name": "status", "type": "text" },
            "placed_at"         : { "name": "orderDate", "type": "text" },
            "total_price"       : { "name": "totalPrice", "type": "integer" },
            "coupon"            : { "name": "coupon", "type": "text" },
        }
    },

    "subscriptions" : {
        "columns" : {
            "subscription_id"   : { "name": "id", "type": "text" },
            "customer"          : { "name": "customerName", "type": "text" },
            "email"             : { "name": "email", "type": "text" },
            "ship_zip_code"     : { "name": "shipZip", "type": "text" },
            "start_date"        : { "name": "startDate", "type": "text" },
            "end_date"          : { "name": "endDate", "type": "text" },
            "term"              : { "name": "term", "type": "text" },
            "gift_message"      : { "name": "message", "type": "text" },
        }
    },

    "transactions" : {
        "columns" : {
            "Order ID"          : { "name": "id", "type": "text" },
            "Customer Name"     : { "name": "customerName", "type": "text" },
            "Email"             : { "name": "email", "type": "text" },
            "Order Date"        : { "name": "orderDate", "type": "text" },
            "Total Price"       : { "name": "totalPrice", "type": "integer" },
            "term"              : { "name": "term", "type": "text" },
            "gift_message"      : { "name": "message", "type": "text" },
        }
    }
}