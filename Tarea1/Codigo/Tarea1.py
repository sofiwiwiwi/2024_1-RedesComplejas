{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import networkx as nx\n",
    "from networkx.algorithms.community import label_propagation_communities\n",
    "import networkx.algorithms.community as nx_comm"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Leo una red en formato pajek\n",
    "G = nx.read_pajek(\"lemis.net\")\n",
    "# Se supone que todos los archivos los dejé no-dirigidos, pero por si acaso...\n",
    "G = G.to_undirected()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Obtengo su descomposición en comunidades con un algoritmo\n",
    "c = list(label_propagation_communities(G))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.49800713860797136"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Evalúo la modularidad de esa partición en comunidades\n",
    "nx_comm.modularity(G, c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Genero otra red, con la misma distribución de grados\n",
    "G1 = nx.configuration_model([d for v, d in G.degree()])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.007804265608531154"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Particiono en comunidades y evalúo, para esa nueva red\n",
    "c1 = list(label_propagation_communities(G1))\n",
    "nx_comm.modularity(G1,c1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [],
   "source": [
    "# obtengo la lista de nodos de la componente conexa más grande\n",
    "giant = max(nx.connected_components(G), key=len)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [],
   "source": [
    "# obtengo el subgrafo consistente SOLO en la componente gigante\n",
    "S = G.subgraph(max(nx.connected_components(G), key=len)).copy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [],
   "source": [
    "# A veces hay aristas repetidas y networkx lee el archivo como\n",
    "# \"multigrafo\", para el cual no funciona k-cores. Así que genero\n",
    "# acá una copia simplificada.\n",
    "Gsimp = nx.Graph()\n",
    "for u,v,data in G.edges(data=True):\n",
    "    if not Gsimp.has_edge(u,v):\n",
    "        Gsimp.add_edge(u, v)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "31"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# veo el tamaño del 7-core\n",
    "len(nx.k_core(Gsimp,7))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-0.16522513442236963"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Calculo el coeficiente de correlación de Pearson\n",
    "nx.degree_pearson_correlation_coefﬁcient(G)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.2082919841758084"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Calculo el coeficiente de correlación, pero sólo para el 7-core\n",
    "nx.degree_pearson_correlation_coefﬁcient(nx.k_core(Gsimp,7))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Grabo el grafo simplificado en formato Pajek\n",
    "nx.write_pajek(Gsimp, \"Gsimp.net\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Grabo sólo el 7-core\n",
    "nx.write_pajek(nx.k_core(Gsimp,7), \"7core.net\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}