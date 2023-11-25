from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from books.forms import BookForm, BookUpdateForm
from books.models import Book


# Create your views here.
class BookCreateView(LoginRequiredMixin, CreateView):
    template_name = 'book/create_book.html'
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('home')


class BookListView(LoginRequiredMixin, ListView):
    template_name = 'book/list_of_books.html'
    model = Book
    context_object_name = 'all_books'


class BookUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'book/update_book.html'
    model = Book
    form_class = BookUpdateForm
    success_url = reverse_lazy('list-of-books')


class BookDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'book/delete_book.html'
    model = Book
    success_url = reverse_lazy('list-of-books')


class BookDetailView(LoginRequiredMixin, DetailView):
    template_name = 'book/details_book.html'
    model = Book
