package pl.wit.projekt;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.util.HashMap;
import java.util.Map;

/**
 * 
 * Klasa kopiująca pojedynczy plik, działająca w oddzielnym wątku.
 * 
 * @author Vadym Mariiechko
 * 
 */
public class CopyFileThread extends Thread {

	// Mapa przechowująca nazwę katalogu i aktualną liczbę plików wewnątrz
	private static Map<String, Integer> mapSubFolders = new HashMap<String, Integer>();
	// Plik do kopiowania
	private File file;
	// Nazwa podkatalogu, do którego będzie skopiowany plik
	private String subFolder;
	// Ścieżka do głównego folderu
	private String rootFolder;
	// Rozszerzenie pliku
	private String extension;

	/**
	 * 
	 * Konstruktor wywołujący konstruktor z klasy bazowej oraz
	 * inicjalizujący niezbędne dane do kopiowania
	 * 
	 * @param threadName         Nazwa wątku
	 * @param file				 Plik do kopiowania
	 * @param creationDate       Data utworzenia pliku
	 * @param rootFolder         Ścieżka do głównego folderu
	 * @param extension			 Rozszerzenie pliku
	 */
	public CopyFileThread(String threadName, File file, String creationDate, String rootFolder, String extension) {
		super(threadName);
		this.file = file;
		this.subFolder = creationDate;
		this.rootFolder = rootFolder;
		this.extension = extension;
	}

	/**
	 * 
	 * Przesłonięta metoda, wykonująca kopiowanie pliku o wyznaczonej nazwie
	 * do istniejącego lub nowo utworzonego folderu
	 * 
	 */
	public void run() {
		String fileName = getFileName(subFolder);
		String folderPath = rootFolder + subFolder + "/";
		File folderFile = new File(folderPath);
		Path newFilePath = Paths.get(folderPath + fileName);
		if (!folderFile.isDirectory()) {
			folderFile.mkdir();
		}

		try {
			Files.copy(this.file.toPath(), newFilePath, StandardCopyOption.REPLACE_EXISTING);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	/**
	 * 
	 * Wyznacza nazwę pliku w podanym katalogu
	 * 
	 * @param subFolder  nazwa katalogu
	 * @return  nazwa pliku jako kolejna liczba całkowita w tym katalogu
	 */
	public String getFileName(String subFolder) {
		int filesCount = 1;
		synchronized (mapSubFolders) {
			if (mapSubFolders.containsKey(subFolder)) {
				filesCount = mapSubFolders.get(subFolder) + 1;
			}
			mapSubFolders.put(subFolder, Integer.valueOf(filesCount));
		}
		return String.valueOf(filesCount) + extension;
	}
}
