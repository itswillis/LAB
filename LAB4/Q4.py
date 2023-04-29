def get_spanish_word(word_dictionary, english_word): 

    try:
        return word_dictionary[english_word] #return corresponding spanish word
    except KeyError:
        print(f"ERROR: {english_word} is not available.")
        return None
    except (TypeError, AttributeError): 
        print("ERROR: Invalid dictionary!")
        return None





dictionary = {'example':'ejemplo','house':'casa','apple':'manzana','love':'amor','food':'comida','hello':'hola','work':'trabaja','sun':'sol','red':'roja','orange':'naranja','black':'negra'}
print(get_spanish_word(dictionary, 'house'))
print(get_spanish_word(dictionary, 'orange'))
print(get_spanish_word([1, 2, 3], 'love'))
print(get_spanish_word(dictionary, 'moon'))