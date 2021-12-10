import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.ListIterator;
import java.util.Queue;

/**
 * Autores:
 * Juan Andrés Romero Colmenares - 202013449
 * Luccas Rojas - 201923052
 */

@SuppressWarnings("unchecked")
public class GrafoBC {
    
        /** 
     * @param args
     */
    public static void main(String[] args)
    {
        try 
        (
            InputStreamReader is = new InputStreamReader(System.in);
            BufferedReader br = new BufferedReader(is);
        )
        {
            Grafo g;
            String line = br.readLine();
            while(line!=null && line.length()>0 && !"0".equals(line))
            {
                ArrayList<Integer> diferencias = new ArrayList<>();
                int numGrafos = Integer.parseInt(line);
                line = br.readLine();
                for (int i =0; i< numGrafos; i++)
                {
                    final String[] dataStr = line.split(" ");
                    g = new Grafo(Integer.parseInt(dataStr[0]), Integer.parseInt(dataStr[1]));
                    for(int p = 2; p<dataStr.length; p+=2) 
                    {
                        g.agregarArco(Integer.parseInt(dataStr[p]), Integer.parseInt(dataStr[p+1]));
                    }
                    if(!g.listaAdyacencia[0].isEmpty())
                    {
                        ArrayList<Integer>[] res = isBipartite(g, g.listaAdyacencia[0].get(0));
                        if (res == null)
                        {
                            diferencias.add(0);
                        }
                        else
                        {
                            diferencias.add(Math.abs(res[0].size()-res[1].size()));
                        }
                    }
                    else
                    {
                        diferencias.add(1);
                    }
                    line = br.readLine();
                }
                int respuesta = subConjuntoMinimoPD(diferencias);
                System.out.println(respuesta);
            }         
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }
    }


    static public class Grafo
    {
        int vertices;
        int pesoTotal;
        int arcos;
        LinkedList<Node>[] listaAdyacencia;

        /**
         * Constructor del grafo
         * @param vertices Cantidad de vertices del grafo
         * @param listaAdyacencia Es la lista que contiene los nodos del grafo
         */
        public Grafo(int vertices, int arcos)
        {
            this.vertices = vertices;
            this.arcos = arcos;
            listaAdyacencia = (LinkedList<Node>[]) new LinkedList<?>[vertices];
            for(int i = 0; i < vertices; i++)
            {
                listaAdyacencia[i] = new LinkedList<Node>();
            }
        }

        /**
         * Metodo para agregar un nodo y un arco al grafo
         * Se necesita el valor del nodo a agregar, el valor del nodo anterior y el peso del arco entre ellos
         * @param nodoRaizAnterior Valor del nodo anterior
         * @param numNodo Valor del nodo a insertar
         * @param peso Peso del arco entre ambos nodos
         */
        public void agregarArco(int nodoRaizAnterior, int numNodo)
        {
            this.listaAdyacencia[nodoRaizAnterior].add(new Node(numNodo));
            this.listaAdyacencia[numNodo].add(new Node(nodoRaizAnterior));
        }
    }

    static public class Node
    {
        int numNodo;
        String color;
        /**
         * Constructor de un nodo
         * @param numNodo Valor del nodo
         * @param peso Peso del arco entre el nodo y el nodo raiz dado por su posicion en la lista del grafo
         */
        public Node(int numNodo) 
        {
            this.numNodo= numNodo;
        }

        public void setColor(String color)
        {
            this.color= color;
        }
    }

    
    /** 
     * @param g Grafo a analizar
     * @param inicio nodo de inicio del algoritmo
     * @return ArrayList<Integer>[]
     */
    public static ArrayList<Integer>[] isBipartite(Grafo g, Node inicio)
    {
        ArrayList<Integer>[] resultado = (ArrayList<Integer>[]) new ArrayList<?>[2];
        Queue<Node> q = new LinkedList<Node>();
        ArrayList<Integer> blancos = new ArrayList<Integer>();
        ArrayList<Integer> negros = new ArrayList<Integer>();
        Node[] descubiertos = new Node[g.vertices]; 
        Node vActual;
        Node vSiguiente;
        LinkedList<Node> p;

        if (g.vertices==1)
        {
            blancos.add(inicio.numNodo);
            resultado[0] = blancos;
            resultado[1] = negros;
            return resultado;
        }
        q.add(inicio);
        descubiertos[inicio.numNodo] = inicio;
        blancos.add(inicio.numNodo);
        inicio.setColor("BLANCO");
        while(!q.isEmpty())
        {
            vActual = q.poll();
            p = g.listaAdyacencia[vActual.numNodo];
            ListIterator<Node> it = p.listIterator();
            while(it.hasNext())
            {
                vSiguiente = it.next();
                if(descubiertos[vSiguiente.numNodo] == null)
                {
                    if(vActual.color.equals("BLANCO"))
                    {
                        negros.add(vSiguiente.numNodo);
                        vSiguiente.setColor("NEGRO");
                    }
                    else
                    {
                        blancos.add(vSiguiente.numNodo);
                        vSiguiente.setColor("BLANCO");
                    } 
                    descubiertos[vSiguiente.numNodo] = vSiguiente;
                    q.add(vSiguiente);
                }
                else if(descubiertos[vSiguiente.numNodo].color.equals(vActual.color))
                {
                    return null;
                }
            }
        }
        resultado[0] = blancos;
        resultado[1] = negros;
        return resultado;
    }

    public static int subConjuntoMinimoPD(ArrayList<Integer> lista)
    {
        //TODO Mirar si la lista es 0
        int total_sum = listSum(lista);
        int n = lista.size();

        boolean[][] matriz = new boolean[n+1][(Math.floorDiv(total_sum, 2)+1)];

        for (int i = 0; i<matriz.length; i++)
        {
            matriz[i][0] = true;
        }

        for (int i = 1; i<matriz.length; i++)
        {
            for(int j = 1; j<matriz[0].length; j++)
            {
                if (lista.get(i-1) <= j)
                {
                    matriz[i][j] = (matriz[i-1][j-(lista.get(i-1))] || matriz[i-1][j]);
                }
                else
                {
                    matriz[i][j] = matriz[i-1][j];
                }
            }
        }

        int minimo = Integer.MAX_VALUE;
        for (int j = total_sum / 2; j >= 0; j--) {
            if (matriz[n][j] == true) {
                minimo = total_sum - 2 * j;
                return minimo;
            }
        }
        return -1;
    }

    public static int listSum(ArrayList<Integer> lista)
    {  
        int suma = 0;
        for (int i :lista)
        {
            suma+= i;
        }
        return suma;
    }
}
