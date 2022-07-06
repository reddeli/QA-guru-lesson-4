def open_browser(browser_name):
    pass


def go_to_companyname_homepage(page_url):
    pass


def find_registration_button_on_login_page(page_url, button_text):
    pass


def print_functions_and_args(func):
    name = func.__name__.replace("_", " ")
    arguments_name = func.__code__.co_varnames

    if len(arguments_name) == 0:
        arguments = 'Аргументы отсутствуют'
    else:
        arguments = f'Аргументы: {", ".join(arguments_name)}'

    print(f'Имя функции {name}. {arguments}')


functions_all = (open_browser, go_to_companyname_homepage, find_registration_button_on_login_page)
for i in functions_all:
    print_functions_and_args(i)