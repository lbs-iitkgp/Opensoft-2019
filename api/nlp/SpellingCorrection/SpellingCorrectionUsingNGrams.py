
# coding: utf-8

# ## Using Bigram-Trigram for real-word error detection

# In[180]:

import sys
import os
import json
import re
import io
import pickle
import operator

from collections import defaultdict

import numpy as np

from bktree import BKTree
from utility import pickle_dump

import nltk
from nltk import ngrams, bigrams, trigrams, FreqDist
from nltk.stem import WordNetLemmatizer 

# ### STEPS :: 
# - First sentence tokenizer to separate the sentences and add **SOS** and **EOS** token to each sentence.
# - Then each sentence to forming cnts using word ngrams method

# ### Will use Vocab class in building BKTree 

# In[220]:

class Vocab:
    def __init__(self):
        self.word2idx = {}
        self.idx2word = {}
        self.word2cnt = {}
        self.idx = 0
        
    def add_word(self, word):
        if word not in self.word2idx:
            self.word2cnt[word] = 1
        else:
            self.word2cnt[word] += 1
    
    def add_words(self, words, min_threshold = 2):
        for word in words:
            self.add_word(word)
        
        self.filter_by_cnt(min_threshold)
    
    def filter_by_cnt(self, min_threshold = 1):
        self.word2cnt = {k : v for k, v in self.word2cnt.items() if v >= min_threshold}
        
        for word, _ in sorted(self.word2cnt.items(), key = operator.itemgetter(1), reverse = True):  
            self.word2idx[word] = self.idx
            self.idx2word[self.idx] = word
            self.idx += 1
    
    def __len__(self):
        return len(self.word2idx)

    def __getitem__(self, key):
        if isinstance(key, int):
            return self.idx2word[key]
        else:
            return self.word2idx[key]

    def __setitem__(self, word, value):
        raise "Can't set items directly, use add_word instead"

    def __delitem__(self, word):
        raise "Can't delete items from index."

    def __contains__(self, word):
        if not isinstance(word, str):
            raise "Presence checks only allowed with words"
        return word in self.word2idx


# In[183]:


def build_preprocessor(lowercase = True):    # No preprocessing for now, can use that from my kaggle kernel
        if lowercase:
            return lambda x : x.strip().lower()
        else:
            return lambda x : x

def build_tokenizer(token_pattern):
    token_pattern = re.compile(token_pattern)
    return lambda doc: token_pattern.findall(doc)


# In[187]:


def load(vocab_path, corpus_path, load = True):
    if os.path.exists(vocab_path) and load:
        print("File already exists. Loading that....")
        with io.open(vocab_path, 'rb') as f:
            vocab = pickle.load(f)
    else:
        vocab = Vocab()
        # bind method
        sent_tokenize = nltk.sent_tokenize

        token_pattern = r"(?u)\b\w\w+\b"
        tokenizer = build_tokenizer(token_pattern)
        preprocessor = build_preprocessor(lowercase = True)

        with io.open(corpus_path, encoding = 'utf-8') as f:
            for paragraph in f:
                for sentence in sent_tokenize(paragraph):
                    words = tokenizer('SOS' + preprocessor(sentence) + 'EOS')
                    if not words:
                        continue                
                    vocab.add_words(words)

        with open(vocab_path, 'wb') as f:
            pickle.dump(vocab, f)

    return vocab


def load_from_words_file(vocab_path, corpus_path, load = True):
    if os.path.exists(vocab_path) and load:
        print("File already exists. Loading that....")
        with io.open(vocab_path, 'rb') as f:
            vocab = pickle.load(f)
    else:
        vocab = Vocab()
        with open(corpus_path) as f:
            for word in f:
                word = word[:-1]
                vocab.add_word(word)
        
        vocab.filter_by_cnt(min_threshold = 1)
        
        with open(vocab_path, 'wb') as f:
            pickle.dump(vocab, f)

    return vocab



# pickle_dump(BKTree(items_dict = load_words('google_1000_english_freq')), 'eng_tree_10K')



