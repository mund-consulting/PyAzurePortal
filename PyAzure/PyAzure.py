from azure import *
from azure.servicemanagement import *

subscription_id = '064ee8c4-2285-4b74-b5da-673dfb3682f7'
certificate_path = 'C:/OpenSSL-Win64/bin/mycert.pem'

sms = ServiceManagementService(subscription_id, certificate_path)

#List available locations
result = sms.list_locations()
for location in result:
    print(location.name)

#Create a cloud service
hname = 'testkamalhostedservice'
label = 'testkamalhostedservice'
desc = 'my hosted service'
location = 'Central India'
sms.create_hosted_service(hname, label, desc, location)

#list_hosted_services
result = sms.list_hosted_services()

for hosted_service in result:
    print('Service name: ' + hosted_service.service_name)
    print('Management URL: ' + hosted_service.url)
    print('Location: ' + hosted_service.hosted_service_properties.location)
    print('')

#Delete a cloud service
sms.delete_hosted_service('testkamalhostedservice')

#Create a storage service
sname = 'testkamalstorage'
label = 'testkamalstorage'
location = 'Central India'
desc = 'My test storage account description.'

result = sms.create_storage_account(sname,desc,label,location=location)

operation_result = sms.get_operation_status(result.request_id)
print('Operation status: ' + operation_result.status)

#Delete a storage service
sms.delete_storage_account('testkamalstorage')

#List available operating systems
result = sms.list_operating_systems()
for os in result:
    print('OS: ' + os.label)
    print('Family: ' + os.family_label)
    print('Active: ' + str(os.is_active))

result = sms.list_operating_system_families()

for family in result:
    print('Family: ' + family.label)
    for os in family.operating_systems:
        if os.is_active:
            print('OS: ' + os.label)
            print('Version: ' + os.version)
    print('')
#######################################
#Create an operating system image

name = 'kamaltestimage'
label = 'kamaltestimage'
os = 'Windows' # Linux or Windows

media_link = 'https://bseresourcegroupdisks346.blob.core.windows.net/vhds/BseTrading-120170418180516.vhd'

result = sms.add_os_image(label, media_link, name, os)

operation_result = sms.get_operation_status(result.request_id)
print('Operation status: ' + operation_result.status)

result = sms.list_os_images()

for image in result:
    print('Name: ' + image.name)
    print('Label: ' + image.label)
    print('OS: ' + image.os)
    print('Category: ' + image.category)
    print('Description: ' + image.description)
    print('Location: ' + image.location)
    print('Media link: ' + image.media_link)
    print('')

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



