from azure import *
from azure.servicemanagement import *

subscription_id = '064ee8c4-2285-4b74-b5da-673dfb3682f7'
certificate_path = 'C:/OpenSSL-Win64/bin/mycert.pem'

sms = ServiceManagementService(subscription_id, certificate_path)

name = 'mycentos'
label = 'mycentos'
os = 'Windows' # Linux or Windows
#media_link = 'url_to_storage_blob_for_source_image_vhd'
#media_link = '03f55de797f546a1b29d1b8d66be687a__VS-2017-Comm-WS2016-2017-04-24'
media_link = 'https://bsetradingsqlvm.blob.core.windows.net/vhds/BseTradingSQLVM20170501100236.vhd'

result = sms.add_os_image(label, media_link, name, os)

operation_result = sms.get_operation_status(result.request_id)
print('Operation status: ' + operation_result.status)