class WordSpellingCorrection:
    def __init__(
        self, 
        filepath_corpus,
        filepath_bk_tree, 
        filepath_token_cnts,
        vocab_path,
        ngram_range = (2, 3), 
        token_pattern = r"(?u)\b\w\w+\b",
        preprocessor = None, 
        tokenizer = None, 
        lowercase = True, 
        stop_words = None   #list of stopwords   #keep it to None
    ):
        self.filepath_corpus = filepath_corpus
        self.filepath_bk_tree = filepath_bk_tree
        self.vocab_path = vocab_path
        self.ngram_range = ngram_range
        self.stop_words = stop_words  
        self.lowercase = lowercase
        self.preprocessor = preprocessor
        self.tokenizer = tokenizer
        self.token_pattern = token_pattern
        
        with open(vocab_path, 'rb') as f:
                word2idx, idx2word = pickle.load(f)

        self.vocab_size = len(word2idx)
        
        try:
            with open(self.filepath_bk_tree, 'rb') as f:
                self.tree = pickle.load(f)

        except Exception as e:
            pickle_dump(BKTree(items_dict = word2idx), self.filepath_bk_tree)
            
            with open(self.filepath_bk_tree, 'rb') as f:
                self.tree = pickle.load(f)


        self.token_cnts = None
        self.bi_pre_token_cnts = None
        self.bi_post_token_cnts = None
        self.tri_token_cnts = None
        
        self.filepath_token_cnts = None
        self.filepath_bi_pre_token_cnts = None
        self.filepath_bi_post_token_cnts = None
        self.filepath_tri_token_cnts = None
        
        if filepath_token_cnts is not None and os.path.exists(filepath_token_cnts):
            print('LOADING...')
            with io.open(filepath_token_cnts, encoding = 'utf-8') as f:
                self.token_cnts = json.load(f)
            
            with io.open('bi_pre_' + filepath_token_cnts, encoding = 'utf-8') as f:
                self.bi_pre_token_cnts = json.load(f)
                
            with io.open('bi_post_' + filepath_token_cnts, encoding = 'utf-8') as f:
                self.bi_post_token_cnts = json.load(f)
            
            with io.open('tri_' + filepath_token_cnts, encoding = 'utf-8') as f:
                self.tri_token_cnts = json.load(f)
            
        else:
            print('GETTING FROM CORPUS...')
            self.token_cnts = defaultdict()
            self.bi_pre_token_cnts = defaultdict()
            self.bi_post_token_cnts = defaultdict()
            self.tri_token_cnts = defaultdict()
            
            self.filepath_token_cnts = filepath_token_cnts
            self.filepath_bi_pre_token_cnts = 'bi_pre_' + filepath_token_cnts
            self.filepath_bi_post_token_cnts = 'bi_post_' + filepath_token_cnts
            self.filepath_tri_token_cnts = 'tri_' + filepath_token_cnts
        
            
            self.build_ngrams_count_from_corpus()
        
    def get_candidate_words(self, word, max_edit_distance = 3):
        """Returns candidate word for a given input word. 
        Currently based on using edit-distance...
        """
        return [i[1] for x in [self.tree.find(word, x) for x in range(max_edit_distance + 1)] for i in x]
    
    def build_preprocessor(self):    # No preprocessing for now, can use that from my kaggle kernel
        """Return a function that preprocesses the doc"""
        if self.preprocessor is not None:
            return self.preprocessor
        
        return build_preprocessor(self.lowercase)
        
    def build_tokenizer(self):
        """Return a function that splits a string into a sequence of tokens"""
        if self.tokenizer is not None:
            return self.tokenizer
        
        return build_tokenizer(self.token_pattern)
    
    def build_analyzer(self):
        """Return a callable that handles preprocessing and tokenization"""
        preprocess = self.build_preprocessor()
        tokenize = self.build_tokenizer()
        return lambda doc : self.word_ngrams(tokenize('SOS ' + preprocess(doc) + ' EOS'), self.ngram_range, self.stop_words)    
    
    def _get_ngram_freq_dict(self, tokens, n):   #Only handling uni, bi and tri-grams
        if n == 1:
            n_grams = ngrams(tokens, n)
        elif n == 2:
            n_grams = bigrams(tokens)
        elif n == 3:
            n_grams = trigrams(tokens)
        
        tokens = []
        
        fdist = FreqDist(n_grams)
        
        space_join = " ".join
        tokens_append = tokens.append
        
        for k, v in fdist.items():
            token = space_join(k)
            if token not in self.token_cnts:
                self.token_cnts[token] = v
            else:
                self.token_cnts[token] += v
            
            if n == 2:
                if k[0] not in self.bi_pre_token_cnts:
                    self.bi_pre_token_cnts[k[0]] = 1
                else:
                    self.bi_pre_token_cnts[k[0]] += 1

                if k[1] not in self.bi_post_token_cnts:
                    self.bi_post_token_cnts[k[1]] = 1
                else:
                    self.bi_post_token_cnts[k[1]] += 1
            
            if n == 3:
                tri_token = ' '.join([k[0], k[2]])
                if tri_token not in self.tri_token_cnts:
                    self.tri_token_cnts[tri_token] = 1
                else:
                    self.tri_token_cnts[tri_token] += 1
            
            tokens_append(space_join(k))
        
        return tokens
        
    def word_ngrams(self, tokens, ngram_range, stop_words):  
        """Turn tokens into a sequence of n-grams"""
        # handle stop words
        if stop_words is not None:
            tokens = [w for w in tokens if w not in stop_words]
        
        original_tokens = tokens[:]
        tokens = []
        
        # handle token n-grams
        min_n, max_n = self.ngram_range
        
        tokens_extend = tokens.extend
        
        for n in range(min_n, max_n + 1):
            tokens_extend(self._get_ngram_freq_dict(original_tokens, n))
        
        return tokens

        
