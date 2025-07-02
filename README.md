This simple script allows me to:

- Record my current budget and debt
- Log biweekly expenses (e.g., gasoline, PC payment, subscriptions)
- Check how much of my biweekly expenses I’ve already paid
- See how much money I still owe
- Calculate how much money I’d need to pay off both my expenses and my debt

### Why I made this

I wanted a fast and simple way to answer one question before spending:  
**"Can I actually afford this right now?"**

This helps me stay grounded and avoid impulsive spending when my financial situation is tight.

### How it works

When you run the script:

1. It asks for your current budget and debt.
2. Then, it asks whether you’ve already paid your recurring biweekly expenses.
3. Finally, it calculates what you still owe and shows you how much money you’d need in total to be financially clear.

### How to use

Make sure you have Python installed, then run the CLI application:

```bash
python app.py
```

### Kivy setup

Install Kivy to launch the mobile interface:

```bash
pip install kivy
```

Run the desktop preview of the Kivy version:

```bash
python mobile_app.py
```

### Building for Android

To generate an APK you can use [Buildozer](https://github.com/kivy/buildozer).
Install it and then build the project:

```bash
pip install buildozer
buildozer init  # creates buildozer.spec
buildozer -v android debug
```