#### Utils

###### Connect through ssh

``ssh <distro-name>@<ip-address> -i <path-to-ssh-file>``

###### Set permission to ssh file

``chmod 600 <filename>``

#### OpenStack Commands

##### Install pip library

``pip install python-openstackclient``

##### Servers

###### List Servers

``openstack server list``

###### Show server info

``openstack server show <ID/Name>``

###### Stop server

``openstack server stop <ID/Name>``

###### Start server

``openstack server start <ID/Name>``

###### Create server

``openstack server create <Name> --image <ImageId> --key-name <KeyName> --security-group <GroupName> --flavor <FlavorId>``

- --volume cannot be at the same time as --image during creation

###### Attach volume to server

``openstack server add volume <ServerName/ID> <VolumeName/ID>``

###### Attach floating ip to server

``openstack server add floating ip <ServerName/ID> <FloatingIP>``

##### Volumes

###### List Volumes

``openstack volume list``

###### Show volume info

``openstack volume show <ID/Name>``

###### Create volume

``openstack volume create <Name> --size <Size>``

##### Networks

###### List networks

``openstack network list``

##### Key Pairs

###### List keys

``openstack keypair list``

##### Floating Ip

###### List floating IPs

``openstack floating ip list``

###### Create floating IP

``openstack floating ip create <NetworkName>``





###### 4433211021902484 RADICADO MOVISTAR XD









