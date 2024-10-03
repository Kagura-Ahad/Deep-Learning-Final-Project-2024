# Urdu Grammar Error Correction Model

## Prework Identified Issues:

- **Wikipedia Corpus for Urdu and error infliction through a small dictionary-like scheme for lemmas**  
  issue: (1) the vocabulary used is not exhaustive therefore can result in overfitting and very low generalization on unseen real-world data. (2) They only produced incorrect data, whereas they could also keep some data where source and target both are identical (as done in the (jared et al)) (3) they have used a subset of errors (only morphological) by filtering out relevant errors using ERRANT (and even subset of those errors which I assume was done as their dataset was not large? idk), most importantly punctuation errors, spelling mistakes are not modeled.

  solution: (1) found a dataset of 500k words and an LSTM-based lemmatizer. We can build our own dictionary of lemmatized words and all of the derived words found. The POS tagger can help us label the morphological information related to each word. This dictionary can be used to inflict errors on data. Moreover, these words are not derived from the data itself so it can better generalize. (2) We will put around 5% of the data for partition as done in (jared et all). (3) We will also do (2) plus probabilistically perform spelling, etc errors by insertion, deletion or substitution (Jared et all uses some heuristic for probability value).

- **Human annotated data**  
  issue: the errors are not natural (which will mess up with the generalization of the model for naturally occurring errors) plus the dataset is small.

- **Wikiedits**  
  issue: (1) Some reviews had a negative opinion about the usage of wikiedits. (2) The tokenizer and segmenter used in wikiedits pipeline are from Stanford NLP ML model on a ConLL dataset. (3) ERRANT is used to filter out morphological errors. The problem is this can lead to overfitting on those features.

  solution: (1) we will use it since it's the most widely used natural source of error and the majority of research of GEC for low-resource languages has been done around it. The negative review is probably due to a lack of a rigorous framework. (2) We will also try some new transformer model (bidirectional-LSTM) for POS tagger. (3) The solution is to train the model on all kinds of revisions, and then fine-tune it on the datasets that are less natural. This way, the model better generalizes the data.

---

## Datasets:

1. **Wikipedia corpus**
2. **Wikiedits corpus**: probably we should choose to only use this. The reason is that if we use 1 alongside this, then data will overlap, which may cause unexpected results.
3. **Urdu dataset from Bushra et al**: contains a very large vocab of 500k words.
4. **Urdu UDTB dataset**: used for Stanford NLP POS tagger model. This is high variant data like Wikipedia, therefore recommended.
5. **IMDB reviews**: This dataset is nuanced and does not have the generic features.
6. **Rekhta**: The previous work scraped only children’s stories. The children’s stories dataset may complement Wikipedia's dataset, but standalone, it can be problematic due to the easier language used. Extended scraping can help.

**Note:** State-of-the-art models for DL in English require datasets in the order of millions. These datasets kind of use exhaustive strategies (overfitting, (my assumption)) rather than generalization.

---

## Techniques for Error Infliction:

1. **Round-trip translation** using Japanese, English, Russian, German, etc. as bridge languages, as these are high-resource. Potential flaw highlighted in this approach is that the errors will be more of those which the translation models are more prone to and will not follow the natural human GEC distribution. One mitigation is to use the Wikipedia edits with similar source and targets for this purpose, and stochastically introduce spelling mistakes, and mistakes found in Wikipedia edits. This strategy is highlighted in Jared et al.
2. **Improve the error infliction strategies for morphological errors** as discussed above.
3. **Wikiedits human error generation**: Requires improvement in the pipeline. Replace tokenizers and other components to be more sophisticated for Urdu datasets that contain English words and numbers.
4. **Stochastic infliction**: based on the distribution of errors in Wikiedits on other datasets. This can improve generalization. However, it's unclear right now how it can be achieved.
5. **Probabilistic infliction** of spelling and punctuation mistakes based on insertion, deletion, substitution.

---

## Issues Identified in Reviews:

- The biggest contribution is actually data collection and compilation, but the paper is not clear on that.
- The technique of error inflection is very simple.
- The data organization is also poor, not much metadata for a reviewer to validate your data collection.
- The types of errors don't cover all types.
- Dataset is overall small, synthetic one is also not that big (which I think is the primary reason for using fewer error types).
- Model is old. [But I think the direction of the paper was incorrect overall, more focus was given on training (model, etc. I think a table would suffice), less on Error generation and results with different strategies].
- Using Wikiedits for testing. (This can be since, testing on artificially generated data itself doesn't prove it would generalize well for natural human mistakes distribution).

---

## State of Art Strategies:

1. **Iterative decoding** as introduced in Jared et al.
2. **Write encoder and decoder** yourself.
3. **Ensemble of models** outperforms single models.

---

## Other Resources:

1. **Urduhack**: tokenizer, POS tagger, lemmatizer.
2. **ERRANT**: given a source and target, tells what type of error correction has been done.
3. **Wikiedits**: extract Wikipedia revision history.
4. **Wikiextract**: extract Wikipedia corpus.
5. **Stanford NLP**: ML models for POS tagger.
6. [TensorFlow Tensor2Tensor](https://github.com/tensorflow/tensor2tensor/blob/master/tensor2tensor/data_generators/wiki_revision.py): A tool to extract Wikipedia revisions.
