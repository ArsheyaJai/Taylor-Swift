MoodvGenre = input('Do you want to learn which Taylor Swift album you should listen to by genre or mood?: ');

if MoodvGenre.lower() == 'genre':
    print('you chose genre')
elif MoodvGenre.lower() == 'mood':
    print('you chose mood')
else:
    print('please enter either "mood" or "genre"')

list_of_genres = ("pop, electro/synth pop, pop rock, indie, soft rock, bedroom pop")

while MoodvGenre.lower() == 'genre':
  print(list_of_genres)
  Genre = input('What is your favorite genre: ')
  print("you said: " + Genre)
  if Genre.lower() == 'pop':
    print("you chose pop")
    break
    while Genre.lower() == 'pop':
      SongRec = input('Do you want song recommendations?: ')
      if SongRec.lower() == 'yes':
        print('Album: 1989\nSong Recommendations: I Know Places✧New Romantics✧Wildest Dreams')
        print('Enjoy ◡̈')
        break
      elif SongRec.lower() == 'no':
        print('Album: 1989')
        print('Enjoy ◡̈')
        break
      else:
        print('please enter "yes" or "no"')
  elif Genre.lower() == 'electro/synth pop':
    print("you chose electro/synth pop")
    break
    while Genre.lower() == 'electro/synth pop':
      SongRec = input('Do you want song recommendations?: ')
      if SongRec.lower() == 'yes':
        print('Album: reputation\nSong Recommendations: Delicate✧Gorgeous✧Dancing With Our Hands Tied')
        print('Enjoy ◡̈')
        break
      elif SongRec.lower() == 'no':
        print('Album: reputation')
        print('Enjoy ◡̈')
        break
      else:
        print('please enter "yes" or "no"')
  elif Genre.lower() == 'pop rock':
    print("you chose pop rock")
    break
    while Genre.lower() == 'pop rock':
      SongRec = input('Do you want song recommendations?: ')
      if SongRec.lower() == 'yes':
        print('Album: Lover\nSong Recommendations: Lover✧The Man✧Its Nice To Have A Friend')
        print('Enjoy ◡̈')
        break
      elif SongRec.lower() == 'no':
        print('Album: Lover')
        print('Enjoy ◡̈')
        break
      else:
        print('please enter "yes" or "no"')
  elif Genre.lower() == 'indie':
    print("you chose indie")
    break
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
  elif Genre.lower() == 'soft rock':
    print("you chose soft rock")
    break
    while Genre.lower() == 'soft rock':
      SongRec = input('Do you want song recommendations?: ')
      if SongRec.lower() == 'yes':
        print('Album: evermore\nSong Recommendations: cowboy like me✧ivy✧gold rush')
        print('Enjoy ◡̈')
        break
      elif SongRec.lower() == 'no':
        print('Album: evermore')
        print('Enjoy ◡̈')
        break
      else:
        print('please enter "yes" or "no"')
  #elif Genre.lower() == 'bedroom pop':
   # print("you chose bedroom pop")
    #break
    #while Genre.lower() == 'bedroom pop':
     # SongRec = input('Do you want song recommendations?: ')
      #if SongRec.lower() == 'yes':
       # print('Album: Midnights\nSong Recommendations: The Great War✧Sweet Nothing✧Bejeweled')
        #print('Enjoy ◡̈')
        #break
     # elif SongRec.lower() == 'no':
      #  print('Album: Midnights')
       # print('Enjoy ◡̈')
        #break
      #else:
        print('please enter "yes" or "no"')
  else:
    print('please enter a genre from the list')

while Genre.lower() == 'bedroom pop':
  SongRec = input('Do you want song recommendations?: ')
  if SongRec.lower() == 'yes':
    print('Album: Midnights\nSong Recommendations: The Great War✧Sweet Nothing✧Bejeweled')
    print('Enjoy ◡̈')
    break
  elif SongRec.lower() == 'no':
    print('Album: Midnights')
    print('Enjoy ◡̈')
    break
  else:
    print('please enter "yes" or "no"')

list_of_moods = ("artsy, sleepy, romantic, unbothered, energetic, mix of everything")

while MoodvGenre.lower() == 'mood':
  print(list_of_moods)
  Mood = input('What is your current mood: ')
  print("you said: " + Mood)
  if Mood.lower() == 'artsy':
    print("you said artsy")
    break
    while Mood.lower() == 'artsy':
      SongRec = input('Do you want song recommendations?: ')
      if SongRec.lower() == 'yes':
        print('Album: evermore\nSong Recommendations: cowboy like me✧ivy✧gold rush')
        print('Enjoy ◡̈')
        break
      elif SongRec.lower() == 'no':
        print('Album: evermore')
        print('Enjoy ◡̈')
        break
      else:
        print('please enter "yes" or "no"')
  #hi
  elif Mood.lower() == 'sleepy':
    print("you said sleepy")
    break
    while Mood.lower() == 'sleepy':
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
  elif Mood.lower() == 'romantic':
    print("you said romantic")
    break
    while Mood.lower() == 'romantic':
      SongRec = input('Do you want song recommendations?: ')
      if SongRec.lower() == 'yes':
        print('Album: Lover\nSong Recommendations: Lover✧The Man✧Its Nice To Have A Friend')
        print('Enjoy ◡̈')
        break
      elif SongRec.lower() == 'no':
        print('Album: Lover')
        print('Enjoy ◡̈')
        break
      else:
        print('please enter "yes" or "no"')
  elif Mood.lower() == 'unbothered':
    print("you said unbothered")
    break
    while Mood.lower() == 'unbothered':
      SongRec = input('Do you want song recommendations?: ')
      if SongRec.lower() == 'yes':
        print('Album: reputation\nSong Recommendations: Delicate✧Gorgeous✧Dancing With Our Hands Tied')
        print('Enjoy ◡̈')
        break
      elif SongRec.lower() == 'no':
        print('Album: reputation')
        print('Enjoy ◡̈')
        break
      else:
        print('please enter "yes" or "no"')
  elif Mood.lower() == 'energetic':
    print("you said energetic")
    break
    while Mood.lower() == 'energetic':
      SongRec = input('Do you want song recommendations?: ')
      if SongRec.lower() == 'yes':
        print('Album: 1989\nSong Recommendations: I Know Places✧New Romantics✧Wildest Dreams')
        print('Enjoy ◡̈')
        break
      elif SongRec.lower() == 'no':
        print('Album: 1989')
        print('Enjoy ◡̈')
        break
      else:
        print('please enter "yes" or "no"')
  elif Mood.lower() == 'mix of everything':
    print("you said a mix of everything")
    break
    while Mood.lower() == 'mix of everything':
      SongRec = input('Do you want song recommendations?: ')
      if SongRec.lower() == 'yes':
        print('Album: Midnights\nSong Recommendations: The Great War✧Sweet Nothing✧Bejeweled')
        print('Enjoy ◡̈')
        break
      elif SongRec.lower() == 'no':
        print('Album: Midnights')
        print('Enjoy ◡̈')
        break
      else:
        print('please enter "yes" or "no"')
  else:
    print('please enter a genre from the list')

