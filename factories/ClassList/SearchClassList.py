from models.Search.CreateDocumentSearch import CreateDocumentSearch
from models.Search.CreateQueryOptions import CreateQueryOptions
from models.Search.User.CreateUserSearchFields import CreateUserSearchFields
from models.Search.Search import Search


SEARCH_CLASS_LIST = {
    'Search': Search,
    'CreateDocumentSearch': CreateDocumentSearch,
    'CreateUserSearchFields': CreateUserSearchFields,
    'CreateQueryOptions': CreateQueryOptions
}