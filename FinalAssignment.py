#Nate Arnold
#Assignment 10.1
#FinalAssignment.py
#This code is a class based on a movie theater.

from random import shuffle
from random import randint

class Movie_Theater:
    
    #Theater name class attribute
    theater_name = 'Santa Cruz Cinema'
    

    #Init for this class
    def __init__(self,theater_number,time):
        #Inputs into private data attributes
        self.__theater_number = theater_number
        self.__time = time
        
        #Default data attributes
        #Dictionary of movies at the theater and their number
        self.__movie_dict = {
            'Theater 1':'The Matrix',
            'Theater 2':'Avengers:Endgame',
            'Theater 3':'Star Wars: A New Hope',
            'Theater 4':'Shrek',
            'Theater 5':'Back to the Future'
            }
        #Dictionary of showtimes in each theater        
        self.__showtimes_dict = {
            'Theater 1':['12:00 PM','3:00 PM','6:00 PM'],
            'Theater 2':['7:00 AM','10: AM','1:00 PM'],
            'Theater 3':['8:00 AM','11:00 AM','2:00 PM'],
            'Theater 4':['5:00 PM','8:00 PM','11:00 PM'],
            'Theater 5':['4:00 PM','7:00 PM','10:00 PM']
            }
        
        #List of the seats available
        self.__seat_list = ['1A','1B','1C','2A','2B','2C','3A','3B','3C']
    #Gets the inputted theater number
    def get_theater(self):
        result = "Your theater is {0}".format(self.__theater_number)
        return(result)
    #Gets the inputted showtime
    def get_showtime(self):
        result = "Your showtime is {0}".format(self.__time)
        return(result)
    #This function returns the movie that is being shown at the time and theater inputted
    def get_movies(self):
        
        #Checks to see if the theater number exists and finds the movie playing in it
        try:
            if self.__theater_number in self.__movie_dict:
                return1 = self.__movie_dict[self.__theater_number]
            else:
                print('This theater doesnt exist')
        except:
            print("This theater doesn't exist")
            return
        #Checks to see if the showtime exists and returns which index it is in the showtime list
        counter = 0
        new_list = self.__showtimes_dict[self.__theater_number]
        if self.__time in new_list:
            for i in new_list:

                if i == new_list[counter]:
                    iterable = i
                    break

                else:
                    counter += 1
            return2 = iterable
            #Getting final result
            final_print = 'Congrats! The movie playing in {0} is {1}, at {2}'.format(return1,self.__theater_number,return2)
            return(final_print)
        else:
            print('There are no movies in this theater with this showtime')
            return

       
    #This function prints the ticket    
    def print_ticket(self):
        
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        #Prints the name of the theater
        namecentered = self.theater_name.center(56)
        print(namecentered)
        
        #Prints the movie playing
        movie = self.__movie_dict[self.__theater_number]
        print("Movie: {0}".format(movie))

        #Prints the showtime
        print("Showtime: {0}".format(self.__time))

        #Assigns a seat
        print("Seat: {0}".format(self.seat_generator()))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        return
    
    #This function randomly assigns seats, then removes them from the list of available seats 
    def seat_generator(self):
        if self.__seat_list == []:
            #If there are no more seats then it returns this message
            return("There are no more seats")
        else:
            #Shuffles the list
            shuffle(self.__seat_list)
            #Imported from the random module, the randint function takes a random number within the range given
            index = randint(0,len(self.__seat_list)-1)
            #Removes the index and returns the value
            return_i = self.__seat_list.pop(index)
            return(return_i)

#Demo program
def main():
    #Creating the object with the inputs Theater 2 and 1:00 PM 
    my_movie_theater = Movie_Theater('Theater 2','1:00 PM')
    #Testing the methods
    #Returns the 2 input arguments
    print(my_movie_theater.get_theater())
    print(my_movie_theater.get_showtime())
    #Returns which movie is playing in this theater
    print(my_movie_theater.get_movies())
    #Prints your ticket, with theater number, movie name, and randomly assigns a seat
    my_movie_theater.print_ticket()
    #Prints the remaining seats
    for i in range(9):
        print(my_movie_theater.seat_generator())
if __name__ == "__main__":
    main()
