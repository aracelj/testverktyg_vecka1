# Testverktyg VeckoUppgift1

By Araceli Jakobsson

Exercises:
  1. UML Diagram(diving*.jpg) - a diagram for classes, functions/method, parameters needed for a diving club.
  2. Creating a testing for the ff:
     - Inventory: set_item(name, rent_price, quantity)
                  rent(item_name)
                  get_amount_left(name)  
       Excursion: get_members()
                  add_member(name)
                  remove_member(name)
                  register_item_rented(member_name, item_name)
                  register_item_returned(member_name, item_name)
                  get_all_who_has_not_returned_items()
  3. Creating testcase for weatherapp and weatherservice using 3 user stories:
           a. As a user, the user can search for the city and see the corresponding weather forecast of the day
           b. As a user, the user can search by location coordinates and see the corresponding weather forecast of the day.
           c. As a user, the user can input no. of days for the next weather forecast


## 

```commandline
python -m tests/inventory.py
python -m tests/test_weatherservice.py
python -m pytest tests/test_weatherservice.py
```