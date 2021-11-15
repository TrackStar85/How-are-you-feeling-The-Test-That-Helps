'''Helper functions for returning new questions for users'''

'''Also functions for the different sections of the screening'''

from colorama import Fore, Back, Style

def r_eligible_answer(answer):
  '''For first section of questions (ranking questions on scale of 1-10), while the answer user inputs is not 1-10, then they must input a new, eligible answer.

    Args:
        answer: users input which is an integer.

    Returns:
        Empty string
    
    Examples:
        r_eligible_answer(-11) --> ("Not eligible answer.")
        r_eligible_answer(5) --> ("")
    '''
  while answer != "1" and answer != "2" and answer != "3" and answer != "4" and answer != "5" and answer != "6" and answer != "7" and answer != "8" and answer != "9" and answer != "10" or answer == "":
    print(Fore.RED + "Not eligible answer." + Style.RESET_ALL)
    answer = input("Enter (1, 2, 3, 4, 5, 6, 7, 8, 9, 10): ")

  return answer


def tf_eligible_answer(answer):
  '''For second section of questions (True and False questions), while the answer user inputs is not "True" or "False", then they must input a new, eligible answer.

    Args:
        answer: users input which is a string
    
    Returns:
        Empty string
    
    Examples:
        tf_eligible_answer("Apple") --> "Not eligible answer."
        tf_eligible_answer("False") --> ""
  '''
  while answer.upper() != "TRUE" and answer.upper() != "FALSE":
    print(Fore.RED + "Not eligible answer." + Style.RESET_ALL)
    answer = input("Enter (True or False): ")
  return ""


def mc_eligible_answer(answer):
  '''For third section of questions (Multiple choice questions), while the answer user inputs is not "A", "B", "C", or "D", then they must input a new, eligible answer.

    Args:
        answer: users input which is a string
    
    Returns:
        Empty string

    Examples:
        mc_eligible_answer("F") --> "Not eligible answer."
        mc_eligible_answer("A") --> ""
  '''
  while answer.upper() not in "ABCD":
    print(Fore.RED + "Not eligible answer." + Style.RESET_ALL)
    answer = input("Enter (A, B, C, D): ")
  return ""

  
def yn_eligible_answer(answer):
  '''For special case "yes or no" question within the third section of the test (multiple choice questions, where A = Yes and B = No), while the answer user inputs is not "A" or "B", then they must input a new, eligible answer.

    Args:
        answer: users input which is a string

    Returns:
        Empty string
    
    Examples:
        yn_eligible_answer("F") --> "Not eligible answer."
        yn_eligible_answer("A") --> ""
  '''
  while answer.upper() not in "AB":
    print(Fore.RED + "Not eligible answer." + Style.RESET_ALL)
    answer = input("Enter A (Yes) or B (No): ")
  return ""


def r_change_question(list_2, score):
  '''For questions that, depending on users response, will result in a new question appearing. This function is to take the list of new questions and adds the responses of these questions to the list.

    Args:
        list_2: A list separate from the original list of questions. Holds a new set of questions that will be asked due to users specific response to original ranking 1-10 questions.

        score: a list to store the responses the user inputs.
    
    Returns:
        Empty string

    Examples:
        r_change_question(["How are you today?"], []) --> [10] (if user's response was 10)
  '''
  question_num = 1
  for item in list_2:
    print(Fore.BLUE + "------------------------------------------------------------------------------------")
    print(item + Style.RESET_ALL)
    r_answer = (input("Enter (1, 2, 3, 4, 5, 6, 7, 8, 9, 10): "))
    r_answer_2 = r_eligible_answer(r_answer)
    score.append(r_answer_2)
  question_num += 1
  return ""


def tf_change_question(list_2, score):
  '''For questions that, depending on users response, will result in a new question appearing. This function is to take the list of new questions and adds the responses of these questions to the list.

    Args:
        list_2: A list separate from the original list of questions. Holds a new set of questions that will be asked due to users specific response to original true or false questions.

        score: a list to store the responses the user inputs.
    
    Returns:
        Empty string

    Examples:
        r_change_question(["Do you feel unhappy?"], []) --> ["True"] (if user's response was "True")
  '''
  question_num = 1
  for item in list_2:
    print(Fore.GREEN + "------------------------------------------------------------------------------------")
    print(item + Style.RESET_ALL)
    tf_answer = input("Enter (True or False): ")
    score.append(tf_answer)
    tf_eligible_answer(tf_answer)
  question_num += 1
  return ""

def mc_change_question(list_2, score):
  '''For questions that, depending on users response, will result in a new question appearing. This function is to take the list of new questions and adds the responses of these questions to the list.

    Args:
        list_2: A list separate from the original list of questions. Holds a new set of questions that will be asked due to users specific response to original multiple choice questions.

        score: a list to store the responses the user inputs.
    
    Returns:
        Empty string

    Examples:
        r_change_question(["Do you feel depressed?"], []) --> ["A"] (if user's response was "A")
  '''
  question_num = 1
  for item in list_2:
    print(Fore.YELLOW + "------------------------------------------------------------------------------------")
    print(item + Style.RESET_ALL)
    mc_answer = input("Enter (A. Yes or B. No): ")
    mc_answer = mc_answer.upper()
    score.append(mc_answer)
    yn_eligible_answer(mc_answer)
  question_num += 1
  return ""


