from user_analysis import display_score, take_test

from how_are_you_feeling import ranking_section, tf_section, mc_section

from colorama import Fore, Back, Style

def main():
  if take_test():

    print(Back.WHITE + Fore.BLACK + "\nWelcome to the mental health screening.\n" + Style.RESET_ALL)
  
    print(Back.WHITE + Fore.BLACK + "How are you feeling?: The Test That Helps\n\nBelow, you will be asked a series of questions. Find a calm, quiet place with no distractions and answer each question as honestly as you can. At the end of the screening you will be given an analysis of your mental health.\n\nGood luck!\n" + Style.RESET_ALL)

    rank_statements = ["Little interest or pleasure in doing things~ ", "Feeling down, depressed or hopeless~ ", "Trouble falling or staying asleep, or sleeping too much ", "Feeling tired or having little energy~ ", "Poor appetite or overeating ", "Feeling bad about yourself - or that you are a failure or have let yourself or your family down~` ", "Trouble concentrating on things, such as doing homework or watching television` ", "Feeling sluggish or tired~ ", "Feeling more restless than usual` ", "Thoughts that you would be better off dead, or hurting yourself~* "]

    analysis = []
    
    ranking_answers = ranking_section(rank_statements, analysis)

    tf_statements = ["I have been experiencing severe mood swings, more energy than usual, less need to sleep.` ", "I have experienced a traumatic experience. For example: a serious accident, a physical or sexual assault or abuse, an earthquake or flood, a war, witnissing a death, or losing a loved one to suicide.^ ", "I am constantly on guard, watchful, or easily startled.^` ", "I feel numb or detached from people, activities or my surroundings. ", "@ I feel like I should cut down on my drinking or drug use. ", "# I am terrified of gaining weight or constantly preoccupied by my eating habits. "]

    tf_answers = tf_section(tf_statements, analysis)

    mc_statements = ["Feeling nervous, anxious, or on edge.` ", "Not being able to stop or control worrying.` ", "Little interest or pleasure in doing things~.", "Feeling down, depressed, or hopeless.~* ", "If you've had any days with issues above, how difficult have these problems made it for you at work, home, school, or with other people? "]

    mc_answers = mc_section(mc_statements, analysis)

    display_score(ranking_answers, tf_answers, mc_answers, analysis)

    print("\nThanks for testing!\n")
  else:
    print("\nMaybe another time. Have a nice day!\n")

if __name__ == "__main__":
  main()