import platform
from subprocess import Popen
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urllib.request import urlopen
import wget
from bs4 import BeautifulSoup
import os
from selenium.webdriver.common.keys import Keys


print("############################### SpiderPackageManager ###############################")
print("### Created by Srirama Dheeraj ###")
print("Device Name: "+platform.node())
print("Platform: "+platform.platform())
print("Architecture:"+str(platform.architecture()))
print("Machine: "+platform.machine())
print("Example: spider install vlc, spider preinstall chrome, spider upgrade winrar,  spider installed software list, spider software list all")

## Software Stack ##
software_stack = []

#### Input Module ###

print("Enter the software name:")
software_name = input(">>")
software_name.lower()
software_name = software_name.split(" ")

# Project Directory Path
dirpath = os.getcwd()
foldername = os.path.basename(dirpath)



def clear_txt_file():
    with open('install.bat','w') as f:
        f.write("")

def clear_un_file():
    with open('uninstall.bat','w') as f:
        f.write("")
def clear_text_pipeline():
    with open('uninstall.bat','w') as f:
        f.write("")

def list_of_softwares_spider():
    print("Softwares Installed in PC Using SpiderPackageManager...")
    if len(software_stack) == 0:
        print("No Softwares installed using SpiderPackageManager")
    for i in software_stack:
        print(i+"\n")

def list_of_softwares_in_pc():
    print("Press Y to get sofware list in the text file or Press N to get software list in command line: ")
    user_choice = input().lower()
    if user_choice == 'y' or user_choice == 'yes':
        print("List generating...")
        clear_text_pipeline()
        with open('pipeline.bat','w') as f:
             f.write("wmic /output:G:\SpiderPackageManager\InstallList.txt product get name,version")    
        Popen("pipeline.bat", cwd=r"G:/SpiderPackageManager")

    elif user_choice == 'n' or user_choice == 'no':
        clear_text_pipeline()
        print("Please wait..")
        with open('pipeline.bat','w') as f:
            f.write("wmic product get name,version")    
        Popen("pipeline.bat",cwd=r"G:\SpiderPackageManager")
    else:
        print("Wrong Command!")     
    
def help():
    print("Example: spider install vlc, spider preinstall chrome, spider upgrade winrar, spider remove recent, spider installed software list, spider software list all, ")

# Install Module
def install(crawl_software_name):
    print("Please wait...")
    # driver = webdriver.PhantomJS(executable_path=r"C:\phantomjs-2.1.1-windows\bin\phantomjs")
    # driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="E:\chromedriver.exe")

    driver = webdriver.Chrome("G:\SpiderPackageManager\chromedriver.exe")
    driver.get('https://filehippo.com/')
    search = driver.find_element_by_xpath('//*[@id="header-collapse"]/form/div/input')
    search.send_keys(crawl_software_name)
    time.sleep(5)
    pyautogui.press('enter')
    print("Initialising Spiders...")
    software_name_check = driver.find_element_by_id('search-header').text

    # Displaying error message if Software Not Found 
    if software_name_check == "Sorry we could not find any results for the search term you entered.":
        print("Sorry could not find any results for the search term you entered.Please try again")

    # System Arcitecture Check
    platform_os_check = str(platform.architecture())

    platform_os = str(platform.architecture())
    platform_os_check = platform_os[2] + platform_os[3]
    soft_os_check = ""
    if platform_os_check == "32":
        soft_os_check = crawl_software_name + " " + str(platform_os_check)
        print(soft_os_check)                      
        fst_click = driver.find_element_by_xpath('//*[@id="programs-list"]/div[1]/div[2]/a')
        fst_click.click()
    elif platform_os_check == "64":
        soft_os_check = crawl_software_name + " " + str(platform_os_check)
        print(soft_os_check)
        fst_click = driver.find_element_by_xpath('//*[@id="programs-list"]/div[2]/div[2]/a')
        fst_click.click()

    print("Establishing connection....")

    scnd_click = driver.find_element_by_xpath('//*[@id="program-header"]/div[2]/div/a[1]')
    scnd_click.click()

    print("Crawling for the", software_name[2], "Package")
    print("Downloading....")
    curl = driver.current_url
    text = urlopen(curl).read()
    soup = BeautifulSoup(text, "lxml")
    data = soup.findAll('div', attrs={'id': "program-download-confirmation"})
    final_download_name = str(crawl_software_name + ".exe")
    for div in data:
        links = div.findAll('a')
        for a in links:
            website_links = "https://filehippo.com/" + a['href']
            wget.download(website_links, final_download_name)

    # Install Module
    clear_txt_file()
    x = os.getcwd()
    x = str(x + "\\")
    y = str(x + final_download_name)
    y = ('"{}"'.format(y))
    a = str(y + ' /s /v"/qn /norestart ”')
    file = open("install.bat", "w")
    file.write(a)
    file.close()
    Popen("install.bat", cwd=r"G:\SpiderPackageManager")
    time.sleep(1)
    print(final_download_name + " Successfully installed")

    # Appending installed software to stack
    software_stack.append(final_download_name)    
