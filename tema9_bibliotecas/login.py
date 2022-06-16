import logging

#MUESTRA MENSAJES LOG. SE ESTABLECE EL ORDEN CON logging.basicConfig(level=logging.xxxxx)
logging.basicConfig(level=logging.CRITICAL)
logging.info("Hace calor")
logging.warning("Hace calor")
logging.error("test")
logging.critical("adios")
