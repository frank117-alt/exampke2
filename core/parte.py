  def get(self, request, *args, **kwargs):
        products = Product.objects.filter(user=self.request.user)
        context={
            'products':products
        }
        return render(request, 'pages/products/user_productlist.html', context)



 if request.user.is_authenticated:
            products = Product.objects.filter(user=self.request.user)

            context={
            'products':products}
            return render(request, 'pages/products/user_productlist.html', context)

           


         else:

            return HttpResponse("no esta autentificvacion")
     



juan

Prueba_23


##este
def get(self, request, *args, **kwargs):

            products = Product.objects.filter(user=self.request.user)
            context={
                'products':products
            }
            return render(request, 'pages/products/user_productlist.html', context)


            