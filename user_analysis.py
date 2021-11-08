'''helper functions for developing the final analysis for user'''

from colorama import Fore, Back, Style

def display_score(answers, answers_2, answers_3, analysis_list):
  '''Calculates what the analysis will be for the user and the total score. Depending on this total score they will be deemed with having certain disorders or being perfectly healthy.

    Args:
        answers: A list of users responses to ranking from 1-10 questions.

        answers_2: A list of user's responses to true or false questions

        answers_3: a list of user's responses to multiple choice questions

        analysis_list: A list of the questions students gave concerning responses to

    Returns:
        Total score between the lists

    Examples:
      display_score([1, 3, 4], ["True", "False", "True"], ["A", "B", "D"])
      returns 32
      display_score([3, 8, 10, 4, 5], ["False", "False", "True", "True", "False", "True"], ["B", "D", "A", "C", "D", "A"])
      returns 74
  '''  
  print(Fore.BLACK + Back.WHITE + "-------------------------------------------------------------------------------")
  print("Results")
  print("-------------------------------------------------------------------------------")

  print("\nBefore you receive your results, please input some basic information about yourself. \n")

  name = input("Name: ")
  age = int(input("Age: "))
  
  count = 0

  for i in answers:
    i = int(i)
    if i <= 10:
      count += int(i)
    else:
      count += 0

  count_2 = 0

  for i in answers_2:
    if i == "True":
      count_2 += 6
    else:
      count_2 += 0

  count_3 = 0

  for i in answers_3:
    if i == "B":
      count_3 += 4
    elif i == "C":
      count_3 += 6
    elif i == "D":
      count_3 += 8
    else:
      count_3 += 0
    
  total_score = count + count_2 + count_3 

  if total_score <= 170 and count <= 50 and count_2 <= 85 and count_3 <= 20:
    print(Style.RESET_ALL + "\n\n{}, you are not displaying the symptoms of a mental illness. No need to worry!\n".format(name))
    if age <= 28:
      print("You are {} years old and still young. You are going through a very important and stressful time in your life. Try and concentrate on the good things and remember that you have so much going for you and so much more time on this earth to do everything that you want to do.\n".format(age))
    else:
      print("You are {} years old and, although you are beginning to get older, you must remember that there are people that love and care about you. Here are some resources to continue to live your best life. \n".format(age))
  else:
    print(Style.RESET_ALL)
    print(Fore.RED + str(analysis(analysis_list)) + Style.RESET_ALL)
    print(Fore.RED + name + depression(analysis_list) + ptsd(analysis_list) + anxiety(analysis_list) + eating_disorder(analysis_list) + substance_abuse(analysis_list) + ", Contact your local mental health provider. Don't hesitate to get help.\n" + Style.RESET_ALL)
  return total_score


def analysis(recorded_answers):
  '''Will display the list of questions/statements user gave concerning answers to.

    Args:
        recorded_answers: A list which has the recorded statements user gave concerning answers to

    Returns:
        Empty string

    Examples:
        analysis(["You sometimes feel discouraged", "You have feelings of sadness"]) --> "According to the answers you provided: 
        -You sometimes feel discouraged
        -You have feelings of sadness"
  '''
  print(Fore.RED + "According to these answers you provided: ")
  for key in recorded_answers:
    key = "-" + key
    print(key)
  return ""


def depression(list_1):
  '''Questions/statements that are associated with depression will have a certain symbol to identify them as such. This function will use these questions/statements to determine if the user is depressed
  
    Args:
        list_1: A recorded list of the questions/statements user gave concerning answers to.

    Returns:
        Empty string
    
    Examples:
        depression(["You sometimes feel discouraged~", "You can't sleep at night~", "you wish you had more friends~"]) --> "You are displaying symptoms of depression."
  '''
  count = 0
  for key in list_1:
    if "~" in key:
      count += 1
  if count > 2 and count <= 4:
    print(Fore.RED + "You are displaying symptoms of depression." + Style.RESET_ALL)
  elif count > 4:
    print(Fore.RED + "Your are displaying major symptoms of depression." + Style.RESET_ALL)
  return ""


