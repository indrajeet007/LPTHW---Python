from sys import argv

script, user_name = argv
prompt = '> '

print("Hi %s, I'm the %s script." % (user_name, script))
print("I would like to ask a few questions.")

print("Which fruit do you prefer ? ")
fruit_likes = input(prompt)

print("When do you prefer %s, %s " % (fruit_likes, user_name))
prefer = input(prompt)

print("Do you prefer '%s Jam' or '%s Pie' ? " % (fruit_likes, fruit_likes))
want = input(prompt)

print ("""
Alright, so you seem like a big fan of %r, Mr. %r.
And also you prefer to have %r, %r.
Not sure why but maybe coz you prefer %r. Good !
""" % (fruit_likes, user_name, fruit_likes, prefer, want))
