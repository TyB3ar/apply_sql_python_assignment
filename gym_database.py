# Main Module where functions are run, showing changes made to database in terminal

import members, sessions

print("Displaying Current Members:") # Display initial table of members
members.fetch_members()
  
print('Adding 2 new members:')   # adding 2 new members to table
members.add_member('4', 'Noah', '29') 
members.add_member('5', 'Arielle', '27')

print("Displaying Current Members:") # Displaying table of members with 2 new additions
members.fetch_members()

print("Updating age of Noah to 30:") # Updating age of Noah with member_id 4
members.update_member('4', '30') 

print("Displaying Current Members:") # Displaying table of members with change in age to Noah 
members.fetch_members()

print("Displaying current Workout Sessions:") # Displaying initial table of workout sessions
sessions.fetch_sessions()

print("Adding new workout session:")
sessions.add_session('4', '4', '2024-10-15', '35', '150')

print("Displaying current Workout Sessions:") # Displaying table of sessions after adding session
sessions.fetch_sessions()

print("Removing session:")
sessions.delete_session('4', )

print("Displaying current Workout Sessions:") # Displaying table of sessions after removing session
sessions.fetch_sessions()