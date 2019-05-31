# Handles item-edit actions
from django.http import HttpResponse

# Handles item routing
class ItemHandler:
    def __init__(self):
        pass

    # For a base record, resolve the nested gridfields to a parent list
    def resolve_list(self, model, recordid, parts):
        # todo
        return None

    # renders edit item view
    def edit(self, *args, model, recordid, parts, itemid, **kwargs):
        list = self.resolve_list(model, recordid, parts)
        # todo - render edit form
        return HttpResponse("Edit view", content_type="text/plain")

    # Renders create-item view
    def create(self, *args, model, recordid, parts, **kwargs):
        list = self.resolve_list(model, recordid, parts)
        # todo - render create view
        return HttpResponse("Create view", content_type="text/plain")
