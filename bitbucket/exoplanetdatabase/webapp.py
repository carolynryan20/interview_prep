#!/usr/bin/python
''' webapp.py

    Kiya Govek & Carolyn Ryan, 4/6/12
'''

import cgi


def sanitizeUserInput(s):
    ''' There are better ways to sanitize input than this, but this is a very
        simple example of the kind of thing you can do to protect your system
        from malicious user input. Unfortunately, this example turns "O'Neill"
        into "ONeill", among other things.
    '''
    charsToRemove = ';,\\/:\'"<>@'
    for ch in charsToRemove:
        s = s.replace(ch, '')
    return s

def getCGIParameters():
    ''' This function grabs the HTTP parameters we care about, sanitizes the
        user input, provides default values for each parameter is no parameter
        is provided by the incoming request, and returns the resulting values
        in a dictionary indexed by the parameter names.
    '''
    form = cgi.FieldStorage()
    parameters = {'planet_name':'', 'mass':'', 'radius':'', 'star_name':'',
                'ra':'', 'dec':''}
        
    for key in parameters:
        if key in form:
            parameters[key] = sanitizeUserInput(form[key].value)

    return parameters

def checkExistParameters(parameters):
    for key in parameters:
        if parameters[key] != '':
            return True
    return False

def formatReport(parameters):
    report = 'You have searched for the following:<br>'
    for key in parameters:
        report += key + ': ' + parameters[key]+'<br>'
    return report

def printMainPageAsHTML(parameters, templateFileName):
    ''' Prints to standard output the main page for this web application, based on
        the specified template file and parameters. The content of the page is
        preceded by a "Content-type: text/html" HTTP header.
    '''
    
    report = ''
    if checkExistParameters(parameters):
        report = formatReport(parameters)
        
    links = ''
    for link in ['webapp.py','template.html','styles.css', 'ExoplanetDataSource.py', 'showsource.py']:
        links += '<a href="showsource.py?source='+link+'">'+link+'</a><br>'
    
    outputText = ''
    try:
        f = open(templateFileName)
        templateText = f.read()
        f.close()
        outputText = templateText % (report,links)
    except Exception, e:
        outputText = 'Cannot read template file "%s" because %s.' % (templateFileName, e)

    print 'Content-type: text/html\r\n\r\n',
    print outputText

def main():
    parameters = getCGIParameters()
    printMainPageAsHTML(parameters, 'template.html')
        
if __name__ == '__main__':
    main()
