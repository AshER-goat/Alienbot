# # importing regex and random libraries
import re
import random

class AlienBot:
  # potential negative responses
  negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
  # keywords for exiting the conversation
  exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later", "stop")
  # random starter questions
  random_questions = (
        "Why are you here? ",
        "Are there many humans like you? ",
        "What do you consume for sustenance? ",
        "Is there intelligent life on this planet? ",
        "Does Earth have a leader? ",
        "What planets have you visited? ",
        "What technology do you have on this planet? "
    )

  def __init__(self):
    self.alienbabble = {'describe_planet_intent': r'.*\s*your planet.*',
                        'answer_why_intent': r'why\sare.*',
                        'cubed_intent': r'.*cube.*(\d+)',
                        'name_intent': r'.*\s*your name.*',
                        'how_you_intent': r'how(?:\s+are)? you.*?'
                            }

  # Define .greet() below:
  def greet(self):
    self.name = input("Hi, what's your name?\n")

    will_help = input(f"Hi {self.name}, I'm not from this planet. Will you help me learn about your planet?\n")

    if will_help in self.negative_responses:
      print("Ok, have a nice Earth day!\n")
      return 

    self.chat() 

  # Define .make_exit() here:
  def make_exit(self, reply):
    for exitwords in self.exit_commands:
      if reply == exitwords:
        print("ok, have a nice Earth day!\n")
        return True

  # Define .chat() next:
  def chat(self):
    reply = input(random.choice(self.random_questions)).lower()
    while not self.make_exit(reply):
      reply = input(self.match_reply(reply))

    
  # Define .match_reply() below:
  def match_reply(self, reply):
    for key,value in self.alienbabble.items():
      intent = key
      regex_pattern = value
      found_match = re.match(regex_pattern,reply)
      if found_match and intent == 'describe_planet_intent':
        return self.describe_planet_intent()
      elif found_match and intent == 'answer_why_intent':
        return self.answer_why_intent()
      elif found_match and intent == 'cubed_intent':
        return self.cubed_intent(found_match.groups()[0])
      elif found_match and intent == 'name_intent':
        return self.name_intent()
      elif found_match and intent == 'how_you_intent':
        return self.how_you_intent()
    # the return self.no_match_intent() should be outside the for loop (instead of being inside an else statement inside the for loop). Otherwise every time you input an intent other than “your planet” it won’t even loop through the rest of the dictionary, instead it will go to no_match in the end.
    else:
      return self.no_match_intent()


  # Define .describe_planet_intent():
  def describe_planet_intent(self):
    responses = ("My planet is a utopia of diverse organisms and species\n","I am from Opidius, the capital of the Wayward Galaxies\n")
    return random.choice(responses)

  # Define .answer_why_intent():
  def answer_why_intent(self):
    responses = ("I come in peace\n","I am here to collect data on your planet and its inhabitants\n", "I heard the coffee is good\n")
    return random.choice(responses)
       
  # Define .cubed_intent():
  def cubed_intent(self, number):
    number = int(number)
    cubed_number = number*number*number
    return f"The cube of {number} is {cubed_number}. Isn't that cool?\n"

  def name_intent(self):
    random_names_list = ("Al", "Bob", "Beep-Boop", "Fizzle")
    random_name = random.choice(random_names_list)
    return f"Aw! You want to know my name? It's {random_name}!\n"

  def how_you_intent(self):
    random_response_list = ("Not so good.", "Great!", "Ok.")
    random_response = random.choice(random_response_list)
    return f"{random_response} I guess. How are you?\n"

  # Define .no_match_intent():
  def no_match_intent(self):
    responses = ("Please tell me more","Tell me more!","Why do you say that?\n","I see. Can you elaborate?\n","Interesting. Can you tell me more?\n","I see. How do you think?\n","why?\n","How do you think I feel when you say that?\n")
    return random.choice(responses)

# Create an instance of AlienBot below:
Chatbot = AlienBot()
Chatbot.greet()
