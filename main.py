from user_analysis import display_score, take_test

from change_question import r_eligible_answer, mc_eligible_answer, tf_eligible_answer, r_change_question, mc_change_question, tf_change_question

from colorama import Fore, Back, Style

if take_test():

  print(Back.WHITE + Fore.BLACK + "\nWelcome to the mental health screening.\n" + Style.RESET_ALL)
  
  print(Back.WHITE + Fore.BLACK + "How are you feeling?: The Test That Helps\n\nBelow, you will be asked a series of questions. Find a calm, quiet place with no distractions and answer each question as honestly as you can. At the end of the screening you will be given an analysis of your mental health.\n\nGood luck!\n" + Style.RESET_ALL)

  print(Back.WHITE + Fore.BLACK + "First, you will be given a series of statements of which you must rate on a scale of 1 to 10. 10 being you completely agree, 5 being you don't care/don't know and 1 being you completely disagree.\n\n" + Style.RESET_ALL)

  rank_statements = ["Little interest or pleasure in doing things~ ", "Feeling down, depressed or hopeless~ ", "Trouble falling or staying asleep, or sleeping too much ", "Feeling tired or having little energy~ ", "Poor appetite or overeating ", "Feeling bad about yourself - or that you are a failure or have let yourself or your family down~` ", "Trouble concentrating on things, such as doing homework or watching television` ", "Feeling sluggish or tired~ ", "Feeling more restless than usual` ", "Thoughts that you would be better off dead, or hurting yourself~* "]

  failure_statements = ["Feel overwhelmed with the pressure to succeed in life.` ", "Believe that you are not as good as what people think.` ", "Feel like a fraud.` "]

  analysis = []

  ranking_answers = []
  question_num = 1

  for key in rank_statements:
    print(Fore.BLUE + "------------------------------------------------------------------------------")
    print(key + Style.RESET_ALL)
    r_answer = int(input("Enter (1, 2, 3, 4, 5, 6, 7, 8, 9, 10): "))
    
    ranking_answers.append(r_answer)

    r_eligible_answer(r_answer)

    if "*" in key:
      if r_answer > 5:
        print(Fore.RED + "If you are having thoughts of suicide please call the suicide hotline number at 1-800-273-8255" + Style.RESET_ALL)

    if key == "Feeling bad about yourself - or that you are a failure or have let yourself or your family down~` ":
      if r_answer > 5:
        print(r_change_question(failure_statements, ranking_answers))
        r_eligible_answer(r_answer)

    if r_answer > 5:
      analysis.append(key)

  question_num += 1
  
  print(Back.WHITE + Fore.BLACK + "\n\nFor the next section of the test, you will be given a series of rank_statements of which you must choose whether it is True or False.\n" + Style.RESET_ALL)

  tf_statements = ["I have been experiencing severe mood swings, more energy than usual, less need to sleep.` ", "I have experienced a traumatic experience. For example: a serious accident, a physical or sexual assault or abuse, an earthquake or flood, a war, witnissing a death, or losing a loved one to suicide.^ ", "I am constantly on guard, watchful, or easily startled.^` ", "I feel numb or detached from people, activities or my surroundings. ", "@ I feel like I should cut down on my drinking or drug use. ", "# I am terrified of gaining weight or constantly preoccupied by my eating habits. "]

  traumatic_event_statements = ["I have nightmares about the events or thoughts about the events.^ ", "I feel guilty and am unable to stop blaming myself or others for the events.^ "]

  drinking_statements = ["@ My family and friends have complained about the amount I drink/use drugs. ", "@ I have tried and failed to quit drinking/using drugs. ", "@ I feel like I can't live without drinking/using drugs. ", "@ I find myself missing out because I have to drink/use drugs. "]

  eating_disorder_statements = ["# I make myself throw up in order to keep the same weight. ", "# I skip meals because I don't want to gain weight. ", "# I take laxatives to lose weight. ", "# I excercise profusely in order to lose weight. ", "# I am never satisfied with my body. "]

  tf_answers = []
  question_num_2 = 1

  for key in tf_statements:
    print(Fore.GREEN + "------------------------------------------------------------------------------")
    print(key + Style.RESET_ALL)

    answer = input("Enter (True or False): ")

    tf_answers.append(answer)

    tf_eligible_answer(answer)

    if key == "I have experienced a traumatic experience. For example: a serious accident, a physical or sexual assault or abuse, an earthquake or flood, a war, witnissing a death, or losing a loved one to suicide.^ ":
      if answer == "True":
        print(tf_change_question(traumatic_event_statements, tf_answers))

    if key == "@ I feel like I should cut down on my drinking or drug use. ":
      if answer == "True":
        print(tf_change_question(drinking_statements, tf_answers))

    if key == "# I am terrified of gaining weight or constantly preoccupied by my eating habits. ":
      if answer == "True":
        print(tf_change_question(eating_disorder_statements, tf_answers))
    
    if answer == "True":
      analysis.append(key)

  question_num_2 += 1


  print(Back.WHITE + Fore.BLACK + "\n\nFor the next section of the test, you will be given a series of multiple choice questions about the last 2 weeks. \n" + Style.RESET_ALL)

  print(Fore.YELLOW + "Over the last 2 weeks, how often have you been bothered by the following problems?\n\n" + Style.RESET_ALL)

  mc_statements = ["Feeling nervous, anxious, or on edge.` ", "Not being able to stop or control worrying.` ", "Little interest or pleasure in doing things~.", "Feeling down, depressed, or hopeless.~* ", "If you've had any days with issues above, how difficult have these problems made it for you at work, home, school, or with other people? "]

  options = [["A. Not at all", "B. Several days", "C. More than half the days", "D. Nearly every day"], ["A. Not at all", "B. Several days", "C. More than half the days", "D. Nearly every day"], ["A. Not at all", "B. Several days", "C. More than half the days", "D. Nearly every day"], ["A. Not at all", "B. Several days", "C. More than half the days", "D. Nearly every day"], ["A. Not difficult at all", "B. Somewhat difficult", "C. Very difficult", "D. Extremely Difficult"]]

  worrying_statements = ["Can you identify any reasons why you may not be able to stop or control your worrying?` (A for 'yes' or B for 'no') ", "Do these reasons involve schoolwork, family issues, or social issues?` "]

  mc_answers = []
  question_num_3 = 1

  for key in mc_statements:
    print(Fore.YELLOW + "------------------------------------------------------------------------------")
    print(key + Style.RESET_ALL)

    for i in options[question_num_3 - 1]:
      print(i)

    answer_2 = input("Enter (A, B, C, D): ")
    answer_2 = answer_2.upper()
    mc_answers.append(answer_2)

    mc_eligible_answer(answer_2)

    if "*" in key:
      if answer_2 == "D":
        print(Fore.RED + "If you are having thoughts of suicide please call the suicide hotline number at 1-800-273-8255" + Style.RESET_ALL)
    
    if key == "Feeling nervous, anxious, or on edge.` ":
      if answer_2 == "D" or answer_2 == "C":
        print(mc_change_question(worrying_statements, mc_answers))
    
    if answer_2 == "D" or answer_2 == "C":
      analysis.append(key)
        
  question_num_3 += 1

  display_score(ranking_answers, tf_answers, mc_answers, analysis)

print("\nThanks for testing!\n")