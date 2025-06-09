def get_template(category):
    templates = {
        "electronics": (
            "Introducing {product_name}, equipped with {features}. "
            "Experience {benefits}. Why choose this? {usp}. "
            "Technical Details:\n{specs}"
        ),
        "fashion": (
            "Stay stylish with {product_name}. Key features include {features}. "
            "Benefits you'll love: {benefits}. Unique because {usp}. "
            "Product Specs:\n{specs}"
        )
    }
    return templates.get(category, templates["electronics"])
