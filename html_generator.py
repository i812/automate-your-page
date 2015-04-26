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


def make_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    return generate_concept_HTML(concept_title, concept_description)


def make_HTML_for_many_concepts(list_of_concepts):
    html = ""
    for concept in list_of_concepts:
        concept_html = make_HTML(concept)
        html = html + concept_html
    return html

CONCEPTS = [ ["If Statements","If Statements use comparisons to make decisions and make the code do something different depending on the results of a comparison"],
    ["While Statements","Loop (code that tells the program to do something over and over again)"
    "<br>As long as a 'text expression' is true, do something over and over again until the 'text expression' is false"],
    ["Break Statement","A break statement gives a way to stop the loop even while the 'text expression' is true"],
    ["Debugging","Bugs are errors in code that cause the code not to work"
    "<br>Debugging is a scientific process of examining code to discover things you didn't expect in it"
    "<br>To debug, you need to develop a strategy for systematically getting rid of bug"
    "<br>When Python code crashes, the message it gives is called a Traceback"
    "<br>--- a Traceback tells what line it crashed on, what file it was running, and how it got there"
    "<br>--- the information in the Traceback can focus your attention on the part of the code that might be going wrong"
    "<br>--- pay attention to the line # & function name to see if you can figure out where the problem lies"],
    ["Five Debugging Strategies","Examine error messages when programs crash"
    "<br>Work from example code"
    "<br>Make sure examples work (test, test, test!)"
    "<br>Check intermediate results by adding print statements"
    "<br>Keep and compare old versions"],
    ['<div class="flowchart">Below is a cool flowchart I found that can help with Python Error Codes','<br><a href="http://i.imgur.com/WRuJV6r.png">'
                        '<img src="http://i.imgur.com/WRuJV6rl.png" title="python debugging flowchart">'
                    '</a>"'
    '</div>'],
    ["Structured Data: Lists & For Loops","Strings - sequence of characters"
    "<br>Lists - sequence of anything"
    "<br>Mutation - changing the value of a list after we've created it"
    "<br>Aliasing - two different ways to refer to the same object"
    "<br>List Operations"
    "<br>--- Append Operator: appends a list, adding an additional element to the original list"
    "<br>--- Plus Operator: <list> + <list>, makes a new list made up of original lists, doesn't change original lists"
    "<br>--- Len Operator: len(<list>), length of any object that is a collection of things"
    "<br>--- Index Operator: pass in a value, the output of the index is the position of that value in the list (if the value is in the list, it returns the first position that value is found, otherwise produces an error"
    "<br>--- In / Not In: <value> in <list> - if value is in list, output is true, otherwise output is false; <value> not in <list> - if value is not in list, output is true, otherwise output is false"
    "<br><br>Append adds an addition element to the end of a list (even if new element is a list, it's only one element)"
    "<br>Plus adds a list to a list (items within the list are added to the list)"
    "<br>For Loop: used to iterate items in a list"],
    ["How to Solve Problems","Problem is defined by possible inputs (set) and the relationship between the inputs and the desired outputs"
    "<br><br>1st Step:  Don't Panic!!"
    "<br>1. What are the inputs?"
    "<br>--- How are the inputs represented?"
    "<br>2. What are the desired outputs?"
    "<br>3. Solve the problem"
    "<br>--- Work out examples"
    "<br>--- Consider systematically how a human solves the problem"
    "<br>4. Come up with a simple mechanical solution"
    "<br>5. Develop incrementally and test as you go"
    "<br><br>Put assertion commands into your code to test conditions and trigger an error if condition is false"] ]


print make_HTML_for_many_concepts(CONCEPTS)
