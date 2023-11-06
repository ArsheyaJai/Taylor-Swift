def main():
  Quiz()

#basic use of an integer variable
num_albums = 10
#this statement will print only once at the beginning, so it is out of the tryAgain loop
print("Heads up: Taylor Swift has ", num_albums, " albums!")


def Quiz():
  tryAgain = True

  #basic while loop for namesake
  #ask user to pick a genre from the list and loop until they pick an available genre
  while tryAgain:
    list_of_genres = (
        "pop, electro/synth pop, pop rock, indie, soft rock, bedroom pop")
    print(list_of_genres)
    Genre = input('What is your favorite genre?: ')
    print("you said: " + Genre)
    if Genre.lower() == 'pop':
      print("you chose pop")
      break
    elif Genre.lower() == 'electro/synth pop':
      print("you chose electro/synth pop")
      break
    elif Genre.lower() == 'pop rock':
      print("you chose pop rock")
      break
    elif Genre.lower() == 'indie':
      print("you chose indie")
      break
    elif Genre.lower() == 'soft rock':
      print("you chose soft rock")
      break
    elif Genre.lower() == 'bedroom pop':
      print("you chose bedroom pop")
      break
    else:
      print('please enter a genre from the list')

  #output based on genre chosen for the 1989 album
  while Genre.lower() == 'pop':
    SongRec = input('Do you want song recommendations?: ')
    if SongRec.lower() == 'yes':
      print(
          'Album: 1989\nSong Recommendations: I Know Places✧New Romantics✧Wildest Dreams'
      )
      print('Enjoy ◡̈')
      break
    elif SongRec.lower() == 'no':
      print('Album: 1989')
      print('Enjoy ◡̈')
      break
    else:
      print('please enter "yes" or "no"')

  #output based on genre chosen for the reputation album
  while Genre.lower() == 'electro/synth pop':
    SongRec = input('Do you want song recommendations?: ')
    if SongRec.lower() == 'yes':
      print(
          'Album: reputation\nSong Recommendations: Delicate✧Gorgeous✧Dancing With Our Hands Tied'
      )
      print('Enjoy ◡̈')
      break
    elif SongRec.lower() == 'no':
      print('Album: reputation')
      print('Enjoy ◡̈')
      break
    else:
      print('please enter "yes" or "no"')

  #output based on genre chosen for the Lover album
  while Genre.lower() == 'pop rock':
    SongRec = input('Do you want song recommendations?: ')
    if SongRec.lower() == 'yes':
      print(
          'Album: Lover\nSong Recommendations: Lover✧The Man✧Its Nice To Have A Friend'
      )
      print('Enjoy ◡̈')
      break
    elif SongRec.lower() == 'no':
      print('Album: Lover')
      print('Enjoy ◡̈')
      break
    else:
      print('please enter "yes" or "no"')

  #output based on genre chosen for the folklore album
  while Genre.lower() == 'indie':
    SongRec = input('Do you want song recommendations?: ')
    if SongRec.lower() == 'yes':
      print('Album: folklore\nSong Recommendations: mirrorball✧seven✧august')
      print('Enjoy ◡̈')
      break
    elif SongRec.lower() == 'no':
      print('Album: folklore')
      print('Enjoy ◡̈')
      break
    else:
      print('please enter "yes" or "no"')

  #output based on genre chosen for the evermore album
  while Genre.lower() == 'soft rock':
    SongRec = input('Do you want song recommendations?: ')
    if SongRec.lower() == 'yes':
      print(
          'Album: evermore\nSong Recommendations: cowboy like me✧ivy✧gold rush'
      )
      print('Enjoy ◡̈')
      break
    elif SongRec.lower() == 'no':
      print('Album: evermore')
      print('Enjoy ◡̈')
      break
    else:
      print('please enter "yes" or "no"')

  #output based on genre chosen for the Midnights album
  while Genre.lower() == 'bedroom pop':
    SongRec = input('Do you want song recommendations?: ')
    if SongRec.lower() == 'yes':
      print(
          'Album: Midnights\nSong Recommendations: The Great War✧Sweet Nothing✧Bejeweled'
      )
      print('Enjoy ◡̈')
      break
    elif SongRec.lower() == 'no':
      print('Album: Midnights')
      print('Enjoy ◡̈')
      break
    else:
      print('please enter "yes" or "no"')

  #ask user if they want to do this again
  #this determines if the main loop is repeated
  again = input('Would you like to try another genre?: ')
  if again.lower() == 'no':
    tryAgain = False
  else:
    main()


main()
