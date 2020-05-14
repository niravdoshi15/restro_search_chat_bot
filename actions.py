from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json
import flask

from flask_mail import Mail, Message

app = flask.Flask(__name__)
app.config.update(
	DEBUG=True,
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'username@gmail.com',
	MAIL_PASSWORD = 'password'
	)
mail = Mail(app)

display_restuarants = []

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'

	def run(self, dispatcher, tracker, domain):

		minAmount = 0
		maxAmount = 0

		def restaurants_price(minAmount, maxAmount):
			def filterPrice(x):
				if x['restaurant']['average_cost_for_two'] >= minAmount and x['restaurant']['average_cost_for_two'] <= maxAmount:
					return x
			return filterPrice

		def filterRestaurant(restaurants, price):
			if price == 'low':
				minAmount = 0
				maxAmount = 299
			elif price == 'med':
				minAmount = 300
				maxAmount = 700
			elif price == 'high':
				minAmount = 701
				maxAmount = 2000

			restaurantsByPrice = restaurants_price(minAmount, maxAmount)

			topRestaurant = list(filter(restaurantsByPrice, restaurants))
			topRestaurant.sort(key=lambda x: x['restaurant']['user_rating']['aggregate_rating'], reverse=True)
			return topRestaurant
		
		config={ "user_key":"f9214f7afc85b5231ec9e49aabdf24ac"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'american':1, 'mexican':73, 'thai':95, 'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 100)
		d = json.loads(results)
		response=""
		if d['results_found'] == 0:
			response= "no results"
		else:
			filter_amount_rating = filterRestaurant(d['restaurants'], price)
			global display_restuarants
			display_restuarants = filter_amount_rating[:10]
			count = 0
			for restaurant in display_restuarants:
				if count < 5:
					response=response + str(count+1) +") " + restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+" " + " has been rated "+restaurant['restaurant']['user_rating']['aggregate_rating']+"\n"
					count = count + 1
		
		dispatcher.utter_message(response)
		return [SlotSet('location',loc)]

class ActionIsValidCity(Action):
	def name(self):
		return 'action_isvalid_city'

	def run(self, dispatcher, tracker, domain):

		topTierCities = ["Ahmedabad","Bangalore","Chennai","Delhi","Hyderabad","Kolkata","Mumbai","Pune",
			"Agra","Ajmer","Aligarh","Allahabad","Amravati","Amritsar","Asansol","Aurangabad",
			"Bareilly","Belgaum","Bhavnagar","Bhiwandi","Bhopal","Bhubaneswar",
			"Bikaner","Bokaro Steel City","Chandigarh","Coimbatore","Cuttack","Dehradun",
			"Dhanbad","Durg-Bhilai Nagar","Durgapur","Erode","Faridabad","Firozabad","Ghaziabad",
			"Gorakhpur","Gulbarga","Guntur","Gurgaon","Guwahati",
			"Gwalior","Hubli-Dharwad","Indore","Jabalpur","Jaipur","Jalandhar","Jammu","Jamnagar","Jamshedpur","Jhansi","Jodhpur",
			"Kannur","Kanpur","Kakinada","Kochi","Kottayam","Kolhapur","Kollam","Kota","Kozhikode","Kurnool","Lucknow","Ludhiana",
			"Madurai","Malappuram","Mathura","Goa","Mangalore","Meerut",
			"Moradabad","Mysore","Nagpur","Nanded","Nashik","Nellore","Noida","Palakkad","Patna","Pondicherry","Raipur","Rajkot",
			"Rajahmundry","Ranchi","Rourkela","Salem","Sangli","Siliguri",
			"Solapur","Srinagar","Sultanpur","Surat","Thiruvananthapuram","Thrissur","Tiruchirappalli","Tirunelveli","Tiruppur",
			"Ujjain","Vijayapura","Vadodara","Varanasi",
			"Vasai-Virar City","Vijayawada","Visakhapatnam","Warangal"]

		topTierCities_list = [i.lower() for i in topTierCities]

		loc = str(tracker.get_slot('location'))
		if loc.lower() not in topTierCities_list:
			return [SlotSet('location',None), SlotSet('is_valid_city',False)]
		return [SlotSet('location',loc), SlotSet('is_valid_city',True)]

class ActionSendEmail(Action):
	def name(self):
		return 'action_send_email'
	
	def run(self, dispatcher, tracker, domain):
		with app.app_context():
			if tracker.get_slot('email'):
				email = tracker.get_slot('email')
				bodyText = ""
				i = 0
				global display_restuarants
				for restaurant in display_restuarants:
					bodyText = bodyText + str(i+1) +") " + restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+" " + " has been rated "+restaurant['restaurant']['user_rating']['aggregate_rating']+"\n"
					i=i+1
				try:
					msg = Message("Your Search on Restaurants in " +str(tracker.get_slot('location')),
					sender="example@gmail.com",
					recipients=[email])
					msg.body = "Our Top Rated Restaurants List:"+"\n" +"\n"+ bodyText +"\n" + "Happy to Help, Thank You :-) "
					mail.send(msg)
				except Exception(e):
					print("Error: "+str(e))
			display_restuarants=[]
			return [SlotSet('location',None), SlotSet('is_valid_city',None),  SlotSet('cuisine',None),  SlotSet('email',None), SlotSet('price',None)]

