try:
    text = input('Enter something --> ')
    if len(text) < 3:
        raise ValueError("Input too short!")
except EOFError:
    print('Why did you do an EOF on me?')
except KeyboardInterrupt:
    print('You cancelled the operation.')
except ValueError as ve:
    print('Error:', ve)
else:
    print('You entered: {}'.format(text))
finally:
    print('Execution complete.')
