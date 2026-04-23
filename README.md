# RAG Pipeline

## Overview

The goal is to implement a full RAG pipeline using 2 different Corpus: 500 Q&A and Quaesta, both technical/scientific data in JSON format, using different chunking strategies and embedding models to see which will perform better for each corpus, and keep the dependecies minimal. 

## Data Model

### Raw Corpus Formats

**500 Questions and Answers**

```json
{
    "<book_name>": {
        "ano_publicacao": "<year>",
        "p_e_r": [
            {
            "pergunta": "<question>", 
            "resposta": "<answer>"
            },
            ...
        ]
    },
    ...
}
```

**Quaesta**

```json
[
  {
    "metadata": {
      "source": "<path>",
      "fonte": "<file_name>",
      "submissaoid": "<id>",
      "codigoprojeto": "<number>",
      "siglainstituicao": "<sigla>",
      "palavrachave": [
        "<palavrachave>",
        ...
      ]
    },
    "content": "<content>",
    "content_length": "<number>" 
  },
  ...
]
```

### Document Definition

**500 Questions and Answers**
One Document = one Q&A pair from one book.
- text: question + answer concatenated (space-separated)
- metadata: `{"book": "<name>", "year": "<year>", "question": "<original question>"}`

**Quaesta**
- text: content
- metadata: `{"source": "<path>", "fonte": "<file_name>", "submissaoid": "<id>", "codigoprojeto": "<number>", "siglainstituicao": "<sigla>", "palavrachave": ["<palavrachave>", ...]}` (for now)