#         if max_n != 1:
#             original_tokens = tokens
#             if min_n == 1:
#                 # no need to do any slicing for unigrams
#                 # just iterate through the original tokens
#                 tokens = list(original_tokens)
#                 for token in tokens:
#                     if token not in self.token_cnts:
#                         self.token_cnts[token] = 1
#                     else:
#                         self.token_cnts[token] += 1
                
#                 min_n += 1
#             else:
#                 tokens = []

#             n_original_tokens = len(original_tokens)

#             # bind method outside of loop to reduce overhead
#             tokens_append = tokens.append
#             space_join = " ".join

#             for n in range(min_n, min(max_n + 1, n_original_tokens + 1)):
#                 for i in range(n_original_tokens - n + 1):
#                     token = " ".join(original_tokens[i: i + n])
#                     if token not in self.token_cnts:
#                         self.token_cnts[token] = 1
#                     else:
#                         self.token_cnts[token] += 1
                        
#                     tokens_append(space_join(original_tokens[i: i + n]))

#         return tokens
    
    def build_ngrams_count_from_corpus(self):       #### Later move these functions to vocab
        sentences = []
        
        # bind method
        sent_tokenize = nltk.sent_tokenize
        analyzer = self.build_analyzer()
        path = self.filepath_corpus
        sentences_append = sentences.append
        
        with io.open(path, encoding = 'utf-8') as f:
            for paragraph in f:
                for sentence in sent_tokenize(paragraph):
                    sentences_append(analyzer(sentence))
        
        if self.filepath_token_cnts is not None:
            with io.open(self.filepath_token_cnts, encoding = 'utf-8', mode = 'w') as f:
                json.dump(self.token_cnts, f)
            
            with io.open(self.filepath_bi_pre_token_cnts, encoding = 'utf-8', mode = 'w') as f:
                json.dump(self.bi_pre_token_cnts, f)
                
            with io.open(self.filepath_bi_post_token_cnts, encoding = 'utf-8', mode = 'w') as f:
                json.dump(self.bi_post_token_cnts, f)
                
            with io.open(self.filepath_tri_token_cnts, encoding = 'utf-8', mode = 'w') as f:
                json.dump(self.tri_token_cnts, f)
        
        return sentences
    
#     def _count_ngram(self, *words, pre = True, tri = False):
#         if pre and tri:
#             raise Exception('Both pre and tri should be true')
        
#         count = 0
        
#         if not tri:
#             word = words[0]
#             index = 0 if pre else 1
            
#             for token, cnt in self.token_cnts.items():
#                 if token.split(' ')[index] == word:
#                     count += cnt
#         else:
#             pre = words[0]
#             post = words[1]
            
#             for token, cnt in self.token_cnts.items():
#                 toks = token.split(' ')
#                 if len(toks) == 3 and toks[0] == pre and toks[2] == post:
#                     count += cnt
                    
#         return count
        
    
    def _score(self, pre_bigram, *words):      #only compatible to handle bigram and trigram
        if len(words) == 2:
            if pre_bigram:
                pre = words[0]
                word = words[1]
                
                token = " ".join([pre, word])
                tokens_cnt = self.token_cnts.get(token, 0)
                return self.token_cnts.get(token, 0)/(self.bi_pre_token_cnts.get(pre, 1))
