class MessageHandler:
    def __init__(self):
        print("\nBem-vindo ao interpretador de mensagens RFID automáticas!")
        self.moduleId = input("Insira o ID do Módulo STR340: ")
        self.rfidTag = input("Insira a TAG do cartão: ")

        calls = [    
        "\n1 - DESATIVAR RFID"
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
        ]
        for call in calls:
            print(call)

        self.rfid = {
            "1": "SGBT|0|",
            "2": "SGBT|1|",
            "3": "SGBT|2|",
            "4": "SGBT|3|",
            "5": "SGBT|45|",
            "6": "SGBT|44|",
            "7": "SGBT|47|03|",
            "8": "SGBT|4|",
            "9": f"SGBT|6|{self.rfidTag}|",
            "10": "SGBT|8|",
            "11": "SGBT|7|",
            "12": "SGBT|5|",
            "13": f"SGBT|9|{self.rfidTag}|", 
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
        
    def checkTagLength(self):
        if len(self.rfidTag) < 10:
            self.rfidTagFormated = self.rfidTag.zfill(10) 
        print(f"\nInformações salvas com sucesso: {self.moduleId} {self.rfidTagFormated}")

    def sendMessage(self):
        message = input("Selecione uma das mensagens anteriores (1 a 48): ")
        self.selectedMessage = self.rfid.get(message)
        if message == "13":
            self.deleteSpecificCard()

    def deleteSpecificCard(self):
        card_to_delete = input("Insira a TAG do cartão a ser apagado: ")
        self.selectedMessage = f"SGBT|9|{self.checkTagLength(card_to_delete)}|"
        print("Salvo.")                             

    def formatMessage(self):
        print(f"\nEssa é sua mensagem completa, formate-a no software SyncTrack: \nSTR300DEX;{self.moduleId};02;{self.selectedMessage + self.rfidTagFormated}")

handler = MessageHandler()
handler.checkTagLength()
handler.sendMessage()
handler.formatMessage()         