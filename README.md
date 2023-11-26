# AnalizadorSintacticoDescendenteRecursivoSQL


__Este es el repositorio de:__


- Muñoz Tapia Alan Arath

- Reyes López Maximiliano

- Santos Alan Eduardo

1. Q → **select** D **from** T
2. D → **distinct** P | P
3. P → * | A
4. A → A<sub>2</sub> A<sub>1</sub>
5. A<sub>1</sub> → __,__ A | Ɛ
6. A<sub>2</sub> → __id__ A<sub>3</sub>
7. A<sub>3</sub> → __.__ __id__ | Ɛ
8. T → T<sub>2</sub> T<sub>1</sub>
9. T<sub>1</sub> → __,__ T | Ɛ
10. T<sub>2</sub> → __id__ T<sub>3</sub>
11. T<sub>3</sub> → __id__ | Ɛ

__Analizar un archivo de texto__

- Para ejecutar `python3 main.py nombre_archivo.txt`

__Analizar texto directamente desde la terminal__

- Para ejecutar `python3 main.py`, ahora solo hay que usar la terminal para introducir las cadenas que se desean analizar. Para salir hay que usar la combinación `ctrl + C`