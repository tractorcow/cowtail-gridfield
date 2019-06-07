from django.template.loader import render_to_string

from wagtail.admin.edit_handlers import EditHandler


class CowTailPanel(EditHandler):
    template = "cowtail/gridfield.html"
    label = None

    def __init__(self, relation_name, label='', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.relation_name = relation_name
        self.label = label

    def clone_kwargs(self):
        kwargs = super().clone_kwargs()
        kwargs.update(
            relation_name=self.relation_name,
        )
        return kwargs

    def render(self):
        return render_to_string(self.template, {
            'self': self,
        })
