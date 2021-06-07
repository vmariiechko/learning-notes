package pl.wit.projekt;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.attribute.BasicFileAttributes;
import java.text.SimpleDateFormat;
import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

/**
 * 
 * Klasa główna wykonująca porządkowanie plików.
 * 
 * @author Vadym Mariiechko
 * 
 */
public class PhotoOrganizer {

	// Egzekutor do kontroli puli wątków o ustalonej wielkości
	private static ExecutorService es;
	// Rozszerzenie plików zdjęciowych
	private String extension;
	// Ścieżka do katalogu źródłowego
	private String sourceFolder;
	// Ścieżka do katalogu docelowego
	private String destinationFolder;

	/**
	 * 
	 * Konstruktor, inicjalizuje katalogi oraz tworzy pulę wątków
	 * 
	 * @param sourceFolder       katalogu źródłowy
	 * @param destinationFolder  katalogu docelowy
	 * @param threadsPoolCount   liczba wątków w puli
	 */
	public PhotoOrganizer(String extension, String sourceFolder, String destinationFolder, int threadsPoolCount) {
		this.extension = extension;
		this.sourceFolder = sourceFolder;
		this.destinationFolder = destinationFolder;
		es = Executors.newFixedThreadPool(threadsPoolCount);
	}

	/**
	 * 
	 * Główna metoda zarządzająca porządkowaniem plików
	 * 
	 * Wykonuje działanie w 4 krokach:
	 * 1. Parsuje katalogi
	 * 2. Zbiera wszystkie pliki zdjęciowe
	 * 3. Zbiera daty utworzenia plików
	 * 4. Kopiuje poszczególne pliki zdjęć w oddzielnym wątku
	 * 
	 * @throws FileNotFoundException  jeżeli podane katalogi nie istnieją (podczas parsowania)
	 * @throws PhotoException         jeżeli w katalogu źródłowym nie ma plików o ustalonym rozszerzeniu
	 */
	public void organizePhotos() throws FileNotFoundException, PhotoException {
		System.out.println("Analizuję podane katalogi...");
		
		// 1. Parsujemy katalogi
		parseFolders();
		// 2. Zbieramy wszystkie pliki zdjęciowe
		File[] files = getFilesByExtension();

		System.out.println("Znaleziono plików: " + files.length);
		System.out.println("Zbieram wszystkie daty tworzenia plików...");
		
		// 3. Zbieramy daty utworzenia plików
		Map<File, String> filesCreationTime = getFilesCreationTime(files);

		System.out.println("Zebrałem wszystkie daty tworzenia plików");
		System.out.println("Zaczynam uporządkowane...");
		
		// 4. Kopiujemy poszczególne pliki zdjęć w oddzielnym wątku
		int i = 1;
		for (File file : filesCreationTime.keySet()) {
			String threadName = "Thread" + i;
			es.execute(new CopyFileThread(threadName, file, filesCreationTime.get(file), destinationFolder, extension));
		}
		es.shutdown();
		try {
			es.awaitTermination(1, TimeUnit.MINUTES);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}

		System.out.println("Sukces! Pliki zostały uporządkowane.");
	}
	
	/**
	 * 
	 * Sprawdza, czy podane ścieżki są katalogami
	 * 
	 * @throws FileNotFoundException  jeżeli podane ścieżki nie są katalogami
	 */
	public void parseFolders() throws FileNotFoundException {
		File sourceDir = new File(sourceFolder);
		File destinationDir = new File(destinationFolder);
		if (!sourceDir.isDirectory()) {
			throw new FileNotFoundException("Nie znaleziono katalogu źródłowego! Spróbuj ponownie");
		}
		if (!destinationDir.isDirectory()) {
			throw new FileNotFoundException("Nie znaleziono katalogu docelowego! Spróbuj ponownie");
		}
		destinationFolder += destinationFolder.endsWith("/") ? "" : "/";
	}

	/**
	 * 
	 * Wyszukuje wszystkie pliki o ustalonym rozszerzeniu w katalogu docelowym
	 * 
	 * @return macierz znalezionych plików
	 * @throws PhotoException  jeżeli w katalogu źródłowym nie znaleziono pliki o ustalonym rozszerzeniu
	 */
	public File[] getFilesByExtension() throws PhotoException {
		File file = new File(sourceFolder);
		File[] filesArray = file.listFiles(new OrganizerFilenameFilter(extension));
		if (filesArray.length == 0) throw new PhotoException("Nie znaleziono plików z rozszerzeniem " + extension 
				+ "! Upewnij się, że podany katalog źródłowy zawiera pliki o tym rozszerzeniu!");
		return filesArray;
	}
	
	/**
	 * 
	 * Wyszukuje daty tworzenia podanych plików.
	 * 
	 * @param files  macierz plików
	 * @return mapa, kluczem jest plik, a wartością data utworzenia pliku
	 */
	public Map<File, String> getFilesCreationTime(File[] files) {
		Map<File, String> filesCreationTime = new HashMap<File, String>();
		SimpleDateFormat sdf = new SimpleDateFormat("MM.dd.yyyy");
		for (File file : files) {
			try {
				Path filePath = Paths.get(file.getPath());
				BasicFileAttributes fileAttributes = Files.readAttributes(filePath, BasicFileAttributes.class);
				String fileCreationTime = sdf.format(fileAttributes.creationTime().toMillis());
				filesCreationTime.put(file, fileCreationTime);
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
		return filesCreationTime;
	}
}
