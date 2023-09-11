from behave import Given, When, Then


@Given("we select the {category_name} category")
def step_impl(context, category_name: str):
    context.app.home_page.open_category_search(category_name)
