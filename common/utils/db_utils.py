def get_many_to_many_fields(model):
    return [
        field.name for field in model._meta.get_fields()
        if field.many_to_many and not field.auto_created
    ]
