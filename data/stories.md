## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_isvalid_city
    - slot{"location": "Mumbai"}
    - slot{"is_valid_city": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_avg_price
* restaurant_search{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_1_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_isvalid_city
    - slot{"location": "Mumbai"}
    - slot{"is_valid_city": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_avg_price
* restaurant_search{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_ask_email_permission
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_isvalid_city
    - slot{"location": "Mumbai"}
    - slot{"is_valid_city": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_avg_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_ask_email_permission
* deny
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_noemail_sent
* affirm
    - utter_goodbye

## interactive_story_3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rhishikesh"}
    - slot{"location": "Rhishikesh"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_isvalid_city
    - slot{"location": "Mumbai"}
    - slot{"is_valid_city": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_avg_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_3_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rhishikesh"}
    - slot{"location": "Rhishikesh"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_isvalid_city
    - slot{"location": "Mumbai"}
    - slot{"is_valid_city": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_avg_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_ask_email_permission
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rhishikesh"}
    - slot{"location": "Rhishikesh"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_isvalid_city
    - slot{"location": "Mumbai"}
    - slot{"is_valid_city": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_avg_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_ask_email_permission
* deny
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_noemail_sent
* affirm
    - utter_goodbye

## interactive_story_5
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rhishikesh"}
    - slot{"location": "Rhishikesh"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Latur"}
    - slot{"location": "Latur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_isvalid_city
    - slot{"location": "bangalore"}
    - slot{"is_valid_city": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_avg_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_5_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rhishikesh"}
    - slot{"location": "Rhishikesh"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Latur"}
    - slot{"location": "Latur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_isvalid_city
    - slot{"location": "bangalore"}
    - slot{"is_valid_city": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_avg_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_ask_email_permission
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_6
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rhishikesh"}
    - slot{"location": "Rhishikesh"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Latur"}
    - slot{"location": "Latur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_isvalid_city
    - slot{"location": "bangalore"}
    - slot{"is_valid_city": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_avg_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_ask_email_permission
* deny
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_noemail_sent
* affirm
    - utter_goodbye

## interactive_story_7
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rhishikesh"}
    - slot{"location": "Rhishikesh"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Latur"}
    - slot{"location": "Latur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Hastinapur"}
    - slot{"location": "Hastinapur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_isvalid_city
    - slot{"location": "bangalore"}
    - slot{"is_valid_city": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_avg_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_7_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rhishikesh"}
    - slot{"location": "Rhishikesh"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Latur"}
    - slot{"location": "Latur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Hastinapur"}
    - slot{"location": "Hastinapur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_isvalid_city
    - slot{"location": "bangalore"}
    - slot{"is_valid_city": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_avg_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_ask_email_permission
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_8
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rhishikesh"}
    - slot{"location": "Rhishikesh"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Latur"}
    - slot{"location": "Latur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Hastinapur"}
    - slot{"location": "Hastinapur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_isvalid_city
    - slot{"location": "bangalore"}
    - slot{"is_valid_city": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_avg_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_ask_email_permission
* deny
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_noemail_sent
* affirm
    - utter_goodbye

## interactive_story_9
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_isvalid_city
    - slot{"location": "Kolkata"}
    - slot{"is_valid_city": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_avg_price
* restaurant_search{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_9_1
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_isvalid_city
    - slot{"location": "Kolkata"}
    - slot{"is_valid_city": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_avg_price
* restaurant_search{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_10
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_isvalid_city
    - slot{"location": "Kolkata"}
    - slot{"is_valid_city": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_avg_price
* restaurant_search{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - utter_ask_email_permission
* deny
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_noemail_sent
* affirm
    - utter_goodbye

## interactive_story_11
* greet
    - utter_greet
* restaurant_search{"location": "latur"}
    - slot{"location": "latur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_isvalid_city
    - slot{"location": "bangalore"}
    - slot{"is_valid_city": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_avg_price
* restaurant_search{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_11_1
* greet
    - utter_greet
* restaurant_search{"location": "latur"}
    - slot{"location": "latur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_isvalid_city
    - slot{"location": "bangalore"}
    - slot{"is_valid_city": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_avg_price
* restaurant_search{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_email_permission
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_12
* greet
    - utter_greet
* restaurant_search{"location": "latur"}
    - slot{"location": "latur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_isvalid_city
    - slot{"location": "bangalore"}
    - slot{"is_valid_city": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_avg_price
* restaurant_search{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_email_permission
* deny
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_noemail_sent
* affirm
    - utter_goodbye

## interactive_story_13
* greet
    - utter_greet
* restaurant_search{"location": "latur"}
    - slot{"location": "latur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Rhishikesh"}
    - slot{"location": "Rhishikesh"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_isvalid_city
    - slot{"location": "bangalore"}
    - slot{"is_valid_city": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_avg_price
* restaurant_search{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_13_1
* greet
    - utter_greet
* restaurant_search{"location": "latur"}
    - slot{"location": "latur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Rhishikesh"}
    - slot{"location": "Rhishikesh"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_isvalid_city
    - slot{"location": "bangalore"}
    - slot{"is_valid_city": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_avg_price
* restaurant_search{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_email_permission
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_14
* greet
    - utter_greet
* restaurant_search{"location": "latur"}
    - slot{"location": "latur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Rhishikesh"}
    - slot{"location": "Rhishikesh"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_isvalid_city
    - slot{"location": "bangalore"}
    - slot{"is_valid_city": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_avg_price
* restaurant_search{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_email_permission
* deny
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_noemail_sent
* affirm
    - utter_goodbye




## interactive_story_15
* greet
    - utter_greet
* restaurant_search{"location": "latur"}
    - slot{"location": "latur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Hastinapur"}
    - slot{"location": "Hastinapur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Rhishikesh"}
    - slot{"location": "Rhishikesh"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_isvalid_city
    - slot{"location": "bangalore"}
    - slot{"is_valid_city": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_avg_price
* restaurant_search{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_15_1
* greet
    - utter_greet
* restaurant_search{"location": "latur"}
    - slot{"location": "latur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Hastinapur"}
    - slot{"location": "Hastinapur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Rhishikesh"}
    - slot{"location": "Rhishikesh"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_isvalid_city
    - slot{"location": "bangalore"}
    - slot{"is_valid_city": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_avg_price
* restaurant_search{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_16
* greet
    - utter_greet
* restaurant_search{"location": "latur"}
    - slot{"location": "latur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Hastinapur"}
    - slot{"location": "Hastinapur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Rhishikesh"}
    - slot{"location": "Rhishikesh"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_isvalid_city
    - slot{"location": "bangalore"}
    - slot{"is_valid_city": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_avg_price
* restaurant_search{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_email_permission
* deny
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_noemail_sent
* affirm
    - utter_goodbye


## interactive_story_17
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_isvalid_city
    - slot{"location": "delhi"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_17_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_isvalid_city
    - slot{"location": "delhi"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email_permission
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_18
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_isvalid_city
    - slot{"location": "delhi"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email_permission
* deny
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_noemail_sent
* affirm
    - utter_goodbye

## interactive_story_19
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "latur"}
    - slot{"location": "latur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_isvalid_city
    - slot{"location": "delhi"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_19_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "latur"}
    - slot{"location": "latur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_isvalid_city
    - slot{"location": "delhi"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email_permission
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_20
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "latur"}
    - slot{"location": "latur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_isvalid_city
    - slot{"location": "delhi"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email_permission
* deny
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_noemail_sent
* affirm
    - utter_goodbye

## interactive_story_21
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "latur"}
    - slot{"location": "latur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Hastinapur"}
    - slot{"location": "Hastinapur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_isvalid_city
    - slot{"location": "delhi"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_21_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "latur"}
    - slot{"location": "latur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Hastinapur"}
    - slot{"location": "Hastinapur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_isvalid_city
    - slot{"location": "delhi"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email_permission
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_22
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "latur"}
    - slot{"location": "latur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Hastinapur"}
    - slot{"location": "Hastinapur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_isvalid_city
    - slot{"location": "delhi"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email_permission
* deny
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_noemail_sent
* affirm
    - utter_goodbye

## interactive_story_23
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "latur"}
    - slot{"location": "latur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Hastinapur"}
    - slot{"location": "Hastinapur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Rhishikesh"}
    - slot{"location": "Rhishikesh"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_isvalid_city
    - slot{"location": "delhi"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_23_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "latur"}
    - slot{"location": "latur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Hastinapur"}
    - slot{"location": "Hastinapur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Rhishikesh"}
    - slot{"location": "Rhishikesh"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_isvalid_city
    - slot{"location": "delhi"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_24
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "latur"}
    - slot{"location": "latur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Hastinapur"}
    - slot{"location": "Hastinapur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Rhishikesh"}
    - slot{"location": "Rhishikesh"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_isvalid_city
    - slot{"location": "delhi"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email_permission
* deny
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_noemail_sent
* affirm
    - utter_goodbye

## interactive_story_25
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_isvalid_city
    - slot{"location": "chandigarh"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - slot{"location": "chandigarh"}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_25_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_isvalid_city
    - slot{"location": "chandigarh"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - slot{"location": "chandigarh"}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_26
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_isvalid_city
    - slot{"location": "chandigarh"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - slot{"location": "chandigarh"}
    - utter_ask_email_permission
* deny
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_noemail_sent
* affirm
    - utter_goodbye

## interactive_story_27
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "latur"}
    - slot{"cuisine": "italian"}
    - slot{"location": "latur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_isvalid_city
    - slot{"location": "Pune"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_27
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "latur"}
    - slot{"cuisine": "italian"}
    - slot{"location": "latur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_isvalid_city
    - slot{"location": "Pune"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - utter_ask_email_permission
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_28
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "latur"}
    - slot{"cuisine": "italian"}
    - slot{"location": "latur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_isvalid_city
    - slot{"location": "Pune"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - utter_ask_email_permission
* deny
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_noemail_sent
* affirm
    - utter_goodbye

## interactive_story_29
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "latur"}
    - slot{"cuisine": "italian"}
    - slot{"location": "latur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Hastinapur"}
    - slot{"location": "Hastinapur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_isvalid_city
    - slot{"location": "Pune"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_29_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "latur"}
    - slot{"cuisine": "italian"}
    - slot{"location": "latur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Hastinapur"}
    - slot{"location": "Hastinapur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_isvalid_city
    - slot{"location": "Pune"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - utter_ask_email_permission
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_30
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "latur"}
    - slot{"cuisine": "italian"}
    - slot{"location": "latur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Hastinapur"}
    - slot{"location": "Hastinapur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_isvalid_city
    - slot{"location": "Pune"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - utter_ask_email_permission
* deny
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_noemail_sent
* affirm
    - utter_goodbye

## interactive_story_31
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "latur"}
    - slot{"cuisine": "italian"}
    - slot{"location": "latur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Hastinapur"}
    - slot{"location": "Hastinapur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Rhishikesh"}
    - slot{"location": "Rhishikesh"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_isvalid_city
    - slot{"location": "Pune"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_31_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "latur"}
    - slot{"cuisine": "italian"}
    - slot{"location": "latur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Hastinapur"}
    - slot{"location": "Hastinapur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Rhishikesh"}
    - slot{"location": "Rhishikesh"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_isvalid_city
    - slot{"location": "Pune"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - utter_ask_email_permission
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_32
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "latur"}
    - slot{"cuisine": "italian"}
    - slot{"location": "latur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Hastinapur"}
    - slot{"location": "Hastinapur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Rhishikesh"}
    - slot{"location": "Rhishikesh"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_isvalid_city
    - slot{"location": "Pune"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - utter_ask_email_permission
* deny
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_noemail_sent
* affirm
    - utter_goodbye


## interactive_story_33
* restaurant_search{"cuisine": "south indian", "location": "Mumbai"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "Mumbai"}
    - action_isvalid_city
    - slot{"location": "Mumbai"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_ask_email_permission
* deny
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_noemail_sent
* affirm
    - utter_goodbye


## interactive_story_34
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - action_isvalid_city
    - slot{"location": "hyderabad"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "hyderabad"}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_34_1
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - action_isvalid_city
    - slot{"location": "hyderabad"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "hyderabad"}
    - utter_ask_email_permission
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_35
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_location
* restaurant_search{"location": "bhopal"}
    - slot{"location": "bhopal"}
    - action_isvalid_city
    - slot{"location": "bhopal"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "bhopal"}
    - utter_ask_email_permission
* deny
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_noemail_sent
* affirm
    - utter_goodbye


## interactive_story_36
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_isvalid_city
    - slot{"location": "delhi"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email_permission
* deny
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_noemail_sent

## interactive_story_37
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_isvalid_city
    - slot{"location": "bangalore"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_email_permission
* deny
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_noemail_sent
* affirm
    - utter_goodbye


## interactive_story_38
* restaurant_search{"cuisine": "chinese", "location": "rishikesh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "rishikesh"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_ask_avg_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}

## interactive_story_39
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Noida"}
    - slot{"location": "Noida"}
    - action_isvalid_city
    - slot{"location": "Noida"}
    - slot{"is_valid_city": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_avg_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "Noida"}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_39_1
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Noida"}
    - slot{"location": "Noida"}
    - action_isvalid_city
    - slot{"location": "Noida"}
    - slot{"is_valid_city": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_avg_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "Noida"}
    - utter_ask_email_permission
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_40
* restaurant_search{"cuisine": "south indian", "location": "Mumbai"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "Mumbai"}
    - action_isvalid_city
    - slot{"location": "Mumbai"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_ask_email_permission
* deny
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_noemail_sent
* affirm
    - utter_goodbye


## interactive_story_41
* restaurant_search{"cuisine": "american", "location": "ooti"}
    - slot{"cuisine": "american"}
    - slot{"location": "ooti"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_ask_avg_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
* greet
    - utter_greet
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_isvalid_city
    - slot{"location": "Mumbai"}
    - slot{"is_valid_city": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_avg_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_ask_email_permission
* deny
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_noemail_sent
* affirm
    - utter_goodbye


## interactive_story_42
* restaurant_search{"cuisine": "north indian", "location": "Chennai"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "Chennai"}
    - action_isvalid_city
    - slot{"location": "Chennai"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "Chennai"}
    - utter_ask_email_permission
* deny
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_noemail_sent
* affirm
    - utter_goodbye

## interactive_story_43
* restaurant_search{"location": "Chennai", "cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "Chennai"}
    - action_isvalid_city
    - slot{"location": "Chennai"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"location": "Chennai"}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_43_1
* restaurant_search{"location": "Chennai", "cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "Chennai"}
    - action_isvalid_city
    - slot{"location": "Chennai"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"location": "Chennai"}
    - utter_ask_email_permission
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye


## interactive_story_44
* restaurant_search{"cuisine": "south indian", "location": "Mumbai"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "Mumbai"}
    - action_isvalid_city
    - slot{"location": "Mumbai"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_44_1
* restaurant_search{"cuisine": "south indian", "location": "Mumbai"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "Mumbai"}
    - action_isvalid_city
    - slot{"location": "Mumbai"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_ask_email_permission
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_45
* restaurant_search{"cuisine": "south indian", "location": "Latur"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "Latur"}
    - action_isvalid_city
    - slot{"location": "null"}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_isvalid_city
    - slot{"location": "Pune"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_ask_email_permission
* deny
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_noemail_sent
* affirm
    - utter_goodbye

## interactive_story_46
* restaurant_search{"cuisine": "south indian", "location": "Latur"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "Latur"}
    - action_isvalid_city
    - slot{"location": "null"}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_isvalid_city
    - slot{"location": "Pune"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_46_1
* restaurant_search{"cuisine": "south indian", "location": "Latur"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "Latur"}
    - action_isvalid_city
    - slot{"location": "null"}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_isvalid_city
    - slot{"location": "Pune"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_47
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Latur"}
    - slot{"location": "Latur"}
    - action_isvalid_city
    - slot{"location": "null"}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_isvalid_city
    - slot{"location": "Pune"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "hyderabad"}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_47_1
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Latur"}
    - slot{"location": "Latur"}
    - action_isvalid_city
    - slot{"location": "null"}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_isvalid_city
    - slot{"location": "Pune"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "hyderabad"}
    - utter_ask_email_permission
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_48
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Latur"}
    - slot{"location": "Latur"}
    - action_isvalid_city
    - slot{"location": "null"}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_isvalid_city
    - slot{"location": "Pune"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "hyderabad"}
    - utter_ask_email_permission
* deny
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_noemail_sent
* affirm
    - utter_goodbye

## interactive_story_49
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_location
* restaurant_search{"location": "Latur"}
    - slot{"location": "Latur"}
    - action_isvalid_city
    - slot{"location": "null"}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "bhopal"}
    - slot{"location": "bhopal"}
    - action_isvalid_city
    - slot{"location": "bhopal"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "bhopal"}
    - utter_ask_email_permission
* deny
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_noemail_sent
* affirm
    - utter_goodbye

## interactive_story_50
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_location
* restaurant_search{"location": "Latur"}
    - slot{"location": "Latur"}
    - action_isvalid_city
    - slot{"location": "null"}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "bhopal"}
    - slot{"location": "bhopal"}
    - action_isvalid_city
    - slot{"location": "bhopal"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "bhopal"}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_50_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_location
* restaurant_search{"location": "Latur"}
    - slot{"location": "Latur"}
    - action_isvalid_city
    - slot{"location": "null"}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "bhopal"}
    - slot{"location": "bhopal"}
    - action_isvalid_city
    - slot{"location": "bhopal"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "bhopal"}
    - utter_ask_email_permission
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_51
* restaurant_search{"cuisine": "south indian", "location": "Latur"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "Latur"}
    - action_isvalid_city
    - slot{"location": "null"}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_isvalid_city
    - slot{"location": "Pune"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - utter_ask_email_permission
* deny
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_noemail_sent
* affirm
    - utter_goodbye

## interactive_story_52
* restaurant_search{"cuisine": "south indian", "location": "Latur"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "Latur"}
    - action_isvalid_city
    - slot{"location": "null"}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_isvalid_city
    - slot{"location": "Pune"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_52_1
* restaurant_search{"cuisine": "south indian", "location": "Latur"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "Latur"}
    - action_isvalid_city
    - slot{"location": "null"}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_isvalid_city
    - slot{"location": "Pune"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - utter_ask_email_permission
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye
## interactive_story_53
* restaurant_search{"cuisine": "chinese", "location": "latur"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "latur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_isvalid_city
    - slot{"location": "Mumbai"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_53_1
* restaurant_search{"cuisine": "chinese", "location": "latur"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "latur"}
    - action_isvalid_city
    - slot{"location": null}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_isvalid_city
    - slot{"location": "Mumbai"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_ask_email_permission
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_54
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_isvalid_city
    - slot{"location": "delhi"}
    - slot{"is_valid_city": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_avg_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email_permission
* deny
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_noemail_sent
* affirm
    - utter_goodbye

## interactive_story_55
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_isvalid_city
    - slot{"location": "delhi"}
    - slot{"is_valid_city": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_avg_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email_permission
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_55_1
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_isvalid_city
    - slot{"location": "delhi"}
    - slot{"is_valid_city": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_avg_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_56
* restaurant_search{"location": "Latur"}
    - slot{"location": "Latur"}
    - action_isvalid_city
    - slot{"location": "Latur"}
    - slot{"is_valid_city": false}
    - utter_invalid_city_message
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_isvalid_city
    - slot{"location": "Delhi"}
    - slot{"is_valid_city": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_avg_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_57
* restaurant_search{"cuisine": "north indian", "location": "bangalore"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "bangalore"}
    - action_isvalid_city
    - slot{"location": "bangalore"}
    - slot{"is_valid_city": true}
    - utter_ask_avg_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "abc@madisonindia.com"}
    - slot{"email": "abc@madisonindia.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
* affirm
    - utter_goodbye
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_isvalid_city
    - slot{"location": "Mumbai"}
    - slot{"is_valid_city": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_avg_price
* restaurant_search{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "abc@madisonindia.com"}
    - slot{"email": "abc@madisonindia.com"}
    - action_send_email
    - slot{"location": null}
    - slot{"is_valid_city": null}
    - slot{"cuisine": null}
    - slot{"email": null}
    - slot{"price": null}
    - utter_email_sent
