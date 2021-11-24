from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from market.models import MarketPostCategory, SellerMarketPost
from market.forms import SellerMarketPostForm
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from datetime import datetime, date, time


# Create your views here.



# CREATE FUNCTION
@login_required
def marketCreate(request):
    form = SellerMarketPostForm()   

    context = {
        'form': form,
        'pageTitle': 'BLOGPOSTFORM'
    }

    if request.method == 'POST':
        form = SellerMarketPostForm(request.POST, request.FILES)
        if form.is_valid():
            savedForm = form.save(commit=False)
            savedForm.seller = request.user
            savedForm.save()
            messages.success(request, f'Post succssfully created by {request.user}')
            return redirect('market:detail', savedForm.slug)

    return render(request, 'market/market_create.html', context)








# DETAILVIEW - CLASS BASED VIEW FOR DISPLAYING INDIVIDUAL POST
class MarketDetailView(DetailView):
    model = SellerMarketPost
    context_object_name = 'object'
    template_name = 'market/market_detail.html'


    # CONTEXT FOR THE CLASS BASED VIEW
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pageTitle'] = 'HOME'

        context['similar_phones_objects'] = SellerMarketPost.objects.filter(sellcategory__category__iexact='Phones & Tablets').order_by('-date_posted')

        context['similar_electronics_objects'] = SellerMarketPost.objects.filter(sellcategory__category__iexact='Electronics').order_by('-date_posted')

        context['similar_vehicles_objects'] = SellerMarketPost.objects.filter(sellcategory__category__iexact='Vehicles').order_by('-date_posted')

        context['similar_fashion_objects'] = SellerMarketPost.objects.filter(sellcategory__category__iexact='Fashion').order_by('-date_posted')

        context['similar_baby_products_objects'] = SellerMarketPost.objects.filter(sellcategory__category__iexact='Baby Products').order_by('-date_posted')

        context['similar_others_objects'] = SellerMarketPost.objects.filter(sellcategory__category__iexact='Others').order_by('-date_posted')

        return context









# UPDATEVIEW - CLASS BASED VIEW FOR UPDATING POST
class MarketUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = SellerMarketPost
    context_object_name = 'form'
    template_name = 'market/market_update.html'
    fields = ['sellcategory',
            'title',
            'description',
            'date_posted',
            'telephone_number',
            'price',
            'picture1',
            'picture2',
            'picture3',
            'picture4',
            'picture5']



    # VALIDATE THE FORM AND CREATE A FORM INSTANCE
    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)


    # MAKES SURE IT IS THE PERSON WHO CREATED THE POST THAT HAS RIGHT TO UPDATE IT
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.seller:
            return True
        else:
            return False









# DELETEVIEW - CLASS-BASE VIEW FOR DELETING A POST
class MarketDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = SellerMarketPost
    context_object_name = 'post'
    template_name = 'market/market_delete.html'


    # MAKES SURE IT IS THE PERSON WHO CREATED THE POST THAT HAS RIGHT TO DELETE IT
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.seller:
            return True
        else:
            return False


    # CREATE A SUCCESS_URL FOR THE CLASS BASED VIEW
    def get_success_url(self):
        return reverse('market:market_home')









# LISTVIEW - CLASS BASED VIEW FOR LISTING ALL POSTS
class MarketListView(ListView):
    model = SellerMarketPost
    context_object_name = 'objects'
    ordering = ['-date_posted']
    template_name = 'market/market_home.html'
    paginate_by = 4


    # CONTEXT FOR THE CLASS BASED VIEW
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pageTitle'] = 'HOME'
        context['planet'] = 'NIGERIA'
        # context['second_row_posts'] = SellerMarketPost.objects.all().order_by('-date_posted')[4:8]
        # context['third_row_posts'] = SellerMarketPost.objects.all().order_by('-date_posted')[8:12]
        return context









# LISTVIEW - USER POST - CLASS BASED VIEW FOR LISTING ALL POSTS MADE BY EACH USER
class MarketSellerListView(ListView):
    model = SellerMarketPost
    template_name = 'market/market_user_post.html'
    context_object_name = 'posts'
    paginate_by = 5


    # DEFINE A FILTER FOR THE CLASS BASED VIEW
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return SellerMarketPost.objects.filter(seller__exact=user).order_by('-date_posted')






# SEARCH FUNCTION
def searchView(request):
    return render(request, 'market/market_search.html')





