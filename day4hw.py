workshop_participants = ['web development', 'data science', 'ui/ux design']
webdev_participant= ['john', 'alice', 'sam']
datasci_participant= ['mike', 'linda', 'lia']
uiux_participant= ['sara', 'tom', 'tina']
all_participants= [webdev_participant , datasci_participant , uiux_participant]
print( all_participants)

webdev_participant.append('jane')
print(webdev_participant)

datasci_participant.insert(2, 'harry')
print(datasci_participant)

uiux_participant.remove('tina')
print(uiux_participant)

datasci_participant2 = datasci_participant.copy()
print(datasci_participant2)

datasci_participant.clear()
print(datasci_participant)

print(webdev_participant[0:2])

length = [len(name) for name in datasci_participant2]
print(length)

if 'asha' in all_participants:
    print("Asha is participating in the workshop.")
else:
    print("Asha is not participating in the workshop.")

first_participant = (webdev_participant[0], datasci_participant2[0:1], uiux_participant[0])
print(first_participant)