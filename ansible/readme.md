# Working with Ansible

YAML uses simple key-value pair to represent the data. The dictionary is represented in key: value pair.

`--- #Optional YAML start syntax` 
`james:` 
`   name: james john` 
`   rollNo: 34` 
`   div: B` 
`   sex: male` 
`… #Optional YAML end syntax`


## Some common words related to Ansible.

    Service/Server − A process on the machine that provides the service.

    Machine − A physical server, vm(virtual machine) or a container.

    Target machine − A machine we are about to configure with Ansible.

    Task − An action(run this, delete that) etc managed by Ansible.

    Playbook − The yml file where Ansible commands are written and yml is executed on a machine.

Ad hoc commands are commands which can be run individually to perform quick functions. These commands need not be performed later.

For example, you have to reboot all your company servers. For this, you will run the Adhoc commands from ‘/usr/bin/ansible’.

These ad-hoc commands are not used for configuration management and deployment, because these commands are of one time usage.

ansible-playbook is used for configuration management and deployment.

Sample playbook file

`---` 
`   name: install and configure DB`
`   hosts: testServer`
`   become: yes`

`   vars:`
`      oracle_db_port_value : 1521`
   
`   tasks:`
`   -name: Install the Oracle DB`
`      yum: <code to install the DB>`
    
`   -name: Ensure the installed service is enabled and running`
`   service:`
`      name: <your service name>`

