name1 = input("Choose a name: \n")
time1 = input("Choose a time of day: \n")
transport1 = input("Choose a method of transportation in the past tense: \n")
place1 = input("Choose a place: \n")
name2 = input("Choose another name: \n")
activity1 = input("Choose an activity for two or more people to do: \n")
name3 = input("Choose yet another name: \n")
negative_emotion1 = input("Choose a negative emotion in the form of a noun: \n")
positive_emotion1 = input("Choose a positive emotion in the form of a noun: \n")
rephrased_end = input("Rephrase the phrase 'They lived happily ever after.' in your own silly words: \n")


message = f"One day at {time1}, {name1} {transport1} to {place1}. At {place1}, he/she saw {name2}, and they \n decided to do some {activity1} together, with everyone around them joining in. Seeing this, {name3} felt \n {negative_emotion1} and started yelling \"AAAHHHHHH I'M SO JEALOUS OF THEIR FUN!\". In the end, {name3}'s observations showed him how \n much fun they were having, and he felt enough {positive_emotion1} to join in with {name1} and {name2}. In the end, \n {rephrased_end}"

print(message)