from azure import *
from azure.servicemanagement import *

subscription_id = '064ee8c4-2285-4b74-b5da-673dfb3682f7'
certificate_path = 'C:/OpenSSL-Win64/bin/mycert.pem'

sms = ServiceManagementService(subscription_id, certificate_path)

#################################
#Create a virtual machine

name = 'kamalvm'
location = 'Central India'

#Set the location (create cloud service)
sms.create_hosted_service(service_name=name,
    label=name,
    location=location)

# Name of an os image as returned by list_os_images
image_name = '03f55de797f546a1b29d1b8d66be687a__VS-2017-Comm-WS2016-2017-04-24'
#image_name = 'https://bsetradingsqlvm.blob.core.windows.net/vhds/BseTradingSQLVM20170501100236.vhd'


# Destination storage account container/blob where the VM disk
# will be created
media_link = 'https://bsetradingsqlvm.blob.core.windows.net/vhds'

#Windows vm Configuration
windows_config = WindowsConfigurationSet(computer_name='KAMAL',admin_password='#welcome1234',reset_password_on_first_logon=None,enable_automatic_updates=None,time_zone=None,admin_username='mcuser',custom_data=None)
windows_config.domain_join = None
windows_config.win_rm = None

os_hd = OSVirtualHardDisk(image_name, media_link)

sms.create_virtual_machine_deployment(service_name=name,
    deployment_name=name,
    deployment_slot='production',
    label=name,
    role_name=name,
    system_config=windows_config,
    os_virtual_hard_disk=os_hd,
    role_size='Small')
