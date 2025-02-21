from behave import given, when, then


@given("Open home page {home_page_url}")
def open_home_page(context, home_page_url):
    context.app.home_page.open_home_page(home_page_url)


@when("Enter search keyword {search_query} in search textbox")
def enter_search_text(context, search_query):
    context.app.home_page.enter_search_text(search_query)


@when("Click on Search button")
def click_search_button(context):
    context.app.home_page.click_search_button()


@then("Verify Product results for {result} are shown on search result page.")
def verify_search_product_result(context, result):
    context.app.search_result_page.verify_search_product_result(result)


@then("Verify page URL has {search_query} in it.")
def verify_search_product_url(context, search_query):
    context.app.search_result_page.verify_search_product_url(search_query)