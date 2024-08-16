from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import ContactForm
from .models import Contact


class ContactListView(ListView):
    model = Contact
    template_name = "contacts/contact_list.html"
    context_object_name = "contacts"
    ordering = ["first_name", "last_name"]

    def get_queryset(self):
        return Contact.objects.filter(is_deleted=False)


class ContactDetailView(DetailView):
    model = Contact
    template_name = "contacts/contact_detail.html"
    context_object_name = "contact"


class ContactCreateView(CreateView):
    model = Contact
    template_name = "contacts/contact_create_form.html"
    form_class = ContactForm
    success_url = reverse_lazy("contacts:contact-list")


class ContactUpdateView(UpdateView):
    model = Contact
    template_name = "contacts/contact_update_form.html"
    form_class = ContactForm
    success_url = reverse_lazy("contacts:contact-list")


class ContactDeleteView(DeleteView):
    model = Contact
    template_name = "contacts/contact_confirm_delete.html"
    success_url = reverse_lazy("contacts:contact-list")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return super().delete(request, *args, **kwargs)
