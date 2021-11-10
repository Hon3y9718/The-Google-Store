from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from mainApp.models import ProductData
from userAuth.models import CartData, UserOrders, UserAddress

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    products = ProductData.objects.all()
    vars = {'products': products}
    return render(request, 'home.html', vars)

def productPage(request):
    addedToCart = request.GET.get('addToCart', 'False')
    if addedToCart == 'True':
        messages.success(request, "Added to Cart!")
    id = request.GET.get('productId', '0')
    id = int(id)
    product = ProductData.objects.filter(id=id)
    MRP = str(int(product[0].price) + 99)
    stars = []
    for i in range(0, int(product[0].rating)):
        stars.append("*")

    allProducts = ProductData.objects.all()
    vars = {'products': product, 'MRP': MRP, 'rating': stars, 'allProducts': allProducts}
    return render(request, 'productPage.html', vars)

def CartPage(request):
    userId = request.user.id
    cartItems = CartData.objects.filter(userId=userId)
    listOfProducts = []
    if cartItems.count() < 1:
        messages.error(request, "Your cart is Empty!")
    else:
        allProducts = ProductData.objects.all()
        totalAmount = 0
        for i in range(0,cartItems.count()):
            product = allProducts.filter(id=cartItems[i].productId)
            listOfProducts.append({
                'name': product[0].Name,
                'price': product[0].price,
                'img': product[0].Img,
                'quantity': cartItems[i].quantity,
                'id': cartItems[i].id,
            })           
            totalAmount += float(product[0].price)
            

    vars = {'cartItems': listOfProducts, 'totalItems': cartItems.count(), 'amount': totalAmount}
    return render(request, 'cart.html', vars)

def addToCart(request):
    current_user = request.user
    productId = request.GET.get('productId')
    productName = request.GET.get('productName')
    cart = CartData(productId=productId, quantity=1, productName=productName, userId=current_user.id)
    cart.save()
    return redirect(f'/productPage?addToCart=True&productId={productId}')

def deleteFromCart(request):
    id = request.GET.get('productId')
    productInCart = CartData.objects.filter(id=id)
    productInCart.delete()
    return redirect('/cart')

def buyNow(request):
    userId = request.user.id
    addressId = request.GET.get('address')
    productId = request.GET.get('productId')
    productName = request.GET.get('productName')
    cart = request.GET.get('cart')
    address = UserAddress.objects.filter(id=addressId)
    if address.count() > 0:
        if cart == 'True':
            cartItems = CartData.objects.filter(userId=request.user.id)
            for item in cartItems:
                buyOrder = UserOrders(productId=item.productId, quantity=item.quantity, productName=item.productName, addressId=addressId, userId=userId)
                buyOrder.save()
        else:
            buyOrder = UserOrders(productId=productId, productName=productName, quantity=1, addressId=addressId, userId=userId)
            buyOrder.save()
        return render(request, 'bought.html')
    return redirect('/')

def AddAddress(request):
    productId = request.GET.get('productId')
    productName = request.GET.get('productName')
    cart = request.GET.get('cart')

    if request.method == "POST":
        Name = request.POST.get('name')
        Mobile = request.POST.get('mobile')
        HouseNo = request.POST.get('HouseNo')
        Street = request.POST.get('Street')
        Locality = request.POST.get('Locality')
        State = request.POST.get('State')
        Zip = request.POST.get('Zip')
        AddressType = request.POST.get('Address_Type')

        address = UserAddress(name=Name, mobileNumber=Mobile, pin=Zip, locality=Locality, Address=HouseNo+ ' ' + Street, state=State, Address_Type=AddressType, userId=request.user.id)
        address.save()

        if cart == True:
            return redirect(f'/buy?address={address.id}&cart={cart}')

        return redirect(f'/buy?address={address.id}&productId={productId}&productName={productName}&cart={cart}')
    
    allAddress = UserAddress.objects.filter(userId = request.user.id)

    vars = {'allAddress': allAddress, 'productId': productId, 'productName': productName, 'cart': cart}

    return render(request, 'address.html', vars)