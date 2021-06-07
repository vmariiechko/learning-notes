package pl.wit.projekt;

import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;


/**
 * 
 * Klasa pobierająca dane od użytkownika, zatem tworzy obiekt klasy 
 * PhotoOrganizer oraz wywołuje na nim metodę organizePhotos().
 * 
 * @author Vadym Mariiechko
 * 
 */
public class App
{
	/**
	 * 
	 * Metoda do uruchomienia projektu
	 * 
	 */
    public static void main( String[] args ) {
    	// Skaner do pobierania danych od użytkownika
    	Scanner scanner = new Scanner(System.in);
    	Set<String> extensions = new HashSet<String>(Arrays.asList(".jpg", ".png", ".bmp", ".gif", ".tif")) ;
    	
    	// Pobieramy od użytkownika katalog źródłowy
        System.out.println("Wpisz ścieżkę do katalogu źródłowego:");
        System.out.println("Na przykład: ./src/test/resources/images/");
        String sourceFolder = scanner.nextLine();
        
    	// Pobieramy od użytkownika katalog docelowy
        System.out.println("Wpisz ścieżkę do katalogu docelowego:");
        System.out.println("Na przykład: ./src/test/resources/sorted/");
        String destinationFolder = scanner.nextLine();
        
    	// Pobieramy od użytkownika liczbę wątków oraz walidujemy, aby to była liczba całkowita z zakresu <1, 32>
        System.out.println("Podaj liczbę wątków w puli: ");
        int threadsPoolCount = -1;
        while(true) {
        	String input = scanner.nextLine();
        	try {
        		threadsPoolCount = Integer.parseInt(input);
        		if(threadsPoolCount < 1 || threadsPoolCount > 32) {
            		System.out.println("Niepoprawna liczba wątków, musi to być "
            				+ "mała liczba z zakresu <1,32>.\nWpisz ją ponownie:");
            	}else {
            		break;
            	}
        	}catch(NumberFormatException e) {
        		System.out.println("Wprowadzone dane są nieprawidłowe, musi to być całkowita liczba!");
        	}
        }
        
        System.out.println("Podaj rozszerzenie pliku: ");
        String extension = scanner.nextLine();
        if (!extensions.contains(extension)) {
    		System.out.println("Podałeś nieznane rozszerzenie zdjęć. Dostępne są: " 
    				+ extensions.toString()+ "\nSpróbuj ponownie");
            scanner.close();
    		return;
        }
        scanner.close();

        // Wykonujemy porządkowanie plików zdjęciowych
    	try {
			new PhotoOrganizer(extension, sourceFolder, destinationFolder, threadsPoolCount).organizePhotos();
		} catch (FileNotFoundException e) {
			System.out.println(e.getMessage());
		} catch (PhotoException e) {
			System.out.println(e.getMessage());
		};
    }
}
