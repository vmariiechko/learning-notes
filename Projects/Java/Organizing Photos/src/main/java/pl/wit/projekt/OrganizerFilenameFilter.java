package pl.wit.projekt;

import java.io.File;
import java.io.FilenameFilter;

/**
 * 
 * Klasa służąca do filtrowania wyszukiwanych plików.
 * 
 * @author Vadym Mariiechko
 * 
 */
public class OrganizerFilenameFilter implements FilenameFilter {

	// Rozszerzenie plików
	private String extension;

	/**
	 * Konstruktor, inicjalizuje rozszerzenie
	 * 
	 * @param extention  rozszerzenie plików
	 */
	public OrganizerFilenameFilter(String extention) {
		this.extension = extention;
	}

	/**
	 * 
	 * Akceptuje pliki o ustalonym rozszerzeniu
	 * 
	 */
	@Override
	public boolean accept(File dir, String name) {
		return name.endsWith(extension);
	}
}
