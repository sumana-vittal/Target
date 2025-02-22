from behave import given, when, then


@when("Click on Add to Cart")
def click_add_to_cart(context):
    context.app.search_result_page.click_add_to_cart()


@when("Click on Add to Cart in right panel")
def add_to_cart_in_right_panel(context):
    context.app.search_result_page.add_to_cart_in_right_panel()
#   store product name and price
    context.product_name = context.app.search_result_page.get_product_name()
    context.product_price = context.app.search_result_page.get_product_price()


@when("Click View cart and check out from right side panel")
def click_view_cart_and_check_out(context):
    context.app.search_result_page.click_view_cart_and_check_out()


