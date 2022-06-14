

class Categorias:
    idCategoria = 0
    nombre = ""

class Proveedores:
    idProveedor = 0
    nombre = 0

class Productos:
    idproducto = 0
    categoriaProducto = Categorias()
    precio = 0
    tamaño = 0
    tipoProducto = 0
    CIFPProveedor = Proveedores()

p = Productos()

#Para ver el nombre del proveedor
p.CIFPProveedor.nombre
#Para ver el Id de la categoria
p.categoriaProducto.idCategoria