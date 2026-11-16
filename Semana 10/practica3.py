from collections import deque

class Grafo:
    def __init__(self):
        self.adyacencia = {}

    def agregar_vertice(self, v):
        self.adyacencia.setdefault(v, [])

    def agregar_arista(self, a, b):
        self.agregar_vertice(a)
        self.agregar_vertice(b)
        if b not in self.adyacencia[a]:
            self.adyacencia[a].append(b)
        if a not in self.adyacencia[b]:
            self.adyacencia[b].append(a)

    def bfs(self, inicio, destino):
        cola = deque([[inicio]])
        visitados = {inicio}
        while cola:
            ruta = cola.popleft()
            actual = ruta[-1]
            if actual == destino:
                return ruta
            for vecino in self.adyacencia.get(actual, []):
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(ruta + [vecino])
        return None