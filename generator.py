import json
from seo_optimizer import optimize_for_seo
from template_system import get_template

def generate_description(product):
    template = get_template(product['category'])
    description = template.format(
        product_name=product['name'],
        features=', '.join(product['features']),
        benefits=', '.join(product['benefits']),
        usp=product['usp'],
        specs='\n'.join(f"{k}: {v}" for k, v in product['specs'].items())
    )
    seo_description = optimize_for_seo(description, product['keywords'])
    return seo_description

if __name__ == "__main__":
    # Load sample product data
    with open('sample_products.json') as f:
        products = json.load(f)

    # Generate and print description for each product
    for product in products:
        result = generate_description(product)
        print("\n--- Product Title ---")
        print(result['title'])
        print("\n--- Meta Description ---")
        print(result['meta'])
        print("\n--- Full Description ---")
        print(result['description'])
        print("\n===============================\n")
