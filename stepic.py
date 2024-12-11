##%%
def make_censored(x: str, y: list):
    '''
    заменяет каждое вхождение указанных слов в предложении на
      последовательность $#%! и возвращает полученную строку
      Словом считается любая непрерывная последовательность символов, 
      включая любые спецсимволы (без пробелов)
    '''
    fuuuu = '$#%!'
    te = list(x.split(" "))


sentence = 'When you play the game of thrones, you win or you die'
result = make_censored(sentence, ['die', 'play'])
print(result)
# When you $#%! the game of thrones, you win or you $#%!

sentence2 = 'chicken chicken? chicken! chicken'
result2 = make_censored(sentence2, ['?', 'chicken'])
print(result2)
# '$#%! chicken? chicken! $#%!';