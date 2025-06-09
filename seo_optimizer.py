def optimize_for_seo(description, keywords):
    for keyword in keywords:
        if keyword.lower() not in description.lower():
            description += f" {keyword}"
    meta_description = description[:155]
    title_suggestion = description.split('.')[0]
    return {
        'description': description,
        'meta': meta_description,
        'title': title_suggestion
    }
