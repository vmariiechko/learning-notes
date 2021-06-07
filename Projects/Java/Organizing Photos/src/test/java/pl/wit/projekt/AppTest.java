package pl.wit.projekt;

import static org.junit.Assert.*;

import java.io.File;
import java.io.FileNotFoundException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.attribute.BasicFileAttributes;
import java.text.SimpleDateFormat;
import java.util.Map;

import org.junit.BeforeClass;
import org.junit.Rule;
import org.junit.Test;
import org.junit.rules.ExpectedException;

/**
 * 
 * Klasa do testowania poprawności działania projektu.
 * W katalogu "./src/test/resources/" są umieszczone niezbędne zasoby do testowania
 * 
 * @author Vadym Mariiechko
 * @author Yevhenii Dotsiak
 * 
 */
public class AppTest {
	
	// Rozszerzenie plików zdjęciowych
	static private String extension;
	// Ścieżka do katalogu źródłowego
	static private String sourceFolder;
	// Ścieżka do katalogu docelowego
	static private String destinationFolder;
	// Liczba wątków w puli
	static int threadsPoolCount;

	// Oczekiwany wyjątek do testowania
	@Rule
	public ExpectedException exceptionRule = ExpectedException.none();
	
	/**
	 * 
	 * Inicjalizuje zmienne statyczne
	 * 
	 */
	@BeforeClass
	public static void setUpBeforeClass() throws Exception {
		extension = ".jpg";
		sourceFolder = "./src/test/resources/images/";
        destinationFolder = "./src/test/resources/sorted/";
        threadsPoolCount = 10;
	}
	
	/**
	 * 
	 * Testuje tworzenie obiektu (konstruktor) klasy PhotoOrganizer
	 * 
	 */
	@Test
	public void notNullTest() {
		PhotoOrganizer notNullOrganizer = new PhotoOrganizer(extension, sourceFolder, destinationFolder, threadsPoolCount);
		assertNotNull(notNullOrganizer);
	}
	
	/**
	 * 
	 * Testuje poprawne parsowanie katalogów dla nieistniejącego katalogu źródłowego
	 * 
	 */
	@Test()
	public void parseNotExistedSrcFolderTest() throws FileNotFoundException, PhotoException{
		exceptionRule.expect(FileNotFoundException.class);
		exceptionRule.expectMessage("Nie znaleziono katalogu źródłowego! Spróbuj ponownie");
		String srcFolderNotExist = "./src/test/resources/imgs/";
		new PhotoOrganizer(extension, srcFolderNotExist, destinationFolder, threadsPoolCount).organizePhotos();
	}
	
	/**
	 * 
	 * Testuje poprawne parsowanie katalogów dla nieistniejącego katalogu docelowego
	 * 
	 */
	@Test()
	public void parseNotExistedDstFolderTest() throws FileNotFoundException, PhotoException {
		exceptionRule.expect(FileNotFoundException.class);
		exceptionRule.expectMessage("Nie znaleziono katalogu docelowego! Spróbuj ponownie");
		String dstFolderNotExist = "./src/test/resources/srt/";
		new PhotoOrganizer(extension, sourceFolder, dstFolderNotExist, threadsPoolCount).organizePhotos();
	}
	
	/**
	 * 
	 * Testuje poprawność wyszukiwania istniejących plików
	 * 
	 */
	@Test
	public void foundFilesTest() throws FileNotFoundException, PhotoException {
		File file = new File(sourceFolder);
		File[] filesArray = file.listFiles(new OrganizerFilenameFilter(extension));
		File[] files = new PhotoOrganizer(extension, sourceFolder, destinationFolder, threadsPoolCount).getFilesByExtension();
		// Są 7 zdjęć w katalogu źródłowym
		assertEquals(filesArray.length, files.length);
	}
	
	/**
	 * 
	 * Testuje poprawność wyszukiwania plików dla pustego istniejącego katalogu
	 * 
	 */
	@Test
	public void notFoundFilesTest() throws FileNotFoundException, PhotoException {
		exceptionRule.expect(PhotoException.class);
		exceptionRule.expectMessage("Nie znaleziono plików z rozszerzeniem " + extension 
				+ "! Upewnij się, że podany katalog źródłowy zawiera pliki o tym rozszerzeniu!");
		String srcFolderNotExist = "./src/test/resources/images_empty_test/";
		new PhotoOrganizer(extension, srcFolderNotExist, destinationFolder, threadsPoolCount).organizePhotos();
	}
	
	/**
	 * 
	 * Testuje poprawność wyszukiwania daty utworzenia plików
	 * 
	 */
	@Test
	public void filesCreationTimeTest() throws Exception {
		PhotoOrganizer organizer = new PhotoOrganizer(extension, sourceFolder, destinationFolder, threadsPoolCount);
		Map<File, String> filesCreationTime = organizer.getFilesCreationTime(organizer.getFilesByExtension());
		assertNotNull(filesCreationTime);
		assertEquals(7, filesCreationTime.size(), 0);
		
		for(File file: filesCreationTime.keySet()) {
			BasicFileAttributes fileAttributes = Files.readAttributes(Paths.get(file.getPath()), BasicFileAttributes.class);
			String fileCreationTime = new SimpleDateFormat("MM.dd.yyyy").format(fileAttributes.creationTime().toMillis());
			assertEquals(fileCreationTime, filesCreationTime.get(file));
		}
	}
	
	/*
	 * Także testowanie poprawności porządkowania zdjęć było sprawdzone ręczenie,
	 * poprzez policzenie plików oraz sprawdzenie przydzielenia ich do odpowiednich katalogów.
	 * W wyniku dostaliśmy oczekiwane z założeń wyniki.
	 * 
	 */
}
