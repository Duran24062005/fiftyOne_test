import fiftyone as fo
import fiftyone.zoo as foz

# 1. Descarga e importa un pequeño set de datos de prueba (por ejemplo, el famoso set COCO)
dataset = foz.load_zoo_dataset("quickstart")

# 2. Lanza la aplicación web interactiva en tu navegador
session = fo.launch_app(dataset)

# 3. Bloquea la ejecución para mantener la app abierta si estás ejecutando un script
session.wait()