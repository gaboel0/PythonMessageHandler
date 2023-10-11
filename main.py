from tkinter import *
class MessageHandler:
    def __init__(self, win):
        self.win = win
        self.win.title("Message Handler - By Gabriel")

        self.initText = Label(win, text="Bem-vindo ao interpretador de mensagens RFID automáticas!")
        self.initText.grid(column=1, row=2)

        self.listMessages = Label(win, text="\n1 - DESATIVAR RFID"
            "\n2 - ATIVAR DESBLOQUEIO COM CARTÃO ESPECÍFICO"
            "\n3 - ATIVAR BLOQUEIO DE QUALQUER CARTÃO"
            "\n4 - DESATIVAR OS BLOQUEIOS DE CARTÕES"
            "\n5 - SAÍDA POR PULSO COM CARTÃO ESPECÍFICO"
            "\n6 - SAÍDA POR PULSO"
            "\n7 - TEMPO DA SAÍDA POR PULSO"
            "\n8 - PERMITE GRAVAR CARTÕES"
            "\n9 - CADASTRAR CARTÃO"
            "\n10 - APAGAR TODOS CARTÕES CADASTRADOS"
            "\n11 - SOLICITAR OS CARTÕES"
            "\n12 - BLOQUEAR A GRAVAÇÃO DE CARTÕES"
            "\n13 - APAGAR O CARTÃO ESPECÍFICO"
            "\n14 - PROTOCOLO MAXTRACK"
            "\n15 - PROTOCOLO SGBT"
            "\n16 - PROTOCOLO CONCOX"
            "\n17 - PROTOCOLO GTSL"
            "\n18 - PROTOCOLO SGBT E GTSL"
            "\n19 - PROTOCOLO QUECLINK N (NOVO)"
            "\n20 - PROTOCOLO QUECLINK (ANTIGO)"
            "\n21 - PROTOCOLO MIX TELEMATICS"
            "\n22 - PROTOCOLO CALAMP LMU2630"
            "\n23 - PROTOCOLO NUMERO CARTAO"
            "\n24 - PROTOCOLO VDO"
            "\n25 - PROTOCOLO ITER"
            "\n26 - SOLICITAR CONFIGURAÇÃO"
            "\n27 - ORDEM INVERSA DOS BYTES"
            "\n28 - ORDEM ORIGINAL DOS BYTES"
            "\n29 - LEITOR MOTORISTA"
            "\n30 - LEITOR MOTORISTA E PASSAGEIRO"
            "\n31 - LEITOR PASSAGEIRO"
            "\n32 - TAXA DE TRANSMISSÃO 19200"
            "\n33 - TAXA DE TRANSMISSÃO 9600"
            "\n34 - TAXA DE TRANSMISSÃO 115200"
            "\n35 - ATIVA BUZZER POR 3 SEGUNDOS"
            "\n36 - ATIVAR BUZZER"
            "\n37 - DESATIVAR BUZZER"
            "\n38 - ATIVA SAÍDA"
            "\n39 - DESATIVA SAÍDA"
            "\n40 - ATIVAR BUZZER AO ACIONAR PÓS CHAVE"
            "\n41 - DESATIVAR BUZZER AO ACIONAR PÓS CHAVE"
            "\n42 - PULSO SAIDA RESUMIDO"
            "\n43 - TEMPO DETECTAR DESLIGAMENTO PÓS CHAVE"
            "\n44 - ATUALIZAR FIRMWARE"
            "\n45 - VERSÃO FIRMWARE"
            "\n46 - POS CHAVE E POSITIVO JUNTOS"
            "\n47 - POS CHAVE E POSITIVO SEPARADOS"
            )
        self.listMessages.grid(column=1, row=4, sticky='w')

        self.rfid = {
            "1": "SGBT|0|",
            "2": "SGBT|1|",
            "3": "SGBT|2|",
            "4": "SGBT|3|",
            "5": "SGBT|45|",
            "6": "SGBT|44|",
            "7": "SGBT|47|03|",
            "8": "SGBT|4|",
            "9": "SGBT|6|",
            "10": "SGBT|8|",
            "11": "SGBT|7|",
            "12": "SGBT|5|",
            "13": "SGBT|9|", 
            "14": "SGBT|10|",
            "15": "SGBT|11|",
            "16": "SGBT|11.1|",
            "17": "SGBT|12|",
            "18": "SGBT|13|",
            "19": "SGBT|14|",
            "20": "SGBT|19|",
            "21": "SGBT|15|",
            "22": "SGBT|16|",
            "23": "SGBT|17|",
            "24": "SGBT|18|",
            "25": "SGBT|50|",
            "26": "SGBT|30|",
            "27": "SGBT|31|",
            "28": "SGBT|32|",
            "29": "SGBT|33|",
            "30": "SGBT|35|",
            "31": "SGBT|34|",
            "32": "SGBT|36|",
            "33": "SGBT|37|",
            "34": "SGBT|43|",
            "35": "SGBT|38|",
            "36": "SGBT|47|",
            "37": "SGBT|48|",
            "38": "SGBT|39|",
            "39": "SGBT|40|",
            "40": "SGBT|41|",
            "41": "SGBT|42|",
            "42": "SGBT|49|",
            "43": "SGBT|20|02|",
            "44": "SGBT|46|",
            "45": "SGBT|21|",
            "46": "SGBT|22|",
            "47": "SGBT|23|"
        }



        self.moduleIdText = Label(win, text="Insira o ID do módulo")
        self.moduleIdText.grid(column=3, row=1)
        self.moduleId = Entry(win)
        self.moduleId.grid(column=3, row=2)

        self.selectMessageText = Label(win, text="Selecione a mensagem (1 a 47)")
        self.selectMessageText.grid(column=4, row=1)
        self.selectedMessage = Entry(win)
        self.selectedMessage.grid(column=4, row=2)

        self.saveInfos = Button(win, text="Salvar informações", command=self.sendMessage)
        self.saveInfos.grid(column=5, row=2)

    def checkTagLength(self):
        if len(self.rfidTag.get()) < 10:
            rfidTagFormated = self.rfidTag.get().zfill(10)
            return rfidTagFormated
    def deleteCard(self):
            
            self.rfidText = Label(win, text="Insira a TAG do cartão RFID a ser deletado")
            self.rfidText.grid(column=2, row=1)
            self.rfidTag = Entry(win)
            self.rfidTag.grid(column=2, row=2)
            deleteTag = self.rfidTag.get()
            
            message_label = Label(self.win, text=f"Essa é a nova mensagem: ST300DEX;{self.moduleId.get()};02;SGBT|9|{deleteTag}|")
            message_label.grid(column=4, row=4)
            
    def registerCard(self):
            self.rfidText = Label(win, text="Insira a TAG do cartão RFID a ser cadastrado")
            self.rfidText.grid(column=2, row=1)
            self.rfidTag = Entry(win)
            self.rfidTag.grid(column=2, row=2)
            registerTag = self.rfidTag.get()

            message_label = Label(self.win, text=f"Essa é a nova mensagem: ST300DEX;{self.moduleId.get()};02;SGBT|6|{registerTag}|")
            message_label.grid(column=4, row=4)   

    def sendMessage(self):
        idModule = self.moduleId.get()
        if len(idModule) < 1:   
             invalidModule = Label(self.win, text="TAG do Módulo está inválido, tente novamente:")
             invalidModule.grid(column=4, row=4)
        message = self.selectedMessage.get()
        if message == "13":
             self.deleteCard()
        elif message == "9":
             self.registerCard()
        else:
            message_label = Label(self.win, text=f"Essa é a nova mensagem: ST300DEX;{self.moduleId.get()};02;{self.rfid[message]}")
            message_label.grid(column=4, row=4)

win = Tk()
handler = MessageHandler(win)
win.mainloop()