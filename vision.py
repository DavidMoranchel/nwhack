import io
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "nwhacks-515bb2a3739e.json"
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

def detect_text_uri(uri):
    """Detects text in the file located in Google Cloud Storage or on the Web.
    """
    client = vision.ImageAnnotatorClient()
    image = types.Image()
    image.source.image_uri = uri

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))

detect_text_uri('http://meteora.contad.unam.mx/escolar/licenciatura/inscripcion_nuevo/images/Instructivo3.jpg')
