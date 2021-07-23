

@when('Select Books Department')
def select_department(context):
    context.app.header.select_department()


@then('Verify books department is selected')
def verify_books_department(contest):
    