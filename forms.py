from django.db.models import fields
from django.db.models.fields.reverse_related import ForeignObjectRel
from django.template.loader import render_to_string
from modelcluster.fields import ChildObjectsDescriptor

from wagtail.admin.edit_handlers import EditHandler


class CowTailPanel(EditHandler):
    """
    Gridfield panel for editing a relation on a parent object
    """
    template = 'cowtail/gridfield.html'
    label = None
    db_field: ForeignObjectRel = None
    relation_list = None
    isbound = False

    # Types of fields that are good to display as summary
    # Todo - Configurable summary fields per model / gridfield
    summary_types = [
        fields.AutoField,
        fields.CharField,
        fields.DateField,
        fields.TextField,
        fields.IntegerField,
        fields.FloatField,
        fields.TimeField,
    ]

    def __init__(self, relation_name, heading='', label='', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.relation_name = relation_name
        self.heading = heading or label
        self.label = label
        self.isbound = False

    # List of field names this grid should display
    # Excludes final "actions" column
    def summary_fields(self):
        # todo Get fields from this
        for field in self.db_field.related_model._meta.fields:
            for type in self.summary_types:
                if isinstance(field, type):
                    yield field

    def clone_kwargs(self):
        kwargs = super().clone_kwargs()
        kwargs.update(
            relation_name=self.relation_name,
            heading=self.heading,
            label=self.label,
        )
        return kwargs

    def on_model_bound(self):
        manager = getattr(self.model, self.relation_name)
        self.db_field = manager.rel

    def on_instance_bound(self):
        self.relation_list = getattr(self.instance, self.relation_name)

    def bind_to(self, instance=None, **kwargs):
        if instance is not None:
            self.instance = instance
        return super(CowTailPanel, self).bind_to(instance=instance, **kwargs)

    def render(self):
        columns = self.summary_fields()

        items = []
        if self.relation_list is not None:
            items = self.relation_list.all()

        # todo - wrap items into inline panel

        # print([column for column in columns])
        # todo get items from self.instance
        return render_to_string(self.template, {
            'self': self,
            'columns': columns,
            'items': [], # items
        })


class CowTailItemPanel:
    """
    Row item representing a single item in a grid
    """
    template = 'cowtail/gridfield_item.html'

    def __init__(self, panel, item):
        self.panel = panel
        self.item = item

    def render(self):
        # todo - get parent summary fields
        return render_to_string(self.template, {
            'self': self,
        })
