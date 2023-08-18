from django.shortcuts import render, get_object_or_404, redirect
from home.models import Product, Campaigns, Category, Descriptions
from django.http import JsonResponse, HttpResponseRedirect 
from django.urls import reverse

# Create your views here.

def index(request):
    context = {
        "campaigns" : Campaigns.objects.filter(isActive = True),
        "saleProduct" : Product.objects.filter(isSaleInMainPage=True, isActive = True),
        "populerProduct" : Product.objects.filter(isPopularInMainPage=True, isActive = True),
        "descriptions" : Descriptions.objects.all()
    }
    # Page from the theme 
    return render(request, 'pages/index.html', context)


def productlist(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    context = { 
        "products" : Product.objects.filter(category=category, isActive=True),
        "campaigns2" : Campaigns.objects.filter(isActive = True),
        "category" : category
    }
    return render(request, 'pages/productlist.html', context)

def contact(request):
    return render (request, 'pages/contact.html')

def aboutUs(request):
    return render (request, 'pages/aboutus.html')

def product(request, slug):
    productdetail = Product.objects.get(slug=slug)
    return render(request, 'pages/product.html', {
        'productdetail' : productdetail
    })

def campaignproductlist(request, campaign_slug):
    campaign = get_object_or_404(Campaigns, slug=campaign_slug)
    context = { 
        "products" : Product.objects.filter(campaign=campaign, isActive=True),
        "campaigns2" : Campaigns.objects.filter(isActive = True)
    }
    return render(request, 'pages/productlist.html', context)

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})
    cart_item = cart.get(str(product_id), {'quantity': 0})
    quantity = int(request.POST.get('quantity', 1))
    size = request.POST.get('size', '')
    cart_item['quantity'] += quantity
    cart_item['size'] = size
    cart[str(product_id)] = cart_item
    request.session['cart'] = cart
    return JsonResponse({'success': True})

def cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    for product_id, cart_item in cart.items():
        product = get_object_or_404(Product, id=int(product_id))
        cart_items.append({
            'product': product,
            'size': cart_item['size'],
            'quantity': cart_item['quantity'],
            'subtotal': cart_item['quantity'] * product.SalePrice
        })

        total_price += product.SalePrice

    # Toplam fiyat 300 TL veya daha fazlaysa 30 TL ekleyin
    if total_price >= 300:
        shipping_fee = 0
    else:
        shipping_fee = 30

    total_price += shipping_fee

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'shipping_fee': shipping_fee  # Kargo ücretini context'e ekliyoruz
    }

    return render(request, 'pages/cart.html', context)

def clear_cart(request):
    if 'cart' in request.session:
        del request.session['cart']
    return redirect('cart')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
    return HttpResponseRedirect(reverse('cart'))
