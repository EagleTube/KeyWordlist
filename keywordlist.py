import random, sys, os, ctypes, sys, platform, argparse
from colorama import Fore, Back, Style
from datetime import date


today = date.today()
d2 = today.strftime("%B %d, %Y")

if platform.system()=='Linux':
    os.system('clear')
    sys.stdout.write("\x1b]2;KEYWORDLIST {}\x07".format(d2))
else:
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW(f'KEYWORDLIST | {d2}')

print(f"""{Style.BRIGHT + Fore.RED}
 ██████╗ ██████╗  █████╗  ██████╗  ██████╗ ███╗   ██╗███████╗ ██████╗ ██████╗  ██████╗███████╗   ██╗ ██████╗ 
 ██╔══██╗██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗████╗  ██║██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝   ██║██╔═══██╗
 ██║  ██║██████╔╝███████║██║  ███╗██║   ██║██╔██╗ ██║█████╗  ██║   ██║██████╔╝██║     █████╗     ██║██║   ██║
 ██║  ██║██╔══██╗██╔══██║██║   ██║██║   ██║██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝     ██║██║   ██║
 ██████╔╝██║  ██║██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║██║     ╚██████╔╝██║  ██║╚██████╗███████╗██╗██║╚██████╔╝
 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝╚═╝╚═╝ ╚═════╝ 
                                                                                                             
{Fore.WHITE}═══════════════════════════════════════════════════════════════════════════════════════════════════════════════
{Style.BRIGHT + Fore.YELLOW}  
                                                 Coded by Eagle Eye
                                            Keywordlist (Keyword to Wordlist)
                                    https://dragonforce.io | Telegram: dragonforceio
                                   Get Started With (pip install -r requirements.txt)                                                                                            

{Fore.WHITE}═══════════════════════════════════════════════════════════════════════════════════════════════════════════════
""")

special = ['!','@','#','$','%','^','&','*','(',')','_','-']
defaults = 1
default_keynum = 2
wordline = 100

def start():

    parser = argparse.ArgumentParser()
    parser.add_argument('--spc', type=int, help='Special char count > 0', required=True)
    parser.add_argument('--key', type=str, help='Keyword List file (eg: key.txt)', required=True)
    parser.add_argument('--kc', type=int, help='Keyword word count > 0', required=True)
    parser.add_argument('--l', type=int, help='Wordlines count (number) > 0', required=True)
    parser.add_argument('--o', type=str, help='Output file (eg:wordlist.txt)', required=True)

    args = parser.parse_args()

    if args.spc < 1:
        spc = defaults
    else:
        spc = args.spc

    if args.kc < 1:
        kc = default_keynum
    else:
        kc = args.kc

    if args.l < 1:
        l = wordline
    else:
        l = args.l

    Wordlisting(spc,l,kc,args.o,args.key)


def getKeywords(keyfile):
    key_temp = []
    flx = open(keyfile,'r')
    lines = flx.readlines()
    for line in lines:
        key_temp.append(line.replace('\n',''))
    flx.close()
    return key_temp

def shifting(kcount,keyfile,spcial):
    keys = getKeywords(keyfile)
    str_word = []
    if kcount > 0:
        for i in range(kcount):
            rndk = random.choice(keys)
            if rndk not in str_word:
                str_word.append(rndk)
        if(spcial > 1):
            for i in range(spcial):
                rspc = random.choice(special)
                if rspc not in str_word:
                    str_word.append(rspc)
        else:
            rspc = random.choice(special)
            if rspc not in str_word:
                str_word.append(rspc)

    #print(str_word)
    return str_word

def saving(text,fname):
    f = open(fname,'a')
    f.write(text.replace(' ','')+'\n')
    f.close()

def Wordlisting(spcial,linex,kcount,fname,keyfile):
    output = ""
    line_generated = 0
    print("Generating wordlist...")
    for i in range(linex):
        kk = shifting(kcount,keyfile,spcial)
        #print(kk)
        if (len(kk) >= ((spcial+kcount)-1)):
            line_generated += 1
            newlist = kk.copy()
            random.shuffle(newlist)
            for mstr in newlist:
                output+=mstr
            saving(output,fname)
        output = ""
    print("Successfully generated lines -> {}".format(line_generated))


start()