#                 return (tokens_cnt+1)/(self.bi_pre_token_cnts.get(pre, 0)+len(self.vocab))
                
            else:
                word = words[0]
                post = words[1]
                
                token = " ".join([word, post])
                tokens_cnt = self.token_cnts.get(token, 0)
#                 return self.token_cnts[token]/self._count_ngram(post, pre = False, tri = False) if token in self.token_cnts else 0
                return self.token_cnts.get(token, 0)/(self.bi_pre_token_cnts.get(post, 1))
#                 return (tokens_cnt+1)/(self.bi_post_token_cnts.get(post, 0)+len(self.vocab))
                
        elif len(words) == 3:
            pre = words[0]
            word = words[1]
            post = words[2]
            
            token = " ".join([pre, word, post])
            tokens_cnt = self.token_cnts.get(token, 0)
#             return self.token_cnts[token]/self._count_ngram(pre, post, pre = False, tri = True) if token in self.token_cnts else 0
            return self.token_cnts.get(token, 0)/(self.bi_pre_token_cnts.get(' '.join([pre, post]), 1))
#             return (tokens_cnt+1)/(self.tri_token_cnts.get(' '.join([pre, post]), 0)+len(self.vocab))
    
    def _detect_real_word(self, word, pre, post, max_edit_dis, scores):
        lemmatizer = WordNetLemmatizer() 
        lemma_word = lemmatizer.lemmatize(word)
        
        score = 0.2 * self._score(False, word, post) + 0.2 * self._score(True, pre, word) + 0.6 * self._score(None, pre, word, post)
        lemma_score = 0.2 * self._score(False, lemma_word, post) + 0.2 * self._score(True, pre, lemma_word) + 0.6 * self._score(None, pre, lemma_word, post)
        
        # print()
        # print(word, lemma_word)
        # print(score, lemma_score, max(scores))
        
        if score == 0:
            if lemma_score == 0:
                return None
            else:
                return lemma_word
        else:
            if lemma_score < 0.1 * max(scores):
                return None
            else:
                return word
            
    
    def _rank_and_replace_word_candidates(self, word, pre, post, max_edit_dis):
        candidates = self.get_candidate_words(word, max_edit_dis)
        
        scores = [0.2 * self._score(False, candidate, post) + 0.2 * self._score(True, pre, candidate) + 
                  0.6 * self._score(None, pre, candidate, post) 
                  for candidate in candidates]
        
        # print(*zip(candidates, scores))
        # print(candidates[np.argmax(scores)])
        
        correct = self._detect_real_word(word, pre, post, max_edit_dis, scores)
        
        return candidates[np.argmax(scores)] if correct is None else correct
    
    def spelling_correction(self, sentence, max_edit_dis = 2):
        analyzer = self.build_analyzer()
        preprocess = self.build_preprocessor()
        tokenize = self.build_tokenizer()
        
        tokens = tokenize('SOS ' + preprocess(sentence) + ' EOS')
        
        for i in range(2, len(tokens) - 1):
            # print("="*80)
            # print(tokens[i-1], tokens[i], tokens[i+1])
            tokens[i] = self._rank_and_replace_word_candidates(tokens[i], tokens[i - 1], tokens[i + 1], max_edit_dis)
            # print(tokens[i])
        
        # print("="*80)
        # print(tokens)

        return " ".join(tokens[1:-1])


# vocab = load('wiki_vocab.pkl', 'wiki.train.tokens')
# vocab = load_from_words_file('google-10000-english_vocab.pkl', 'google-10000-english.txt', False)

def get_spelling_correction(sent, spellCorr, max_edit_dis = 2):
    # spellCorr = WordSpellingCorrection('en_wikinews.txt', 'wiki_dump.pkl', 'token_cnts_wiki.json', 'word_vocab.pkl')
    return spellCorr.spelling_correction(sent, max_edit_dis)


if __name__ == '__main__':
    # with open('word_vocab.pkl', 'rb') as f:
    #     word2idx, idx2word = pickle.load(f)
    # pickle_dump(BKTree(items_dict = word2idx), 'wiki_dump.pkl')

    spellCorr = WordSpellingCorrection('en_wikinews.txt', 'wiki_dump.pkl', 'token_cnts_wiki.json', 'word_vocab.pkl')
    print(get_spelling_correction("You hut is beautiful", spellCorr))