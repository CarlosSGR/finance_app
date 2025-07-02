from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button

import finance_core


class FinanceWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        self.add_widget(Label(text="Current Budget"))
        self.budget_input = TextInput(multiline=False, input_filter="float")
        self.add_widget(self.budget_input)

        self.add_widget(Label(text="Current Debt"))
        self.debt_input = TextInput(multiline=False, input_filter="float")
        self.add_widget(self.debt_input)

        # Expense checkboxes
        self.expense_layout = BoxLayout(orientation="vertical")

        self.gas_cb = CheckBox()
        self.expense_layout.add_widget(self._wrap_checkbox("Gasoline", self.gas_cb))
        self.pc_cb = CheckBox()
        self.expense_layout.add_widget(self._wrap_checkbox("PC payment", self.pc_cb))
        self.crunchy_cb = CheckBox()
        self.expense_layout.add_widget(self._wrap_checkbox("Crunchyroll", self.crunchy_cb))
        self.chatgpt_cb = CheckBox()
        self.expense_layout.add_widget(self._wrap_checkbox("ChatGPT subscription", self.chatgpt_cb))

        self.add_widget(self.expense_layout)

        self.calc_btn = Button(text="Calculate")
        self.calc_btn.bind(on_press=self.calculate)
        self.add_widget(self.calc_btn)

        self.result = Label(text="")
        self.add_widget(self.result)

    def _wrap_checkbox(self, text, cb):
        layout = BoxLayout(orientation="horizontal")
        layout.add_widget(Label(text=text))
        layout.add_widget(cb)
        return layout

    def calculate(self, instance):
        try:
            budget = float(self.budget_input.text)
            debt = float(self.debt_input.text)
        except ValueError:
            self.result.text = "Invalid number input."
            return

        total = finance_core.calculate_net_budget(budget, debt)
        self.result.text = finance_core.summarize_payments(
            self.gas_cb.active,
            self.pc_cb.active,
            self.crunchy_cb.active,
            self.chatgpt_cb.active,
            total,
        )


class FinanceApp(App):
    def build(self):
        return FinanceWidget()


if __name__ == "__main__":
    FinanceApp().run()