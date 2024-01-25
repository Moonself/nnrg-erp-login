import requests
from bs4 import BeautifulSoup

class erplogin:
    def __init__(self):
        self.base ='https://exams-nnrg.in/BeeSERP/Login.aspx?ReturnUrl=%2fBeeSERP'
        self.base_std_db = 'https://exams-nnrg.in/BeeSERP/StudentLogin/StudLoginDashboard.aspx?ReturnUrl=%2fBeeSERP'
        self.session  = requests.session()
    
    def get_tags(self , content):
        """ Return the dict contain the hidden input
        """
        tags = dict()
        soup = BeautifulSoup(content.text, 'html.parser')
        hidden_tags = soup.find_all('input', type='hidden')
        for tag in hidden_tags:
            tags[tag.get('name')] = tag.get('value')

        return tags
    def remove_tags(self , content):
        soup = BeautifulSoup(content.text, 'html.parser')
        for data in soup(['style', 'script']):
            # Remove tags
            data.decompose()
 
        # return data by retrieving the tag content
        return ' '.join(soup.stripped_strings)
    
    def printer(self,data):
        inde = data.index('WELCOME')
        while ( data[inde] != ")"):
            print(data[inde],end='')
            inde += 1
        print(') \n')
        inde = data.index('Your Latest Attendance is:')  # maintain 65 above enough    ｡^‿^｡  
        for n in range(34):
            print(data[inde +n],end='')
        print('\n')
    def get_data(self):
        response = self.session.get(self.base)
        self.data = self.get_tags(response)
        
    def poster(self,data):
        data.update(self.data)
        self.response = self.session.post(self.base,headers=self.session.headers,cookies=self.session.cookies,data= data)
        self.data = self.get_tags(self.response)
        
    def about(self):
        print('Hello this is moonself i made this to see if this was possible or not turns out it is possible to scrape our erp page , hope u like it  \nif u find any errors or bugs try to describe it using github\ni will probably update this rarely so u can commit changes once i approve \n Thank you for visiting Bye (｡◕‿◕｡) ')
        
    def get_atd(self):
        data = self.data
        data['__EVENTTARGET'] = 'ctl00$cpStud$lnkStudentMain'
        data.update(self.data)
        self.response = self.session.post(self.base_std_db,headers=self.session.headers,cookies=self.session.cookies,data= data)
        # self.resonse is raw data of the attendance page , use this to manupulate and get a ur desired data
        self.printer(self.remove_tags(self.response))
    
    def get_marks(self,dec,dec1):  # i will  refer the a article to find a better method to pass a sigle argument later
        data = self.data
        data['__EVENTTARGET'] = 'ctl00$cpStud$lnkOverallMarksSemwiseMarks'
        self.response = self.session.post(self.base_std_db,headers=self.session.headers,cookies=self.session.cookies,data= data)
        some = self.remove_tags(self.response).split(' ') 
        '''some gives a tags less scriptless data which is easy to manupulate and get desired data but is not complete html response
        self.response is the raw data, use this to get desired data  and format it as u like
        A note for me: 1)find if subjects are not passed
                        2)a attribute to print failed or passed subjects
        '''
        for n in range(len(some)):
        # print(n,some[n])  
            if dec is True and dec1 is True:
                if some[n] == 'WELCOME':
                    while (some[n] != ')'): 
                        print(some[n], end=' ')
                        n+=1
                    print(') \n')
                    n+=50
        
            if some[n] == 'CGPA:':
                print(some[n], some[n+1] , end=' ')
                print('\n')
                n +=110
            if some[n] == 'SEM':
                print(some[n] , some[n-1], end=' ')
                print('\n')
                n+=85
            if some[n] == 'SGPA:':
                print(some[n] , some[n+1], end=' ')
                print('\n')
                n +=20
        
    def login(self,roll):
        self.roll = roll.upper()
        self.get_data()
        first = {    'txtUserName': self.roll,
                    'btnNext': 'Next'}
        self.poster(first) # same view_state everytime for same roll no:   ¯\(°_o)/¯
        second = { 'txtPassword': self.roll,   #  change your password and they will call you for changing,why give the option to change  ಠ_ಠ
                    'btnSubmit': 'Submit'}
        self.poster(second)   
        if self.response.status_code == 200:
            print("Successfully logged in :)")
        else:
            print('Pretty much everything here is useless if u cannot login.\n why do they shutdown servers on holidays though?!! :(')