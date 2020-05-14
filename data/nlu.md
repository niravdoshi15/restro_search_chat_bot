## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks
- Thanks
- Yeah
- yup
- ya
- thank you
- bye

## intent:deny
- no
- no thanks
- nope
- nope thanks
- no need

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- dear sir
- hola

## intent:send_email
- [pqr@gmail.com](email)
- send it to [niravdoshi15@gmail.com](email)
- [niravdoshi15@gmail.com](email)
- [abc@gmail.com](email)
- [dinagaran.david@gmail.com](email)
- [dhinathemaximus@gmail.com](email)
- [dinagaran.david@madisonindia.com](email)

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines](cuisine:chinese) restaurants in the [New Delhi](location:Delhi)
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [294328](location)
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese](cuisine:chinese)
- [chinese](cuisine)
- [low](price)
- [med](price)
- [high](price)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- can you book a table in [rome](location) in a [moderate](price:med) price range with [british](cuisine) food for [four](people:4) people
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- [mumbai](location)
- show me restaurants
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- find me a restaurant
- in [pune](location)
- Okay. Some me in [Mumbai](location)
- in [Pune](location)
- in [Mumbai](location)
- in [mumbai](location)
- show me restaurants in [Mumbai](location)
- find me a restauarnt
- in [Rhishikesh](location)
- in [Hastinapur](location)
- find me restaurant
- in [mumbai](location:Mumbai)
- find me restauarnt
- show me restauarnt
- [Thai](cuisine)
- [American](cuisine)
- [Mexican](cuisine)
- [Chinese](cuisine)
- [bengaluru](location)
- in [Latur](location)
- [bengaluru](location:bangalore)
- Can you suggest some good restaurants in [kolkata](location:Kolkata)
- show me restauarnt in [latur](location)
- in [bengaluru](location:bangalore)
- Can you suggest some good [italian](cuisine) restaurants
- somewhere in [delhi](location)
- Im hungry. Looking out for some good [chinese](cuisine) restaurants in [chandigarh](location)
- find me [italian](cuisine) restauarnt in [latur](location)
- in [pune](location:Pune)
- find me a [chinese](cuisine) restaurant in [mumbai](location:Mumbai)
- find me a [south indian](cuisine) restaurant in [mumbai](location:Mumbai)
- find me a [chinese](cuisine) restaurant
- [hyderabad](location)
- find me a [north indian](cuisine) restaurant
- [bhopal](location)
- find me restro
- find me a [american](cuisine) restro
- [bangalore](location)
- find me a [chinese](cuisine) restaurant in [rishikesh](location)
- find me restaurant in [rishikesh](location)
- [Noida](location)
- [south indian](cuisine) restaurant in [Mumbai](location)
- hi bot, can you find me a [american](cuisine) restaurant in [ooti](location)
- find me in [mumbai](location:Mumbai)
- find me a [north indian](cuisine) restaurant in [chennai](location:Chennai)
- hi find me a good restaurant in [chennai](location:Chennai) cuisine [south indian](cuisine)
- find me [chinese](cuisine) restaurant in [latur](location)
- find me a restaurant in [delhi](location)
- [Mexican](cuisine)
- [high](price)

## synonym:4
- four

## synonym:Chennai
- chennai
- Madras
- madras

## synonym:Delhi
- New Delhi

## synonym:Kochi
- kochi
- Cochin
- cochin

## synonym:Kolkata
- kolkata
- Calcutta
- calcutta

## synonym:Mumbai
- mumbai
- Bombay
- bombay
- Bambai
- bambai
- New Mumbai

## synonym:No
- no
- nah
- nope
- na

## synonym:Pune
- pune
- Puna
- puna
- Poona
- poona

## synonym:Yes
- yeah
- yes
- ya
- yaa
- yup
- sure
- okay

## synonym:bangalore
- bengaluru
- Bengaluru

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:med
- moderate

## regex:email
- ^\\w+(\\w+)*\\@(\\w+)*\\.(\\w+)*(.(\\w+)*)?$

## regex:greet
- hey[^\s]*

## regex:pincode
- [0-9]{6}