def ptsd(list_1):
  '''Questions/statements that are associated with ptsd will have a certain symbol to identify them as such. This function will use these questions/statements to determine if the user is experiencing ptsd
  
    Args:
        list_1: A recorded list of the questions/statements user gave concerning answers to.

    Returns:
        Empty string
    
    Examples:
        ptsd(["You feel jumpy^", "You can't sleep at night^", "you have nightmares^"]) --> "You are displaying symptoms of ptsd."
  '''
  count = 0
  for key in list_1:
    if "^" in key:
      count += 1
  if count > 2 and count <= 4:
    print(Fore.RED + "You are displaying symptoms of ptsd." + Style.RESET_ALL)
  if count > 4:
    print(Fore.RED + "You are displaying major symptoms of PTSD (Post Traumatic Stress Disorder" + Style.RESET_ALL)
  return ""


def anxiety(list_1):
  '''Questions/statements that are associated with anxiety will have a certain symbol to identify them as such. This function will use these questions/statements to determine if the user has anxiety
  
    Args:
        list_1: A recorded list of the questions/statements user gave concerning answers to.

    Returns:
        Empty string
    
    Examples:
        anxiety(["You feel nervous all the time`", "You can't stop worrying`", "You feel alone`"]) --> "You are displaying symptoms of anxiety disorder."
  '''
  count = 0
  for key in list_1:
    if "`" in key:
      count += 1
  if count > 2 and count <= 4:
    print(Fore.RED + "You are displaying symptoms of anxiety disorder." + Style.RESET_ALL)
  elif count > 4:
    print(Fore.RED + "You are displaying major symptoms of an anxiety disorder." + Style.RESET_ALL)
  return ""


def eating_disorder(list_1):
  '''Questions/statements that are associated with eating disorders will have a certain symbol to identify them as such. This function will use these questions/statements to determine if the user has an eating disorder
  
    Args:
        list_1: A recorded list of the questions/statements user gave concerning answers to.

    Returns:
        Empty string
    
    Examples:
        eating_disorder(["# You can't stop eating.", "# You feel like you can't eat.", "# you wish you had more friends"]) --> "You are displaying symptoms of an eating disording."
  '''
  count = 0
  for key in list_1:
    if "#" in key:
      count += 1
  if count > 2 and count <= 4:
    print(Fore.RED + "Youa re displaying symptoms of an eating disorder." + Style.RESET_ALL)
  elif count > 4:
    print(Fore.RED + "You are displaying major symptoms of an eating_disorder." + Style.RESET_ALL)
  return ""


def substance_abuse(list_1):
  '''Questions/statements that are associated with substance abuse will have a certain symbol to identify them as such. This function will use these questions/statements to determine if has problems with substance abuse
  
    Args:
        list_1: A recorded list of the questions/statements user gave concerning answers to.

    Returns:
        Empty string
    
    Examples:
        substance_abuse(["@ You drink too much", "@ You can't function without drinking", "@ you feel as though you can't go a day without drinking"]) --> "You are displaying symptoms of substance abuse."
  '''
  count = 0
  for key in list_1:
    if "@" in key:
      count += 1
  if count > 2 and count <= 4:
    print(Fore.RED + "You are displaying symptoms of substance abuse." + Style.RESET_ALL)
  elif count > 4:
    print(Fore.RED + "You are displaying major symptoms of substance abuse." + Style.RESET_ALL)
  return ""


def take_test():
  '''Allows user the choice to take the quiz or not.
  
    Args:
        None

    Returns:
        True if user response is "YES"
        False if the user's response is no or anything that is not "YES"
    
    Examples:
        take_test("YES") --> True
  '''
  
  response = input("Would you like to take a mental health test? (yes or no): ")
  response = response.upper()

  if response == "YES":
    return True
  return False
