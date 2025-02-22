from behave import given, when, then


@then("verify it navigates to cart page")
def verify_cart_page(context):
    context.app.cart_page.verify_cart_page()


@then("verify one product is added in the cart")
def verify_product_added_to_cart(context):
    context.app.cart_page.verify_product_added_to_cart()


@then("verify price and product is same as added.")
def verify_price_and_product_is_right(context):
    context.app.cart_page.verify_price_and_product_is_right(context.product_name, context.product_price)