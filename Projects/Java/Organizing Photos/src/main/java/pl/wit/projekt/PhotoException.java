package pl.wit.projekt;

/**
 * 
 * Klasa reprezentująca wyjątki związane z brakiem zdjęć
 * w ustalonym katalogu źródłowym.
 * 
 * @author Vadym Mariiechko
 * 
 */
public class PhotoException extends Exception {

	// Identyfikator wersji
	private static final long serialVersionUID = 1L;

	/**
	 * 
	 * Konstruktor jednoargumentowy
	 * 
	 * @param message  tekst wyjątku
	 */
	public PhotoException(String message) {
		super(message);
	}

	/**
	 * 
	 * Konstruktor dwuargumentowy
	 * 
	 * @param message  tekst wyjątku
	 * @param e        obiekt klasy Exeption
	 */
	public PhotoException(String message, Exception e) {
		super(message, e);
	}
}
