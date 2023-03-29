# urine_strip_app/views.py
import cv2
import numpy as np
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def identify_colors(request):
    if request.method == 'POST':
        # get the uploaded image
        file = request.FILES['image']
        image = np.asarray(bytearray(file.read()), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)

        # identify the colors on the strip
        colors = []
        for i in range(10):
            color = image[10, i*10]
            colors.append([int(c) for c in color])

        # return the results as JSON
        return JsonResponse({'colors': colors})