# SEARCH RESULT FUNCTION
def searchResultView(request):
    lookup_word = request.GET.get('search')

    # CONDITION: IF THE LENGTH OF THE LOOKUP_WORD IS GREATER THAN ONE
    if len(lookup_word)>=3:
        objects = SellerMarketPost.objects.filter(title__icontains=lookup_word) | SellerMarketPost.objects.filter(description__icontains=lookup_word)
        num_of_objects = objects.count()
        time = datetime.today().strftime('%I:' '%M ' '%p')

        context = {
            'objects': objects,
            'num_of_posts': num_of_objects,
            'time': time
        }

        # CONDITION: IF THE POSTS RESULT IS TRUE I.E. CONTAINS THE LOOKUP_WORD
        if objects:
            return render(request, 'market/market_search_result.html', context)
        else:
            messages.error(request, 'Nothing was found!')
            return redirect('market:market_search')

    # CONDITION: IF THE LENGTH OF THE LOOKUP_WORD IS LESSER THAN ONE

    messages.error(request, 'Search keyword length not enough!')
    return redirect('market:market_search')










# LISTVIEW - CLASS BASED VIEW FOR LISTING ALL VEHICLE PAGE POSTS
class marketCategoryVehicleView(ListView):
    model = SellerMarketPost
    context_object_name = 'objects'
    ordering = ['-date_posted']
    template_name = 'market/market_category_vehicles.html'
    paginate_by = 4



    # QUERYSET FUNCTION TO OVERWRITE THE "context_object_name"
    def get_queryset(self):
        # user = get_object_or_404(User, username=self.kwargs.get('username'))
        return SellerMarketPost.objects.filter(sellcategory__category__iexact='vehicles').order_by('-date_posted')


    # CONTEXT FUNCTION FOR context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pageTitle'] = 'HOME'
        return context









# LISTVIEW - CLASS BASED VIEW FOR LISTING ALL MOBILE PHONES PAGE POSTS
class marketCategoryPhoneView(ListView):
    model = SellerMarketPost
    context_object_name = 'objects'
    ordering = ['-date_posted']
    template_name = 'market/market_category_phones.html'
    paginate_by = 4



    # QUERYSET FUNCTION TO OVERWRITE THE "context_object_name"
    def get_queryset(self):
        # user = get_object_or_404(User, username=self.kwargs.get('username'))
        return SellerMarketPost.objects.filter(sellcategory__category__iexact='Phones & Tablets').order_by('-date_posted')


    # CONTEXT FUNCTION FOR context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pageTitle'] = 'HOME'
        return context









# LISTVIEW - CLASS BASED VIEW FOR LISTING ALL ELECTRONICS PAGE POSTS
class marketCategoryElectronicsView(ListView):
    model = SellerMarketPost
    context_object_name = 'objects'
    ordering = ['-date_posted']
    template_name = 'market/market_category_electronics.html'
    paginate_by = 4



    # QUERYSET FUNCTION TO OVERWRITE THE "context_object_name"
    def get_queryset(self):
        # user = get_object_or_404(User, username=self.kwargs.get('username'))
        return SellerMarketPost.objects.filter(sellcategory__category__iexact='Electronics').order_by('-date_posted')


    # CONTEXT FUNCTION FOR context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pageTitle'] = 'HOME'
        return context






# LISTVIEW - CLASS BASED VIEW FOR LISTING ALL FASHION PAGE POSTS
class marketCategoryFashionView(ListView):
    model = SellerMarketPost
    context_object_name = 'objects'
    ordering = ['-date_posted']
    template_name = 'market/market_category_fashion.html'
    paginate_by = 4



    # QUERYSET FUNCTION TO OVERWRITE THE "context_object_name"
    def get_queryset(self):
        # user = get_object_or_404(User, username=self.kwargs.get('username'))
        return SellerMarketPost.objects.filter(sellcategory__category__iexact='Fashion').order_by('-date_posted')


    # CONTEXT FUNCTION FOR context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pageTitle'] = 'HOME'
        return context





# LISTVIEW - CLASS BASED VIEW FOR LISTING ALL BABY PRODUCTS PAGE POSTS
class marketCategoryBabyProductsView(ListView):
    model = SellerMarketPost
    context_object_name = 'objects'
    ordering = ['-date_posted']
    template_name = 'market/market_category_baby_products.html'
    paginate_by = 4



    # QUERYSET FUNCTION TO OVERWRITE THE "context_object_name"
    def get_queryset(self):
        # user = get_object_or_404(User, username=self.kwargs.get('username'))
        return SellerMarketPost.objects.filter(sellcategory__category__iexact='Baby Products').order_by('-date_posted')


    # CONTEXT FUNCTION FOR context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pageTitle'] = 'HOME'
        return context






# LISTVIEW - CLASS BASED VIEW FOR LISTING ALL OTHERS PAGE POSTS
class marketCategoryOthersView(ListView):
    model = SellerMarketPost
    context_object_name = 'objects'
    ordering = ['-date_posted']
    template_name = 'market/market_category_others.html'
    paginate_by = 4



    # QUERYSET FUNCTION TO OVERWRITE THE "context_object_name"
    def get_queryset(self):
        # user = get_object_or_404(User, username=self.kwargs.get('username'))
        return SellerMarketPost.objects.filter(sellcategory__category__iexact='others').order_by('-date_posted')


    # CONTEXT FUNCTION FOR context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pageTitle'] = 'HOME'
        return context