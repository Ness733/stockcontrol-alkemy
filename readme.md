## Proyecto Integrador - StockControl - Alkemy

Alumno: Nestor Rosales

Este es mi proyecto de control de stock realizado en el marco del Plan de Formación Profesional y Continua brindado por la plataforma Alkemy basado en Python y Django.

# Sección Lista de Productos

Además de listar los productos, implementé la lógica para que según la cantidad de stock, el texto se presente de la siguiente manera:

-   Verde: Stock > 30
-   Amarillo: Stock < 30
-   Rojo: Stock < 10

```
<div class="row w-100 mx-auto gap-4 mb-5">
	{% if productos|length > 0 %} {% for producto in productos %}
	<div class="col p-3 producto">
		<h2>{{producto.nombre}} - ${{producto.precio}}</h2>
		<h4 class="fw-bold">Proveedor: {{producto.proveedor}}</h4>
		<p
			class="fw-bold {%if producto.stock_actual < 10 %} text-danger {% elif producto.stock_actual <= 30 %} warning {%else%} text-success {% endif %}"
		>
			Stock actual: {{producto.stock_actual}}
		</p>
	</div>
	{% endfor %} {% else %}
	<p class="text-center">No hay productos</p>
	{% endif %}
</div>
```

![](./imagenes/lista_productos.png)

# Sección Lista de Proveedores

![](./imagenes/lista_proveedores.png)

# Sección Agregar Producto

![](./imagenes/agregar_producto.png)

# Sección Agregar Proveedor

![](./imagenes/agregar_proveedor.png)

# Sección Panel Administración para Productos

![](./imagenes/admin_productos.png)

# Sección Panel Administración para Proveedores

![](./imagenes/admin_proveedores.png)

## Funcionalidad de Login

En la rama userCreation implementé que se requiera estar logueado para acceder al sitio y poder realizar las operaciones.

![](./imagenes/login.png)
