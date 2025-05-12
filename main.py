from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget

class WidgetsExample(GridLayout):
  my_text = StringProperty('0')
  count=0
  count_enable = BooleanProperty(False)

  def click_count(self):
    self.count+=1
    print(self.count)

  def on_button_click(self):
    if self.count_enable:
      self.count+=1
      self.my_text = str(self.count)
    print('button clicked')

  def on_toogle_button_state(self, widget):
    print('toogle state: '+widget.state)
    if widget.state == 'normal':
      widget.text = 'OFF'
      self.count_enable = False
    else:
      widget.text = 'ON'
      self.count_enable = True

  def on_switch_active(self, widget):
    print('switch: '+str(widget.active))

  def on_slider_value(self, widget):
    print('slider: '+str(int(widget.value)))

class StackLayoutExample(StackLayout):
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    self.orientation = 'lr-tb'
    for i in range(0,100):
      #size= dp(100)+i*10
      size= dp(100)
      b = Button(text=str(i+1), size_hint=(None, None), size=(size, size))
      self.add_widget(b)
  pass


#class GridLayoutExample(GridLayout):
#  pass

class AnchorLayoutExample(AnchorLayout):
  pass


class BoxLayoutExample(BoxLayout):
  pass
  """def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.orientation = 'vertical'
    b1 = Button(text='A')
    b2 = Button(text='B')
    b3 = Button(text='C')
    self.add_widget(b1)
    self.add_widget(b2)
    self.add_widget(b3)
  """

class MainWidget(Widget):
  pass

class TheLabApp(App):
  pass

TheLabApp().run()

