from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('nosotras/', views.nosotras, name='Nosotras'),
    path('productos/', views.productos, name='Productos'), 
    path('vendedores/', views.vendedores, name='Vendedores'),
    path('pago/', views.pago, name='Pago'), 
    path('pagoApi/', views.pagoapi), 
    path('productosApi/', views.productosapi),
    path('vendedoresApi/', views.vendedoresapi),
    path('busquedaCategoria/', views.buscarcategoria, name='buscar'),
    path('buscar/', views.buscar),
    path('leerVendedores/', views.leer_vendedores), 
    path('crearVendedores/', views.crear_vendedores),
    path('editarVendedores/', views.editar_vendedores),
    path('eliminarVendedores/', views.eliminar_vendedores),
    path('vendedores/list/', views.vendedoresList.as_view(),name='List'),
    path('vendedores/create/', views.vendedoresCreate.as_view(),name='New'),
    path('vendedores/edit/<pk>', views.vendedoresEdit.as_view(),name='Edit'),
    path('vendedores/detail/<pk>', views.vendedoresDetail.as_view(),name='Detail'),
    path('vendedores/delete/<pk>', views.vendedoresDelete.as_view(),name='Delete'),
    path('leerProductos/', views.leer_productos),
    path('crearProductos/', views.crear_productos),
    path('editarProductos/', views.editar_productos),
    path('eliminarProductos/', views.eliminar_productos),
    path('productos/list/', views.productosList.as_view(),name='Productos'),
    path('productos/create/', views.productosCreate.as_view(),name='NewProductos'),
    path('productos/edit/<pk>', views.productosEdit.as_view(),name='EditProductos'),
    path('productos/detail/<pk>', views.productosDetail.as_view(),name='DetailProductos'),
    path('productos/delete/<pk>', views.productosDelete.as_view(),name='DeleteProductos'),
    
]
