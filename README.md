# Urdu Grammar Error Correction Model

This repository contains code for building an Urdu grammar error correction model. The project addresses issues in current grammar correction approaches and aims to improve generalization, error diversity, and naturalness in Urdu GEC (Grammatical Error Correction).

## Table of Contents

- [Overview](#overview)
- [Identified Issues](#identified-issues)
- [Datasets](#datasets)
- [Error Infliction Techniques](#error-infliction-techniques)
- [Challenges in Previous Work](#challenges-in-previous-work)
- [State-of-the-Art Strategies](#state-of-the-art-strategies)
- [Additional Resources](#additional-resources)

## Overview

This project tackles the problem of creating a robust Urdu grammar correction model, incorporating natural and artificial error generation techniques to improve model generalization and handle real-world data.

## Identified Issues

### Prework Identified Issues:
1. **Wikipedia Corpus**: Limited vocabulary leading to overfitting and poor generalization on unseen data. Only morphological errors are considered, neglecting punctuation and spelling mistakes.
   - **Solution**: Use a dataset with 500k words and a POS tagger to create a comprehensive dictionary for error infliction. Add probabilistic spelling errors and ensure a partition of data with identical source and target sentences.
   
2. **Human Annotated Data**: Errors in manually annotated data may not represent naturally occurring mistakes, leading to poor model generalization.
   
3. **Wikiedits**:
   - Issues: Negative reviews, reliance on a Stanford NLP tokenizer and segmenter, and an overfocus on morphological errors.
   - **Solution**: Use Wikiedits data, refine tokenizer and segmenter, and train the model on all types of revisions before fine-tuning with more structured datasets.

## Datasets

1. **Wikipedia Corpus**: A general resource for Urdu text.
2. **Wikiedits Corpus**: Extracts Wikipedia revision history with a focus on capturing natural errors.
3. **Bushra et al Urdu Dataset**: A large vocabulary dataset with 500k words, useful for generalization.
4. **Urdu UDTB Dataset**: Used for POS tagging with varied data, recommended for training Urdu NLP models.
5. **IMDB Reviews**: A nuanced dataset that lacks generic features, useful for diverse error contexts.
6. **Rekhta Dataset**: Previous work focused on children’s stories. Extended scraping can provide more sophisticated content.

> **Note**: State-of-the-art models for English GEC typically use millions of words. In contrast, Urdu remains low-resource, and the current strategy seeks to balance overfitting and generalization.

## Error Infliction Techniques

1. **Round-Trip Translation**: Errors can be induced using bridge languages (Japanese, English, Russian, etc.), but these errors might be biased towards translation model errors. Mitigate by combining with probabilistic spelling/punctuation mistakes.
   
2. **Improved Morphological Error Generation**: Enhanced error infliction strategies using a comprehensive dictionary.
   
3. **Wikiedits-Based Error Generation**: Requires pipeline improvements like replacing tokenizers for better handling of Urdu data containing English and numbers.
   
4. **Stochastic Infliction**: Introduce spelling and punctuation mistakes based on error distributions found in Wikiedits.
   
5. **Probabilistic Infliction**: Insertion, deletion, and substitution errors, inspired by human error tendencies.

## Challenges in Previous Work

1. **Data Organization**: Poor metadata, limiting validation of data collection processes.
2. **Error Types**: Insufficient variety in error types.
3. **Model Selection**: Outdated models were used, and there was too much focus on training rather than error generation techniques.
4. **Testing on Wikiedits**: Evaluating on artificially generated data doesn't guarantee generalization to natural errors.

## State-of-the-Art Strategies

1. **Iterative Decoding**: As introduced in Jared et al, iterative decoding refines model predictions.
2. **Custom Encoder-Decoder Architectures**: Writing custom models for specific error types.
3. **Ensemble Models**: Combining multiple models can improve overall performance.

## Additional Resources

- **Urduhack**: Tools for tokenizing, POS tagging, and lemmatizing Urdu text.
- **ERRANT**: A framework for detecting and labeling grammatical errors.
- **Wikiedits**: Extracts natural error corrections from Wikipedia revisions.
- **Wikiextract**: Extracts a raw Wikipedia corpus.
- **Stanford NLP**: POS tagging models based on ConLL datasets.
- **TensorFlow Tensor2Tensor**: [Wiki Revision Code](https://github.com/tensorflow/tensor2tensor/blob/master/tensor2tensor/data_generators/wiki_revision.py) for extracting revision history.

## License

This project is licensed under [MIT License](LICENSE).
# Urdu Grammar Error Correction Model

This repository contains code for building an Urdu grammar error correction model. The project addresses issues in current grammar correction approaches and aims to improve generalization, error diversity, and naturalness in Urdu GEC (Grammatical Error Correction).

## Table of Contents

- [Overview](#overview)
- [Identified Issues](#identified-issues)
- [Datasets](#datasets)
- [Error Infliction Techniques](#error-infliction-techniques)
- [Challenges in Previous Work](#challenges-in-previous-work)
- [State-of-the-Art Strategies](#state-of-the-art-strategies)
- [Additional Resources](#additional-resources)

## Overview

This project tackles the problem of creating a robust Urdu grammar correction model, incorporating natural and artificial error generation techniques to improve model generalization and handle real-world data.

## Identified Issues

### Prework Identified Issues:
1. **Wikipedia Corpus**: Limited vocabulary leading to overfitting and poor generalization on unseen data. Only morphological errors are considered, neglecting punctuation and spelling mistakes.
   - **Solution**: Use a dataset with 500k words and a POS tagger to create a comprehensive dictionary for error infliction. Add probabilistic spelling errors and ensure a partition of data with identical source and target sentences.
   
2. **Human Annotated Data**: Errors in manually annotated data may not represent naturally occurring mistakes, leading to poor model generalization.
   
3. **Wikiedits**:
   - Issues: Negative reviews, reliance on a Stanford NLP tokenizer and segmenter, and an overfocus on morphological errors.
   - **Solution**: Use Wikiedits data, refine tokenizer and segmenter, and train the model on all types of revisions before fine-tuning with more structured datasets.

## Datasets

1. **Wikipedia Corpus**: A general resource for Urdu text.
2. **Wikiedits Corpus**: Extracts Wikipedia revision history with a focus on capturing natural errors.
3. **Bushra et al Urdu Dataset**: A large vocabulary dataset with 500k words, useful for generalization.
4. **Urdu UDTB Dataset**: Used for POS tagging with varied data, recommended for training Urdu NLP models.
5. **IMDB Reviews**: A nuanced dataset that lacks generic features, useful for diverse error contexts.
6. **Rekhta Dataset**: Previous work focused on children’s stories. Extended scraping can provide more sophisticated content.

> **Note**: State-of-the-art models for English GEC typically use millions of words. In contrast, Urdu remains low-resource, and the current strategy seeks to balance overfitting and generalization.

## Error Infliction Techniques

1. **Round-Trip Translation**: Errors can be induced using bridge languages (Japanese, English, Russian, etc.), but these errors might be biased towards translation model errors. Mitigate by combining with probabilistic spelling/punctuation mistakes.
   
2. **Improved Morphological Error Generation**: Enhanced error infliction strategies using a comprehensive dictionary.
   
3. **Wikiedits-Based Error Generation**: Requires pipeline improvements like replacing tokenizers for better handling of Urdu data containing English and numbers.
   
4. **Stochastic Infliction**: Introduce spelling and punctuation mistakes based on error distributions found in Wikiedits.
   
5. **Probabilistic Infliction**: Insertion, deletion, and substitution errors, inspired by human error tendencies.

## Challenges in Previous Work

1. **Data Organization**: Poor metadata, limiting validation of data collection processes.
2. **Error Types**: Insufficient variety in error types.
3. **Model Selection**: Outdated models were used, and there was too much focus on training rather than error generation techniques.
4. **Testing on Wikiedits**: Evaluating on artificially generated data doesn't guarantee generalization to natural errors.

## State-of-the-Art Strategies

1. **Iterative Decoding**: As introduced in Jared et al, iterative decoding refines model predictions.
2. **Custom Encoder-Decoder Architectures**: Writing custom models for specific error types.
3. **Ensemble Models**: Combining multiple models can improve overall performance.

## Additional Resources

- **Urduhack**: Tools for tokenizing, POS tagging, and lemmatizing Urdu text.
- **ERRANT**: A framework for detecting and labeling grammatical errors.
- **Wikiedits**: Extracts natural error corrections from Wikipedia revisions.
- **Wikiextract**: Extracts a raw Wikipedia corpus.
- **Stanford NLP**: POS tagging models based on ConLL datasets.
- **TensorFlow Tensor2Tensor**: [Wiki Revision Code](https://github.com/tensorflow/tensor2tensor/blob/master/tensor2tensor/data_generators/wiki_revision.py) for extracting revision history.

## License

This project is licensed under [MIT License](LICENSE).
