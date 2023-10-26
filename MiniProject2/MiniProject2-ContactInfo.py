class Contact():
    def __init__(self, name, phone_number, email_address, physical_address):
        self.name = name
        self.first_name = name.split()[0]
        self.last_name = name.split()[1]

        self.phone_number = phone_number

        self.email_address = email_address

        self.physical_address = ', '.join(physical_address.values()) # Joins the dictionary physical address into the usual address format
        self.street = physical_address['street']
        self.city = physical_address['city']
        self.state = physical_address['state']
        self.zip = physical_address['zip']

    def print_contact_info(self):
        print(f'{self.name:^48}\n{self.phone_number:^48}\n{self.email_address:^48}\n{self.physical_address:^48}\n')

    def print_phone_number(self):
        print(f'{self.name}\'s phone number is: {self.phone_number}\n')



# <<< Stored Contacts >>>
contacts = [Contact('Georgie Frank', '(292) 409-4527', 'georgiefrank@gmail.com', {'street' : '22363 Forge Lane', 'city': 'Miniappolis', 'state' : 'Washington', 'zip' : '36523'}),
            Contact('Anne Galager', '(634) 723-9573', 'annethegoat@gmail.com', {'street' : '89453 Hunted Road', 'city': 'Knottingham', 'state' : 'Minnesota', 'zip' : '67345'}),
            Contact('Calzone Italburg', '(285) 673-2848', 'cazloneyital@gmail.com', {'street' : '89453 Talian Court', 'city': 'Jersey', 'state' : 'New Jersey', 'zip' : '46238'})]

for i in range(0, 2): # Prints contact info and phone number for every contact in the the contacts list
    for contact in contacts:
        contact.print_contact_info() if i == 0 else contact.print_phone_number()
    print('------------------------------------------------------------------------------\n')



# <<< Additional Inputs >>>
input_name = input('Input name (full name for phone # and first name for physical address): ')

while input_name != 'd' and input_name != 'done' and input_name != 'Done':
    for contact in contacts:
        if input_name == contact.name: # Prints the phone number of an inputted full name
            print(f'{input_name}\'s phone number is: {contact.phone_number}\n')
            break
        elif input_name == contact.first_name: # Prints the physical address of an inputted first name
            print(f'{input_name}\'s physical address is: {contact.physical_address}\n')
            break
    else:
        print('Name not found in contacts.\n')
    input_name = input('Input name (full name for phone # and first name for physical address): ')
else:
    print('<<< Program Ended >>>')

