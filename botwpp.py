from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

class Wpp:
    def __init__(self):
        self.mensagem = []
        while True:

            self.mensagem.append(str(input('Adicionar Mensagem ')))
            sair = str(input('Adicionar mais Mensagens ? [S/N]')).upper()
          
            if sair != 'S' and sair != 'N':
                while True:
                   sair = str(input('Por favor Apenas [S/N]').upper())
                   if sair == 'S' or sair == 'N':
                       break
            else:
                if sair == 'N':
                    break
        
        self.grupo = []
        while True:
            self.grupo.append(str(input('Adicionar Grupos ou pessoas ')))
            sair = str(input('Adicionar mais Grupos ou pessoas ? [S/N]')).upper()
           
            if sair != 'S' and sair != 'N':
                while True:
                   sair = str(input('Por favor Apenas [S/N]').upper())
                   if sair == 'S' or sair == 'N':
                       break
            else:
                if sair == 'N':
                    break

        opcao = webdriver.ChromeOptions()
        opcao.add_argument('lang=pt-br')
        self.drive = webdriver.Chrome(executable_path='//usr/lib/chromium-browser/chromedriver')
        print(self.mensagem)
        print(self.grupo)


    def comentarios(self):
        self.drive.get('https://web.whatsapp.com/')
        print('Esperando O Login...')
        temp = str(input('Aberte qualquer tecla para continuar'))
        for grupo in self.grupo:
            novoGrupo = grupo
            grupo = self.drive.find_element_by_class_name('_3FRCZ')
           # grupo = self.drive.find_element_by_xpath(f"//span[@title='{grupo}']")
            sleep(1)
            grupo.click()
            sleep(1)
            grupo.send_keys(f'{novoGrupo}')
            print(f'{novoGrupo}')
            sleep(3)
            grupo.send_keys(Keys.ENTER)
            sleep(2)
            chat = self.drive.find_element_by_class_name('_3uMse')
            sleep(2)
            chat.click()
            for msg in self.mensagem:
                sleep(3)
                chat.send_keys(msg)
                sleep(1)
                chat.send_keys(Keys.ENTER)
            
           

bot = Wpp()
bot.comentarios()
