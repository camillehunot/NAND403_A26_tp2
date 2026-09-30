import sys
import json
import maya.cmds as cmds #permet de gérer les commandes de maya, on peut faire des commandes comme cmds.ls() pour lister les objets selectionnésb 
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout,QTextEdit, QPushButton, QMessageBox, QApplication, QCheckBox, QLineEdit



class OutlinerOrganization(QWidget): #definition de la classe
    def __init__(self): #constructeur self équivalent de this du cpp, le constructeur dans python prend self en paramètre
        super().__init__() # Constructeur de notre parent (super = mot clé générique pour l'héritage)
        self.setWindowTitle("Outliner Organization")   #fonction qui existe déjà dans QWidget self(en gros la class messageBoard) appel la fonction setWindoTitle
        self.create_ui()#pas besoin de mettre self ici. permet d'appeler create UI


    #definir une fonction
    def create_ui(self): #premier parametre toujours self dans les class
        print("create ui")
        app = QApplication.instance() #permet de récupérer l'instance de l'application
       
        layout = QVBoxLayout(self)   #container
        title = QLabel("enter JSON rule path")
        layout.addWidget(title) #permet de ranger le title dans le layout

        self.texte = QLineEdit(self) #zone ou on va pouvoir écrire le chemin du fichier .json
        layout.addWidget(self.texte) #ajouter le QLineEdit dans le layout
 
        self.check_box_selection = QCheckBox("Apply on selection only", self)
        self.check_box_color = QCheckBox("Apply on color only", self)
        self.check_box_reorder = QCheckBox("Apply reorder", self)

        #ici on ajoute les checkboxes dans le layout
        layout.addWidget(self.check_box_selection) 
        layout.addWidget(self.check_box_color)
        layout.addWidget(self.check_box_reorder)

        button = QPushButton("Organize Outliner", self) #ajouter un string pour ajouter du texte sur notre bouton
        layout.addWidget(button)
        button.clicked.connect(self.on_click) #permet de connecter le bouton a un évenement, ici c'est activer la fonction on_click

    def get_checkbox_states(self): #permet de récupérer l'état des checkboxes avec un true ou false
        return {
            "selection": self.check_box_selection.isChecked(),
            "color": self.check_box_color.isChecked(),
            "reorder": self.check_box_reorder.isChecked()
        }   

    def read_json(self):

        json_path = self.texte.text().strip() #.text() permet de récupérer le texte du QLineEdit sans les balises html

        if not json_path:
            QMessageBox.warning(self, "Warning", "No json file path provided") #self = la class, titre de la boite, message
            self.texte.setStyleSheet("background-color: #ffd9d9; color: #155724;") 
            #permet de changer la couleur de fond et du texte de la zone de texte pour indiquer que le chemin est vide
            return

        #>>>>>>>> permet de load le .json en toute sécurité
        try: 
            rules = json.load(open(json_path)) #ouvre le fichier json et le met dans une variable rules 
            self.texte.setStyleSheet("background-color: #D4EDDA; color: #155724;")
            #permet de confirmer que le fichier json a été chargé en changeant la couleur de la zone de texte
        except:
            print(f"Could not load JSON file: {json_path}")
            self.texte.setStyleSheet("background-color: #ffd9d9; color: #155724;") #I love CSS
            QMessageBox.warning(self, "Warning", "Could not load JSON file from path: \n" + json_path + "\n Please check the file path and try again") #self = la class, titre de la boite, message
            #permet d'indiquer que le chemin n'est pas utilisable
            




# definit ce qui se passe quand on clic sur le bouton
    def on_click(self):
       
        self.read_json() #execute la fonction read_json 
        checkbox_states = self.get_checkbox_states() #récupère l'état des checkboxes et le met dans la variable checkbox_states

#pseudo code pour l'organisation de l'outliner en fonction des règles du fichier json et des états des checkboxes
        #if checkbox_states["selection"]:
        #    #    # Appliquer les règles sur la sélection uniquement
        #if checkbox_states["color"]:
        #    #    # Appliquer les règles sur la couleur uniquement
        #if checkbox_states["reorder"]:
        #    #    # Appliquer les règles de réorganisation uniquement

        

    

        


 
def main(): #definition fonction main
    global widget #global permet que la variable widget est accessible partout, permet de garder la variable pour plus tard
    

    try: #permet de pas les accumuler plus d'une fois
        widget.close()
    except Exception:
        pass

    
    widget = OutlinerOrganization() 
    widget.show()
 
main() #call la fonction main

 