import logging

logger = logging.getLogger(__name__)


def pack_backpack(hero):
    logger.info("Packing Backpack.")
    for key, value in hero.gear.items():
        if key == "Backpack":
            continue
        logger.info(f"\tPacking {key}")
