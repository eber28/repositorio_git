#Las tuplas en Python son inmutables, lo que significa que una vez creada una tupla, sus elementos no pueden cambiar. Las tuplas no pueden ser alteradas. No puedes añadir, reemplazar, reasignar o eliminar ningún elemento ya que las tuplas no pueden cambiar su configuración.
>ejemplo:
```pythom
lista = [1, 2, 3]
tupla = tuple(lista)
print(type(tupla)) #<class 'tuple'>
print(tupla)       #(1, 2, 3)
```