## install module ends here ##

## Version Module  ##
def previous_version_install(crawl_software_name):
    print("Please wait...")
    driver = webdriver.Chrome(foldername+r"/chromedriver.exe")
    driver.get('https://filehippo.com/')
    search = driver.find_element_by_xpath('//*[@id="header-collapse"]/form/div/input')
    search.send_keys(crawl_software_name)
    time.sleep(1)
    pyautogui.press('enter')
    print("Initialising Spiders...")
    software_name_check = driver.find_element_by_id('search-header').text

    if software_name_check == "Sorry we could not find any results for the search term you entered.":
        print("Sorry could not find any results for the search term you entered.Please try again")

    platform_os_check = str(platform.architecture())
#//*[@id="program-older-versions"]/div[1]/a
    #//*[@id="program-header"]/div[2]/div/a[1]
    platform_os = str(platform.architecture())
    platform_os_check = platform_os[2] + platform_os[3]
    soft_os_check = ""
    if platform_os_check == "32":
        soft_os_check = crawl_software_name + " " + str(platform_os_check)
        print(soft_os_check)
        fst_click = driver.find_element_by_xpath('//*[@id="programs-list"]/div[1]/div[2]/a')
        fst_click.click()
    elif platform_os_check == "64":
        soft_os_check = crawl_software_name + " " + str(platform_os_check)
        print(soft_os_check)
        fst_click = driver.find_element_by_xpath('//*[@id="programs-list"]/div[2]/div[2]/a')
        fst_click.click()
        print("Establishing connection....")

        scnd_click = driver.find_element_by_xpath('//*[@id="program-older-versions"]/div[1]/a')
        scnd_click.click()

        scnd_click1 = driver.find_element_by_xpath('//*[@id="program-header"]/div[2]/div/a[1]')
        scnd_click1.click()

        print("Crawling for the", software_name[2], "Package")
        print("Downloading....")
        curl = driver.current_url
        text = urlopen(curl).read()
        soup = BeautifulSoup(text, "lxml")
        data = soup.findAll('div', attrs={'id': "program-download-confirmation"})
        final_download_name = str(crawl_software_name + ".exe")
        for div in data:
            links = div.findAll('a')
            for a in links:
                website_links = "https://filehippo.com/" + a['href']
                wget.download(website_links, final_download_name)

        # Install Module
        clear_txt_file()
        x = os.getcwd()
        x = str(x + "\\")
        y = str(x + final_download_name)
        y = ('"{}"'.format(y))
        a = str(y + ' /s /v"/qn /norestart ”')
        file = open("install.bat", "w")
        file.write(a)
        file.close()
        p = Popen("install.bat", cwd=r"G:\SpiderPackageManager")
        time.sleep(1)
        print(final_download_name + " Successfully installed the previous version")

        if final_download_name not in software_stack:
            software_stack.append(final_download_name)

# Remove Module            
def remove(final_sof):
    print("Please wait...")
    clear_un_file()
    remove = str('wmic product where name='+'"'+final_sof+'"'+ ' call uninstall')
    print(remove)
    file = open("uninstall.bat", "w")
    file.write(remove)
    file.close()
    p = Popen("uninstall.bat",  cwd=r"G:\SpiderPackageManager")
    time.sleep(3)
    print(final_sof + " Successfully Uninstalled")

    # removing uninstalled element from the list 
    if final_sof in software_stack:
        software_stack.remove(final_sof)

def remove_recent_software():
    recent_software_name = software_stack.pop()
    remove(recent_software_name)            
       
    
if software_name[0] == "spider" and software_name[1] == "install" and software_name[2] != None:
    crawl_software_name = software_name[2]
    install(crawl_software_name)

#Version module
elif software_name[0] == "spider" and software_name[1] == "preinstall" and software_name[2] != None:
    crawl_software_name = software_name[2]
    previous_version_install(crawl_software_name)


#Remove module
elif software_name[0] == "spider" and software_name[1] == "remove" and software_name[2] != None:
    final_sof = software_name[2]
    remove(final_sof)


#Upgrade module
elif software_name[0] == "spider" and software_name[1] == "upgrade" and software_name[3] != None:
    print("upgrading the package...")
    print("Removing package and updating...")
    final_sof = software_name[2]
    remove(final_sof)
    crawl_software_name = software_name
    install(crawl_software_name)

#Remove module
elif software_name[0] == "spider" and software_name[1] == "remove" and software_name[2] == "recent":
    final_sof = software_name[2]
    remove(final_sof)    

#Spider installed software list 
elif software_name[0] == "spider" and software_name[1] == "installed" and software_name[2] == "software" and software_name[3] == "list":
    list_of_softwares_spider()


#All list_of_softwares_in_pc   
elif software_name[0] == "spider" and software_name[1] == "software" and software_name[2] == "list" and software_name[3] == "all": 
    list_of_softwares_in_pc()

#Help Module 
elif software_name[0] == "spider" and software_name[1] == "help":
    help()
else:
    print("Wrong commmand! Please try again.")







