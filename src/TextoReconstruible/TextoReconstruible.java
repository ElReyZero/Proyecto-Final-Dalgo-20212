package TextoReconstruible;

import java.util.ArrayList;
import java.util.LinkedList;

@SuppressWarnings("unchecked")
public class TextoReconstruible 
{
    static public class Grafo
    {
        int vertices;
        LinkedList<Node>[] listaAdyacencia;
        ArrayList<String> cadenas;
        /**
         * Constructor del grafo
         * @param vertices Cantidad de vertices del grafo
         * @param listaAdyacencia Es la lista que contiene los nodos del grafo
         */
        public Grafo(int vertices, ArrayList<String> cadenas)
        {
            this.vertices = vertices;
            listaAdyacencia = (LinkedList<Node>[]) new LinkedList<?>[vertices];
            for(int i = 0; i < vertices; i++)
            {
                listaAdyacencia[i] = new LinkedList<Node>();
            }
            this.cadenas = cadenas;
        }

        public void agregarArco(int numNodo1, int numNodo2, int peso)
        {
            this.listaAdyacencia[numNodo1].add(new Node(numNodo1, peso));
            this.listaAdyacencia[numNodo2].add(new Node(numNodo2, peso));
        }
    }

    static public class Node
    {
        int numNodo;
        int peso;
        /**
         * Constructor de un nodo
         * @param numNodo Valor del nodo
         * @param peso Peso del arco entre el nodo y el nodo raiz dado por su posicion en la lista del grafo
         */
        public Node(int numNodo, int peso) 
        {
            this.numNodo= numNodo;
            this.peso = peso;
        }
    }

    static int overlapInt(String str1, String str2)
    {
        int max = 0;
        int len1 = str1.length();
        int len2 = str2.length();
 
        for (int i = 1; i <= Math.min(len1, len2); i++)
        {
            if (str1.substring(len1 - i).compareTo(str2.substring(0, i)) == 0)
            {
                if (max < i)
                {
                    max = i;
                }
            }
        }
        for (int i = 1; i <= Math.min(len1, len2); i++)
        {
            if (str1.substring(0, i).compareTo(str2.substring(len2 - i)) == 0)
            {
                if (max < i)
                {
                    max = i;
                }
            }
        }
        return max;
    }

    static String overlapStr(String str1, String str2)
    {
        int max = 0;
        int len1 = str1.length();
        int len2 = str2.length();
        String res ="";
        for (int i = 1; i <= Math.min(len1, len2); i++)
        {
            if (str1.substring(len1 - i).compareTo(str2.substring(0, i)) == 0)
            {
                if (max < i)
                {
                    max = i;
                    res = str1 + str2.substring(i);
                }
            }
        }
        for (int i = 1; i <= Math.min(len1, len2); i++)
        {
            if (str1.substring(0, i).compareTo(str2.substring(len2 - i)) == 0)
            {
                if (max < i)
                {
                    max = i;
                    res = str2 + str1.substring(i);
                }
            }
        }
        return res;
    }
    
    public static void main(String[] args)
    {
        System.out.println(overlapInt("caaab", "aba"));
        System.out.println(overlapStr("caaab", "aba"));
    }
}
