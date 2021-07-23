

@when('Move mouse over flag icon')
def hover_flag_icon(context):
    context.app.header.hover_flag_icon()


@then('Spanish language selection is visible')
def verify_spanish_lang_present(context):
    pass