#imports
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import random

#app class
class RandomUsernameApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.username_list = []
        with open('usernames.txt', 'r') as file: #usernames txt file
            for line in file:
                self.username_list.append(line.strip())
        self.username_label = Button(text='Generate Random Username', font_size=20)
        self.username_label.bind(on_press=self.update_username)
        layout.add_widget(self.username_label)
        return layout
    def update_username(self, instance):
        random_username = random.choice(self.username_list)
        self.username_label.text = random_username

#run command
if __name__ == '__main__':
    RandomUsernameApp().run()