def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="concept">
    <div class="concept-title">
        ''' + concept_title
    html_text_2 = '''
    </div>
    <div class="concept-description">
        ''' + concept_description
    html_text_3 = '''
    </div>
</div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def get_title(concept):
    start_location = concept.find('TITLE:')
    end_location = concept.find('DESCRIPTION:')
    title = concept[start_location+7 : end_location-1]
    return title

def get_description(concept):
    start_location = concept.find('DESCRIPTION:')
    description = concept[start_location+13 :]
    return description

def get_concept_by_number(text, concept_number):
    counter = 0
    while counter < concept_number:
        counter = counter + 1
        next_concept_start = text.find('TITLE:')
        next_concept_end   = text.find('TITLE:', next_concept_start + 1)
        concept = text[next_concept_start:next_concept_end]
        text = text[next_concept_end:]
    return concept
        

TEST_TEXT = """TITLE: Computers
DESCRIPTION: Computers are universal machines that we can program to essentially any computation.  Programmers must be precise with the programs the utilize as if we recall from previous lesson, Computers are stupid and do not auto correct what we as programmers input.
TITLE: Computer Programs
DESCRIPTION: A computer program is a list of instructions that are input via programmers.
TITLE: Python
DESCRIPTION: Python is a high level computer language. Python is also called an Interpreter as it runs, interprets, and executes.
TITLE: Variables
DESCRIPTION: Variables give programmers a way to give names to values.
TITLE: Strings
DESCRIPTION: Strings are basically words that are encased with either a single or double quote.
TITLE: What is a function?
DESCRIPTION: A function takes input , does something with it, which then produes an output.
TITLE: Making Decisions
DESCRIPTION: First you will need comparisons to be able to test and decide wht to do.
TITLE: If and Else Statements.
DESCRIPTION: The way to make a code do something different, depending on the result of a comparison is to use "IF" or "Else" Statements.
The "IF" statement will produce a TRUE and "ELSE" as a "False" output.
TITLE: While Loops
DESCRIPTION: This is a way to do things over and over again. WHILE can execute any number of times.
TITLE: Nested Lists
DESCRIPTION: List data is a sequence of anything and they are much more powerful than Strings.
Nested Lists are elements that can be anything, and any number of elements.
TITLE: Mutation
DESCRIPTION: Lists support mutation, I know it sounds scary. We can change the value of the list after we have
created them. Mutation modifies the existing object with an element.
TITLE: Aliasing
DESCRIPTION: Aliasing can be thought of as two vaibles with the same names with the same property.
TITLE: List Operations.
DESCRIPTION: There are many built-in list operations such as, APPEND, CONCANTENATION, and LENGTH."""

def generate_all_html(text):
    current_concept_number = 1
    concept = get_concept_by_number(text, current_concept_number)
    all_html = ''
    while concept != '':
        title = get_title(concept)
        description = get_description(concept)
        concept_html = generate_concept_HTML(title, description)
        all_html = all_html + concept_html
        current_concept_number = current_concept_number + 1
        concept = get_concept_by_number(text, current_concept_number)
    return all_html


print generate_all_html(TEST_TEXT)