from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes
import json, os
from django.conf import settings
from django.utils.translation import activate, gettext_lazy as _
from contextlib import closing


@api_view(['POST'])
def files_storage(request):
    # if request.method == "GET":
    #     data = request.GET
    # else:
    #     data = json.loads(request.body or "{}")
    user = request.user
    files = []
    if os.getenv('DEVELOPMENT_MODE') == "dev":
        for file_key, file in request.FILES.items():
            with closing(file):
                name = file.name
                mime_type = file.content_type
                import pdb;pdb.set_trace()
                # file_key = gd_storage.save(file.name, file)  # The save method return a key for the file
                # url = gd_storage.url(file_key)  # The url method return the url for the stored file
                files.append({
                    'url': "",
                    'name': name,
                    'content_type': mime_type
                })
    elif os.getenv('DEVELOPMENT_MODE') == "prod":
        return JsonResponse({
            'error': _("Storage is not yet configured for production."),
        }, 400)
    return JsonResponse({
        'success': True,
        'files': files,
    })

