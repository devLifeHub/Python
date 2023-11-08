import copy


def site_dict(product):
    site = {
        'html': {
            'head': {
                'title': 'Куплю/продам {} недорого'.format(product)
            },
            'body': {
                'h2': 'У нас самая низкая цена на {}'.format(product),
                'div': 'Купить',
                'p': 'продать'
            }
        }
    }
    return copy.deepcopy(site)


websites = {}

num_websites = int(input("Сколько сайтов: "))

for i in range(num_websites):
    product_name = input(f"Введите название продукта для нового сайта: ")
    websites[product_name] = site_dict(product_name)
    for name, website in websites.items():
        print('Сайт для {}:'.format(name))
        print('site =', website)
