README

Class Movie_Theater

This class represents and contains the attributes of a movie theater. It has movies, theaters, showtimes, and seats. The defining feature of this class is
the ability to print a ticket based on the given parameters. The only attribute that can be changed is the seat list, 
and it will narrow down as seats are assigned to the user's ticket.

Theaters available and their showtimes:

'Theater 1':['12:00 PM','3:00 PM','6:00 PM']
'Theater 2':['7:00 AM','10: AM','1:00 PM']
'Theater 3':['8:00 AM','11:00 AM','2:00 PM']
'Theater 4':['5:00 PM','8:00 PM','11:00 PM']
'Theater 5':['4:00 PM','7:00 PM','10:00 PM']

Class Attribute

-theater_name: This represents the name of the theater, and can be changed to whatever is desired, therefore it is public. It will be printed on the ticket.

Private Data Attributes 

-self.__theater_number: There are 5 theaters in total, each are assigned their own movie and showtime. The theater inputted must match 1 of the 5 theaters in the list. If it does match,
and the get_movies method is called, then the user will be returned which movie they will be watching. The format must be "Theater 1". The number must be a number and not typed out, and 
must be separate from the theater.

-self.__time: This is an inputted argument that represents the time that the user wants to show up to the movie. This is returned on the ticket and must line up with the showtime list
for said theater. Must be in  the following format: "1:00 PM","7:00 AM","10:00 PM". The "AM" or "PM" must be separate from the time and must be capitalized.

-self.__movie_dict: This is a dictionary of the movies that are playing in the theaters they are assigned to. The keys are the theater number and the values are the movies.

-self.__showtimes_dict: This is a dictionary of the showtimes for their assigned theater. The keys are the theater number and the values are a list with 3 showtimes per theater.

-self.__seat_list: This is a list of available seats. This will be updated as the program is ran, so seats can be taken out of the list as they are assigned.

Methods:

Note:All methods use 'self' as their only argument.
 
-get_theater and get_showtime: These methods simply return the two arguments that are inputted. Both will return a string that tells you what your theater number is or your showtime.

-get_movies: This method will check to make sure both the arguments to the object are valid and fufill the previous requirements. It will return a message saying either dont exist if this
is the case. Then the theater number is matched with the movie in the theater and makes sure the showtime is within that theater. Finally it prints a final message letting the user what 
movie they will be watching in their theater at the inputted showtime.

-print_ticket: This method prints a ticket using all of the previous attributes. This ticket has all of the necessary information on it, and it will assign a seat to the user. 
This seat is determined by the seat_generator method.

-seat_generator: This method will take the list of seats and randomly return one of them. It also will remove the seat from the list which means there will be no duplicate seats.

Demo Program:

The demo program runs all of the methods based off of the called object. This object is called my_movie_theater. In the demo the inputs will be returned, the movie playing in the desired
theater, a ticket will be printed, then all of the remaining seats will be returned until there are none left.

Instructions:

The demo program is ran through the main() function. All that must be done to test different inputs is to change the arguments in the object my_movie_theater.
Be sure to use the formatting mentioned previously.
Example:
my_movie_theater = Movie_Theater("Theater 4","8:00 PM")





