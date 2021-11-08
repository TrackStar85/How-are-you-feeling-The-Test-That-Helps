'''Helper functions for returning new questions for users'''

from colorama import Fore, Style

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
  while answer > 10 or answer < 1 or answer == "":
    print(Fore.RED + "Not eligible answer." + Style.RESET_ALL)
    answer = int(input("Enter (1, 2, 3, 4, 5, 6, 7, 8, 9, 10): "))
  return ""


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
  while answer != "True" and answer != "False":
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
    r_answer = input("Enter (1, 2, 3, 4, 5, 6, 7, 8, 9, 10): ")
    score.append(r_answer)
    r_eligible_answer(r_answer)
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