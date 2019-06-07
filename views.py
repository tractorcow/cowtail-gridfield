# Handles item-edit actions

# Handles item routing
from django.utils.translation import ugettext_lazy
from wagtail.admin.forms.collections import CollectionForm
from wagtail.admin.views.generic import CreateView, EditView


class ItemView:
    parts = []


class Create(CreateView, ItemView):
    page_title = ugettext_lazy("Add item")
    form_class = CollectionForm
    template_name = 'cowtail/add.html'
    success_message = ugettext_lazy("Collection '{0}' created.")
    add_url_name = 'cowtail_gridfield:add'
    edit_url_name = 'cowtail_gridfield:edit'
    index_url_name = 'cowtail_gridfield:index'
    header_icon = 'folder-open-1'
    parts = []

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        # todo: Resolve nested model from parent model + parts + pk
        self.model = kwargs['model']
        self.parts = kwargs['parts']

    def save_instance(self):
        # Always create new collections as children of root
        # instance = self.form.save(commit=False)
        # root_collection = Collection.get_first_root_node()
        # root_collection.add_child(instance=instance)
        # return instance
        pass


class Edit(EditView, ItemView):
    form_class = CollectionForm
    template_name = 'cowtail/edit.html'
    success_message = ugettext_lazy("Collection '{0}' updated.")
    error_message = ugettext_lazy("The collection could not be saved due to errors.")
    delete_item_label = ugettext_lazy("Delete collection")
    edit_url_name = 'cowtail_gridfield:edit'
    index_url_name = 'cowtail_gridfield:index'
    delete_url_name = 'cowtail_gridfield:delete'
    context_object_name = 'collection'
    header_icon = 'folder-open-1'
    parts = []

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        # todo: Resolve nested model from parent model + parts + pk
        self.model = kwargs['model']
        self.parts = kwargs['parts']
