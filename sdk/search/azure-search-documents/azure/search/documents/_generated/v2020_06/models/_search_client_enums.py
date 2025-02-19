# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class AutocompleteMode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Specifies the mode for Autocomplete. The default is 'oneTerm'. Use 'twoTerms' to get shingles
    and 'oneTermWithContext' to use the current context in producing autocomplete terms.
    """

    #: Only one term is suggested. If the query has two terms, only the last term is completed. For
    #: example, if the input is 'washington medic', the suggested terms could include 'medicaid',
    #: 'medicare', and 'medicine'.
    ONE_TERM = "oneTerm"
    #: Matching two-term phrases in the index will be suggested. For example, if the input is 'medic',
    #: the suggested terms could include 'medicare coverage' and 'medical assistant'.
    TWO_TERMS = "twoTerms"
    #: Completes the last term in a query with two or more terms, where the last two terms are a
    #: phrase that exists in the index. For example, if the input is 'washington medic', the suggested
    #: terms could include 'washington medicaid' and 'washington medical'.
    ONE_TERM_WITH_CONTEXT = "oneTermWithContext"

class IndexActionType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The operation to perform on a document in an indexing batch.
    """

    #: Inserts the document into the index if it is new and updates it if it exists. All fields are
    #: replaced in the update case.
    UPLOAD = "upload"
    #: Merges the specified field values with an existing document. If the document does not exist,
    #: the merge will fail. Any field you specify in a merge will replace the existing field in the
    #: document. This also applies to collections of primitive and complex types.
    MERGE = "merge"
    #: Behaves like merge if a document with the given key already exists in the index. If the
    #: document does not exist, it behaves like upload with a new document.
    MERGE_OR_UPLOAD = "mergeOrUpload"
    #: Removes the specified document from the index. Any field you specify in a delete operation
    #: other than the key field will be ignored. If you want to remove an individual field from a
    #: document, use merge instead and set the field explicitly to null.
    DELETE = "delete"

class QueryType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Specifies the syntax of the search query. The default is 'simple'. Use 'full' if your query
    uses the Lucene query syntax.
    """

    #: Uses the simple query syntax for searches. Search text is interpreted using a simple query
    #: language that allows for symbols such as +, * and "". Queries are evaluated across all
    #: searchable fields by default, unless the searchFields parameter is specified.
    SIMPLE = "simple"
    #: Uses the full Lucene query syntax for searches. Search text is interpreted using the Lucene
    #: query language which allows field-specific and weighted searches, as well as other advanced
    #: features.
    FULL = "full"

class ScoringStatistics(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """A value that specifies whether we want to calculate scoring statistics (such as document
    frequency) globally for more consistent scoring, or locally, for lower latency. The default is
    'local'. Use 'global' to aggregate scoring statistics globally before scoring. Using global
    scoring statistics can increase latency of search queries.
    """

    #: The scoring statistics will be calculated locally for lower latency.
    LOCAL = "local"
    #: The scoring statistics will be calculated globally for more consistent scoring.
    GLOBAL_ENUM = "global"

class SearchMode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Specifies whether any or all of the search terms must be matched in order to count the document
    as a match.
    """

    #: Any of the search terms must be matched in order to count the document as a match.
    ANY = "any"
    #: All of the search terms must be matched in order to count the document as a match.
    ALL = "all"
