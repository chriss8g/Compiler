# Hitos

## SuperHito 1: Expresiones

print(5)
print(PI + E)
print(sin(PI / 2))
print(3 + 4.5 * 10)
print((3 + 4) * 10.5)
print(true && false || true)
print(3.0 >= 2)
print("Hello" @ " World!")
print(log(100, 10))
print(rand())
print(3.14 + 2.71)
print(5 == 5)
print(10 != 20)
print(sqrt(4))
print(exp(1))
print(4 / 2.0)
print(10 - 5)
print(true)
print(false)
print(sin(PI) + cos(E))

### hito 1.1

- `print(<string> @ 42)`
- `rand()` devuelve numero random entre 0 y 1

### hito 1.2

- `sin(<angle>)` devuelve el seno de un angulo en radianes
- `cos(<angle>)` devuelve el coseno de un angulo en radianes

### hito 1.3

- `sqrt(<value>)`
- `exp(<value>)`
- `log(<base>, <value>)`

### hito 1.4

- `PI` constante
- `E` constante
- Bloques de código entre paréntesis, ese bloque puede o no terminar en `;` o no, pero las expresiones en su interior si tienen que estar delimitadas por `;`

```py
{
    print(42);
    print(sin(PI/2));
}
```

## SuperHito 2: Funciones

### hito 2.1

- Funciones inline

```js
function tan(x) => sin(x)/cos(x);
```

### hito 2.1

- Funciones de toda la vida

```js
function operate(x,y) {
    print(x+y);
    print(x-y);
    print(x*y);
    print(x/y);
}
```

## SuperHito 3: Variables

### hito 3.1

- Inferencia de tipo

```js
let a = 5;
let b = "msg";
```

- Reconocer donde quiera que se use la variable su valor
- Reconocer variables no creadas

Nota: `let` retorna el valor de la variable que acompaña

```js
print(let a = 5);
```

### hito 3.2

- Implementar multivariables en una linea

```js
let n = 3, text = "msg";
```

### hito 3.3

- `in` se usa para llamar funciones que usan variables creadas en la misma linea

Las siguientes 3 expresiones son equivalentes

```js
let n = 3, text = "msg" in
    print(text @ number)
```

```js
let n = 42 in 
    let text = "msg" in
        print(text @ number);
```

```js
let n = 42 in (
    let text = "msg" in (
        print(text @ number)
    )
);
```

También `in` puede usar bloques de expresión

```js
let a = 5, b = 10, c = 1 in {
    print(a);
    print(b);
    print(c);
}
```

### hito 3.4

- Los nuevos contextos pueden redefinir variables del contexto padre

```js
let a = 5 in {
    let a = 20 in print(a);
    print(a);
}
```

- Resignación

```js
let a = 0 in {
    print(a);
    a := 1;
    print(a);
}
```

## SuperHito 4: Condicionales

### hito 4.1

$$
...
$$