def ranking_section(statements, analysis):
  '''This is the function that will run the ranking portion of the test.

    Args:
        statements: A list of the statements/questions of the ranking section

        analysis: A list that will keep track of specific statements/questions the user gives certain answers to

    returns:
        A list of the answers the user gives
    
    Examples:
        ranking_section(["You feel depressed", "You have low energy throughout the day", "You find it difficult to concentrat on certain tasks"], [])
        returns [5, 7, 3]

  '''

  print(Back.WHITE + Fore.BLACK + "First, you will be given a series of statements of which you must rate on a scale of 1 to 10. 10 being you completely agree, 5 being you don't care/don't know and 1 being you completely disagree.\n\n" + Style.RESET_ALL)

  failure_statements = ["Feel overwhelmed with the pressure to succeed in life.` ", "Believe that you are not as good as what people think.` ", "Feel like a fraud.` "]

  ranking_answers = []
  question_num = 1

  for key in statements:
    print(Fore.BLUE + "------------------------------------------------------------------------------")
    print(key + Style.RESET_ALL)
    rank = (input("Enter (1, 2, 3, 4, 5, 6, 7, 8, 9, 10): "))
    
    response = r_eligible_answer(rank)

    ranking_answers.append(int(response))
  
    if "*" in key:
      if response not in "12345":
        print(Fore.RED + "If you are having thoughts of suicide please call the suicide hotline number at 1-800-273-8255" + Style.RESET_ALL)

    if key == "Feeling bad about yourself - or that you are a failure or have let yourself or your family down~` ":
      if response in "678910":
        print(r_change_question(failure_statements, ranking_answers))
        response = r_eligible_answer(rank)
        ranking_answers.append(int(response))

    if response not in "12345":
      analysis.append(key)
      
    question_num += 1
  return ranking_answers

def tf_section(statements, analysis):

  print(Back.WHITE + Fore.BLACK + "\n\nFor the next section of the test, you will be given a series of multiple choice questions about the last 2 weeks. \n" + Style.RESET_ALL)

  print(Fore.YELLOW + "Over the last 2 weeks, how often have you been bothered by the following problems?\n\n" + Style.RESET_ALL)

  traumatic_event_statements = ["I have nightmares about the events or thoughts about the events.^ ", "I feel guilty and am unable to stop blaming myself or others for the events.^ "]

  drinking_statements = ["@ My family and friends have complained about the amount I drink/use drugs. ", "@ I have tried and failed to quit drinking/using drugs. ", "@ I feel like I can't live without drinking/using drugs. ", "@ I find myself missing out because I have to drink/use drugs. "]

  eating_disorder_statements = ["# I make myself throw up in order to keep the same weight. ", "# I skip meals because I don't want to gain weight. ", "# I take laxatives to lose weight. ", "# I excercise profusely in order to lose weight. ", "# I am never satisfied with my body. "]

  tf_answers = []
  question_num_2 = 1

  for key in statements:
    print(Fore.GREEN + "------------------------------------------------------------------------------")
    print(key + Style.RESET_ALL)

    answer = input("Enter (True or False): ")

    response = tf_eligible_answer(answer)
    
    tf_answers.append(response)

    if key == "I have experienced a traumatic experience. For example: a serious accident, a physical or sexual assault or abuse, an earthquake or flood, a war, witnissing a death, or losing a loved one to suicide.^ ":
      if response == "True":
        print(tf_change_question(traumatic_event_statements, tf_answers))

    if key == "@ I feel like I should cut down on my drinking or drug use. ":
      if response == "True":
        print(tf_change_question(drinking_statements, tf_answers))

    if key == "# I am terrified of gaining weight or constantly preoccupied by my eating habits. ":
      if response == "True":
        print(tf_change_question(eating_disorder_statements, tf_answers))
    
    if response == "True":
      analysis.append(key)

  question_num_2 += 1
  return tf_answers

def mc_section(statements, analysis):

  print(Back.WHITE + Fore.BLACK + "\n\nFor the next section of the test, you will be given a series of rank_statements of which you must choose whether it is True or False.\n" + Style.RESET_ALL)

  options = [["A. Not at all", "B. Several days", "C. More than half the days", "D. Nearly every day"], ["A. Not at all", "B. Several days", "C. More than half the days", "D. Nearly every day"], ["A. Not at all", "B. Several days", "C. More than half the days", "D. Nearly every day"], ["A. Not at all", "B. Several days", "C. More than half the days", "D. Nearly every day"], ["A. Not difficult at all", "B. Somewhat difficult", "C. Very difficult", "D. Extremely Difficult"]]

  worrying_statements = ["Can you identify any reasons why you may not be able to stop or control your worrying?` (A for 'yes' or B for 'no') ", "Do these reasons involve schoolwork, family issues, or social issues?` "]
  
  mc_answers = []
  question_num_3 = 1

  for key in statements:
    print(Fore.YELLOW + "------------------------------------------------------------------------------")
    print(key + Style.RESET_ALL)

    for i in options[question_num_3 - 1]:
      print(i)

    answer = input("Enter (A, B, C, D): ")
    answer = answer.upper()

    response = mc_eligible_answer(answer)
    
    mc_answers.append(response)

    if "*" in key:
      if response.upper() == "D":
        print(Fore.RED + "If you are having thoughts of suicide please call the suicide hotline number at 1-800-273-8255" + Style.RESET_ALL)
    
    if key == "Feeling nervous, anxious, or on edge.` ":
      if response.upper() == "D" or response.upper() == "C":
        print(mc_change_question(worrying_statements, mc_answers))
    
    if response.upper() == "D" or response.upper() == "C":
      analysis.append(key)
        
  question_num_3 += 1
  return mc_answers
  