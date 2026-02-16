
from scraper.elpais_scraper import ElPaisScraper
from scraper.translator import TitleTranslator
from scraper.text_analyzer import TextAnalyzer

from dotenv import load_dotenv
load_dotenv()

def main():

    scraper = ElPaisScraper()
    translator = TitleTranslator()
    analyzer = TextAnalyzer()

    scraper.open_opinions_section()
    links= scraper.get_first_five_article_links()
    translated_headers = []

    for i, link in enumerate(links):

        title, content, image_url = scraper.extract_article_details(link)

        if not title or title.strip() == "":
            print("Skipping article with empty title.")
            continue

        print("\n ORIGINAL TITLE :")
        print(title)

        print("\n CONTENT :")
        print(content[:500])

        if image_url:
            scraper.download_image_from_url(image_url, i)

        translated = translator.translate_to_english(title)

        if translated:
            translated_headers.append(translated)
            print("\n TRANSLATED TITLE :")
            print(translated)
        else:
            print("\n TRANSLATED TITLE : None (Skipped)")

    repeated_words = analyzer.find_repeated_words(translated_headers)

    print("\n REPEATED WORDS (>2 times) : ")
    print(repeated_words)

    try:
        scraper.driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", '
            '"arguments": {"status":"passed","reason": "Scraping and translation completed successfully"}}'
        )
    except:
        pass

    scraper.driver.quit()

if __name__ == "__main__":
    main()