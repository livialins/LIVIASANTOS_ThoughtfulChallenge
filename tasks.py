from robocorp.tasks import task
# from robocorp import workitems
from RPA.Robocorp.WorkItems import WorkItems
from automation.search_latimes import NewsSearcher
from automation.scrapping_latimes import ScrapeNews
from automation.save_data import SaveData
from src.challenge import AppController


@task
def run_process():
    
    app_controller = AppController()
    app_controller.initialize()
    logger = app_controller.logger

    workitems = WorkItems()
    workitems.get_input_work_item()
    payload = workitems.get_work_item_payload()

    try:
        # payload = app_controller.validator.validate_payload(payload)
        logger.info(f"Item payload: {payload}")

        search_news = NewsSearcher(app_controller, payload)
        scrape_news_instance = ScrapeNews(app_controller, payload)
        save_data = SaveData(app_controller)

        search_news.execute_news_search()
        data = scrape_news_instance.scrape_news()
        save_data.create_excel_file(data, payload["search_phrase"])

        logger.info(f"Scrape of phrase '{payload['search_phrase']}' finished.")

    except Exception as e:
        logger.error(f"Error scraping fresh news: {(e)}")
        # raise Exception(e)

    app_controller.end_process()
    logger.info("Finishing process: Scrape Fresh News...")
