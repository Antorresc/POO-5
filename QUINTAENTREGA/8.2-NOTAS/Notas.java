package Notas;
/**
* Esta clase denominada Notas define un array de notas numéricas de tipo double.
* @version 1.2/2020
*/

public class Notas {
    double[] listaNotas; // Atributo que identifica un array de notas de tipo double

    /**
    * Constructor de la clase Notas, instancia un array con 5 notas de tipo double
    */
    public Notas() {
        listaNotas = new double[5]; // Crea un array de 5 notas
    }

    /**
    * Método que calcula el promedio de notas
    * @return El promedio de notas calculado
    */
    double calcularPromedio() {
        double suma = 0;
        for(int i = 0; i < listaNotas.length; i++) { // Se recorre el array
            suma += listaNotas[i]; // Suma las notas del array
        }
        return (suma / listaNotas.length); // Retorna el promedio
    }

    /**
    * Método que calcula la desviación estándar del array de notas
    * @return La desviación estándar del array de notas
    */
    double calcularDesviación() {
        double prom = calcularPromedio();
        double suma = 0;
        for(int i = 0; i < listaNotas.length; i++) {
            suma += Math.pow(listaNotas[i] - prom, 2);
        }
        return Math.sqrt(suma / listaNotas.length); // Retorna la desviación estándar
    }

    /**
    * Método que calcula el valor menor del array de notas
    * @return El valor menor del array de notas
    */
    double calcularMenor() {
        double menor = listaNotas[0];
        for(int i = 0; i < listaNotas.length; i++) {
            if (listaNotas[i] < menor) {
                menor = listaNotas[i];
            }
        }
        return menor;
    }

    /**
    * Método que calcula el valor mayor del array de notas
    * @return El valor mayor del array de notas
    */
    double calcularMayor() {
        double mayor = listaNotas[0];
        for(int i = 0; i < listaNotas.length; i++) {
            if (listaNotas[i] > mayor) {
                mayor = listaNotas[i];
            }
        }
        return mayor;
    }
}
