import pandas as pd
import nltk
from nltk.corpus import stopwords
import string
from progress.bar import IncrementalBar
import spacy
nlp = spacy.load('en_core_web_lg')

humanist_vols = pd.read_csv('web_scraped_humanist_listserv.csv')
humanist_vols_dates = humanist_vols[humanist_vols.dates.str.contains('-')]
humanist_vols_dates['original_text_length'] = humanist_vols_dates.text.apply(len)

def split_on_text(row):
    
    val = round(row['original_text_length'] / 1000000)
    final_texts = []
    count = 1000000
    counter = 0
    for i in range(0, val):
        if (count + 1000000) > row['original_text_length']:
            final_texts.append(row.text[count:])
                
        else:
            final_texts.append(row.text[counter:count])
        counter = counter + 1000000
        count = count + 1000000
    return final_texts

humanist_vols_dates['split_text'] = humanist_vols_dates.apply(split_on_text, axis=1)
processing = IncrementalBar('identifying named entities', max=len(humanist_vols_dates.index))

def get_ner(row, types):
    processing.next()
    ner_terms= ''
    cleaned_terms = ''
    for text in row.split_text:

        tokens = nltk.word_tokenize(text)

        cleaned_text = ''
        for token in tokens:
            token_lower = token.lower()
            if ( token_lower not in string.punctuation) and (token_lower not in stopwords.words('english')):
                cleaned_text = cleaned_text + token_lower + ' '
                

        spacy_text = nlp(cleaned_text)
        
        for ent in spacy_text:
            if len(ent.ent_type_) > 0 or ent.is_alpha:
                if( ent.is_punct == False) and (any(i.isdigit() for i in ent.text) == False) and (ent.is_stop ==False):
                    text = ('').join(ent.text.split('.')) if '.' in ent.text else ent.text
                    cleaned_terms += text + ' '
                    if ent.ent_type_ in types:
                        ner_terms += text + ' '
                    
    return ner_terms, cleaned_terms
ner_types = ['LOC', 'GPE']
humanist_vols_dates[['ner','cleaned_text']] = humanist_vols_dates.apply(get_ner, types=ner_types, axis=1, result_type='expand')
processing.finish()

humanist_vols_dates.to_csv('humanist_vols_ner.csv')